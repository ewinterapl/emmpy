"""emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients
"""


# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.java.lang.double import Double
from emmpy.utilities.isrealnumber import isRealNumber


class Ts07EquatorialVariableCoefficients:
    """author G.K.Stephens"""

    def __init__(self, currThicks, hingeDist, warpingParam, twistParam,
                 equatorialLinearCoeffs):
        if (isRealNumber(currThicks) and isRealNumber(hingeDist) and
            isRealNumber(warpingParam) and isRealNumber(twistParam) and
            isinstance(equatorialLinearCoeffs, list)):
            raise Exception
    #         # @param currThicks
    #         # @param hingeDist
    #         # @param warpingParam
    #         # @param twistParam
    #         # @param equatorialLinearCoeffs
    #         self.currThicks = [currThicks]
    #         self.hingeDist = hingeDist
    #         self.warpingParam = warpingParam
    #         self.twistParam = twistParam
    #         self.equatorialLinearCoeffs = Preconditions.checkNotNull(
    #             equatorialLinearCoeffs)
        elif isinstance(currThicks, list):
            # param currThicks
            # param hingeDist
            # param warpingParam
            # param twistParam
            # param equatorialLinearCoeffs
            # The current sheet thickness and the number of sets of linear
            # coeffs must be the same size.
            self.currThicks = currThicks
            self.hingeDist = hingeDist
            self.warpingParam = warpingParam
            self.twistParam = twistParam
            self.equatorialLinearCoeffs = equatorialLinearCoeffs
        else:
            raise Exception

    def getCurrThicks(self):
        return self.currThicks

    def getHingeDistance(self):
        return self.hingeDist

    def getWarpingParam(self):
        return self.warpingParam

    def getTwistParam(self):
        return self.twistParam

    # def getLinearCoeffs(self):
    #     return self.equatorialLinearCoeffs

    # def getTotalNumberOfParameters(self):
    #     return (self.getTotalNumberOfLinearParameters() +
    #             self.getTotalNumberOfNonLinearParameters())

    # def getTotalNumberOfLinearParameters(self):
    #     numLinear = 0

    #     # loop through all the linear parameters and add them up
    #     for lin in self.equatorialLinearCoeffs:
    #         m = lin.getNumAzimuthalExpansions()
    #         n = lin.getNumRadialExpansions()
    #         numLinear += 2 * (n + 2 * (n * m))
    #     return numLinear

    # def getTotalNumberOfNonLinearParameters(self):
    #     # currThicks, hingeDist, warpingParam,TwistParam
    #     return len(self.currThicks) + 3

    # def toString(self):
    #     elc_str = ""
    #     for elc in self.equatorialLinearCoeffs:
    #         elc_str += elc.toString()
    #     return (
    #         "Ts07EquatorialVariableCoefficients [currThicks=%s, hingeDist=%s, "
    #         "warpingParam=%s, twistParam=%s, equatorialLinearCoeffs=%s]" %
    #         (self.currThicks, self.hingeDist, self.warpingParam,
    #          self.twistParam, elc_str)
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     result = prime*result
    #     if self.currThicks:
    #         # result += self.currThicks.hashCode())
    #         result += len(self.currThicks)  # HACK
    #     result = prime*result
    #     if self.equatorialLinearCoeffs:
    #         # result += self.equatorialLinearCoeffs.hashCode()
    #         result += len(self.equatorialLinearCoeffs)  # HACK
    #     temp = Double.doubleToLongBits(self.hingeDist)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.twistParam)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.warpingParam)
    #     result = prime*result + temp ^ (temp >> 32)
    #     return result

    # def equals(self, obj):
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if self.__class__ != obj.__class__:
    #         return False
    #     other = obj
    #     if self.currThicks is None:
    #         if other.currThicks is not None:
    #             return False
    #     elif self.currThicks != other.currThicks:
    #         return False
    #     if self.equatorialLinearCoeffs is None:
    #         if other.equatorialLinearCoeffs is not None:
    #             return False
    #     elif self.equatorialLinearCoeffs != other.equatorialLinearCoeffs:
    #         return False
    #     if (Double.doubleToLongBits(self.hingeDist) !=
    #         Double.doubleToLongBits(other.hingeDist)):
    #         return False
    #     if (Double.doubleToLongBits(self.twistParam) !=
    #         Double.doubleToLongBits(other.twistParam)):
    #         return False
    #     if (Double.doubleToLongBits(self.warpingParam) !=
    #         Double.doubleToLongBits(other.warpingParam)):
    #         return False
    #     return True
