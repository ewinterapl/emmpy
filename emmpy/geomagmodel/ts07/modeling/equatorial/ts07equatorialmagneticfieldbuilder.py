"""emmpy.geomagmodel.ts07.modeling.equatorial.ts07equtorialmagneticfieldbuilder"""


from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)
from emmpy.geomagmodel.t01.deformation.positionbender import (
    PositionBender
)
from emmpy.geomagmodel.t01.deformation.twistwarpffunction import (
    TwistWarpFfunction
)
from emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses import (
    CurrentSheetHalfThicknesses
)
from emmpy.geomagmodel.ts07.modeling.equatorial.shieldedthincurrentsheetfield import (
    ShieldedThinCurrentSheetField
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)


class Ts07EquatorialMagneticFieldBuilder:
    """A Builder for constructing the TS07D empirical magnetic field
    model and derivatives of the model.

    author Nicholas Sharp
    author G.K.Stephens
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
                 shieldingCoeffs):
        self.dipoleTiltAngle = dipoleTiltAngle
        self.dynamicPressure = dynamicPressure
        self.coeffs = coeffs
        self.tailLength = tailLength
        self.shieldingCoeffs = shieldingCoeffs
        self.bessel = None
        self.includeShield = True
        self.withTA15deformation = 0

    # def withAlbertBessel(self):
    #     """Use Jay Albert's faster Bessel function evaluator.

    #     By default, the Bessel function evaluator will be Tsyganenko's, if this
    #     is set, Jay Albert's Bessel function evaluator will be used instead.
    #     Jay Albert's implementation is about 4 times faster, although it gives
    #     slightly different, but negligible, differences.

    #     @return this builder object
    #     """
    #     # self.bessel = AlbertBesselFunctionEvaluator(14)
    #     return self

    # def set_withTA15deformation(self, bzIMF):
    #     """Use the TA15 bending and warping deformation instead of the T01
    #     bending and warping deformation.

    #     By default, the model uses the T01 bending and warping deformation.

    #     @param bzIMF the z-component of the IMF (interplanetary magnetic field)
    #     averaged over the previous 30 minutes
    #     @return this builder object
    #     """
    #     self.withTA15deformation = bzIMF
    #     return self

    def withEquatorialShielding(self):
        """Turn on equatorial shielding.

        By default, the equatorial shielding fields are evaluated, so if you
        haven't previously turned them off, you won't need to call this.

        return this builder object
        """
        self.includeShield = True
        return self

    def withoutEquatorialShielding(self):
        """Turn off equatorial shielding.

        By default, the equatorial shielding fields are evaluated. Evaluating
        the shielding of the equatorial fields, is about 90% of the computation
        time required of the model. Since they are not needed in all
        applications, like computing the current density inside the
        magnetopause, the option to turn them off can significantly speed up
        the code.

        return this builder object
        """
        self.includeShield = False
        return self

    def build(self):
        # int numCurrSheets
        numCurrSheets = len(self.coeffs.getCurrThicks())
        # float hingeDistance, warpingParam, twistParam
        hingeDistance = self.coeffs.getHingeDistance()
        warpingParam = self.coeffs.getWarpingParam()
        twistParam = self.coeffs.getTwistParam()
        # [BasisVectorField] equatorialFields
        equatorialFields = [None]*numCurrSheets

        # loop through each of the current sheets
        for currSheetIndex in range(numCurrSheets):
            # double currSheetThick
            currSheetThick = self.coeffs.getCurrThicks()[currSheetIndex]
            # Ts07EquatorialLinearCoefficients linearCoeffs
            linearCoeffs = self.coeffs.getLinearCoeffs()[currSheetIndex]

            # Construct a constant current sheet half thickness
            # DifferentiableScalarFieldIJ currentSheetHalfThickness
            currentSheetHalfThickness = (
                CurrentSheetHalfThicknesses.createConstant(currSheetThick)
            )
    
            # Construct the shielded thin current sheet
            # ShieldedThinCurrentSheetField thinCurrentSheet
            thinCurrentSheet = ShieldedThinCurrentSheetField.createUnity(
                currentSheetHalfThickness, self.tailLength, self.bessel,
                self.shieldingCoeffs, self.includeShield)

            # if the with TA15 deformation was called, apply the TA15
            # deformation instead of the T01 deformation
            # BasisVectorField bentWarpedField
            bentWarpedField = thinCurrentSheet
            if self.withTA15deformation:
                raise Exception
    #     #         // warp the shielded thin current sheet
    #     #         BasisVectorField warpedField = DeformationII.deformBasisField(dipoleTiltAngle,
    #     #             hingeDistance, warpingParam, twistParam, thinCurrentSheet);

    #     #         double bzIMF = withTA15deformation.getAsDouble();

    #     #         // now apply the bending deformation to the warped field
    #     #         bentWarpedField =
    #     #             DeformationI.deformBasisField(dipoleTiltAngle, hingeDistance, bzIMF, warpedField);
            else:
                # the T01 deformation (standard for TS07D)

                # warp the shielded thin current sheet
                # BasisVectorField warpedField
                warpedField = TwistWarpFfunction.deformBasisField(
                    self.dipoleTiltAngle, warpingParam, twistParam,
                    thinCurrentSheet)

                # now apply the bending deformation to the warped field
                # BasisVectorFieldDeformation bentWarpedField
                bentWarpedField = PositionBender.deformBasisField(
                    self.dipoleTiltAngle, hingeDistance, warpedField)

                # Scale position vector for solar wind (see Tsy 2002-1 2.4)
                # Note: this is a point of inconsistency with the Fortran
                # code, in the Fortran this calculation is done in single
                # precision. When the field values are very large, this can
                # result in tenths of differences between the Java and the
                # Fortran version of the model
                pdynScaling = pow(self.dynamicPressure/2.0, 0.155)
                # BasisVectorField scaledBentWarpedField
                scaledBentWarpedField = BasisVectorFields.scaleLocation(
                    bentWarpedField, pdynScaling)

                # CoefficientExpansion1D or ArrayCoefficientExpansion1D?
                coeffs = linearCoeffs.getCoeffs().getAsSingleExpansion()
                # TailSheetCoefficients pdsc
                pdsc = linearCoeffs.getPdynScaledCoeffs(self.dynamicPressure)
                pdynCoeffs = pdsc.getAsSingleExpansion()
                # pdynCoeffs = (
                #     linearCoeffs.getPdynScaledCoeffs(self.dynamicPressure).
                #     getAsSingleExpansion()
                # )

                # Finally, expand the coefficients by including a term that
                # includes the dynamical pressure
                # BasisVectorField
                equatorialField = BasisVectorFields.expandCoefficients2(
                    scaledBentWarpedField, coeffs, [pdynCoeffs])

                equatorialFields[currSheetIndex] = equatorialField

            return BasisVectorFields.concatAll(equatorialFields)
