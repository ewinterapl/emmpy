"""Build a TS07D equatorial magnetic field.

Build a TS07D equatorial magnetic field.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectorfields.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)
from emmpy.geomagmodel.t01.deformation.positionbender import (
    PositionBender
)
from emmpy.geomagmodel.t01.deformation.twistwarpffunction import (
    TwistWarpFfunction
)
from emmpy.geomagmodel.ts07.modeling.equatorial.shieldedthincurrentsheetfield import (
    ShieldedThinCurrentSheetField
)
from emmpy.magmodel.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)
from emmpy.utilities.nones import nones


class Ts07EquatorialMagneticFieldBuilder:
    """Build the TS07D empirical magnetic field model.

    Build the TS07D empirical magnetic field model.

    Attributes
    ----------
    dipoleTiltAngle : float
        Dipole tilt angle.
    dynamicPressure : float
        Dynamic pressure.
    coeffs : Ts07EquatorialVariableCoefficients
        The variable coefficients.
    tailLength : float
        The tail length.
    shieldingCoeffs : ThinCurrentSheetShieldingCoefficients
        Shielding coefficients.
    includeShield : bool
        True to include the shielding field.
    withTA15deformation : float
        z-component of interplanetary magnetic field.
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
                 shieldingCoeffs):
        """Initialize a new Ts07EquatorialMagneticFieldBuilder object.
        
        Initialize a new Ts07EquatorialMagneticFieldBuilder object.

        Parameters
        ----------
        dipoleTiltAngle : float
            Dipole tilt angle.
        dynamicPressure : float
            Dynamic pressure.
        coeffs : Ts07EquatorialVariableCoefficients
            The variable coefficients.
        tailLength : float
            The tail length.
        shieldingCoeffs : ThinCurrentSheetShieldingCoefficients
            Shielding coefficients.
        """
        self.dipoleTiltAngle = dipoleTiltAngle
        self.dynamicPressure = dynamicPressure
        self.coeffs = coeffs
        self.tailLength = tailLength
        self.shieldingCoeffs = shieldingCoeffs
        self.includeShield = True
        self.withTA15deformation = 0.0

    def withEquatorialShielding(self):
        """Turn on equatorial shielding.

        By default, the equatorial shielding fields are evaluated, so if
        you haven't previously turned them off, you won't need to call
        this.

        Parameters
        ----------
        None

        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This builder object.
        """
        self.includeShield = True
        return self

    def withoutEquatorialShielding(self):
        """Turn off equatorial shielding.

        By default, the equatorial shielding fields are evaluated.
        Evaluating the shielding of the equatorial fields, is about 90%
        of the computation time required of the model. Since they are not
        needed in all applications, like computing the current density
        inside the magnetopause, the option to turn them off can
        significantly speed up the code.

        Parameters
        ----------
        None

        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This builder object.
        """
        self.includeShield = False
        return self

    def build(self):
        """Build the equatorial magnetic field.

        Build the equatorial magnetic field.

        Parameters
        ----------
        None

        Returns
        -------
        result : BasisVectorField
            The magnetic field components.
        """
        numCurrSheets = len(self.coeffs.currThicks)
        hingeDistance = self.coeffs.hingeDist
        warpingParam = self.coeffs.warpingParam
        twistParam = self.coeffs.twistParam
        equatorialFields = nones((numCurrSheets,))

        # Loop through each of the current sheets.
        for currSheetIndex in range(numCurrSheets):
            currSheetThick = self.coeffs.currThicks[currSheetIndex]
            linearCoeffs = self.coeffs.equatorialLinearCoeffs[currSheetIndex]

            # Construct a constant current sheet half thickness.
            currentSheetHalfThickness = DifferentiableScalarFieldIJ.createConstant(
                currSheetThick
            )
    
            # Construct the shielded thin current sheet.
            thinCurrentSheet = ShieldedThinCurrentSheetField.createUnity(
                currentSheetHalfThickness, self.tailLength,
                self.shieldingCoeffs, self.includeShield)

            # If the with TA15 deformation was called, apply the TA15
            # deformation instead of the T01 deformation.
            bentWarpedField = thinCurrentSheet
            if self.withTA15deformation:
                raise Exception("NOT IMPLEMENTED!")
            else:
                # The T01 deformation (standard for TS07D).

                # Warp the shielded thin current sheet.
                warpedField = TwistWarpFfunction.deformBasisField(
                    self.dipoleTiltAngle, warpingParam, twistParam,
                    thinCurrentSheet)

                # Now apply the bending deformation to the warped field.
                bentWarpedField = PositionBender.deformBasisField(
                    self.dipoleTiltAngle, hingeDistance, warpedField)

                # Scale position vector for solar wind
                # (see Tsy 2002-1 2.4).
                # Note: this is a point of inconsistency with the Fortran
                # code, in the Fortran this calculation is done in single
                # precision. When the field values are very large, this
                # can result in tenths of differences between the Java and
                # the Fortran version of the model.
                pdynScaling = pow(self.dynamicPressure/2.0, 0.155)
                scaledBentWarpedField = BasisVectorFields.scaleLocation(
                    bentWarpedField, pdynScaling)
                coeffs = linearCoeffs.coeffs.getAsSingleExpansion()
                pdsc = linearCoeffs.getPdynScaledCoeffs(self.dynamicPressure)
                pdynCoeffs = pdsc.getAsSingleExpansion()

                # Finally, expand the coefficients by including a term
                # that includes the dynamical pressure.
                equatorialField = BasisVectorFields.expandCoefficients2(
                    scaledBentWarpedField, coeffs, [pdynCoeffs])
                equatorialFields[currSheetIndex] = equatorialField

            return BasisVectorFields.concatAll(equatorialFields)
