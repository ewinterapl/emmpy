"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients"""


from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)


class TailSheetCoefficients:
    """This is a container class for the coefficients used for the
    ThinAsymmetricCurrentSheetBasisVectorField class.

    That is, this class holds the symmetric a_n^s, odd a_mn^o>, and even
    a_mn^e) coefficients used in the expansion.

    author G.K.Stephens
    """

    def __init__(self, tailSheetSymmetricValues, tailSheetOddValues,
                 tailSheetEvenValues):
        """Constructor"""
        self.tailSheetSymmetricValues = tailSheetSymmetricValues
        self.tailSheetOddValues = tailSheetOddValues
        self.tailSheetEvenValues = tailSheetEvenValues
        self.numAzimuthalExpansions = tailSheetOddValues.iSize()
        self.numRadialExpansions = tailSheetOddValues.jSize()

    @staticmethod
    def createUnity(numAzimuthalExpansions, numRadialExpansions):
        """Creates a TailSheetCoefficientswhere all the coefficients have been
        set to 1"""
        return TailSheetCoefficients(
            CoefficientExpansions.createUnity(1, numRadialExpansions),
            CoefficientExpansions.createUnity(1, numAzimuthalExpansions, 1,
                                              numRadialExpansions),
            CoefficientExpansions.createUnity(1, numAzimuthalExpansions, 1,
                                              numRadialExpansions)
        )

    # @staticmethod
    # def createFromArray(array, numAzimuthalExpansions, numRadialExpansions):
    #     """Creates a {@link TailSheetCoefficients} from a double array.

    #     @param array
    #     @param numAzimuthalExpansions
    #     @param numRadialExpansions
    #     @retuxrn
    #     """

    #     sym = [None]*numRadialExpansions
    #     odd = []
    #     even = []
    #     for i in range(numAzimuthalExpansions):
    #         odd.append([None]*numRadialExpansions)
    #         even.append([None]*numRadialExpansions)

    #     # n is the radial expansion number
    #     count = 0
    #     for n in range(1, numRadialExpansions + 1):
    #         sym[n - 1] = array[count]
    #         count += 1

    #     # n is the radial expansion number
    #     # m is the azimuthal expansion number
    #     for n in range(1, numRadialExpansions + 1):
    #         for m in range(1, numAzimuthalExpansions + 1):
    #             odd[m - 1][n - 1] = array[count]
    #             count += 1

    #     # n is the radial expansion number
    #     # m is the azimuthal expansion number
    #     for n in range(1, numRadialExpansions + 1):
    #         for m in range(1, numAzimuthalExpansions + 1):
    #             even[m - 1][n - 1] = array[count]
    #             count += 1

    #     if numAzimuthalExpansions == 0:
    #         return TailSheetCoefficients(
    #             CoefficientExpansions.createExpansionFromArray(sym, 1),
    #             CoefficientExpansions.createNullExpansion(1, 1,
    #                                                       numRadialExpansions),
    #             CoefficientExpansions.createNullExpansion(1, 1,
    #                                                       numRadialExpansions)
    #         )

    #     return TailSheetCoefficients(
    #         CoefficientExpansions.createExpansionFromArray(sym, 1),
    #         CoefficientExpansions.createExpansionFromArray(odd, 1, 1),
    #         CoefficientExpansions.createExpansionFromArray(even, 1, 1))

    def getTailSheetSymmetricValues(self):
        """return the symmetric coefficients a_n^s"""
        return self.tailSheetSymmetricValues

    def getTailSheetOddValues(self):
        """return the odd coefficients a_mn^o"""
        return self.tailSheetOddValues

    def getTailSheetEvenValues(self):
        """return the even coefficients a_n^e"""
        return self.tailSheetEvenValues

    # def getAsSingleExpansion(self):
    #     """@return the {@link TailSheetCoefficients} expressed as a single
    #     {@link CoefficientExpansion1D} expansion"""
    #     firstM = 1
    #     lastM = self.numAzimuthalExpansions
    #     firstN = 1
    #     lastN = self.numRadialExpansions
    #     coeffs = [None]*self.getNumberOfExpansions()
    #     count = 0

    #     # the pressure independent terms
    #     for n in range(firstN, lastN + 1):
    #         coeffs[count] = self.tailSheetSymmetricValues.getCoefficient(n)
    #         count += 1

    #     for n in range(firstN, lastN + 1):
    #         for m in range(firstM, lastM + 1):
    #             coeffs[count] = self.tailSheetOddValues.getCoefficient(m, n)
    #             count += 1

    #     for n in range(firstN, lastN + 1):
    #         for m in range(firstM, lastM + 1):
    #             coeffs[count] = self.tailSheetEvenValues.getCoefficient(m, n)
    #             count += 1
    #     return CoefficientExpansions.createExpansionFromArray(coeffs, 1)

    def getNumAzimuthalExpansions(self):
        return self.numAzimuthalExpansions

    def getNumRadialExpansions(self):
        return self.numRadialExpansions

    # def getNumberOfExpansions(self):
    #     return (self.numRadialExpansions +
    #             2*(self.numAzimuthalExpansions*self.numRadialExpansions))

    # def toString(self):
    #     return ("TailSheetCoefficients [tailSheetSymmetricValues=%s"
    #             ", tailSheetOddValues=%s, tailSheetEvenValues=%s"
    #             ", numAzimuthalExpansions=%s, numRadialExpansions=%s]" %
    #             (self.tailSheetSymmetricValues,
    #              self.tailSheetOddValues,
    #              self.tailSheetEvenValues,
    #              self.numAzimuthalExpansions, self.numRadialExpansions))

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     result = prime*result + self.numAzimuthalExpansions
    #     result = prime*result + self.numRadialExpansions
    #     result = prime*result
    #     if self.tailSheetEvenValues:
    #         result += self.tailSheetEvenValues.hashCode()
    #     result = prime*result
    #     if self.tailSheetOddValues:
    #         result += self.tailSheetOddValues.hashCode()
    #     result = prime*result
    #     if self.tailSheetSymmetricValues:
    #         result += self.tailSheetSymmetricValues.hashCode()
    #     return result

    # def equals(self, obj):
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if self.__class__ != obj.__class__:
    #         return False
    #     other = obj
    #     if self.numAzimuthalExpansions != other.numAzimuthalExpansions:
    #         return False
    #     if self.numRadialExpansions != other.numRadialExpansions:
    #         return False

    #     if self.tailSheetEvenValues is None:
    #         if other.tailSheetEvenValues:
    #             return False
    #     elif not self.tailSheetEvenValues.equals(other.tailSheetEvenValues):
    #         return False

    #     if self.tailSheetOddValues is None:
    #         if other.tailSheetOddValues:
    #             return False
    #     elif not self.tailSheetOddValues.equals(other.tailSheetOddValues):
    #         return False
    #     if self.tailSheetSymmetricValues is None:
    #         if other.tailSheetSymmetricValues:
    #             return False
    #     elif not self.tailSheetSymmetricValues.equals(
    #         other.tailSheetSymmetricValues
    #         ):
    #         return False
    #     return True
