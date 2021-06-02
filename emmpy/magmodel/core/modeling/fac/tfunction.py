"""emmpy.magmodel.core.modeling.fac.tfunction"""


# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.tan;

from math import cos, sin, tan

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)


class TFunction(DifferentiableUnivariateFunction):
    """Represents the function given in "Methods for quantitative modeling of
    the magnetic field from Birkeland currents" by N. A. Tsyganenko.
    
    See eq. (14). The cone's axis is the +Z axis.
    see href="http://www.sciencedirect.com/science/article/pii/003206339190058I"
    (Tsyganenko, 1990)

    author G.K.Stephens
    """

    def __init__(self, thetaNeg, thetaPos, mode):
        """Constructor

        param double thetaNeg
        param double thetaPos
        param int mode
        """
        self.thetaNeg = thetaNeg
        self.thetaPos = thetaPos
        self.mode = mode
        # double twoMplus1
        self.twoMplus1 = 2.0*mode + 1.0
        # double tanHalfThetaNeg
        self.tanHalfThetaNeg = tan(thetaNeg/2)
        # double tanHalfThetaPos
        self.tanHalfThetaPos = tan(thetaPos/2)
        # double tanMhalfThetaNeg
        tanMhalfThetaNeg = pow(self.tanHalfThetaNeg, mode)
        # double tanMhalfThetaPos
        tanMhalfThetaPos = pow(self.tanHalfThetaPos, mode)
        # double tan2mp1HalfThetaNeg
        self.tan2mp1HalfThetaNeg = tanMhalfThetaNeg*tanMhalfThetaNeg*self.tanHalfThetaNeg
        # double tan2mp1HalfThetaPos;
        self.tan2mp1HalfThetaPos = tanMhalfThetaPos*tanMhalfThetaPos*self.tanHalfThetaPos
        # double constFactor
        self.constFactor = 1./(self.tanHalfThetaPos - self.tanHalfThetaNeg)

    @staticmethod
    def createFromDelta(theta0, deltaTheta, mode):
        """createFromDelta

        param double theta0 a polar angle (colatitude) that is the center of
        the conical current sheet
        param double deltaTheta the half thickness of the conical current sheet
        param int mode the mode of the harmonic (m)
        return a newly constructed TFunction
        """
        # double thetaPos
        thetaPos = theta0 + deltaTheta
        # double thetaNeg
        thetaNeg = theta0 - deltaTheta
        return TFunction(thetaNeg, thetaPos, mode)

    def evaluate(self, theta):
        """evaluate

        param double theta
        return double
        """
        # double tanHalfTheta
        tanHalfTheta = tan(theta/2)
        # double tanMhalfTheta
        tanMhalfTheta = pow(tanHalfTheta, self.mode)

        # First piecewise condition: theta < theta-
        if theta <= self.thetaNeg:
            return tanMhalfTheta

        # Second piecewise condition: theta- < theta < theta+
        # Note that this looks a bit different than the form given in
        # Tsy 2002-1 Eqn 17, however it is algebraically equivalent.
        if theta < self.thetaPos:
            # double tan2mp1HalfTheta
            tan2mp1HalfTheta = tanMhalfTheta*tanMhalfTheta*tanHalfTheta
            return self.constFactor*(
                tanMhalfTheta*(self.tanHalfThetaPos - tanHalfTheta) +
                (tan2mp1HalfTheta - self.tan2mp1HalfThetaNeg) /
                (self.twoMplus1*tanMhalfTheta)
            )

        # Third piecewise condition: theta >= theta+
        return self.constFactor*(self.tan2mp1HalfThetaPos -
            self.tan2mp1HalfThetaNeg)/(tanMhalfTheta*self.twoMplus1)

    def differentiate(self, theta):
        """differentiate

        param double theta
        return double
        """
        # double tanHalfTheta
        tanHalfTheta = tan(theta/2)
        # double tanMhalfTheta
        tanMhalfTheta = pow(tanHalfTheta, self.mode)
        # double cosHalfTheta
        cosHalfTheta = cos(theta/2)

        # First piecewise condition: theta < theta-
        if theta <= self.thetaNeg:
            return (
                0.5*self.mode*tanMhalfTheta /
                (tanHalfTheta*cosHalfTheta*cosHalfTheta)
            )
        elif theta < self.thetaPos:
            # Second piecewise condition: theta- < theta < theta+
            # Note that this looks a bit different than the form given in
            # Tsy 2002-1 Eqn 17, however it is algebraically equivalent.
            return (
                0.5*self.mode*self.constFactor *
                (1 + self.tanHalfTheta*self.tanHalfTheta) *
                (self.tanMhalfTheta/self.tanHalfTheta *
                (self.tanHalfThetaPos - self.tanHalfTheta) -
                1/self.twoMplus1 *
                (self.tanMhalfTheta - self.tan2mp1HalfThetaNeg /
                    (self.tanMhalfTheta*self.tanHalfTheta)))
            )

        # Third piecewise condition: theta >= theta+
        return (
            -self.mode*self.constFactor *
            (self.tan2mp1HalfThetaPos - self.tan2mp1HalfThetaNeg) /
            (sin(theta)*self.tanMhalfTheta*self.twoMplus1)
        )
