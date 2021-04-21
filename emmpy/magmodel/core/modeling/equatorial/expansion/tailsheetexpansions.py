"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions"""

# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import magmodel.core.math.expansions.Expansion1D;
# import magmodel.core.math.expansions.Expansion1Ds;
# import magmodel.core.math.expansions.Expansion2D;
# import magmodel.core.math.expansions.Expansion2Ds;
# import magmodel.core.math.vectorfields.BasisVectorField;


class TailSheetExpansions:
    pass

    # /**
    #  * A container for the Basis functions expansion of a thin current sheet, i.e. it represents the
    #  * individual basis functions in the following summation:
    #  * <p>
    #  * <img src="./doc-files/ts07_eq_16.png" /> <img src="./doc-files/ts07_eq_17.png" />
    #  * 
    #  * @author G.K.Stephens
    #  *
    #  */
    # public class TailSheetExpansions {

    #   private final Expansion1D<UnwritableVectorIJK> tailSheetSymmetricValues;
    #   private final Expansion2D<UnwritableVectorIJK> tailSheetOddValues;
    #   private final Expansion2D<UnwritableVectorIJK> tailSheetEvenValues;

    #   private final int numAzimuthalExpansions;
    #   private final int numRadialExpansions;

    #   public TailSheetExpansions(Expansion1D<UnwritableVectorIJK> tailSheetSymmetricValues,
    #       Expansion2D<UnwritableVectorIJK> tailSheetOddValues,
    #       Expansion2D<UnwritableVectorIJK> tailSheetEvenValues) {
    #     super();
    #     this.tailSheetSymmetricValues = tailSheetSymmetricValues;
    #     this.tailSheetOddValues = tailSheetOddValues;
    #     this.tailSheetEvenValues = tailSheetEvenValues;

    #     this.numAzimuthalExpansions = tailSheetOddValues.iSize();
    #     this.numRadialExpansions = tailSheetOddValues.jSize();
    #   }

    #   public Expansion1D<UnwritableVectorIJK> getTailSheetSymmetricValues() {
    #     return tailSheetSymmetricValues;
    #   }

    #   public Expansion2D<UnwritableVectorIJK> getTailSheetOddValues() {
    #     return tailSheetOddValues;
    #   }

    #   public Expansion2D<UnwritableVectorIJK> getTailSheetEvenValues() {
    #     return tailSheetEvenValues;
    #   }

    #   /**
    #    * Converts an {@link ImmutableList} of {@link UnwritableVectorIJK} representing the results of a
    #    * {@link BasisVectorField} into a {@link TailSheetExpansions}
    #    * 
    #    * @param expansion
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @return
    #    */
    #   public static TailSheetExpansions getAsTailSheetExpansions(
    #       ImmutableList<UnwritableVectorIJK> expansion, int numAzimuthalExpansions,
    #       int numRadialExpansions) {

    #     UnwritableVectorIJK[] symmetricExpansions = new UnwritableVectorIJK[numRadialExpansions];
    #     UnwritableVectorIJK[][] oddExpansions =
    #         new UnwritableVectorIJK[numAzimuthalExpansions][numRadialExpansions];
    #     UnwritableVectorIJK[][] evenExpansions =
    #         new UnwritableVectorIJK[numAzimuthalExpansions][numRadialExpansions];

    #     int count = 0;

    #     // n is the radial expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       symmetricExpansions[n - 1] = expansion.get(count);
    #       count++;
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         oddExpansions[m - 1][n - 1] = expansion.get(count);
    #         count++;
    #       }
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         evenExpansions[m - 1][n - 1] = expansion.get(count);
    #         count++;
    #       }
    #     }

    #     return new TailSheetExpansions(Expansion1Ds.createFromArray(symmetricExpansions, 1),
    #         Expansion2Ds.createFromArray(oddExpansions, 1, 1),
    #         Expansion2Ds.createFromArray(evenExpansions, 1, 1));
    #   }

    #   /**
    #    * 
    #    * @return
    #    */
    #   public ImmutableList<UnwritableVectorIJK> getExpansionsAsList() {

    #     ImmutableList.Builder<UnwritableVectorIJK> basisFunctions = ImmutableList.builder();

    #     // n is the radial expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       basisFunctions.add(tailSheetSymmetricValues.getExpansion(n));
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         basisFunctions.add(tailSheetOddValues.getExpansion(m, n));
    #       }
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         basisFunctions.add(tailSheetEvenValues.getExpansion(m, n));
    #       }
    #     }

    #     return basisFunctions.build();
    #   }

    #   /**
    #    * 
    #    * @return
    #    */
    #   public UnwritableVectorIJK sum() {

    #     double bxSum = 0.0;
    #     double bySum = 0.0;
    #     double bzSum = 0.0;

    #     // n is the radial expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       UnwritableVectorIJK basisFunction = tailSheetSymmetricValues.getExpansion(n);
    #       bxSum += basisFunction.getI();
    #       bySum += basisFunction.getJ();
    #       bzSum += basisFunction.getK();
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         UnwritableVectorIJK basisFunction = tailSheetOddValues.getExpansion(m, n);
    #         bxSum += basisFunction.getI();
    #         bySum += basisFunction.getJ();
    #         bzSum += basisFunction.getK();
    #       }
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         UnwritableVectorIJK basisFunction = tailSheetEvenValues.getExpansion(m, n);
    #         bxSum += basisFunction.getI();
    #         bySum += basisFunction.getJ();
    #         bzSum += basisFunction.getK();
    #       }
    #     }

    #     return new UnwritableVectorIJK(bxSum, bySum, bzSum);
    #   }

    # }
