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

from emmpy.magmodel.core.chebysheviteration import ChebyshevIteration
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
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
    firstM, lastM, firstN, lastN : int
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
        firstM, lastM, firstN, lastN : int
            First and last indices in first and second dimensions.
        trigParity : TrigParity
            Even = cosine, odd = sine.
        """
        self.coefficientsExpansion = coefficientsExpansion
        self.waveNumberExpansion = waveNumberExpansion
        self.firstM = coefficientsExpansion.iLowerBoundIndex
        self.lastM = coefficientsExpansion.iUpperBoundIndex
        self.firstN = coefficientsExpansion.jLowerBoundIndex
        self.lastN = coefficientsExpansion.jUpperBoundIndex
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
        expansions = nones((self.coefficientsExpansion.iSize,
                            self.coefficientsExpansion.jSize))
        x = location.x
        y = location.y
        cylindricalLocation = cartesianToCylindrical(CartesianVector(location))
        rho = cylindricalLocation.rho
        phi = cylindricalLocation.phi
        z = cylindricalLocation.z

        # Precompute the sin(m*phi) and cos(m*phi), for speed.
        sinMphis = np.empty(self.lastM + 1)
        cosMphis = np.empty(self.lastM + 1)
        ChebyshevIteration.evaluateTrigExpansions(phi, sinMphis, cosMphis,
                                                  self.trigParity)
        # for n in range(self.firstN, self.lastN + 1):
        for n in range(self.lastN - self.firstN + 1):
            # The wave number.
            # kn = abs(self.waveNumberExpansion[n - self.firstN])
            kn = abs(self.waveNumberExpansion[n])
            rhoK = rho*kn
            coshKZ = cosh(z*kn)
            sinhKZ = sinh(z*kn)
            # Cap rho^-1 and (coA*rho)^-1 at 10^8.
            rhoKInv = min(1/rhoK, CylindricalHarmonicField.invMaxVal)
            rhoInv = min(1/rho, CylindricalHarmonicField.invMaxVal)
            # Calculate Bessel terms and their derivatives.
            jns = jv(range(self.lastM + 1), rhoK)
            jnsDer = np.empty(self.lastM + 1)
            jnsDer[0] = -jns[1]
            jnsDer[1:] = [jns[m - 1] - m*jns[m]*rhoKInv for m in range(1, self.lastM + 1)]

            for m in range(self.firstM, self.lastM + 1):
                # Sine if odd, -cosine if even.
                sinLPhi = sinMphis[m - self.firstM]
                # Cosine if odd, sine if even.
                cosLPhi = cosMphis[m - self.firstM]
                jM = jns[m]
                jMDer = jnsDer[m]
                bRho = kn*jMDer*cosLPhi*sinhKZ
                bPhi = rhoInv*m*jM*sinLPhi*sinhKZ
                bz = kn*cosLPhi*coshKZ*jM
                bx = x*rhoInv*bRho + y*rhoInv*bPhi
                by = y*rhoInv*bRho - x*rhoInv*bPhi
                # Get the linear scaling coefficient.
                # coeff = self.coefficientsExpansion[m, n]
                coeff = self.coefficientsExpansion[m, n + self.firstN]
                # Scale the vector, the minus sign comes from the
                # B=-del U.
                vect = VectorIJK(bx, by, bz)*-coeff
                # expansions[m - self.firstM][n - self.firstN] = vect
                expansions[m - self.firstM][n] = vect
        return Expansion2Ds.createFromArray(expansions, self.firstM, self.firstN)

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
        # for m in range(self.firstM, self.lastM + 1):
        for m in range(self.lastM - self.firstM + 1):
            # for n in range(self.firstN, self.lastN + 1):
            for n in range(self.lastN - self.firstN + 1):
                functions.append(expansions.getExpansion(m + self.firstM, n + self.firstN))
        return functions
