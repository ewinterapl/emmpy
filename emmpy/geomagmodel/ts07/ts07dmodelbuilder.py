"""emmpy.geomagmodel.ts07.ts07modelbuilder"""

# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;

# import java.nio.file.Path;
# import java.util.List;
# import java.util.OptionalDouble;

# import com.google.common.base.Predicate;

# import crucible.core.designpatterns.Builder;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import geomagmodel.T96Magnetopause;
# import geomagmodel.ts07.coefficientreader.FacConfiguration;
# import geomagmodel.ts07.coefficientreader.TS07DStaticCoefficientsFactory;
# import geomagmodel.ts07.coefficientreader.TS07DVariableCoefficients;
# import geomagmodel.ts07.coefficientreader.TS07DVariableCoefficientsUtils;
# import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
# import geomagmodel.ts07.coefficientreader.Ts07EquatorialVariableCoefficients;
# import geomagmodel.ts07.coefficientreader.Ts07NonLinearParameters;
# import geomagmodel.ts07.modeling.dipoleshield.DipoleShieldingField;
# import geomagmodel.ts07.modeling.equatorial.Ts07EquatorialMagneticFieldBuilder;
# import geomagmodel.ts07.modeling.fieldaligned.Ts07DFieldAlignedMagneticField;
# import magmodel.core.math.vectorfields.BasisVectorField;
# import magmodel.core.math.vectorfields.BasisVectorFields;


from emmpy.crucible.core.designpatterns.builder import Builder


class TS07DModelBuilder(Builder):
    pass

# /**
#  * A {@link Builder} class that can be used to build the TS07D empirical magnetic field model.
#  * <p>
#  * This builder let's you customize your creation of the TS07D model. Some of the options include
#  * the dipole tilt angle, the dynamic pressure, the set of static and dynamic coefficients,
#  * evaluation of the shielding fields, and the model resolution.
#  *
#  * @author G.K.Stephens
#  *
#  */
# public class TS07DModelBuilder implements Builder<VectorField, Exception> {

#   private double dipoleTiltAngle;
#   private double dynamicPressure;

#   private TS07DVariableCoefficients variableCoefficients;
#   private Ts07NonLinearParameters parameters;

#   private boolean twistParameterSet = false;
#   private double twistParameter;

#   private double tailLength;
#   private boolean includeEquatorialShielding;

#   private ThinCurrentSheetShieldingCoefficients staticCoefficients;

#   private boolean withAlbertBessel;
#   private OptionalDouble withTA15deformation = OptionalDouble.empty();

#   private boolean withMagnetopause;

#   /**
#    * Constructor, this is package private as this should be constructed using the create methods
#    *
#    * @param dipoleTiltAngle
#    * @param dynamicPressure
#    * @param variableCoefficients
#    */
#   TS07DModelBuilder(double dipoleTiltAngle, double dynamicPressure,
#       TS07DVariableCoefficients variableCoefficients) {

#     this.dipoleTiltAngle = dipoleTiltAngle;
#     this.dynamicPressure = dynamicPressure;

#     includeEquatorialShielding = true;

#     this.variableCoefficients = variableCoefficients;
#     this.parameters = null;

#     // the standard tail length is 20.0 Re
#     this.tailLength = 20.0;

#     // by default the equatorial shielding is included
#     this.includeEquatorialShielding = true;

#     /*
#      * Constructing the static coefficients is expensive, much more expensive than the model
#      * evaluation, so don't construct until/unless necessary. When build is called, if it is still
#      * null (i.e. the user never called a withStaticCoeffs method), construct using the default at
#      * that time.
#      */
#     this.staticCoefficients = null;

#     // by default, do not use Albert's Bessel function evaluator, use Tsyganenko's by default
#     this.withAlbertBessel = false;

#     // by default, we will be consistent with the original FORTRAN code and will not check the
#     // magnetopause boundary
#     this.withMagnetopause = false;
#   }

#   /**
#    * Creates a new Builder that can be used to construct the TS07D model.
#    * <p>
#    * This set of inputs (dipole tilt, dynamic pressure, and variable coefficients) is the minimal
#    * set to construct the standard TS07D model. Other customizations to the model are available as
#    * methods on the builder.
#    * <p>
#    * Defaults set: shielding fields ON, static coeffs ORIGINAL
#    *
#    * @param dipoleTiltAngle the dipole tilt angle in radians
#    * @param dynamicPressure the dynamic pressure of the solar wind
#    * @param variableCoefficients the set of coefficients for the model
#    *
#    * @return a newly constructed builder
#    */
#   public static TS07DModelBuilder create(double dipoleTiltAngle, double dynamicPressure,
#       TS07DVariableCoefficients variableCoefficients) {
#     return new TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, variableCoefficients);
#   }

