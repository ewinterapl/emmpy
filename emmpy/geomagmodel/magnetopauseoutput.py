"""emmpy.geomagmodel.magnetopauseoutput"""


# import crucible.core.math.vectorspace.UnwritableVectorIJK;
from emmpy.java.lang.double import Double


class MagnetopauseOutput:

    # private final UnwritableVectorIJK magnetopauseLocation;
    # private final double distanceToMagnetopause;
    # private final boolean withinMagnetosphere;

    def __init__(self, magnetopauseLocation, distanceToMagnetopause,
                 withinMagnetosphere):
        """Constructor"""
        self.magnetopauseLocation = magnetopauseLocation
        self.distanceToMagnetopause = distanceToMagnetopause
        self.withinMagnetosphere = withinMagnetosphere

    def getDistanceToMagnetopause(self):
        return self.distanceToMagnetopause

    def isWithinMagnetosphere(self):
        return self.withinMagnetosphere

    def getMagnetopauseLocation(self):
        return self.magnetopauseLocation

    def toString(self):
        return (
            "MagnetopauseOutput [magnetopauseLocation=%s, "
            "distanceToMagnetopause=%s, withinMagnetosphere=%s]" %
            (self.magnetopauseLocation.toString(), self.distanceToMagnetopause,
             self.withinMagnetosphere)
        )

    def hashCode(self):
        prime = 31
        result = 1
        temp = Double.doubleToLongBits(self.distanceToMagnetopause)
        result = prime*result + temp ^ (temp >> 32)
        result = prime*result
        if self.magnetopauseLocation:
            result += self.magnetopauseLocation.hashCode()
        result = prime*result
        if self.withinMagnetosphere:
            result += 1231
        else:
            result += 1237
        return result

    def equals(self, obj):
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if (Double.doubleToLongBits(self.distanceToMagnetopause) !=
            Double.doubleToLongBits(other.distanceToMagnetopause)):
            return False
        if self.magnetopauseLocation is None:
            if other.magnetopauseLocation is not None:
                return False
        elif not self.magnetopauseLocation.equals(other.magnetopauseLocation):
            return False
        if self.withinMagnetosphere != other.withinMagnetosphere:
            return False
        return True
