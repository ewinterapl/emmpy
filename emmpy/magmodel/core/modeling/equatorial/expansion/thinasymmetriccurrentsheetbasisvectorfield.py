"""emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield"""


from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetasymmetricexpansion import (
    TailSheetAsymmetricExpansion
)
# from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
#     TailSheetCoefficients
# )
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
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

    author G.K.Stephens
    """

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs, bessel):
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        self.numRadialExpansions = coeffs.getNumRadialExpansions()
        self.tailLength = tailLength
        self.currentSheetHalfThickness = currentSheetHalfThickness
        self.bessel = bessel

    # @staticmethod
    # def createUnity(
    #     tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
    #     numRadialExpansions, bessel
    # ):
    #     """Creates a ThinAsymmetricCurrentSheetBasisVectorField where all
    #     the coefficients have been set to 1.

    #     @param tailLength
    #     @param currentSheetHalfThickness
    #     @param numAzimuthalExpansions
    #     @param numRadialExpansions
    #     param bessel
    #     return
    #     """
    #     coeffs = TailSheetCoefficients.createUnity(
    #         numAzimuthalExpansions, numRadialExpansions
    #     )

    #     return ThinAsymmetricCurrentSheetBasisVectorField(
    #         tailLength, currentSheetHalfThickness, coeffs, bessel)

    def evaluate(self, location):
        buffer = VectorIJK()
        e = self.evaluateExpansions(location)
        # sum = e.sum()
        # buffer.setTo(sum)
        # ORIGINAL
        # return buffer.setTo(self.evaluateExpansions(location).sum())

    # def evaluateExpansion(self, location):
    #     return self.evaluateExpansions(location).getExpansionsAsList()

    def evaluateExpansions(self, location):
        """This guy recalculates everything"""

        # Preallocate the arrays of vectors for the expansions.
        zeros = [0, 0, 0]
        symmetricExpansions = [
            UnwritableVectorIJK(zeros) for i in range(self.numRadialExpansions)
        ]
        oddExpansions = (
            [[UnwritableVectorIJK(zeros)
              for j in range(self.numRadialExpansions)]
             for i in range(self.numAzimuthalExpansions)]
        )
        evenExpansions = (
            [[UnwritableVectorIJK(zeros)
              for j in range(self.numRadialExpansions)]
             for i in range(self.numAzimuthalExpansions)]
        )

        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):

            # Calculate the wave number (kn = n/rho0)
            kn = n/self.tailLength

            symBasisFunction = TailSheetSymmetricExpansion(
                kn, self.currentSheetHalfThickness, self.bessel
            )
            tssv = self.coeffs.getTailSheetSymmetricValues()
            a = tssv.getCoefficient(n)
            # ORIGINAL CODE
            # a = self.coeffs.getTailSheetSymmetricValues().getCoefficient(n)
            sbf_eval = symBasisFunction.evaluate(location)
            sbf_eval.scale(a)
            symmetricExpansions[n - 1] = sbf_eval
            # ORIGINAL CODE
            # symmetricExpansions[n - 1] = (
            #     symBasisFunction.evaluate(location).scale(a)
            # )

            # m is the azimuthal expansion number
            for m in range(1, self.numAzimuthalExpansions + 1):
                aOdd = self.coeffs.getTailSheetOddValues().getCoefficient(m, n)
                oddBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, TrigParity.ODD, self.currentSheetHalfThickness,
                    self.bessel
                )
                oddExpansions[m - 1][n - 1] = (
                    oddBasisFunction.evaluate(location).scale(aOdd)
                )
                aEven = (
                    self.coeffs.getTailSheetEvenValues().getCoefficient(m, n)
                )
                evenBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, TrigParity.EVEN, self.currentSheetHalfThickness,
                    self.bessel
                )
                evenExpansions[m - 1][n - 1] = (
                    evenBasisFunction.evaluate(location).scale(aEven)
                )

        if self.numAzimuthalExpansions == 0:
            return TailSheetExpansions(
                Expansion1Ds.createFromArray(symmetricExpansions, 1),
                Expansion2Ds.createNull(1, 1, self.numRadialExpansions),
                Expansion2Ds.createNull(1, 1, self.numRadialExpansions)
            )

    #     return TailSheetExpansions(
    #         Expansion1Ds.createFromArray(symmetricExpansions, 1),
    #         Expansion2Ds.createFromArray(oddExpansions, 1, 1),
    #         Expansion2Ds.createFromArray(evenExpansions, 1, 1)
    #     )

    # def getNumAzimuthalExpansions(self):
    #     return self.numAzimuthalExpansions

    # def getNumRadialExpansions(self):
    #     return self.numRadialExpansions

    # def getNumberOfBasisFunctions(self):
    #     return (
    #         self.numRadialExpansions +
    #         2*self.numRadialExpansions*self.numAzimuthalExpansions
    #     )