#   /**
#    * Creates a new Builder that can be used to construct the TS07D model with a different equatorial
#    * resolution than M=4, N=5.
#    *
#    * @param dipoleTiltAngle the dipole tilt angle in radians
#    * @param dynamicPressure the dynamic pressure of the solar wind
#    * @param variableCoefficients the set of coefficients for the model
#    * @param numAzimuthalExpansions the number of equatorial azimuthal expansions (M)
#    * @param numRadialExpansions the number of equatorial radial expansions (N)
#    * @return
#    */
#   public static TS07DModelBuilder create(double dipoleTiltAngle, double dynamicPressure,
#       Path variableCoefficientsFile, int numAzimuthalExpansions, int numRadialExpansions,
#       FacConfiguration facConfiguration) {

#     // this will throw a runtime exception if the input number of expansions
#     // doesn't match the size of the file
#     TS07DVariableCoefficients coeffs = TS07DVariableCoefficientsUtils.create(
#         variableCoefficientsFile, numAzimuthalExpansions, numRadialExpansions, facConfiguration);

#     return new TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs);
#   }

#   /**
#    *
#    * @param dipoleTiltAngle
#    * @param dynamicPressure
#    * @param variableCoefficientsFile
#    * @param numAzimuthalExpansions
#    * @param numRadialExpansions
#    * @return
#    */
#   public static TS07DModelBuilder createStandardResolution(double dipoleTiltAngle,
#       double dynamicPressure, Path variableCoefficientsFile, FacConfiguration facConfiguration) {

#     int numAzimuthalExpansions = 4;
#     int numRadialExpansions = 5;

#     // this will throw a runtime exception if the input number of expansions
#     // doesn't match the size of the file
#     TS07DVariableCoefficients coeffs = TS07DVariableCoefficientsUtils.create(
#         variableCoefficientsFile, numAzimuthalExpansions, numRadialExpansions, facConfiguration);

#     return new TS07DModelBuilder(dipoleTiltAngle, dynamicPressure, coeffs);
#   }

#   /**
#    * Replaces the initial dipole tilt angle with the supplied value.
#    *
#    * @param dipoleTiltAngle a new dipole tilt angle to use when building the model
#    * 
#    * @return this builder object
#    */
#   public TS07DModelBuilder withDipoleTiltAngleValue(double dipoleTiltAngle) {

#     this.dipoleTiltAngle = dipoleTiltAngle;

#     return this;
#   }

#   /**
#    * Replaces the initial dynamic pressure with the supplied value.
#    *
#    * @param dynamicPressure a new dynamic pressure to use when building the model
#    * 
#    * @return this builder object
#    */
#   public TS07DModelBuilder withDynamicPressureValue(double dynamicPressure) {

#     this.dynamicPressure = dynamicPressure;

#     return this;
#   }

#   /**
#    * Replaces the initial set of variable coefficients with the supplied set. NOTE, this will not
#    * override the value of the twist angle if the {@link #withTwistParameter(double)} was called.
#    * 
#    * @param TS07DVariableCoefficients a new set of variable coefficients to use when building the
#    *        model
#    * 
#    * @return this builder object
#    */
#   public TS07DModelBuilder withVariableCoefficientValues(
#       TS07DVariableCoefficients variableCoefficients) {

#     this.variableCoefficients = variableCoefficients;

#     return this;
#   }

#   /**
#    * By default, the equatorial shielding fields are evaluated, so if you haven't previously turned
#    * them off, you won't need to call this.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withEquatorialShielding() {
#     includeEquatorialShielding = true;
#     return this;
#   }

#   /**
#    * By default, the equatorial shielding fields are evaluated. Evaluating the shielding of the
#    * equatorial fields, is about 90% of the computation time required of the model. Since they are
#    * not needed in all applications, like computing the current density inside the magnetopause, the
#    * option to turn them off can significantly speed up the code.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withoutEquatorialShielding() {
#     includeEquatorialShielding = false;
#     return this;
#   }

#   /**
#    * Use Jay Albert's faster Bessel function evaluator.
#    * <p>
#    * By default, the Bessel function evaluator will be Tsyganenko's, if this is set, Jay Albert's
#    * Bessel function evaluator will be used instead. Jay Albert's implementation is about 4 times
#    * faster, although it gives slightly different, but negligible, differences.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withAlbertBessel() {
#     withAlbertBessel = true;
#     return this;
#   }

#   /**
#    * Use Tsyganenko's default Bessel function evaluator.
#    * <p>
#    * By default, the Bessel function evaluator will be Tsyganenko's, if this is set, Jay Albert's
#    * Bessel function evaluator will be used instead. Jay Albert's implementation is about 4 times
#    * faster, although it gives slightly different, but negligible, differences.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withoutAlbertBessel() {
#     withAlbertBessel = false;
#     return this;
#   }

