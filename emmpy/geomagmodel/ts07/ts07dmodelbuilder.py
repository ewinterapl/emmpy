"""Build the TS07D model.

Build the TS07D model.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07dstaticcoefficientsfactory import (
    TS07DStaticCoefficientsFactory
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils import (
    TS07DVariableCoefficientsUtils
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)
from emmpy.geomagmodel.ts07.modeling.dipoleshield.dipoleshieldingfield import (
    DipoleShieldingField
)
from emmpy.geomagmodel.ts07.modeling.equatorial.ts07equatorialmagneticfieldbuilder import (
    Ts07EquatorialMagneticFieldBuilder
)
from emmpy.geomagmodel.ts07.modeling.fieldaligned.ts07dfieldalignedmagneticfield import (
    Ts07DFieldAlignedMagneticField
)
from emmpy.magmodel.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TS07DModelBuilder:
    """Build the TS07D model.

    A Builder class that can be used to build the TS07D empirical magnetic
    field model.

    This builder lets you customize your creation of the TS07D model. Some
    of the options include the dipole tilt angle, the dynamic pressure,
    the set of static and dynamic coefficients, evaluation of the
    shielding fields, and the model resolution.

    Attributes
    ----------
    dipoleTiltAngle : float
        dipoleTiltAngle
    dynamicPressure : float
        dynamicPressure
    variableCoefficients : TS07DVariableCoefficients
        variableCoefficients
    parameters : Ts07NonLinearParameters
        parameters
    twistParameterSet : bool
        twistParameterSet
    twistParameter : float
        twistParameter
    tailLength : float
        tailLength
    includeEquatorialShielding : bool
        includeEquatorialShielding
    staticCoefficients : ThinCurrentSheetShieldingCoefficients
        staticCoefficients
    _withTA15deformation : float
        withTA15deformation
    _withMagnetopause : bool
        withMagnetopause
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, variableCoefficients):
        """Initialize a new TS07DModelBuilder object.
        
        Initialize a new TS07DModelBuilder object.

        Parameters
        ----------
        dipoleTiltAngle : float
            dipoleTiltAngle
        dynamicPressure : float
            dynamicPressure
        variableCoefficients : TS07DVariableCoefficients
            variableCoefficients
        """
        self.dipoleTiltAngle = dipoleTiltAngle
        self.dynamicPressure = dynamicPressure
        self.variableCoefficients = variableCoefficients
        self.parameters = None

        # The standard tail length is 20.0 Re.
        self.tailLength = 20.0

        # By default the equatorial shielding is included.
        self.includeEquatorialShielding = True

        # Constructing the static coefficients is expensive, much more
        # expensive than the model evaluation, so don't construct until/unless
        # necessary. When build is called, if it is still null (i.e. the user
        # never called a withStaticCoeffs method), construct using the default
        # at that time.
        self.staticCoefficients = None

        # By default, we will be consistent with the original FORTRAN code and
        # will not check the magnetopause boundary.
        self._withMagnetopause = False

        self.twistParameterSet = None
        self.twistParameter = None
        self._withTA15deformation = None

    @staticmethod
    def create(*args):
        """Create a new object that can construct the TS07D model.

        Create a new object that can construct the TS07D model.

        Parameters
        ----------
        dipoleTiltAngle : float
            The dipole tilt angle in radians.
        dynamicPressure : float
            The dynamic pressure of the solar wind.
        variableCoefficients : str
            Path to coefficients file.
        OR
        dipoleTiltAngle : float
            The dipole tilt angle in radians.
        dynamicPressure : float
            The dynamic pressure of the solar wind.
        variableCoefficientsFile : str
            Path to coefficients file.
        numAzimuthalExpansions : int
            Number of equatorial azimuthal expansions (M).
        numRadialExpansions : int
            Number of equatorial radial expansions (N).
        facConfiguration : FacConfiguration
            facConfiguration

        Returns
        -------
        result : TS07DModelBuilder
            The new model builder object.

        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if len(args) == 3:
            (dipoleTiltAngle, dynamicPressure, variableCoefficients) = args
            # This set of inputs (dipole tilt, dynamic pressure, and
            # variable coefficients) is the minimal set to construct the
            # standard TS07D model. Other customizations to the model are
            # available as methods on the builder.
            return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure,
                                     variableCoefficients)
        elif len(args) == 5:
            (dipoleTiltAngle, dynamicPressure, variableCoefficientsFile,
             numAzimuthalExpansions, numRadialExpansions,
             facConfiguration) = args
            # Creates a new Builder that can be used to construct the TS07D
            # model with a different equatorial resolution than M=4, N=5.
            # This will throw a runtime exception if the input number of
            # expansions doesn't match the size of the file.
            coeffs = TS07DVariableCoefficientsUtils.create(
                variableCoefficientsFile, numAzimuthalExpansions,
                numRadialExpansions, facConfiguration)
            return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs)
        else:
            raise TypeError

    @staticmethod
    def createStandardResolution(dipoleTiltAngle, dynamicPressure,
                                 variableCoefficientsFile, facConfiguration):
        """Create a new model builder with standard resolution.

        Create a new model builder with standard resolution.

        Parameters
        ----------
        dipoleTiltAngle : float
            The dipole tilt angle in radians.
        dynamicPressure : float
            The dynamic pressure of the solar wind.
        variableCoefficientsFile : str
            Path to coefficients file.
        facConfiguration : FacConfiguration
            facConfiguration

        Returns
        -------
        result : TS07DModelBuilder
            The new model builder object.
        """
        numAzimuthalExpansions = 4
        numRadialExpansions = 5

        # This will throw a runtime exception if the input number of expansions
        # doesn't match the size of the file.
        coeffs = TS07DVariableCoefficientsUtils.create(
            variableCoefficientsFile, numAzimuthalExpansions,
            numRadialExpansions, facConfiguration)
        return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs)

    def withDipoleTiltAngleValue(self, dipoleTiltAngle):
        """Replace the initial dipole tilt angle with the supplied value.

        Replace the initial dipole tilt angle with the supplied value.

        Parameters
        ----------
        dipoleTiltAngle : float
            New value for dipole tilt angle.
        
        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.dipoleTiltAngle = dipoleTiltAngle
        return self

    def withDynamicPressureValue(self, dynamicPressure):
        """Replace the initial dynamic pressure with the supplied value.

        Replace the initial dynamic pressure with the supplied value.

        Parameters
        ----------
        dynamicPressure : float
            New value for dynamic pressure.
        
        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.dynamicPressure = dynamicPressure
        return self

    def withVariableCoefficientValues(self, variableCoefficients):
        """Replace the initial set of variable coefficients.

        Replace the initial set of variable coefficients

        NOTE, this will not override the value of the twist angle if the
        withTwistParameter(double)} was called.

        Parameters
        ----------
        variableCoefficients : TS07DVariableCoefficients
            A new set of variable coefficients to use when building the model.

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.variableCoefficients = variableCoefficients
        return self

    def withEquatorialShielding(self):
        """Set the equatorial shielding field flag.

        By default, the equatorial shielding fields are evaluated, so if
        you haven't previously turned them off, you won't need to call
        this.

        Parameters
        ----------
        None

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.includeEquatorialShielding = True
        return self

    def withoutEquatorialShielding(self):
        """Clear the equatorial shielding flag.

        Evaluating the shielding of the equatorial fields, is about 90% of
        the computation time required of the model. Since they are not
        needed in all applications, like computing the current density
        inside the magnetopause, the option to turn them off can
        significantly speed up the code.

        Parameters
        ----------
        None

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.includeEquatorialShielding = False
        return self

    def withTA15deformation(self, bzIMF):
        """Set the z-component of the IMF.

        Use the TA15 bending and warping deformation instead of the T01
        bending and warping deformation for the equatorial field,

        By default, the model uses the T01 bending and warping
        deformation.

        Parameters
        ----------
        bzIMF : float
            The z-component of the IMF (interplanetary magnetic field)
            averaged over the previous 30 minutes.

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self._withTA15deformation = bzIMF
        return self

    def withOriginalStaticCoefficients(self):
        """Return to the original set of static coefficients.

        Use the original set of static coefficients, this is the default
        set, so if you haven't changed them overridden them with another
        method, it is unnecessary to call this method.

        This set has resolution up to M=6, N=8, so if you want higher
        resolution than this, you must use a different set of
        coefficients.

        Parameters
        ----------
        None

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.staticCoefficients = (
            TS07DStaticCoefficientsFactory.create(
                TS07DStaticCoefficientsFactory.
                retrieveOriginalBuiltInCoefficientsPath())
        )
        return self

    def withNewStaticCoefficients(self):
        """Use a new set of static coefficients.

        This is an advanced user setting and most users should never call
        this method.

        Uses a precomputed set of static coefficients that were recomputed
        by Grant to have up to M=20, N=20 resolution.

        Parameters
        ----------
        None

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        numAzimuthalExpansions = (
            self.variableCoefficients.getEquatorialCoefficients().
            getLinearCoeffs().get(0).getNumAzimuthalExpansions()
        )
        numRadialExpansions = (
            self.variableCoefficients.getEquatorialCoefficients().
            getLinearCoeffs().get(0).numRadialExpansions
        )
        self.staticCoefficients = TS07DStaticCoefficientsFactory.create(
            TS07DStaticCoefficientsFactory.retrieveNewBuiltInCoefficientsPath(),
            numAzimuthalExpansions, numRadialExpansions)
        return self

    def withStaticCoefficients(self, *args):
        """Assign a new set of static coefficients.
        
        Assign a new set of coefficients.
        
        Parameters
        ----------
        staticCoefficientsDirectory : str
            Path to static coefficients directory.

        Returns
        -------
        self : TS07DModelBuilder
            This object.

        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if isinstance(args[0], str):
            (staticCoefficientsDirectory,) = args
            # By default, the static coefficients are the original set of
            # coefficients. This method allows you to set your own set of
            # static coefficients.
            self.staticCoefficients = TS07DStaticCoefficientsFactory.create(
                staticCoefficientsDirectory)
            return self
        elif isinstance(args[0], ThinCurrentSheetShieldingCoefficients):
            (staticCoefficients,) = args
            # By default, the static coefficients are the original set of
            # coefficients. This method allows you to set your own set of
            # static coefficients.
            self.staticCoefficients = staticCoefficients
            return self
        else:
            raise TypeError

    def withTailLength(self, tailLength):
        """Set the length of the geomagnetic tail.

        This is an advanced user setting and most users should never call
        this method.

        By default, the tail length is 20.0, note, the static coefficients
        and the variable coefficients should have been fit with a model
        that matches the incoming tail length.

        Parameters
        ----------
        tailLength : float
            Tail length, in units of Earth radii.

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.tailLength = tailLength
        return self

    def withTwistParameter(self, twistParameter):
        """Set the twist parameter to the supplied value.

        If this method has been called, the supplied value will OVERRIDE
        the value of the twist parameter that is contained in the supplied
        set of TS07DVariableCoefficients, even if
        withVariableCoefficientValues(TS07DVariableCoefficients) was
        called afterwards.

        Parameters
        ----------
        twistParameter : float
            twistParameter

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.twistParameter = twistParameter
        self.twistParameterSet = True
        return self

    def withNonLinearParameters(self, parameters):
        """Specify a new set of non-linear parameters.

        Specify a new set of non-linear parameters.

        Parameters
        ----------
        parameters : Ts07NonLinearParameters
            New set of nonlinear parameters to use.

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self.parameters = parameters
        return self

    def withMagnetopause(self):
        """Set the magnetopause flag.

        Set the magnetopause flag.

        Parameters
        ----------
        None

        Returns
        -------
        self : TS07DModelBuilder
            This object.
        """
        self._withMagnetopause = True
        return self

    def build(self):
        """Build a new dipole shielding field.
        
        Build a new dipole shielding field.

        Parameters
        ----------
        None

        Returns
        -------
        totalExternalField : VectorField
            The total field computed by the model.
        """
        # Construct the dipole shielding field.
        dipoleShieldingField = (
            BasisVectorFields.asBasisField(
                DipoleShieldingField.createScaled(
                    self.dipoleTiltAngle, self.dynamicPressure,
                    self.variableCoefficients.cfAmplitude
                )
            )
        )

        # If the staticCoeffs are still null, than the user never specified
        # them with one of the withStaticCoeffs methods. By default, they will
        # now be initialized to the original set of TS07D static coefficients.
        if self.staticCoefficients is None:
            self.staticCoefficients = (
                TS07DStaticCoefficientsFactory.create(
                    TS07DStaticCoefficientsFactory.
                    retrieveOriginalBuiltInCoefficientsPath()
                )
            )

        # These are constant across all the current sheets.
        hingeDistance = (
            self.variableCoefficients.equatorialCoeffs.hingeDist
        )
        warpingParam = (
            self.variableCoefficients.equatorialCoeffs.warpingParam
        )
        twistFact = (
            self.variableCoefficients.equatorialCoeffs.twistParam
        )
        region1KappaScaling = (
            self.variableCoefficients.facCoeffs.region1KappaScaling
        )
        region2KappaScaling = (
            self.variableCoefficients.facCoeffs.region2KappaScaling
        )

        # Current sheet thickness.
        currentSheetThicknesses = (
            self.variableCoefficients.nonLinearParameters.currThicks
        )

        # The parameters have been updated.
        if self.parameters is not None:
            hingeDistance = self.parameters.getHingeDist()
            warpingParam = self.parameters.getWarpParam()
            twistFact = self.parameters.getTwistFact()
            region1KappaScaling = self.parameters.getFacRegion1Kappa()
            region2KappaScaling = self.parameters.getFacRegion2Kappa()
            currentSheetThicknesses = (
                self.parameters.getCurrentSheetThicknesses()
            )

        # If the withTwistParameter method has been called, then use the value
        # provided when the method was called. TODO, what if the user calls
        # withTwistParameter and then later calls
        # withVariableCoefficientValues? Wouldn't you expect the last method
        # call to override the previous, this is not what happens.
        if self.twistParameterSet:
            twistFact = self.twistParameter

        currentCoeffs = Ts07EquatorialVariableCoefficients(
            currentSheetThicknesses, hingeDistance, warpingParam, twistFact,
            self.variableCoefficients.equatorialCoeffs.equatorialLinearCoeffs
        )

        equatorialFieldBuilder = Ts07EquatorialMagneticFieldBuilder(
            self.dipoleTiltAngle, self.dynamicPressure, currentCoeffs,
            self.tailLength, self.staticCoefficients
        )

        # If true, the equatorial fields are shielded.
        if self.includeEquatorialShielding:
            equatorialFieldBuilder.withEquatorialShielding()
        else:
            equatorialFieldBuilder.withoutEquatorialShielding()

        # If true, the equatorial fields are deformed using the TA15 instead
        # of the T01 deformation.
        if self._withTA15deformation is not None:
            equatorialFieldBuilder.withTA15deformation(
                self._withTA15deformation
            )

        # The field aligned current.
        fc = self.variableCoefficients.facCoeffs
        fcs = fc.facConfigurations
        fieldAlignedField = Ts07DFieldAlignedMagneticField.create(
            self.dipoleTiltAngle, self.dynamicPressure, region1KappaScaling,
            region2KappaScaling, fcs, True)

        # And finally construct the total model.
        emf = equatorialFieldBuilder.build()
        totalExternalField = BasisVectorFields.concatAll(
            [dipoleShieldingField, emf,
             fieldAlignedField])

        if self._withMagnetopause:
            if self.dipoleTiltAngle == 0:
                magnetopause = T96Magnetopause.createTS07(self.dynamicPressure)
            else:
                magnetopause = T96Magnetopause.createBentTS07(
                    self.dynamicPressure, self.dipoleTiltAngle, hingeDistance)
            return BasisVectorFields.filter(
                totalExternalField, magnetopause, VectorIJK.ZERO)
        return totalExternalField
