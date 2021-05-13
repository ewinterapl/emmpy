"""emmpy.geomagmodel.ts07.coefficientreader.ts07nonlinearparameters"""


# from emmpy.java.lang.double import Double


class Ts07NonLinearParameters:
    """A container class for all the non-linear parameters of the TS07D model,
    current sheet thicknesses, hinge distance, warping parameter, region-1 FAC
    scaling, region-2 FAC scaling, and the twisting parameter.

    author G.K.Stephens
    """

    def __init__(
        self, facRegion1Kappa, facRegion2Kappa, currThicks, hingeDist,
        warpParam, twistFact
    ):
        """Constructor"""
        self.facRegion1Kappa = facRegion1Kappa
        self.facRegion2Kappa = facRegion2Kappa
        self.currThicks = currThicks
        self.hingeDist = hingeDist
        self.warpParam = warpParam
        self.twistFact = twistFact

    # def getFacRegion1Kappa(self):
    #     return self.facRegion1Kappa

    # def getFacRegion2Kappa(self):
    #     return self.facRegion2Kappa

    # def getCurrentSheetThicknesses(self):
    #     return self.currThicks

    # def getHingeDist(self):
    #     return self.hingeDist

    # def getWarpParam(self):
    #     return self.warpParam

    # def getTwistFact(self):
    #     return self.twistFact

    # @staticmethod
    # def average(paramsA, paramsB):
    #     """Average the two sets of non-linear parameters."""

    #     # average FAC kappas
    #     facRegion1Kappa = (
    #         (paramsA.getFacRegion1Kappa() + paramsB.getFacRegion1Kappa())/2
    #     )
    #     facRegion2Kappa = (
    #         (paramsA.getFacRegion2Kappa() + paramsB.getFacRegion2Kappa())/2
    #     )

    #     currThicks = []
    #     for i in range(len(paramsA.currThicks.size())):
    #         currThickA = paramsA.getCurrentSheetThicknesses()[i]
    #         currThickB = paramsB.getCurrentSheetThicknesses()[i]
    #         currThick = (currThickA + currThickB)/2
    #         currThicks.append(currThick)

    #     hingeDist = (paramsA.getHingeDist() + paramsB.getHingeDist())/2
    #     warpParam = (paramsA.getWarpParam() + paramsB.getWarpParam())/2
    #     twistFact = (paramsA.getTwistFact() + paramsB.getTwistFact())/2

    #     return Ts07NonLinearParameters(
    #         facRegion1Kappa, facRegion2Kappa, currThicks, hingeDist, warpParam,
    #         twistFact
    #     )

    # def asArray(self):
    #     """Get all the non-linear parameters as an array of doubles. The order
    #     of the array follows the order in the output .par files and is:

    #     current sheet thicknesses (may be multiple)
    #     hinge distance
    #     warping parameter
    #     region-1 scaling
    #     region-2 scaling
    #     twist factor

    #     @return the array of non-linear parameters
    #     """
    #     # converting the non-linear params to an array
    #     nonLinearParams = [None]*(len(self.currThicks) + 5)
    #     for i in range(len(self.currThicks)):
    #         nonLinearParams[i] = self.currThicks[i]
    #     nonLinearParams[len(self.currThicks)] = self.hingeDist
    #     nonLinearParams[len(self.currThicks) + 1] = self.warpParam
    #     nonLinearParams[len(self.currThicks) + 2] = self.facRegion1Kappa
    #     nonLinearParams[len(self.currThicks) + 3] = self.facRegion2Kappa
    #     nonLinearParams[len(self.currThicks) + 4] = self.twistFact

    #     return nonLinearParams

    # def toString(self):
    #     return (
    #         "Ts07NonLinearParameters [currThicks=%s, hingeDist=%s, "
    #         "warpParam=%s, facRegion1Kappa=%s, facRegion2Kappa=%s, "
    #         "twistFact=%s]" %
    #         (self.currThicks, self.hingeDist, self.warpParam,
    #          self.facRegion1Kappa, self.facRegion2Kappa, self.twistFact)
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     result = prime*result
    #     if self.currThicks:
    #         result += self.currThicks.hashCode()
    #     temp = Double.doubleToLongBits(self.facRegion1Kappa)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.facRegion2Kappa)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.hingeDist)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.twistFact)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.warpParam)
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
    #     elif not self.currThicks.equals(other.currThicks):
    #         return False
    #     if (Double.doubleToLongBits(self.facRegion1Kappa) !=
    #         Double.doubleToLongBits(other.facRegion1Kappa)):
    #         return False
    #     if (Double.doubleToLongBits(self.facRegion2Kappa) !=
    #         Double.doubleToLongBits(other.facRegion2Kappa)):
    #         return False
    #     if (Double.doubleToLongBits(self.hingeDist) !=
    #         Double.doubleToLongBits(other.hingeDist)):
    #         return False
    #     if (Double.doubleToLongBits(self.twistFact) !=
    #         Double.doubleToLongBits(other.twistFact)):
    #         return False
    #     if (Double.doubleToLongBits(self.warpParam) !=
    #         Double.doubleToLongBits(other.warpParam)):
    #         return False
    #     return True
