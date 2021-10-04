"""A harmonic field in cylindrical coordinates.

A harmonic field in cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cosh, sinh

from scipy.special import jv

from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.chebysheviteration import ChebyshevIteration
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
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
    bessel : BesselFunctionEvaluator
    firstM, lastM, firstN, lastN : int
    trigParity : TrigParity
    """

    invMaxVal = pow(10.0, 8.0)

    def __init__(self, coefficientsExpansion, waveNumberExpansion, bessel,
                 trigParity):
        """Initialize a new CylindricalHarmonicField object.

        Initialize a new CylindricalHarmonicField object.

        Parameters
        ----------
        coefficientsExpansion : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients c_mn.
        waveNumberExpansion : CoefficientExpansion1D
            An expansion containing the non-linear wave numbers k_n.
        bessel : BesselFunctionEvaluator (ignored)
            Evaluates the Bessel function.
        firstM, lastM, firstN, lastN : int
            First and last indices in first and second dimensions.
        trigParity : TrigParity
            Even = cosine, odd = sine.
        """
        self.coefficientsExpansion = coefficientsExpansion
        self.waveNumberExpansion = waveNumberExpansion
        self.bessel = bessel
        self.firstM = coefficientsExpansion.getILowerBoundIndex()
        self.lastM = coefficientsExpansion.getIUpperBoundIndex()
        self.firstN = coefficientsExpansion.getJLowerBoundIndex()
        self.lastN = coefficientsExpansion.getJUpperBoundIndex()
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
        expansions = nones((self.coefficientsExpansion.iSize(),
                            self.coefficientsExpansion.jSize()))
        x = location.i
        y = location.j
        cylindricalLocation = CoordConverters.convertToCylindrical(location)
        rho = cylindricalLocation.rho
        phi = cylindricalLocation.phi
        z = cylindricalLocation.z

        # Precompute the sin(m*phi) and cos(m*phi), for speed.
        sinMphis = nones((self.lastM + 1,))
        cosMphis = nones((self.lastM + 1,))
        ChebyshevIteration.evaluateTrigExpansions(phi, sinMphis, cosMphis,
                                                  self.trigParity)
        for n in range(self.firstN, self.lastN + 1):
            # The wave number.
            kn = abs(self.waveNumberExpansion.getCoefficient(n))
            rhoK = rho*kn
            coshKZ = cosh(z*kn)
            sinhKZ = sinh(z*kn)
            # Cap rho^-1 and (coA*rho)^-1 at 10^8.
            rhoKInv = min(1/rhoK, CylindricalHarmonicField.invMaxVal)
            rhoInv = min(1/rho, CylindricalHarmonicField.invMaxVal)
            # Calculate Bessel terms and their derivatives.
            jns = []
            for i in range(self.lastM + 1):
                jns.append(jv(i, rhoK))
            jnsDer = nones((len(jns),))
            for m in range(1, self.lastM + 1):
                jnsDer[m] = jns[m - 1] - m*jns[m]*rhoKInv
            jnsDer[0] = -jns[1]

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
                coeff = self.coefficientsExpansion.getCoefficient(m, n)
                # Scale the vector, the minus sign comes from the
                # B=-del U.
                vect = VectorIJK(bx, by, bz)*-coeff
                expansions[m - self.firstM][n - self.firstN] = vect
        return Expansion2Ds.createFromArray(
            expansions, self.firstM, self.firstN
        )

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
        for m in range(self.firstM, self.lastM + 1):
            for n in range(self.firstN, self.lastN + 1):
                functions.append(expansions.getExpansion(m, n))
        return functions