#   /**
#    * Use the TA15 bending and warping deformation instead of the T01 bending and warping deformation
#    * for the equatorial field,
#    * <p>
#    * By default, the model uses the T01 bending and warping deformation.
#    * 
#    * @param bzIMF the z-component of the IMF (interplanetary magnetic field) averaged over the
#    *        previous 30 minutes
#    * @return this builder object
#    */
#   public TS07DModelBuilder withTA15deformation(double bzIMF) {
#     withTA15deformation = OptionalDouble.of(bzIMF);
#     return this;
#   }

#   /**
#    * Use the original set of static coefficients, this is the default set, so if you haven't changed
#    * them overridden them with another method, it is unnecessary to call this method.
#    * <p>
#    * This set has resolution up to M=6, N=8, so if you want higher resolution than this, you must
#    * use a different set of coefficients.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withOriginalStaticCoefficients() {
#     // TODO add checking
#     this.staticCoefficients = TS07DStaticCoefficientsFactory
#         .create(TS07DStaticCoefficientsFactory.retrieveOriginalBuiltInCoefficientsPath());
#     return this;
#   }

#   /**
#    * This is an advanced user setting and most users should never call this method.
#    * <p>
#    * Uses a precomputed set of static coefficients that were recomputed by Grant to have up to M=20,
#    * N=20 resolution.
#    *
#    * @return this builder object
#    */
#   public TS07DModelBuilder withNewStaticCoefficients() {
#     // TODO add checking

#     int numAzimuthalExpansions = variableCoefficients.getEquatorialCoefficients().getLinearCoeffs()
#         .get(0).getNumAzimuthalExpansions();
#     int numRadialExpansions = variableCoefficients.getEquatorialCoefficients().getLinearCoeffs()
#         .get(0).getNumRadialExpansions();

#     this.staticCoefficients = TS07DStaticCoefficientsFactory.create(
#         TS07DStaticCoefficientsFactory.retrieveNewBuiltInCoefficientsPath(), numAzimuthalExpansions,
#         numRadialExpansions);
#     return this;
#   }

#   /**
#    * By default, the static coefficients are the original set of coefficients. This method allows
#    * you to set your own set of static coefficients.
#    *
#    * @param staticCoefficientsDirectory
#    * @return this builder object
#    */
#   public TS07DModelBuilder withStaticCoefficients(Path staticCoefficientsDirectory) {
#     this.staticCoefficients = TS07DStaticCoefficientsFactory.create(staticCoefficientsDirectory);
#     return this;
#   }

#   /**
#    * By default, the static coefficients are the original set of coefficients. This method allows
#    * you to set your own set of static coefficients.
#    *
#    * @param staticCoefficientsDirectory
#    * @return this builder object
#    */
#   public TS07DModelBuilder withStaticCoefficients(
#       ThinCurrentSheetShieldingCoefficients staticCoefficients) {
#     this.staticCoefficients = staticCoefficients;
#     return this;
#   }

#   /**
#    * This is an advanced user setting and most users should never call this method.
#    * <p>
#    * By default, the tail length is 20.0, note, the static coefficients and the variable
#    * coefficients should have been fit with a model that matches the incoming tail length.
#    *
#    * @param tailLength
#    * @return this builder object
#    */
#   public TS07DModelBuilder withTailLength(double tailLength) {
#     this.tailLength = tailLength;
#     return this;
#   }

#   /**
#    * Sets the twist parameter to the supplied value.
#    * <p>
#    * If this method has been called, the supplied value will OVERRIDE the value of the twist
#    * parameter that is contained in the supplied set of {@link TS07DVariableCoefficients}, even if
#    * the {@link #withVariableCoefficientValues(TS07DVariableCoefficients)} was called afterwards.
#    * 
#    * @param twistParameter
#    * @return this builder object
#    */
#   public TS07DModelBuilder withTwistParameter(double twistParameter) {
#     this.twistParameter = twistParameter;
#     this.twistParameterSet = true;
#     return this;
#   }

#   public TS07DModelBuilder withNonLinearParameters(Ts07NonLinearParameters parameters) {
#     this.parameters = checkNotNull(parameters);
#     return this;
#   }

#   /**
#    * 
#    * @return
#    */
#   public TS07DModelBuilder withMagnetopause() {
#     this.withMagnetopause = true;
#     return this;
#   }

#   /**
#    *
#    */
#   @Override
#   public BasisVectorField build() {

