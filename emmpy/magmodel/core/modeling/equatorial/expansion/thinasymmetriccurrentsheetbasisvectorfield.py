"""emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield"""

# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;
# import static magmodel.core.math.expansions.Expansion1Ds.createFromArray;
# import static magmodel.core.math.expansions.Expansion2Ds.createFromArray;
# import static magmodel.core.math.expansions.Expansion2Ds.createNull;

# import com.google.common.collect.ImmutableList;

# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.vectorfields.BasisVectorField;

class ThinAsymmetricCurrentSheetBasisVectorField:
    # /**
    #  * This module described the tail fields as stated in Tsyganenko and Sitnov 2007 "Magnetospheric
    #  * configurations from a high-resolution data-based magnetic fields model", eq. 14.
    #  * <p>
    #  * <img src="./doc-files/ts07_eq_14.png" />
    #  * <p>
    #  * This is equivalent to the FORTRAN subroutine:
    #  * <p>
    #  * <pre>
    #  *      SUBROUTINE UNWARPED (X,Y,Z,BXS,BYS,BZS,BXO,BYO,BZO,BXE,BYE,BZE)
    #  *</pre>
    #  *
    #  * @author G.K.Stephens
    #  *
    #  */
    # public class ThinAsymmetricCurrentSheetBasisVectorField implements VectorField, BasisVectorField {

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs, bessel):
        """Constructor"""
        pass

    def evaluate(self, pos):
        pass

    #   private final int numAzimuthalExpansions;
    #   private final int numRadialExpansions;

    #   private final double tailLength;

    #   private final DifferentiableScalarFieldIJ currentSheetHalfThickness;
    #   private final BesselFunctionEvaluator bessel;

    #   private final TailSheetCoefficients coeffs;

    #   /**
    #    * Constructor for:
    #    * <p>
    #    * <img src="./doc-files/ts07_eq_14.png" />
    #    *
    #    * @param tailLength
    #    * @param currentSheetHalfThickness
    #    * @param bessel
    #    */
    #   public ThinAsymmetricCurrentSheetBasisVectorField(double tailLength,
    #       final DifferentiableScalarFieldIJ currentSheetHalfThickness, TailSheetCoefficients coeffs,
    #       BesselFunctionEvaluator bessel) {

    #     // checkArgument(tailLength > 0.0, "Tail length must be greater than zero, it was %s", tailLength);

    #     // this.coeffs = checkNotNull(coeffs);
    #     this.coeffs = coeffs;

    #     this.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions();
    #     this.numRadialExpansions = coeffs.getNumRadialExpansions();

    #     this.tailLength = tailLength;

    #     // this.currentSheetHalfThickness = checkNotNull(currentSheetHalfThickness);
    #     this.currentSheetHalfThickness = currentSheetHalfThickness;
    #     // this.bessel = checkNotNull(bessel);
    #     this.bessel = bessel;
    #   }

    #   /**
    #    * Creates a {@link ThinAsymmetricCurrentSheetBasisVectorField} where all the coefficients have
    #    * been set to 1.
    #    * <p>
    #    * <img src="./doc-files/ts07_eq_14.png" />
    #    * <p>
    #    * 
    #    * @param tailLength
    #    * @param currentSheetHalfThickness
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @param bessel
    #    * @return
    #    */
    #   public static ThinAsymmetricCurrentSheetBasisVectorField createUnity(double tailLength,
    #       final DifferentiableScalarFieldIJ currentSheetHalfThickness, int numAzimuthalExpansions,
    #       int numRadialExpansions, BesselFunctionEvaluator bessel) {

    #     TailSheetCoefficients coeffs =
    #         TailSheetCoefficients.createUnity(numAzimuthalExpansions, numRadialExpansions);

    #     return new ThinAsymmetricCurrentSheetBasisVectorField(tailLength, currentSheetHalfThickness,
    #         coeffs, bessel);
    #   }

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #     return buffer.setTo(evaluateExpansions(location).sum());
    #   }

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {
    #     return evaluateExpansions(location).getExpansionsAsList();
    #   }

    #   /**
    #    * This guy recalculates everything
    #    * 
    #    * @param positionVector
    #    * @param dipoleTilt
    #    * @param dynamicPressure
    #    * @param includeShield
    #    */
    #   public TailSheetExpansions evaluateExpansions(UnwritableVectorIJK location) {

    #     UnwritableVectorIJK[] symmetricExpansions = new UnwritableVectorIJK[numRadialExpansions];
    #     UnwritableVectorIJK[][] oddExpansions =
    #         new UnwritableVectorIJK[numAzimuthalExpansions][numRadialExpansions];
    #     UnwritableVectorIJK[][] evenExpansions =
    #         new UnwritableVectorIJK[numAzimuthalExpansions][numRadialExpansions];

    #     // n is the radial expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       // Calculate the wave number (kn = n/rho0)
    #       double kn = n / tailLength;

    #       VectorField symBasisFunction =
    #           new TailSheetSymmetricExpansion(kn, currentSheetHalfThickness, bessel);

    #       double a = coeffs.getTailSheetSymmetricValues().getCoefficient(n);

    #       symmetricExpansions[n - 1] = symBasisFunction.evaluate(location).scale(a);

    #       // m is the azimuthal expansion number
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {

    #         double aOdd = coeffs.getTailSheetOddValues().getCoefficient(m, n);
    #         VectorField oddBasisFunction = new TailSheetAsymmetricExpansion(kn, m, TrigParity.ODD,
    #             currentSheetHalfThickness, bessel);
    #         oddExpansions[m - 1][n - 1] = oddBasisFunction.evaluate(location).scale(aOdd);

    #         double aEven = coeffs.getTailSheetEvenValues().getCoefficient(m, n);
    #         VectorField evenBasisFunction = new TailSheetAsymmetricExpansion(kn, m, TrigParity.EVEN,
    #             currentSheetHalfThickness, bessel);
    #         evenExpansions[m - 1][n - 1] = evenBasisFunction.evaluate(location).scale(aEven);

    #       }

    #     }

    #     if (numAzimuthalExpansions == 0) {
    #       return new TailSheetExpansions(createFromArray(symmetricExpansions, 1),
    #           createNull(1, 1, numRadialExpansions), createNull(1, 1, numRadialExpansions));
    #     }

    #     return new TailSheetExpansions(createFromArray(symmetricExpansions, 1),
    #         createFromArray(oddExpansions, 1, 1), createFromArray(evenExpansions, 1, 1));
    #   }

    #   public int getNumAzimuthalExpansions() {
    #     return numAzimuthalExpansions;
    #   }

    #   public int getNumRadialExpansions() {
    #     return numRadialExpansions;
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return numRadialExpansions + 2 * numRadialExpansions * numAzimuthalExpansions;
    #   }

    # }
