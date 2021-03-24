"""emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients.py"""



from emmpy.com.google.common.base.preconditions import Preconditions
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.Expansion1D;
# import magmodel.core.math.expansions.Expansion2D;


class ThinCurrentSheetShieldingCoefficients:
    """This class stores the static coefficients for the TS07D model. These
    are available on the model webpage at
    http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.

    To construct this class, use the {@link TS07DStaticCoefficientsFactory}
    class.

    @author Nicholas Sharp
    @author G.K.Stephens
    """

    # private final int numAzimuthalExpansions;
    # private final int numRadialExpansions;
    # private final Expansion1D<CoefficientExpansion2D> symmetricTailExpansion;
    # private final Expansion1D<CoefficientExpansion1D> symmetricTailWaveExpansion;
    # private final Expansion2D<CoefficientExpansion2D> oddTailExpansion;
    # private final Expansion2D<CoefficientExpansion1D> oddTailWaveExpansion;
    # private final Expansion2D<CoefficientExpansion2D> evenTailExpansion;
    # private final Expansion2D<CoefficientExpansion1D> evenTailWaveExpansion;

    def __init__(
        self, numAzimuthalExpansions, numRadialExpansions,
        symmetricTailExpansion, symmetricTailWaveExpansion,
        oddTailExpansion, oddTailWaveExpansion,
        evenTailExpansion, evenTailWaveExpansion):
        """Constructor is package private, should be constructed using the
        {@link TS07DStaticCoefficientsFactory} class.

        @param numAzimuthalExpansions
        @param numRadialExpansions
        @param symmetricTailExpansion
        @param symmetricTailWaveExpansion
        @param oddTailExpansion
        @param oddTailWaveExpansion
        @param evenTailExpansion
        @param evenTailWaveExpansion
        """
        # ThinCurrentSheetShieldingCoefficients(int numAzimuthalExpansions, int numRadialExpansions,
        #     Expansion1D<CoefficientExpansion2D> symmetricTailExpansion,
        #     Expansion1D<CoefficientExpansion1D> symmetricTailWaveExpansion,
        #     Expansion2D<CoefficientExpansion2D> oddTailExpansion,
        #     Expansion2D<CoefficientExpansion1D> oddTailWaveExpansion,
        #     Expansion2D<CoefficientExpansion2D> evenTailExpansion,
        #     Expansion2D<CoefficientExpansion1D> evenTailWaveExpansion) {

        self.numRadialExpansions = (
            Preconditions.checkNotNull(numRadialExpansions)
        )
        self.numAzimuthalExpansions = (
            Preconditions.checkNotNull(numAzimuthalExpansions)
        )
        self.symmetricTailExpansion = (
            Preconditions.checkNotNull(symmetricTailExpansion)
        )
        self.symmetricTailWaveExpansion = (
            Preconditions.checkNotNull(symmetricTailWaveExpansion)
        )
        self.oddTailExpansion = Preconditions.checkNotNull(oddTailExpansion)
        self.oddTailWaveExpansion = (
            Preconditions.checkNotNull(oddTailWaveExpansion)
        )
        self.evenTailExpansion = Preconditions.checkNotNull(evenTailExpansion)
        self.evenTailWaveExpansion = (
            Preconditions.checkNotNull(evenTailWaveExpansion)
        )

    def getSymmetricTailExpansion(self):
        return self.symmetricTailExpansion

    def getSymmetricTailWaveExpansion(self):
        return self.symmetricTailWaveExpansion

    def getOddTailExpansion(self):
        return self.oddTailExpansion

    def getOddTailWaveExpansion(self):
        return self.oddTailWaveExpansion

    def getEvenTailExpansion(self):
        return self.evenTailExpansion

    def getEvenTailWaveExpansion(self):
        return self.evenTailWaveExpansion

    def getNumRadialExpansions(self):
        return self.numRadialExpansions

    def getNumAzimuthalExpansions(self):
        return self.numAzimuthalExpansions
