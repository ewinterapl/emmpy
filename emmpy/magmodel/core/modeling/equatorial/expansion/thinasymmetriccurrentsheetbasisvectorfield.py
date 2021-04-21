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

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetasymmetricexpansion import (
    TailSheetAsymmetricExpansion
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetsymmetricexpansion import (
    TailSheetSymmetricExpansion
)


class ThinAsymmetricCurrentSheetBasisVectorField(BasisVectorField):
    """This module described the tail fields as stated in Tsyganenko and Sitnov
    2007

    "Magnetospheric configurations from a high-resolution data-based magnetic
    fields model", eq. 14.

    This is equivalent to the FORTRAN subroutine:
    SUBROUTINE UNWARPED (X,Y,Z,BXS,BYS,BZS,BXO,BYO,BZO,BXE,BYE,BZE)

    @author G.K.Stephens
    """

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs, bessel):
        """Constructor

        @param tailLength
        @param currentSheetHalfThickness
        @param bessel
        """
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        self.numRadialExpansions = coeffs.getNumRadialExpansions()
        self.tailLength = tailLength
        self.currentSheetHalfThickness = currentSheetHalfThickness
        self.bessel = bessel

    @staticmethod
    def createUnity(
        tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
        numRadialExpansions, bessel
    ):
        """Creates a ThinAsymmetricCurrentSheetBasisVectorField where all
        the coefficients have been set to 1.

        @param tailLength
        @param currentSheetHalfThickness
        @param numAzimuthalExpansions
        @param numRadialExpansions
        param bessel
        return
        """
        coeffs = TailSheetCoefficients.createUnity(
            numAzimuthalExpansions, numRadialExpansions
        )

        return ThinAsymmetricCurrentSheetBasisVectorField(
            tailLength, currentSheetHalfThickness, coeffs, bessel)

    def evaluate(self, location):
        buffer = VectorIJK()
        return buffer.setTo(self.evaluateExpansions(location).sum())

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {
    #     return evaluateExpansions(location).getExpansionsAsList();
    #   }

    def evaluateExpansions(self, location):
        """This guy recalculates everything

        @param positionVector
        @param dipoleTilt
        @param dynamicPressure
        @param includeShield
        """
        zeros = [0, 0, 0]
        symmetricExpansions = [UnwritableVectorIJK(zeros) for i in range(self.numRadialExpansions)]
        oddExpansions = (
            [[UnwritableVectorIJK(zeros) for j in range(self.numRadialExpansions)]
             for i in range(self.numAzimuthalExpansions)]
        )
        evenExpansions = (
            [[UnwritableVectorIJK(zeros) for j in range(self.numRadialExpansions)]
             for i in range(self.numAzimuthalExpansions)]
        )

        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):

            # Calculate the wave number (kn = n/rho0)
            kn = n/self.tailLength

            symBasisFunction = TailSheetSymmetricExpansion(
                kn, self.currentSheetHalfThickness, self.bessel
            )

            a = self.coeffs.getTailSheetSymmetricValues().getCoefficient(n)

            symmetricExpansions[n - 1] = symBasisFunction.evaluate(location).scale(a)

            # m is the azimuthal expansion number
            for m in range(1, self.numAzimuthalExpansions + 1):
                aOdd = self.coeffs.getTailSheetOddValues().getCoefficient(m, n)
                oddBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, TrigParity.ODD, self.currentSheetHalfThickness, self.bessel
                )
                oddExpansions[m - 1][n - 1] = oddBasisFunction.evaluate(location).scale(aOdd)
                aEven = self.coeffs.getTailSheetEvenValues().getCoefficient(m, n)
                evenBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, TrigParity.EVEN, self.currentSheetHalfThickness, self.bessel
                )
                evenExpansions[m - 1][n - 1] = evenBasisFunction.evaluate(location).scale(aEven)

            if self.numAzimuthalExpansions == 0:
                return TailSheetExpansions(
                    createFromArray(symmetricExpansions, 1),
                   createNull(1, 1, numRadialExpansions), createNull(1, 1, numRadialExpansions)
                )

            return TailSheetExpansions(
                self.createFromArray(symmetricExpansions, 1),
                self.createFromArray(oddExpansions, 1, 1),
                self.createFromArray(evenExpansions, 1, 1)
            )

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
