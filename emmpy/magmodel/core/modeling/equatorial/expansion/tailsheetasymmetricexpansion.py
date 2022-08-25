"""Asymmetric expansion for a tail current sheet.

Asymmetric expansion for a tail current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, exp, sin, sqrt

from scipy.special import jv

from emmpy.magmodel.math.trigparity import ODD
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.vectorij import VectorIJ
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


class TailSheetAsymmetricExpansion(VectorField):
    """Asymmetric expansion for a tail current sheet.

    This is the odd and even type azimuthal symmetry part of the expansion
    of the solution of the magnetic field from a thin current sheet along
    the z=0 plane, from Tsyganenko and Sitnov 2007, eq. 16 and 17.

    The choice between odd or even is based on the provided TrigParity.

    Attributes
    ----------
    waveNumber : float
        The wave number of this expansion.
    azimuthalExpansionNumber : int
        The azimuthal expansion number.
    trigParity : TrigParity
        Sine function is odd cosine is even.
    currentSheetHalfThickness : DifferentiableScalarFieldIJ
        A 2D scalar field representing the current sheet half thickness
        throughout the equatorial current system.
    """

    def __init__(self, waveNumber, azimuthalExpansionNumber, trigParity,
                 currentSheetHalfThickness):
        """Initialize a new TailSheetAsymmetricExpansion object.

        Initialize a new TailSheetAsymmetricExpansion object.

        Parameters
        ----------
        waveNumber : float
            The wave number of this expansion.
        azimuthalExpansionNumber : int
            The azimuthal expansion number.
        trigParity : TrigParity
            Sine function is odd cosine is even.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            A 2D scalar field representing the current sheet half thickness
            throughout the equatorial current system.
        """
        self.waveNumber = waveNumber
        self.azimuthalExpansionNumber = azimuthalExpansionNumber
        self.trigParity = trigParity
        self.currentSheetHalfThickness = currentSheetHalfThickness

    def evaluate(self, location):
        """Evaluate the expansion.

        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location to evaluate expansion.

        Returns
        -------
        buffer : VectorIJK
            Value of expansion at location.
        """
        buffer = VectorIJK([0, 0, 0])

        m = self.azimuthalExpansionNumber
        x = location.x
        y = location.y
        z = location.z
        locationIJ = VectorIJ(x, y)

        # Get the current sheet half thickness.
        thick = self.currentSheetHalfThickness.evaluate(locationIJ)

        # Now get the current sheet half thickness derivatives.
        dThickdx = self.currentSheetHalfThickness.differentiateFDi(
            locationIJ)
        dThickdy = self.currentSheetHalfThickness.differentiateFDj(
            locationIJ)

        # Convert to polar.
        rho = sqrt(x*x + y*y)
        dThickdRho = (x*dThickdx + y*dThickdy)/rho
        dThickdPhi = -y*dThickdx + x*dThickdy
        cosPhi = x/rho
        sinPhi = y/rho
        phi = atan2(y, x)

        # Introduce a finite thickness in z by replacing z with this value.
        zDist = sqrt(z*z + thick*thick)

        # Sine if odd, -cosine if even.
        if self.trigParity is ODD:
            sinMPhi = sin(m*phi)
            cosMPhi = cos(m*phi)
        else:
            sinMPhi = cos(m*phi)
            cosMPhi = -sin(m*phi)

        kn = self.waveNumber
        ex = exp(-kn*zDist)

        # Calculate the bessel function.
        jK = jv(m, kn*rho)

        # Calculate the derivative of the bessel function.
        jKDer = jv(m - 1, kn*rho) - m*jK/(kn*rho)

        # Eq. 16 and 17 from Tsyganenko and Sitnov 2007.
        bRho = (-(kn*z*jKDer*ex/zDist) *
                (cosMPhi - thick*(dThickdPhi*(kn + 1.0/zDist)*sinMPhi) /
                    (m*zDist)))
        bPhi = ((kn*z*ex*sinMPhi/zDist) *
                (m*jK/(kn*rho) - rho*thick*dThickdRho*jKDer *
                    (kn + 1.0/zDist) / (m*zDist)))
        bZ = kn*jK*ex*(cosMPhi - kn*thick*dThickdPhi*sinMPhi/(m*zDist))

        # Convert from cylindrical coordinates to GSM.
        buffer[:] = (
            bRho*cosPhi - bPhi*sinPhi, bRho*sinPhi + bPhi*cosPhi, bZ)

        # TODO for what ever reason, in the code the vectors are scaled by
        # the azimuthal expansion number divided by the wave number, this
        # is not in the paper, this is okay, as this will just rescale the
        # scaling coeffs.
        buffer *= -m/kn
        return buffer