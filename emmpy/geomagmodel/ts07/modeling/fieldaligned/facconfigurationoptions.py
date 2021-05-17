"""emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions"""


# from emmpy.java.lang.double import Double


class FacConfigurationOptions:
    """A set of configuration options that tells how to construct a magnetic
    vector field for a Field Aligned Current.

    author G.K.Stephens
    """

    def __init__(
        self, amplitudeScaling, region, mode, trigParity, theta0, deltaTheta,
        smoothed, shielded
    ):
        """Constructor

        param amplitudeScaling the linear coefficient that determines the
        strength of the field
        param region region-1 or region-2
        param mode the mode of the fac sin(k*phi)
        param trigParity the parity even-cos(k*phi) or odd-sin(k*phi)
        param theta0 the center polar angle of the FAC system
        param deltaTheta the half thickness angle of FAC system
        param smoothed smooth the field along theta, the original models were
        not smoothed
        param shielded the magnetopause shielding fields should be evaluated,
        normally you should shield the fields
        """
        self.amplitudeScaling = float(amplitudeScaling)
        self.region = region
        self.mode = mode
        self.trigParity = trigParity
        self.theta0 = theta0
        self.deltaTheta = float(deltaTheta)
        self.smoothed = smoothed
        self.shielded = shielded

    def getAmplitudeScaling(self):
        return self.amplitudeScaling

    def getRegion(self):
        return self.region

    def getMode(self):
        return self.mode

    def getTrigParity(self):
        return self.trigParity

    def getTheta0(self):
        return self.theta0

    def getDeltaTheta(self):
        return self.deltaTheta

    def isSmoothed(self):
        return self.smoothed

    def isShielded(self):
        return self.shielded

    # def toString(self):
    #     return (
    #         "FacConfigurationOptions [amplitudeScaling=%s, region=%s, mode=%s,"
    #         " trigParity=%s, theta0=%s, deltaTheta=%s, smoothed=%s, "
    #         "shielded=%s]"
    #         % (self.amplitudeScaling, self.region, self.mode, self.trigParity,
    #            self.theta0, self.deltaTheta, self.smoothed, self.shielded)
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     temp = Double.doubleToLongBits(self.amplitudeScaling)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.deltaTheta)
    #     result = prime*result + temp ^ (temp >> 32)
    #     result = prime*result + self.mode
    #     result = prime*result
    #     if self.region is not None:
    #         result += self.region
    #     result = prime*result
    #     if self.shielded:
    #         result += 1231
    #     else:
    #         result += 1237
    #     result = prime*result
    #     if self.smoothed:
    #         result += 1231
    #     else:
    #         result += 1237
    #     temp = Double.doubleToLongBits(self.theta0)
    #     result = prime*result + temp ^ (temp >> 32)
    #     # NEED THIS
    #     # result = prime*result + ((trigParity == null) ?
    #     # 0 : trigParity.hashCode());
    #     return result

    # def equals(self, obj):
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if self.__class__ != obj.__class__:
    #         return False
    #     other = obj
    #     if (Double.doubleToLongBits(self.amplitudeScaling) !=
    #         Double.doubleToLongBits(other.amplitudeScaling)):
    #         return False
    #     if (Double.doubleToLongBits(self.deltaTheta) !=
    #         Double.doubleToLongBits(other.deltaTheta)):
    #         return False
    #     if self.mode != other.mode:
    #         return False
    #     if self.region != other.region:
    #         return False
    #     if self.shielded != other.shielded:
    #         return False
    #     if self.smoothed != other.smoothed:
    #         return False
    #     if (Double.doubleToLongBits(self.theta0) !=
    #         Double.doubleToLongBits(other.theta0)):
    #         return False
    #     if self.trigParity != other.trigParity:
    #         return False
    #     return True
