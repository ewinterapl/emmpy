"""emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions"""


from emmpy.utilities.doubletolongbits import doubleToLongBits


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
