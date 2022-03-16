"""A modeling function for Birkeland currents.

A modeling function for Birkeland currents.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin, tan


class TFunction:
    """A modeling function for Birkeland currents.

    Represents the function given in "Methods for quantitative modeling of
    the magnetic field from Birkeland currents" by N. A. Tsyganenko.

    See eq. (14). The cone's axis is the +Z axis.
    see http://www.sciencedirect.com/science/article/pii/003206339190058I
    (Tsyganenko, 1990).

    Attributes
    ----------
    thetaNeg : float
        thetaNeg
    thetaPos : float
        thetaPos
    mode : int
        mode
    """

    def __init__(self, thetaNeg, thetaPos, mode):
        """Initialize a new TFunction object.

        Initialize a new TFunction object.

        Parameters
        ----------
        thetaNeg : float
            thetaNeg
        thetaPos : float
            thetaPos
        mode : int
            mode
        twoMplus1 : float
            twoMplus1
        tanHalfThetaNeg : float
            tanHalfThetaNeg
        tanHalfThetaPos : float
            tanHalfThetaPos
        tanMhalfThetaNeg : float
            tanMhalfThetaNeg
        tanMhalfThetaPos : float
            tanMhalfThetaPos
        tan2mp1HalfThetaNeg : float
            tan2mp1HalfThetaNeg
        tan2mp1HalfThetaPos : float
            tan2mp1HalfThetaPos
        constFactor : float
            constFactor
        """
        self.thetaNeg = thetaNeg
        self.thetaPos = thetaPos
        self.mode = mode
        self.twoMplus1 = 2.0*mode + 1.0
        self.tanHalfThetaNeg = tan(thetaNeg/2)
        self.tanHalfThetaPos = tan(thetaPos/2)
        tanMhalfThetaNeg = pow(self.tanHalfThetaNeg, mode)
        tanMhalfThetaPos = pow(self.tanHalfThetaPos, mode)
        self.tan2mp1HalfThetaNeg = (
            tanMhalfThetaNeg*tanMhalfThetaNeg*self.tanHalfThetaNeg
        )
        self.tan2mp1HalfThetaPos = (
            tanMhalfThetaPos*tanMhalfThetaPos*self.tanHalfThetaPos
        )
        self.constFactor = 1./(self.tanHalfThetaPos - self.tanHalfThetaNeg)

    @staticmethod
    def createFromDelta(theta0, deltaTheta, mode):
        """Create the function using a current sheet half thickness.

        Create the function using a current sheet half thickness.

        Parameters
        ----------
        theta0 : float
            A polar angle (colatitude) that is the center of the conical
            current sheet.
        deltaTheta : float
            The half thickness of the conical current sheet.
        mode : int
            The mode of the harmonic (m).
        
        Returns
        -------
        result : TFunction
            A newly constructed TFunction.
        """
        thetaPos = theta0 + deltaTheta
        thetaNeg = theta0 - deltaTheta
        return TFunction(thetaNeg, thetaPos, mode)

    def evaluate(self, theta):
        """Evaluate the function.

        Evaluate the function.

        Parameters
        ----------
        theta : float
            thera
        
        Returns
        -------
        result : float
            Result of function evaluation.
        """
        tanHalfTheta = tan(theta/2)
        tanMhalfTheta = pow(tanHalfTheta, self.mode)

        # First piecewise condition: theta < theta-
        if theta <= self.thetaNeg:
            return tanMhalfTheta

        # Second piecewise condition: theta- < theta < theta+
        # Note that this looks a bit different than the form given in
        # Tsy 2002-1 Eqn 17, however it is algebraically equivalent.
        if theta < self.thetaPos:
            tan2mp1HalfTheta = tanMhalfTheta*tanMhalfTheta*tanHalfTheta
            return self.constFactor*(
                tanMhalfTheta*(self.tanHalfThetaPos - tanHalfTheta) +
                (tan2mp1HalfTheta - self.tan2mp1HalfThetaNeg) /
                (self.twoMplus1*tanMhalfTheta)
            )

        # Third piecewise condition: theta >= theta+
        return (
            self.constFactor*(self.tan2mp1HalfThetaPos -
                              self.tan2mp1HalfThetaNeg) /
            (tanMhalfTheta*self.twoMplus1)
        )

    def differentiate(self, theta):
        """Differentiate the function.

        Differentiate the function.

        Parameters
        ----------
        theta : float
            theta
        
        Returns
        -------
        result : float
            Result of the differentiation.
        """
        tanHalfTheta = tan(theta/2)
        tanMhalfTheta = pow(tanHalfTheta, self.mode)
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
                (1 + tanHalfTheta*tanHalfTheta) *
                (tanMhalfTheta/tanHalfTheta *
                 (self.tanHalfThetaPos - tanHalfTheta) -
                 1/self.twoMplus1*(
                     tanMhalfTheta - self.tan2mp1HalfThetaNeg /
                     (tanMhalfTheta*tanHalfTheta)
                 )
                )
            )

        # Third piecewise condition: theta >= theta+
        return (
            -self.mode*self.constFactor *
            (self.tan2mp1HalfThetaPos - self.tan2mp1HalfThetaNeg) /
            (sin(theta)*tanMhalfTheta*self.twoMplus1)
        )
