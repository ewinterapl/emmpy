"""A harmonic field in cylindrical coordinates.

A harmonic field in cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cosh, sinh

import numpy as np
from scipy.special import jv

from emmpy.magmodel.math.chebysheviteration import ChebyshevIteration
from emmpy.magmodel.math.expansions.arrayexpansion2d import ArrayExpansion2D
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.cylindricalvector import cartesianToCylindrical
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class CylindricalHarmonicField(BasisVectorField):
    """A harmonic field in cylindrical coordinates.

    A vector field that is associated with the scalar potential solution
    of Laplace's equation in Ccylindrical coordinates.

    Uses a Fourier-Bessel expansion representation, from TS07 eq. 20.

    Attributes
    ----------
    coefficientsExpansion : CoefficientExpansion2D
    waveNumberExpansion : CoefficientExpansion1D
    trigParity : TrigParity
    """

    invMaxVal = pow(10.0, 8.0)

    def __init__(self, coefficientsExpansion, waveNumberExpansion,
                 trigParity):
        """Initialize a new CylindricalHarmonicField object.

        Initialize a new CylindricalHarmonicField object.

        Parameters
        ----------
        coefficientsExpansion : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients c_mn.
        waveNumberExpansion : CoefficientExpansion1D
            An expansion containing the non-linear wave numbers k_n.
        trigParity : TrigParity
            Even = cosine, odd = sine.
        """
        self.coefficientsExpansion = coefficientsExpansion
        self.waveNumberExpansion = waveNumberExpansion
        self.trigParity = trigParity

    def evaluateExpansion2D(self, location):
        """Return the full expansion results.

        Return the full expansion results.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location to evaluate the expansion.
        
        Returns
        -------
        result : Expansion2D
            Functions for the expansion.
        """
        expansions = nones((len(self.coefficientsExpansion),
                            len(self.coefficientsExpansion[0])))
        x = location.x
        y = location.y
        cylindricalLocation = cartesianToCylindrical(CartesianVector(location))
        rho = cylindricalLocation.rho
        phi = cylindricalLocation.phi
        z = cylindricalLocation.z

        # Precompute the sin(m*phi) and cos(m*phi), for speed.
        sinMphis = np.empty(len(self.coefficientsExpansion))
        cosMphis = np.empty(len(self.coefficientsExpansion))
        ChebyshevIteration.evaluateTrigExpansions(phi, sinMphis, cosMphis,
                                                  self.trigParity)
        for n in range(len(self.coefficientsExpansion[0])):
            # The wave number.
            kn = abs(self.waveNumberExpansion[n])
            rhoK = rho*kn
            coshKZ = cosh(z*kn)
            sinhKZ = sinh(z*kn)
            # Cap rho^-1 and (coA*rho)^-1 at 10^8.
            rhoKInv = min(1/rhoK, CylindricalHarmonicField.invMaxVal)
            rhoInv = min(1/rho, CylindricalHarmonicField.invMaxVal)
            # Calculate Bessel terms and their derivatives.
            jns = jv(range(len(self.coefficientsExpansion)), rhoK)
            jnsDer = np.empty(len(self.coefficientsExpansion))
            jnsDer[0] = -jns[1]
            jnsDer[1:] = [jns[m - 1] - m*jns[m]*rhoKInv for m in range(1, len(self.coefficientsExpansion))]

            for m in range(len(self.coefficientsExpansion)):
                # Sine if odd, -cosine if even.
                sinLPhi = sinMphis[m]
                # Cosine if odd, sine if even.
                cosLPhi = cosMphis[m]
                jM = jns[m]
                jMDer = jnsDer[m]
                bRho = kn*jMDer*cosLPhi*sinhKZ
                bPhi = rhoInv*m*jM*sinLPhi*sinhKZ
                bz = kn*cosLPhi*coshKZ*jM
                bx = x*rhoInv*bRho + y*rhoInv*bPhi
                by = y*rhoInv*bRho - x*rhoInv*bPhi
                # Get the linear scaling coefficient.
                coeff = self.coefficientsExpansion[m, n]
                # Scale the vector, the minus sign comes from the
                # B=-del U.
                vect = VectorIJK(bx, by, bz)*-coeff
                expansions[m][n] = vect
        return ArrayExpansion2D(expansions)

    def evaluateExpansion(self, location):
        """Evaluate the expansion at a location.

        Evaluate the expansion at a location.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location to evaluate the expansion.
        
        Returns
        -------
        functions : list of function
            List of functions representing the expansion.
        """
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for m in range(len(self.coefficientsExpansion)):
            for n in range(len(self.coefficientsExpansion[0])):
                functions.append(expansions[m][n])
        return functions
