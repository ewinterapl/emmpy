"""emmpy.geomagmodel.ts07.coefficientreader.ts07facvariablecoefficients"""


from emmpy.java.lang.double import Double


class Ts07FacVariableCoefficients:

    def __init__(
        self, region1KappaScaling, region2KappaScaling, facConfigurations
    ):
        """Constructor"""
        self.region1KappaScaling = region1KappaScaling
        self.region2KappaScaling = region2KappaScaling
        self.facConfigurations = facConfigurations

    def getRegion1KappaScaling(self):
        return self.region1KappaScaling

    def getRegion2KappaScaling(self):
        return self.region2KappaScaling

    # def getFacConfigurations(self):
    #     return self.facConfigurations

    # def getLienarCoefficients(self):
    #     """we must construct a new one every time so that it doesn't change"""
    #     linearCoeefs = [None]*len(self.facConfigurations)
    #     for i in range(len(linearCoeefs)):
    #         linearCoeefs[i] = self.facConfigurations[i].getAmplitudeScaling()
    #     return linearCoeefs

    # def toString(self):
    #     return (
    #         "Ts07FacVariableCoefficients2 [region1KappaScaling=%s,"
    #         " region2KappaScaling=%s,"
    #         " facConfigurations=%s]"
    #         % (self.region1KappaScaling, self.region2KappaScaling,
    #            self.facConfigurations)
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     result = prime*result
    #     if self.facConfigurations:
    #         result += self.facConfigurations.hashCode()
    #     temp = Double.doubleToLongBits(self.region1KappaScaling)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.region2KappaScaling)
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
    #     if self.facConfigurations is None:
    #         if other.facConfigurations is not None:
    #             return False
    #     elif not self.facConfigurations.equals(other.facConfigurations):
    #         return False
    #     if (Double.doubleToLongBits(self.region1KappaScaling) !=
    #         Double.doubleToLongBits(other.region1KappaScaling)):
    #         return False
    #     if (Double.doubleToLongBits(self.region2KappaScaling) !=
    #         Double.doubleToLongBits(other.region2KappaScaling)):
    #         return False
    #     return True