#     // construct the dipole shielding field
#     BasisVectorField dipoleShieldingField =
#         BasisVectorFields.asBasisField(DipoleShieldingField.createScaled(dipoleTiltAngle,
#             dynamicPressure, variableCoefficients.getDipoleShieldingAmplitude()));

#     /*
#      * If the staticCoeffs are still null, than the user never specified them with one of the
#      * withStaticCoeffs methods. By default, they will now be initialized to the original set of
#      * TS07D static coefficients.
#      */
#     if (staticCoefficients == null) {
#       this.staticCoefficients = TS07DStaticCoefficientsFactory
#           .create(TS07DStaticCoefficientsFactory.retrieveOriginalBuiltInCoefficientsPath());
#     }

#     // these are constant across all the current sheets
#     double hingeDistance = variableCoefficients.getEquatorialCoefficients().getHingeDistance();
#     double warpingParam = variableCoefficients.getEquatorialCoefficients().getWarpingParam();
#     double twistFact = variableCoefficients.getEquatorialCoefficients().getTwistParam();

#     double region1KappaScaling = variableCoefficients.getFacCoefficients().getRegion1KappaScaling();
#     double region2KappaScaling = variableCoefficients.getFacCoefficients().getRegion2KappaScaling();

#     /*
#      * Current sheet thickness
#      */
#     List<Double> currentSheetThicknesses =
#         variableCoefficients.getNonLinearParameters().getCurrentSheetThicknesses();
#     int numCurrSheets =
#         variableCoefficients.getNonLinearParameters().getCurrentSheetThicknesses().size();

#     /*
#      * The parameters have been updated
#      */
#     if (parameters != null) {
#       hingeDistance = parameters.getHingeDist();
#       warpingParam = parameters.getWarpParam();
#       twistFact = parameters.getTwistFact();
#       region1KappaScaling = parameters.getFacRegion1Kappa();
#       region2KappaScaling = parameters.getFacRegion2Kappa();
#       checkArgument(numCurrSheets == parameters.getCurrentSheetThicknesses().size());
#       currentSheetThicknesses = parameters.getCurrentSheetThicknesses();
#     }

#     /*
#      * If the withTwistParameter method has been called, then use the value provided when the method
#      * was called. TODO, what if the user calls withTwistParameter and then later calls
#      * withVariableCoefficientValues? Wouldn't you expect the last method call to override the
#      * previous, this is not what happens.
#      */
#     if (twistParameterSet) {
#       twistFact = twistParameter;
#     }

#     Ts07EquatorialVariableCoefficients currentCoeffs =
#         new Ts07EquatorialVariableCoefficients(currentSheetThicknesses, hingeDistance, warpingParam,
#             twistFact, variableCoefficients.getEquatorialCoefficients().getLinearCoeffs());

#     Ts07EquatorialMagneticFieldBuilder equatorialFieldBuilder =
#         new Ts07EquatorialMagneticFieldBuilder(dipoleTiltAngle, dynamicPressure, currentCoeffs,
#             tailLength, staticCoefficients);

#     /*
#      * If true, use Jay Albert's Bessel function evaluator
#      */
#     if (withAlbertBessel) {
#       equatorialFieldBuilder.withAlbertBessel();
#     }

#     /*
#      * If true, the equatorial fields are shielded
#      */
#     if (includeEquatorialShielding) {
#       equatorialFieldBuilder.withEquatorialShielding();
#     } else {
#       equatorialFieldBuilder.withoutEquatorialShielding();
#     }

#     /*
#      * If true, the equatorial fields are deformed using the TA15 instead of the T01 deformation
#      */
#     if (withTA15deformation.isPresent()) {
#       equatorialFieldBuilder.withTA15deformation(withTA15deformation.getAsDouble());
#     }

#     /*
#      * The field aligned current
#      */
#     Ts07DFieldAlignedMagneticField fieldAlignedField = Ts07DFieldAlignedMagneticField.create(
#         dipoleTiltAngle, dynamicPressure, region1KappaScaling, region2KappaScaling,
#         variableCoefficients.getFacCoefficients().getFacConfigurations(), true);

#     // and finally construct the total model
#     BasisVectorField totalExternalField = BasisVectorFields.concatAll(dipoleShieldingField,
#         equatorialFieldBuilder.build(), fieldAlignedField);

#     if (withMagnetopause) {
#       Predicate<UnwritableVectorIJK> magnetopause = (dipoleTiltAngle == 0.0)
#           ? T96Magnetopause.createTS07(dynamicPressure)
#           : T96Magnetopause.createBentTS07(dynamicPressure, dipoleTiltAngle, hingeDistance);

#       return BasisVectorFields.filter(totalExternalField, magnetopause, VectorIJK.ZERO);
#     }

#     return totalExternalField;
#   }
# }
