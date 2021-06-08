"""Asymmetric expansion for a tail current sheet."""


from math import atan2, exp, sqrt

from scipy.special import jv

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TailSheetAsymmetricExpansion(VectorField):
    """Asymmetric expansion for a tail current sheet.

    This is the odd and even type azimuthal symmetry part of the expansion
    of the solution of the magnetic field from a thin current sheet along the
    z=0 plane, from Tsyganenko and Sitnov 2007, eq. 16 and 17.

    The choice between odd or even is based on the provided TrigParity.

    SUBROUTINE TAILSHT_OE (M,X,Y,Z,BX,BY,BZ)

    author G.K.Stephens
    """

    def __init__(self, waveNumber, azimuthalExpansionNumber, trigParity,
                 currentSheetHalfThickness, bessel):
        """Build a new object.

        param waveNumber the wave number of this expansion
        param azimuthalExpansionNumber the azimuthal expansion number
        param trigParity sine function is odd cosine is even
        param currentSheetHalfThickness a 2D scalar field representing the
        current sheet half thickness throughout the equatorial current system
        param bessel the Bessel function evaluator
        """
        self.waveNumber = waveNumber
        self.azimuthalExpansionNumber = azimuthalExpansionNumber
        self.trigParity = trigParity
        self.currentSheetHalfThickness = currentSheetHalfThickness
        self.bessel = bessel

    def evaluate(self, *args):
        """Evaluate the expansion."""
        if len(args) == 1:
            (location,) = args
            buffer = VectorIJK([0, 0, 0])
            return self.evaluate(location, buffer)
        elif len(args) == 2:
            (location, buffer) = args
            m = self.azimuthalExpansionNumber
            x = location.getI()
            y = location.getJ()
            z = location.getK()
            locationIJ = UnwritableVectorIJ(x, y)

            # get the current sheet half thickness
            thick = self.currentSheetHalfThickness.evaluate(locationIJ)

            # now get the current sheet half thickness derivatives
            dThickdx = self.currentSheetHalfThickness.differentiateFDi(
                locationIJ)
            dThickdy = self.currentSheetHalfThickness.differentiateFDj(
                locationIJ)

            # convert to polar
            rho = sqrt(x*x + y*y)

            # convert to polar
            dThickdRho = (x*dThickdx + y*dThickdy)/rho
            dThickdPhi = -y*dThickdx + x*dThickdy
            cosPhi = x/rho
            sinPhi = y/rho
            phi = atan2(y, x)

            # introduce a finite thickness in z by replacing z with this value
            zDist = sqrt(z*z + thick*thick)

            # sine if odd, -cosine if even
            sinMPhi = self.trigParity.evaluate(m*phi)

            # cosine if odd, sine if even
            cosMPhi = self.trigParity.differentiate(m*phi)

            kn = self.waveNumber
            ex = exp(-kn*zDist)

            # calculate the bessel function
            jK = jv(m, kn*rho)

            # calculate the derivative of the bessel function
            jKDer = jv(m - 1, kn*rho) - m*jK/(kn*rho)

            # Eq. 16 and 17 from Tsyganenko and Sitnov 2007
            bRho = (-(kn*z*jKDer*ex/zDist) *
                    (cosMPhi - thick*(dThickdPhi*(kn + 1.0/zDist)*sinMPhi) /
                     (m*zDist)))
            bPhi = ((kn*z*ex*sinMPhi/zDist) *
                    (m*jK/(kn*rho) - rho*thick*dThickdRho*jKDer *
                     (kn + 1.0/zDist) / (m*zDist)))
            bZ = kn*jK*ex*(cosMPhi - kn*thick*dThickdPhi*sinMPhi/(m*zDist))

            # Convert from cylindrical coordinates to GSM
            buffer.setTo(
                bRho*cosPhi - bPhi*sinPhi, bRho*sinPhi + bPhi*cosPhi, bZ)

            # TODO for what ever reason, in the code the vectors are scaled by
            # the azimuthal expansion number divided by the wave number, this
            # is not in the paper, this is okay, as this will just rescale the
            # scaling coeffs.
            return buffer.scale(-m/kn)
        else:
            raise Exception
