"""emmpy.geomagmodel.ts07.modeling.equatorial.thinasymmetriccurrentsheetbasisvectorshieldingfield"""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
# import magmodel.core.math.CylindricalHarmonicField;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.Expansion1Ds;
# import magmodel.core.math.expansions.Expansion2Ds;
# import magmodel.core.modeling.equatorial.expansion.TailSheetExpansions;

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class ThinAsymmetricCurrentSheetBasisVectorShieldingField(BasisVectorField):

    # private final ThinCurrentSheetShieldingCoefficients coeffs;
    # private final BesselFunctionEvaluator bessel;
    # private final int numAzimuthalExpansions;
    # private final int numRadialExpansions;

    def __init__(self, coeffs, bessel):
        """Constructor

        param ThinCurrentSheetShieldingCoefficients coeffs
        param BesselFunctionEvaluator bessel
        """
        self.coeffs = coeffs
        self.bessel = bessel
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        self.numRadialExpansions = coeffs.getNumRadialExpansions()

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {
    #     return evaluateExpansions(location).getExpansionsAsList();
    #   }

    def evaluateExpansions(self, location):
        """evaluateExpansions

        param UnwritableVectorIJK location
        return TailSheetExpansions
        """
        # [UnwritableVectorIJK] symmetricExpansions
        symmetricExpansions = [None]*self.numRadialExpansions
        # [[UnwritableVectorIJK]] oddExpansions, evenExpansions
        oddExpansions = []
        evenExpansions = []
        for i in range(self.numAzimuthalExpansions):
            oddExpansions.append([None])
            evenExpansions.append([None])
            for j in range(self.numRadialExpansions):
                oddExpansions[i].append(None)
                evenExpansions[i].append(None)

        # n is the radial expansion number
        for n in range(self.numRadialExpansions + 1):
            # CoefficientExpansion2D tailExpansion
            tailExpansion = (
                self.coeffs.getSymmetricTailExpansion().getExpansion(n)
            )
            waveNumberExpansion = (
                self.coeffs.getSymmetricTailWaveExpansion().getExpansion(n)
            )
            buffer = VectorIJK()
            chf = CylindricalHarmonicField(tailExpansion, waveNumberExpansion,
                                           bessel, TrigParity.ODD)
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       CoefficientExpansion2D tailExpansion = coeffs.getSymmetricTailExpansion().getExpansion(n);
    #       CoefficientExpansion1D waveNumberExpansion =
    #           coeffs.getSymmetricTailWaveExpansion().getExpansion(n);
    #       VectorIJK buffer = new VectorIJK();
    #       new CylindricalHarmonicField(tailExpansion, waveNumberExpansion, bessel, TrigParity.ODD)
    #           .evaluate(location, buffer);
    #       symmetricExpansions[n - 1] =
    #           new UnwritableVectorIJK(buffer.getI(), buffer.getJ(), buffer.getK());
    #     }

    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     double negateConst = 1.0;
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         CoefficientExpansion2D tailExpansion = coeffs.getOddTailExpansion().getExpansion(m, n);
    #         CoefficientExpansion1D waveNumberExpansion =
    #             coeffs.getOddTailWaveExpansion().getExpansion(m, n);
    #         VectorIJK buffer = new VectorIJK();
    #         new CylindricalHarmonicField(tailExpansion, waveNumberExpansion, bessel, TrigParity.ODD)
    #             .evaluate(location, buffer);
    #         buffer.scale(negateConst);
    #         oddExpansions[m - 1][n - 1] =
    #             new UnwritableVectorIJK(buffer.getI(), buffer.getJ(), buffer.getK());
    #       }
    #     }
    #     // n is the radial expansion number
    #     // m is the azimuthal expansion number
    #     negateConst = -1.0;
    #     for (int n = 1; n <= numRadialExpansions; n++) {
    #       for (int m = 1; m <= numAzimuthalExpansions; m++) {
    #         CoefficientExpansion2D tailExpansion = coeffs.getEvenTailExpansion().getExpansion(m, n);
    #         CoefficientExpansion1D waveNumberExpansion =
    #             coeffs.getEvenTailWaveExpansion().getExpansion(m, n);
    #         VectorIJK buffer = new VectorIJK();
    #         new CylindricalHarmonicField(tailExpansion, waveNumberExpansion, bessel, TrigParity.EVEN)
    #             .evaluate(location, buffer);
    #         buffer.scale(negateConst);
    #         evenExpansions[m - 1][n - 1] =
    #             new UnwritableVectorIJK(buffer.getI(), buffer.getJ(), buffer.getK());
    #       }
    #     }
    #     return new TailSheetExpansions(Expansion1Ds.createFromArray(symmetricExpansions, 1),
    #         Expansion2Ds.createFromArray(oddExpansions, 1, 1),
    #         Expansion2Ds.createFromArray(evenExpansions, 1, 1));
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return numRadialExpansions + 2 * numRadialExpansions * numAzimuthalExpansions;
    #   }
