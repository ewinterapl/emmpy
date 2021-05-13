"""emmpy.geomagmodel.ts07.ts07dmodelbuilder"""


# from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
#     ThinCurrentSheetShieldingCoefficients
# )
# from emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils import (
#     TS07DVariableCoefficientsUtils
# )
from emmpy.geomagmodel.ts07.coefficientreader.ts07dstaticcoefficientsfactory import (
    TS07DStaticCoefficientsFactory
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
from emmpy.magmodel.core.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)


class TS07DModelBuilder:
    """A Builder class that can be used to build the TS07D empirical magnetic
    field model.

    This builder lets you customize your creation of the TS07D model. Some of
    the options include the dipole tilt angle, the dynamic pressure, the set of
    static and dynamic coefficients, evaluation of the shielding fields, and
    the model resolution.

    author G.K.Stephens
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, variableCoefficients):
        """Constructor, this is package private as this should be constructed
        using the create methods"""
        self.dipoleTiltAngle = dipoleTiltAngle
        self.dynamicPressure = dynamicPressure
        self.variableCoefficients = variableCoefficients
        self.parameters = None

        # the standard tail length is 20.0 Re
        self.tailLength = 20.0

        # by default the equatorial shielding is included
        self.includeEquatorialShielding = True

        # Constructing the static coefficients is expensive, much more
        # expensive than the model evaluation, so don't construct until/unless
        # necessary. When build is called, if it is still null (i.e. the user
        # never called a withStaticCoeffs method), construct using the default
        # at that time.
        self.staticCoefficients = None

        # by default, do not use Albert's Bessel function evaluator, use
        # Tsyganenko's by default
        self.withAlbertBesselFunction = False

        # by default, we will be consistent with the original FORTRAN code and
        # will not check the magnetopause boundary
        self.withMagnetopause = False

        self.twistParameterSet = None
        self.twistParameter = None
        self.withTA15deformation = None

    @staticmethod
    def create(*args):
        """Creates a new Builder that can be used to construct the TS07D
        model."""
        if len(args) == 3:
            (dipoleTiltAngle, dynamicPressure, variableCoefficients) = args
            # This set of inputs (dipole tilt, dynamic pressure, and
            # variable coefficients) is the minimal set to construct the
            # standard TS07D model. Other customizations to the model are
            # available as methods on the builder.
            # Defaults set: shielding fields ON, static coeffs ORIGINAL
            # param dipoleTiltAngle the dipole tilt angle in radians
            # param dynamicPressure the dynamic pressure of the solar wind
            # param variableCoefficients the set of coefficients for the model
            # return a newly constructed builder
            return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure,
                                     variableCoefficients)
        elif len(args) == 5:
            raise Exception
    #         (dipoleTiltAngle, dynamicPressure, variableCoefficientsFile,
    #          numAzimuthalExpansions, numRadialExpansions,
    #          facConfiguration) = args
    #         # Creates a new Builder that can be used to construct the TS07D
    #         # model with a different equatorial resolution than M=4, N=5.
    #         # param dipoleTiltAngle the dipole tilt angle in radians
    #         # param dynamicPressure the dynamic pressure of the solar wind
    #         # param variableCoefficients the set of coefficients for the model
    #         # param numAzimuthalExpansions the number of equatorial azimuthal
    #         # expansions (M)
    #         # param numRadialExpansions the number of equatorial radial
    #         # expansions (N)

    #         # this will throw a runtime exception if the input number of
    #         # expansions doesn't match the size of the file
    #         coeffs = TS07DVariableCoefficientsUtils.create(
    #             variableCoefficientsFile, numAzimuthalExpansions,
    #             numRadialExpansions, facConfiguration)
    #         return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs)
        else:
            raise Exception

    # @staticmethod
    # def createStandardResolution(dipoleTiltAngle, dynamicPressure,
    #                              variableCoefficientsFile, facConfiguration):
    #     numAzimuthalExpansions = 4
    #     numRadialExpansions = 5

    #     # this will throw a runtime exception if the input number of expansions
    #     # doesn't match the size of the file
    #     coeffs = TS07DVariableCoefficientsUtils.create(
    #         variableCoefficientsFile, numAzimuthalExpansions,
    #         numRadialExpansions, facConfiguration)
    #     return TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs)

    # def withDipoleTiltAngleValue(self, dipoleTiltAngle):
    #     """Replaces the initial dipole tilt angle with the supplied value.

    #     param dipoleTiltAngle a new dipole tilt angle to use when building
    #     the model

    #     return this builder object
    #     """
    #     self.dipoleTiltAngle = dipoleTiltAngle
    #     return self

    # def withDynamicPressureValue(self, dynamicPressure):
    #     """Replaces the initial dynamic pressure with the supplied value.

    #     param dynamicPressure a new dynamic pressure to use when building the
    #     model

    #     return this builder object
    #     """
    #     self.dynamicPressure = dynamicPressure
    #     return self

    # def withVariableCoefficientValues(self, variableCoefficients):
    #     """Replaces the initial set of variable coefficients with the supplied
    #     set.

    #     NOTE, this will not override the value of the twist angle if the
    #     withTwistParameter(double)} was called.

    #     param TS07DVariableCoefficients a new set of variable coefficients to
    #     use when building the model

    #     preturn this builder object
    #     """
    #     self.variableCoefficients = variableCoefficients
    #     return self

    # def withEquatorialShielding(self):
    #     """By default, the equatorial shielding fields are evaluated, so if you
    #     haven't previously turned them off, you won't need to call this.

    #     return this builder object
    #     """
    #     self.includeEquatorialShielding = True
    #     return self

    # def withoutEquatorialShielding(self):
    #     """By default, the equatorial shielding fields are evaluated.

    #     Evaluating the shielding of the equatorial fields, is about 90% of the
    #     computation time required of the model. Since they are not needed in
    #     all applications, like computing the current density inside the
    #     magnetopause, the option to turn them off can significantly speed up
    #     the code.

    #     return this builder object
    #     """
    #     self.includeEquatorialShielding = False
    #     return self

    # def withAlbertBessel(self):
    #     """Use Jay Albert's faster Bessel function evaluator.

    #     By default, the Bessel function evaluator will be Tsyganenko's, if this
    #     is set, Jay Albert's Bessel function evaluator will be used instead.
    #     Jay Albert's implementation is about 4 times faster, although it gives
    #     slightly different, but negligible, differences.

    #     return this builder object
    #     """
    #     self.withAlbertBesselFunction = True
    #     return self

    # def withoutAlbertBessel(self):
    #     """Use Tsyganenko's default Bessel function evaluator.

    #     By default, the Bessel function evaluator will be Tsyganenko's, if this
    #     is set, Jay Albert's Bessel function evaluator will be used instead.
    #     Jay Albert's implementation is about 4 times faster, although it gives
    #     slightly different, but negligible, differences.

    #     return this builder object
    #     """
    #     self.withAlbertBesselFunction = False
    #     return self

    # def withTA15deformation(self, bzIMF):
    #     """Use the TA15 bending and warping deformation instead of the T01
    #     bending and warping deformation for the equatorial field,

    #     By default, the model uses the T01 bending and warping deformation.

    #     param bzIMF the z-component of the IMF (interplanetary magnetic field)
    #     averaged over the previous 30 minutes
    #     return this builder object
    #     """
    #     self.withTA15deformation = bzIMF
    #     return self

    # def withOriginalStaticCoefficients(self):
    #     """Use the original set of static coefficients, this is the default
    #     set, so if you haven't changed them overridden them with another
    #     method, it is unnecessary to call this method.

    #     This set has resolution up to M=6, N=8, so if you want higher
    #     resolution than this, you must use a different set of coefficients.

    #     return this builder object
    #     """
    #     self.staticCoefficients = (
    #         TS07DStaticCoefficientsFactory.create(
    #             TS07DStaticCoefficientsFactory.
    #             retrieveOriginalBuiltInCoefficientsPath())
    #     )
    #     return self

    # def withNewStaticCoefficients(self):
    #     """This is an advanced user setting and most users should never call
    #     this method.

    #     Uses a precomputed set of static coefficients that were recomputed by
    #     Grant to have up to M=20, N=20 resolution.

    #     return this builder object
    #     """
    #     numAzimuthalExpansions = (
    #         self.variableCoefficients.getEquatorialCoefficients().
    #         getLinearCoeffs().get(0).getNumAzimuthalExpansions()
    #     )
    #     numRadialExpansions = (
    #         self.variableCoefficients.getEquatorialCoefficients().
    #         getLinearCoeffs().get(0).getNumRadialExpansions()
    #     )
    #     self.staticCoefficients = TS07DStaticCoefficientsFactory.create(
    #         TS07DStaticCoefficientsFactory.
    #         retrieveNewBuiltInCoefficientsPath(),
    #         numAzimuthalExpansions, numRadialExpansions)
    #     return self

    # def withStaticCoefficients(self, *args):
    #     if isinstance(args[0], str):
    #         (staticCoefficientsDirectory,) = args
    #         # By default, the static coefficients are the original set of
    #         # coefficients.
    #         # This method allows you to set your own set of static
    #         # coefficients.
    #         # param staticCoefficientsDirectory
    #         # return this builder object
    #         self.staticCoefficients = TS07DStaticCoefficientsFactory.create(
    #             staticCoefficientsDirectory)
    #         return self
    #     elif isinstance(args[0], ThinCurrentSheetShieldingCoefficients):
    #         (staticCoefficients,) = args
    #         # By default, the static coefficients are the original set of
    #         # coefficients. This method allows you to set your own set of
    #         # static coefficients.
    #         # param staticCoefficientsDirectory
    #         # return this builder object
    #         self.staticCoefficients = staticCoefficients
    #         return self
    #     else:
    #         raise Exception

    # def withTailLength(self, tailLength):
    #     """This is an advanced user setting and most users should never call
    #     this method.

    #     By default, the tail length is 20.0, note, the static coefficients and
    #     the variable coefficients should have been fit with a model that
    #     matches the incoming tail length.

    #     param tailLength
    #     return this builder object
    #     """
    #     self.tailLength = tailLength
    #     return self

    # def withTwistParameter(self, twistParameter):
    #     """Sets the twist parameter to the supplied value.

    #     If this method has been called, the supplied value will OVERRIDE the
    #     value of the twist parameter that is contained in the supplied set of
    #     TS07DVariableCoefficients, even if the
    #     withVariableCoefficientValues(TS07DVariableCoefficients)}was called
    #     afterwards.

    #     param twistParameter
    #     return this builder object
    #     """
    #     self.twistParameter = twistParameter
    #     self.twistParameterSet = True
    #     return self

    # def withNonLinearParameters(self, parameters):
    #     self.parameters = parameters
    #     return self

    # def withMagnetopause(self):
    #     self.withMagnetopause = True
    #     return self

    def build(self):

        # construct the dipole shielding field
        dipoleShieldingField = (
            BasisVectorFields.asBasisField(
                DipoleShieldingField.createScaled(
                    self.dipoleTiltAngle, self.dynamicPressure,
                    self.variableCoefficients.getDipoleShieldingAmplitude()
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

        # these are constant across all the current sheets
        hingeDistance = (
            self.variableCoefficients.getEquatorialCoefficients().
            getHingeDistance()
        )
        warpingParam = (
            self.variableCoefficients.getEquatorialCoefficients().
            getWarpingParam()
        )
        twistFact = (
            self.variableCoefficients.getEquatorialCoefficients().
            getTwistParam()
        )
        region1KappaScaling = (
            self.variableCoefficients.getFacCoefficients().
            getRegion1KappaScaling()
        )
        region2KappaScaling = (
            self.variableCoefficients.getFacCoefficients().
            getRegion2KappaScaling()
        )

        # Current sheet thickness
        currentSheetThicknesses = (
            self.variableCoefficients.getNonLinearParameters().
            getCurrentSheetThicknesses()
        )
        numCurrSheets = (
            len(self.variableCoefficients.getNonLinearParameters().
                getCurrentSheetThicknesses())
        )

        # The parameters have been updated
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
            self.variableCoefficients.getEquatorialCoefficients().
            getLinearCoeffs()
        )

        equatorialFieldBuilder = Ts07EquatorialMagneticFieldBuilder(
            self.dipoleTiltAngle, self.dynamicPressure, currentCoeffs,
            self.tailLength, self.staticCoefficients
        )

        # If true, use Jay Albert's Bessel function evaluator
        if self.withAlbertBesselFunction:
            equatorialFieldBuilder.withAlbertBessel()

        # If true, the equatorial fields are shielded
        if self.includeEquatorialShielding:
            equatorialFieldBuilder.withEquatorialShielding()
        else:
            equatorialFieldBuilder.withoutEquatorialShielding()

        # If true, the equatorial fields are deformed using the TA15 instead
        # of the T01 deformation
        if self.withTA15deformation is not None:
            equatorialFieldBuilder.withTA15deformation(
                self.withTA15deformation
            )

        # The field aligned current
        # self.variableCoefficients is a TS07DVariableCoefficients
        fc = self.variableCoefficients.getFacCoefficients()
        fcs = fc.getFacConfigurations()
        fieldAlignedField = Ts07DFieldAlignedMagneticField.create(
            self.dipoleTiltAngle, self.dynamicPressure, region1KappaScaling,
            region2KappaScaling, fcs, True)

        # and finally construct the total model
        totalExternalField = BasisVectorFields.concatAll(
            [dipoleShieldingField, equatorialFieldBuilder.build(),
             fieldAlignedField])

        if self.withMagnetopause:
            if self.dipoleTiltAngle == 0:
                raise Exception
    #             magnetopause = T96Magnetopause.createTS07(self.dynamicPressure)
            else:
                raise Exception
    #             magnetopause = T96Magnetopause.createBentTS07(
    #                 self.dynamicPressure, self.dipoleTiltAngle, hingeDistance)
    #         return BasisVectorFields.filter(
    #             totalExternalField, magnetopause, VectorIJK.ZERO)
        return totalExternalField
