"""emmpy.geomagmodel.ts07.modeling.equatorial.shieldedthincurrentsheetfield"""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.expansions.Expansion1D;
# import magmodel.core.math.expansions.Expansion2D;
# import magmodel.core.math.expansions.Expansion2Ds;
# import magmodel.core.modeling.equatorial.expansion.TailSheetCoefficients;
# import magmodel.core.modeling.equatorial.expansion.TailSheetExpansions;

from emmpy.geomagmodel.ts07.modeling.equatorial.thinasymmetriccurrentsheetbasisvectorshieldingfield import (
    ThinAsymmetricCurrentSheetBasisVectorShieldingField
)
from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield import (
    ThinAsymmetricCurrentSheetBasisVectorField
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class ShieldedThinCurrentSheetField(BasisVectorField):
    """author G.K.Stephens"""

    #   private final ThinAsymmetricCurrentSheetBasisVectorField thinCurrentSheet;
    #   private final ThinAsymmetricCurrentSheetBasisVectorShieldingField thinCurrentSheetShield;
    #   private final int numAzimuthalExpansions;
    #   private final int numRadialExpansions;
    #   private final boolean includeShield;

    def __init__(self, thinCurrentSheet, thinCurrentSheetShield,
        includeShield):
        """Constructor

        param ThinAsymmetricCurrentSheetBasisVectorField thinCurrentSheet
        param ThinAsymmetricCurrentSheetBasisVectorShieldingField thinCurrentSheetShield
        param includeShield includeShield
        """
        self.thinCurrentSheet = thinCurrentSheet
        self.thinCurrentSheetShield = thinCurrentSheetShield
        self.includeShield = includeShield
        self.numAzimuthalExpansions = thinCurrentSheet.getNumAzimuthalExpansions()
        self.numRadialExpansions = thinCurrentSheet.getNumRadialExpansions()

    #   /**
    #    * 
    #    * @param tailCoeffs
    #    * @param currentSheetHalfThickness
    #    * @param tailLength
    #    * @param bessel
    #    * @param staticCoefficients
    #    * @param includeShield
    #    * @return
    #    */
    #   public static ShieldedThinCurrentSheetField create(TailSheetCoefficients tailCoeffs,
    #       DifferentiableScalarFieldIJ currentSheetHalfThickness, double tailLength,
    #       BesselFunctionEvaluator bessel, ThinCurrentSheetShieldingCoefficients staticCoefficients,
    #       boolean includeShield) {
    #     ThinAsymmetricCurrentSheetBasisVectorField thinCurrentSheet =
    #         new ThinAsymmetricCurrentSheetBasisVectorField(tailLength, currentSheetHalfThickness,
    #             tailCoeffs, bessel);
    #     ThinAsymmetricCurrentSheetBasisVectorShieldingField thinCurrentSheetShield =
    #         new ThinAsymmetricCurrentSheetBasisVectorShieldingField(staticCoefficients, bessel);
    #     return new ShieldedThinCurrentSheetField(thinCurrentSheet, thinCurrentSheetShield,
    #         includeShield);
    #   }

    @staticmethod
    def createUnity(currentSheetHalfThickness, tailLength, bessel,
                    staticCoefficients, includeShield):
        """createUnity

        param DifferentiableScalarFieldIJ currentSheetHalfThickness
        param double tailLength
        param BesselFunctionEvaluator bessel
        param ThinCurrentSheetShieldingCoefficients staticCoefficients
        param boolean includeShield
        return ShieldedThinCurrentSheetField
        """
        thinCurrentSheet = (
            ThinAsymmetricCurrentSheetBasisVectorField.createUnity(
                tailLength, currentSheetHalfThickness,
                staticCoefficients.getNumAzimuthalExpansions(),
                staticCoefficients.getNumRadialExpansions(), bessel)
        )
        thinCurrentSheetShield = ThinAsymmetricCurrentSheetBasisVectorShieldingField(
            staticCoefficients, bessel)
        return ShieldedThinCurrentSheetField(
            thinCurrentSheet, thinCurrentSheetShield, includeShield)

    def evaluateExpansions(self, position):
        """evaluateExpansions

        param UnwritableVectorIJK position
        return TailSheetExpansions
        """

        # TailSheetExpansions equatorialExpansions
        equatorialExpansions = (
            self.thinCurrentSheet.evaluateExpansions(position)
        )

        # Calculate the field expansions
        # Expansion1D<UnwritableVectorIJK> tailSheetSymmetricValues
        tailSheetSymmetricValues = (
            equatorialExpansions.getTailSheetSymmetricValues()
        )
        # Expansion2D<UnwritableVectorIJK> tailSheetOddValues,
        # tailSheetEvenValues
        tailSheetOddValues = equatorialExpansions.getTailSheetOddValues()
        tailSheetEvenValues = equatorialExpansions.getTailSheetEvenValues()

        # This is the most expensive lines of the module, If you don't need the
        # shielding, it should NOT be computed. These three lines account for
        # for over 90% of the model evaluation
        if self.includeShield:
            # TailSheetExpansions shield
            shield = self.thinCurrentSheetShield.evaluateExpansions(position)
            # Expansion1D<UnwritableVectorIJK> tailSheetSymmetricShieldValues
            tailSheetSymmetricShieldValues = (
                shield.getTailSheetSymmetricValues()
            )
            # Expansion2D<UnwritableVectorIJK> tailSheetOddShieldValues
            tailSheetOddShieldValues = shield.getTailSheetOddValues()
            # Expansion2D<UnwritableVectorIJK> tailSheetEvenShieldValues
            tailSheetEvenShieldValues = shield.getTailSheetEvenValues()
            tailSheetSymmetricValues = (
                Expansion1Ds.Vectors.add(tailSheetSymmetricValues,
                                         tailSheetSymmetricShieldValues)
            )
    #       tailSheetOddValues = Expansion2Ds.Vectors.add(tailSheetOddValues, tailSheetOddShieldValues);
    #       tailSheetEvenValues =
    #           Expansion2Ds.Vectors.add(tailSheetEvenValues, tailSheetEvenShieldValues);
    #     }

    #     return new TailSheetExpansions(tailSheetSymmetricValues, tailSheetOddValues,
    #         tailSheetEvenValues);
    #   }

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {
    #     return evaluateExpansions(location).getExpansionsAsList();
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return numRadialExpansions + 2 * (numAzimuthalExpansions * numRadialExpansions);
    #   }

    # }
