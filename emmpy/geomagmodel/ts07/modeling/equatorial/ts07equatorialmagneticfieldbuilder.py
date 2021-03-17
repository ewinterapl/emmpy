"""emmpy.geomagmodel.ts07.modeling.equatorial.ts07equtorialmagneticfieldbuilder"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.magmodel.core.math.bessel.albertbesselfunctionevaluator import (
    AlbertBesselFunctionEvaluator
)
from emmpy.magmodel.core.math.bessel.coltbesselfunctionevaluator import (
    ColtBesselFunctionEvaluator
)

# package geomagmodel.ts07.modeling.equatorial;

# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;
# import static crucible.core.math.CrucibleMath.pow;

# import java.util.OptionalDouble;

# import crucible.core.designpatterns.Builder;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import geomagmodel.t01.deformation.PositionBender;
# import geomagmodel.t01.deformation.TwistWarpFfunction;
# import geomagmodel.ta15.modeling.deformation.DeformationI;
# import geomagmodel.ta15.modeling.deformation.DeformationII;
# import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
# import geomagmodel.ts07.coefficientreader.Ts07EquatorialLinearCoefficients;
# import geomagmodel.ts07.coefficientreader.Ts07EquatorialVariableCoefficients;
# import magmodel.core.math.bessel.AlbertBesselFunctionEvaluator;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.bessel.ColtBesselFunctionEvaluator;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.vectorfields.BasisVectorField;
# import magmodel.core.math.vectorfields.BasisVectorFields;

class Ts07EquatorialMagneticFieldBuilder:
    """A {@link Builder} for constructing the TS07D empirical magnetic field
    model and derivatives of the model.

    @author Nicholas Sharp
    @author G.K.Stephens
    """

    # public class Ts07EquatorialMagneticFieldBuilder implements Builder<BasisVectorField, Exception> {

    #   private double dipoleTiltAngle;
    #   private double dynamicPressure;

    #   private Ts07EquatorialVariableCoefficients coeffs;
    #   private double tailLength;
    #   private ThinCurrentSheetShieldingCoefficients shieldingCoeffs;

    #   /*
    #    * Optional settings
    #    */
    #   private BesselFunctionEvaluator bessel = new ColtBesselFunctionEvaluator();
    #   private boolean includeShield = true;
    #   private OptionalDouble withTA15deformation = OptionalDouble.empty();

    def __init__(self, dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
                 shieldingCoeffs):
        """Constructor

        @param dipoleTiltAngle
        @param dynamicPressure
        @param coeffs
        @param tailLength
        @param shieldingCoeffs
        """
        #   public Ts07EquatorialMagneticFieldBuilder(double dipoleTiltAngle, double dynamicPressure,
        #       Ts07EquatorialVariableCoefficients coeffs, double tailLength,
        #       ThinCurrentSheetShieldingCoefficients shieldingCoeffs) {
        self.dipoleTiltAngle = dipoleTiltAngle
        self.dynamicPressure = dynamicPressure
        self.coeffs = Preconditions.checkNotNull(coeffs)
        self.tailLength = tailLength
        self.shieldingCoeffs = Preconditions.checkNotNull(shieldingCoeffs)
        self.bessel = ColtBesselFunctionEvaluator()
        self.includeShield = True
        self.withTA15deformation = 0

    def withAlbertBessel(self):
        """Use Jay Albert's faster Bessel function evaluator.

        By default, the Bessel function evaluator will be Tsyganenko's, if this
        is set, Jay Albert's Bessel function evaluator will be used instead.
        Jay Albert's implementation is about 4 times faster, although it gives
        slightly different, but negligible, differences.

        @return this builder object
        """
        self.bessel = AlbertBesselFunctionEvaluator(14)
        return self

    def set_withTA15deformation(self, bzIMF):
        """Use the TA15 bending and warping deformation instead of the T01
        bending and warping deformation.

        By default, the model uses the T01 bending and warping deformation.

        @param bzIMF the z-component of the IMF (interplanetary magnetic field)
        averaged over the previous 30 minutes
        @return this builder object
        """
        self.withTA15deformation = bzIMF
        return self

    def withEquatorialShielding(self):
        """Turn on equatorial shielding.

        By default, the equatorial shielding fields are evaluated, so if you
        haven't previously turned them off, you won't need to call this.

        @return this builder object
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

        @return this builder object
        """
        self.includeShield = False
        return self

    def build(self):
        """Builder"""
        numCurrSheets = self.coeffs.getCurrThicks().size()

        #     double hingeDistance = coeffs.getHingeDistance();
        #     double warpingParam = coeffs.getWarpingParam();
        #     double twistParam = coeffs.getTwistParam();

        #     BasisVectorField[] equatorialFields = new BasisVectorField[numCurrSheets];

        #     // loop through each of the current sheets
        #     for (int currSheetIndex = 0; currSheetIndex < numCurrSheets; currSheetIndex++) {

        #       double currSheetThick = coeffs.getCurrThicks().get(currSheetIndex);

        #       Ts07EquatorialLinearCoefficients linearCoeffs = coeffs.getLinearCoeffs().get(currSheetIndex);

        #       /*
        #        * Check the inputs
        #        */
        #       checkArgument(dynamicPressure > 0, "dynamic pressure must be greater than zero");
        #       // check that the number of expansions is consistent
        #       checkArgument(
        #           linearCoeffs.getNumAzimuthalExpansions() == shieldingCoeffs.getNumAzimuthalExpansions(),
        #           "The number of radial expansions for the variable coefficients "
        #               + "is %s, while for the shielding coefficients it is %s",
        #           linearCoeffs.getNumAzimuthalExpansions(), shieldingCoeffs.getNumAzimuthalExpansions());
        #       checkArgument(
        #           linearCoeffs.getNumRadialExpansions() == shieldingCoeffs.getNumRadialExpansions(),
        #           "The number of radial expansions for the variable coefficients "
        #               + "is %s, while for the shielding coefficients it is %s",
        #           linearCoeffs.getNumRadialExpansions(), shieldingCoeffs.getNumRadialExpansions());

        #       // Construct a constant current sheet half thickness
        #       DifferentiableScalarFieldIJ currentSheetHalfThickness =
        #           CurrentSheetHalfThicknesses.createConstant(currSheetThick);

        #       // Construct the shielded thin current sheet
        #       ShieldedThinCurrentSheetField thinCurrentSheet = ShieldedThinCurrentSheetField.createUnity(
        #           currentSheetHalfThickness, tailLength, bessel, shieldingCoeffs, includeShield);

        #       /*
        #        * if the with TA15 deformation was called, apply the TA15 deformation instead of the T01
        #        * deformation
        #        */
        #       BasisVectorField bentWarpedField = thinCurrentSheet;
        #       if (withTA15deformation.isPresent()) {

        #         // warp the shielded thin current sheet
        #         BasisVectorField warpedField = DeformationII.deformBasisField(dipoleTiltAngle,
        #             hingeDistance, warpingParam, twistParam, thinCurrentSheet);

        #         double bzIMF = withTA15deformation.getAsDouble();

        #         // now apply the bending deformation to the warped field
        #         bentWarpedField =
        #             DeformationI.deformBasisField(dipoleTiltAngle, hingeDistance, bzIMF, warpedField);
        #       }
        #       // the T01 deformation (standard for TS07D)
        #       else {

        #         // warp the shielded thin current sheet
        #         BasisVectorField warpedField = TwistWarpFfunction.deformBasisField(dipoleTiltAngle,
        #             warpingParam, twistParam, thinCurrentSheet);

        #         // now apply the bending deformation to the warped field
        #         bentWarpedField =
        #             PositionBender.deformBasisField(dipoleTiltAngle, hingeDistance, warpedField);
        #       }

        #       // Scale position vector for solar wind (see Tsy 2002-1 2.4)
        #       /*
        #        * Note: this is a point of inconsistency with the Fortran code, in the Fortran this
        #        * calculation is done in single precision. When the field values are very large, this can
        #        * result in tenths of differences between the Java and the Fortran version of the model
        #        */
        #       double pdynScaling = pow(dynamicPressure / 2.0, 0.155);
        #       BasisVectorField scaledBentWarpedField =
        #           BasisVectorFields.scaleLocation(bentWarpedField, pdynScaling);

        #       CoefficientExpansion1D coeffs = linearCoeffs.getCoeffs().getAsSingleExpansion();
        #       CoefficientExpansion1D pdynCoeffs =
        #           linearCoeffs.getPdynScaledCoeffs(dynamicPressure).getAsSingleExpansion();

        #       // Finally, expand the coefficients by including a term that includes the dynamical pressure
        #       BasisVectorField equatorialField =
        #           BasisVectorFields.expandCoefficients2(scaledBentWarpedField, coeffs, pdynCoeffs);

        #       equatorialFields[currSheetIndex] = equatorialField;
        #     }

        #     return BasisVectorFields.concatAll(equatorialFields);
        #   }

    # }
