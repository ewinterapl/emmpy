"""emmpy.magmodel.core.modeling.fac.conicalcurrentmagneticfield"""


from math import sin

from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.magmodel.core.modeling.fac.tfunction import TFunction
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


class ConicalCurrentMagneticField(SphericalVectorField):
    """Represents the magnetic field of an azimuthal harmonic of a finite
    thickness conical current sheet
    
    As described in "Methods for quantitative modeling of the magnetic field
    from Birkeland currents" by N. A. Tsyganenko. See eq. (16). The cone's axis
    is the +Z axis.

    The magnetic field is the curl of the following vector potential:
    see http://www.sciencedirect.com/science/article/pii/003206339190058I
    (Tsyganenko, 1990)

           SUBROUTINE ONE_CONE(A,X,Y,Z,BX,BY,BZ)
    c
    c  RETURNS FIELD COMPONENTS FOR A DEFORMED CONICAL CURRENT SYSTEM, FITTED TO A BIOSAVART FIELD
    c    BY SIM_14.FOR.  HERE ONLY THE NORTHERN CONE IS TAKEN INTO ACCOUNT.

    author G.K.Stephens
    """

    def __init__(self, tFunction, mode, trigParity):
        """Constructor

        param TFunction tFunction
        param int mode
        param TrigParity trigParity
        """
        # DifferentiableUnivariateFunction tFunction
        self.tFunction = tFunction
        # int mode
        self.mode = mode
        # TrigParity trigParity
        self.trigParity = trigParity

    @staticmethod
    def create(theta0, deltaTheta, mode, trigParity):
        """Creates a ConicalCurrentMagneticField where the current sheet is
        centered at theta0 and has a half thickness of deltaTheta.
        
        The theta co-latitude dependence (theta) is determined by the
        TFunction.

        param double theta0 a polar angle (colatitude) that is the center of
        the conical current sheet
        param double deltaTheta the half thickness of the conical current sheet
        param int mode the mode of the harmonic (m)
        param TrigParity trigParity the parity of the harmonic (EVEN for cosine
        and ODD for sine)
        return a newly constructed ConicalCurrentMagneticField
        """
        return ConicalCurrentMagneticField(
            TFunction.createFromDelta(theta0, deltaTheta, mode),
            mode, trigParity
        )

    def evaluate(self, location):
        """Evaluates the field at the given position in the spherical
        coordinate system

        param SphericalVector location the location to evaluate the field
        return SphericalVector the result of the evaluation
        """

        # This is the curl of equation 16
        # float r, phi, theta, t, dt_dTheta, sinMphi, cosMphi, br, bTheta, bPhi
        r = location.getRadius()
        phi = location.getLongitude()
        theta = location.getColatitude()
        t = self.tFunction.evaluate(theta)
        dt_dTheta = self.tFunction.differentiate(theta)
        # even or odd
        sinMphi = self.trigParity.evaluate(self.mode*phi)
        cosMphi = self.trigParity.differentiate(self.mode*phi)
        br = 0.0
        bTheta = self.mode*t*cosMphi/(r*sin(theta))
        bPhi = -dt_dTheta*sinMphi/r
        return SphericalVector(br, bTheta, bPhi)
