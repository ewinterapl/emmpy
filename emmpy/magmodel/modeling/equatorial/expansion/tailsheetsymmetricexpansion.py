"""Symmetric tail current sheet expansion.

Symmetric tail current sheet expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import exp, sqrt

import scipy.special as sps
from emmpy.math.coordinates.cartesianvector import CartesianVector

from emmpy.math.coordinates.vectorij import VectorIJ
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


class TailSheetSymmetricExpansion(VectorField):
    """Symmetric tail current sheet expansion.

    This is the symmetric (axisymmetric) part of the expansion of the
    solution of the magnetic field from a thin current sheet along the z=0
    plane, from Tsyganenko and Sitnov 2007, eq. 15.

    Attributes
    ----------
    waveNumber : float
        The wave number of this expansion.
    currentSheetHalfThickness : DifferentiableScalarFieldIJ
        A 2D scalar field representing the current sheet half thickness
        throughout the equatorial current system.
    """

    def __init__(self, waveNumber, currentSheetHalfThickness):
        """Initialize a new TailSheetSymmetricExpansion object.

        Initialize a new TailSheetSymmetricExpansion object.

        Parameters
        ----------
        waveNumber : float
            The wave number of this expansion.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            A 2D scalar field representing the current sheet half thickness
            throughout the equatorial current system.
        """
        self.waveNumber = waveNumber
        self.currentSheetHalfThickness = currentSheetHalfThickness

    def evaluate(self, *args):
        """Evaluate the expansion.
        
        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location to evaluate the field.
        buffer : VectorIJK, optional
            Buffer to hold the result.
        
        Returns
        -------
        buffer : VectorIJK
            Result of expansion at location.
        
        Raises
        ------
        TypeError
            If incorrect parameters are supplied.
        """
        if len(args) == 1:
            (location,) = args
            buffer = CartesianVector()
        elif len(args) == 2:
            (location, buffer) = args
        else:
            raise TypeError

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
        cosPhi = x/rho
        sinPhi = y/rho

        # Introduce a finite thickness in z by replacing z with this value.
        zDist = sqrt(z*z + thick*thick)

        # kn is the wave number.
        kn = self.waveNumber

        # Evaluate the Bessel function.
        j0 = sps.jv(0, kn*rho)
        j1 = sps.jv(1, kn*rho)

        ex = exp(-kn*zDist)
        bx = kn*z*j1*cosPhi*ex/zDist
        by = kn*z*j1*sinPhi*ex/zDist
        bz = kn*ex*(j0 - thick*dThickdRho*j1/zDist)

        buffer[:] = [bx, by, bz]
        return buffer
