"""Variable equatorial coefficients for the TS07 geomagnetic field model."""


from emmpy.utilities.doubletolongbits import doubleToLongBits
from emmpy.utilities.isrealnumber import isRealNumber


class Ts07EquatorialVariableCoefficients:
    """Variable equatorial coefficients for the TS07 geomagnetic field model.

    author G.K.Stephens
    """

    def __init__(self, currThicks, hingeDist, warpingParam, twistParam,
                 equatorialLinearCoeffs):
        """Build a new object."""
        if (isRealNumber(currThicks) and isRealNumber(hingeDist) and
            isRealNumber(warpingParam) and isRealNumber(twistParam) and
            isinstance(equatorialLinearCoeffs, list)):
            # @param currThicks
            # @param hingeDist
            # @param warpingParam
            # @param twistParam
            # @param equatorialLinearCoeffs
            self.currThicks = [currThicks]
            self.hingeDist = hingeDist
            self.warpingParam = warpingParam
            self.twistParam = twistParam
            self.equatorialLinearCoeffs = equatorialLinearCoeffs
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
        """Return the current sheet thicknesses."""
        return self.currThicks

    def getHingeDistance(self):
        """Return the hinge distance."""
        return self.hingeDist

    def getWarpingParam(self):
        """Return the warping parameter."""
        return self.warpingParam

    def getTwistParam(self):
        """Return the twist parameter."""
        return self.twistParam

    def getLinearCoeffs(self):
        """Return the linear coefficients."""
        return self.equatorialLinearCoeffs

    def getTotalNumberOfParameters(self):
        """Return the total number of parameters."""
        return (self.getTotalNumberOfLinearParameters() +
                self.getTotalNumberOfNonLinearParameters())

    def getTotalNumberOfLinearParameters(self):
        """Return the total number of linear parameters."""
        numLinear = 0

        # loop through all the linear parameters and add them up
        for lin in self.equatorialLinearCoeffs:
            m = lin.getNumAzimuthalExpansions()
            n = lin.getNumRadialExpansions()
            numLinear += 2 * (n + 2 * (n * m))
        return numLinear

    def getTotalNumberOfNonLinearParameters(self):
        """Return the total number of nonlinear parameters."""
        # currThicks, hingeDist, warpingParam,TwistParam
        return len(self.currThicks) + 3

    def toString(self):
        """Convert the object to a string."""
        elc_str = ""
        for elc in self.equatorialLinearCoeffs:
            elc_str += elc.toString()
        return (
            "Ts07EquatorialVariableCoefficients [currThicks=%s, hingeDist=%s, "
            "warpingParam=%s, twistParam=%s, equatorialLinearCoeffs=%s]" %
            (self.currThicks, self.hingeDist, self.warpingParam,
             self.twistParam, elc_str)
        )

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result
        if self.currThicks:
            # result += self.currThicks.hashCode())
            result += len(self.currThicks)  # HACK
        result = prime*result
        if self.equatorialLinearCoeffs:
            # result += self.equatorialLinearCoeffs.hashCode()
            result += len(self.equatorialLinearCoeffs)  # HACK
        temp = doubleToLongBits(self.hingeDist)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.twistParam)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.warpingParam)
        result = prime*result + temp ^ (temp >> 32)
        return result

    def equals(self, obj):
        """Check for equality with another object."""
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.currThicks is None:
            if other.currThicks is not None:
                return False
        elif self.currThicks != other.currThicks:
            return False
        if self.equatorialLinearCoeffs is None:
            if other.equatorialLinearCoeffs is not None:
                return False
        elif self.equatorialLinearCoeffs != other.equatorialLinearCoeffs:
            return False
        if (doubleToLongBits(self.hingeDist) !=
            doubleToLongBits(other.hingeDist)):
            return False
        if (doubleToLongBits(self.twistParam) !=
            doubleToLongBits(other.twistParam)):
            return False
        if (doubleToLongBits(self.warpingParam) !=
            doubleToLongBits(other.warpingParam)):
            return False
        return True
