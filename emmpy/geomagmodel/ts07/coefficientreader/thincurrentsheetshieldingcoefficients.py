"""emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients.py"""

# package geomagmodel.ts07.coefficientreader;

# import static com.google.common.base.Preconditions.checkNotNull;

# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.Expansion1D;
# import magmodel.core.math.expansions.Expansion2D;

class ThinCurrentSheetShieldingCoefficients:
    pass

    # /**
    #  * This class stores the static coefficients for the TS07D model. These are available on the model
    #  * webpage at http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.
    #  * <p>
    #  * To construct this class, use the {@link TS07DStaticCoefficientsFactory} class.
    #  * <p>
    #  * 
    #  * @author Nicholas Sharp
    #  * @author G.K.Stephens
    #  * 
    #  */
    # public class ThinCurrentSheetShieldingCoefficients {

    #   private final int numAzimuthalExpansions;
    #   private final int numRadialExpansions;

    #   private final Expansion1D<CoefficientExpansion2D> symmetricTailExpansion;
    #   private final Expansion1D<CoefficientExpansion1D> symmetricTailWaveExpansion;

    #   private final Expansion2D<CoefficientExpansion2D> oddTailExpansion;
    #   private final Expansion2D<CoefficientExpansion1D> oddTailWaveExpansion;

    #   private final Expansion2D<CoefficientExpansion2D> evenTailExpansion;
    #   private final Expansion2D<CoefficientExpansion1D> evenTailWaveExpansion;

    #   /**
    #    * Constructor is package private, should be constructed using the
    #    * {@link TS07DStaticCoefficientsFactory} class.
    #    * 
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @param symmetricTailExpansion
    #    * @param symmetricTailWaveExpansion
    #    * @param oddTailExpansion
    #    * @param oddTailWaveExpansion
    #    * @param evenTailExpansion
    #    * @param evenTailWaveExpansion
    #    */
    #   ThinCurrentSheetShieldingCoefficients(int numAzimuthalExpansions, int numRadialExpansions,
    #       Expansion1D<CoefficientExpansion2D> symmetricTailExpansion,
    #       Expansion1D<CoefficientExpansion1D> symmetricTailWaveExpansion,
    #       Expansion2D<CoefficientExpansion2D> oddTailExpansion,
    #       Expansion2D<CoefficientExpansion1D> oddTailWaveExpansion,
    #       Expansion2D<CoefficientExpansion2D> evenTailExpansion,
    #       Expansion2D<CoefficientExpansion1D> evenTailWaveExpansion) {
    #     super();
    #     this.numRadialExpansions = checkNotNull(numRadialExpansions);
    #     this.numAzimuthalExpansions = checkNotNull(numAzimuthalExpansions);
    #     this.symmetricTailExpansion = checkNotNull(symmetricTailExpansion);
    #     this.symmetricTailWaveExpansion = checkNotNull(symmetricTailWaveExpansion);
    #     this.oddTailExpansion = checkNotNull(oddTailExpansion);
    #     this.oddTailWaveExpansion = checkNotNull(oddTailWaveExpansion);
    #     this.evenTailExpansion = checkNotNull(evenTailExpansion);
    #     this.evenTailWaveExpansion = checkNotNull(evenTailWaveExpansion);
    #   }

    #   public Expansion1D<CoefficientExpansion2D> getSymmetricTailExpansion() {
    #     return symmetricTailExpansion;
    #   }

    #   public Expansion1D<CoefficientExpansion1D> getSymmetricTailWaveExpansion() {
    #     return symmetricTailWaveExpansion;
    #   }

    #   public Expansion2D<CoefficientExpansion2D> getOddTailExpansion() {
    #     return oddTailExpansion;
    #   }

    #   public Expansion2D<CoefficientExpansion1D> getOddTailWaveExpansion() {
    #     return oddTailWaveExpansion;
    #   }

    #   public Expansion2D<CoefficientExpansion2D> getEvenTailExpansion() {
    #     return evenTailExpansion;
    #   }

    #   public Expansion2D<CoefficientExpansion1D> getEvenTailWaveExpansion() {
    #     return evenTailWaveExpansion;
    #   }

    #   public int getNumRadialExpansions() {
    #     return numRadialExpansions;
    #   }

    #   public int getNumAzimuthalExpansions() {
    #     return numAzimuthalExpansions;
    #   }

    # }
