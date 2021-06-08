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
