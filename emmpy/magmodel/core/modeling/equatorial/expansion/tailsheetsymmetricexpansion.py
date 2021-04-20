"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetsymmetricexpansion"""


from math import exp, sqrt

import scipy.special as sps

from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class TailSheetSymmetricExpansion(VectorField):
    """This is the symmetric (axissymmetric) part of the expansion of the
    solution of the magnetic field from a thin current sheet along the z=0
    plane, from Tsyganenko and Sitnov 2007, eq. 15.

    SUBROUTINE TAILSHT_S (M,X,Y,Z,BX,BY,BZ)

    @author G.K.Stephens
    """

    def __init__(self, waveNumber, currentSheetHalfThickness, bessel):
        """Constructor

        @param waveNumber the wave number of this expansion
        @param currentSheetHalfThickness a 2D scalar field representing the
        current sheet half thickness throughout the equatorial current system
        @param bessel the Bessel function evaluator
        """
        self.waveNumber = waveNumber
        self.currentSheetHalfThickness = currentSheetHalfThickness
        self.bessel = bessel

    def evaluate(self, *args):
        if len(args) == 1:
            (location,) = args
            buffer = VectorIJK()
            return self.evaluate(location, buffer)
        elif len(args) == 2:
            (location, buffer) = args
            x = location.getI()
            y = location.getJ()
            z = location.getK()
            locationIJ = UnwritableVectorIJ(x, y)

            # get the current sheet half thickness
            thick = self.currentSheetHalfThickness.evaluate(locationIJ)

            # now get the current sheet half thickness derivatives
            dThickdx = self.currentSheetHalfThickness.differentiateFDi(locationIJ)
            dThickdy = self.currentSheetHalfThickness.differentiateFDj(locationIJ)

            # convert to polar
            rho = sqrt(x*x + y*y)

            # convert derivatives to polar
            dThickdRho = (x*dThickdx + y*dThickdy)/rho

            cosPhi = x/rho
            sinPhi = y/rho

            # introduce a finite thickness in z by replacing z with this value
            zDist = sqrt(z*z + thick*thick)

            # kn is the wave number
            kn = self.waveNumber

            # evaluate the Bessel function
            j0 = sps.j0(kn*rho)
            j1 = sps.j1(kn*rho)

            ex = exp(-kn*zDist)
            bx = kn*z*j1*cosPhi*ex/zDist
            by = kn*z*j1*sinPhi*ex/zDist
            bz = kn*ex*(j0 - thick*dThickdRho*j1/zDist)

            return buffer.setTo(bx, by, bz)
        else:
            raise Exception
