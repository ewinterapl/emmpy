"""A specialized version of a Cartesian harmonic field.

A specialized version of a Cartesian harmonic field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import exp, sqrt

from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class AlternateCartesianHarmonicField(BasisVectorField):
    """A specialized version of a Cartesian harmonic field.

    This class is very similar to CartesianHarmonicField which represents
    scalar potential solution of Laplace's equation in Cartesian
    coordinates.

    The difference is that the last K expansion is the 'derivative' term
    of the expansion. See Tsyganenko 2002, A model of the near
    magnetosphere with a dawn-dusk asymmetry 1. Mathematical structure
    Eq. 31 and 32, as he explains:

    "The potentials (equation (31)) were obtained by taking a derivative
    of equation (30) with respect to 1/rk; combining the potentials
    (equations (30) and (31)) was found necessary in order to avoid the
    tendency of the parameters rk to cluster in close pairs, accompanied
    by an unlimited growth of the corresponding linear coefficients in the
    course of the iterative minimization of Bn^2"

    TODO Using SVD to solve for the coefficients may alleviate the issue
    described above.

    Attributes
    ----------
    piCoeffs : CoefficientExpansion1D
        piCoeffs
    pkCoeffs : CoefficientExpansion1D
        pkCoeffs
    aikCoeffs : CoefficientExpansion2D
        aikCoeffs
    trigParityI : TrigParity
        trigParityI
    trigParityK : TrigParity
        trigParityK
    firstI : int
        firstI
    lastI : int
        lastI
    firstK : int
        firstK
    lastK : int
        lastK
    """

    def __init__(self, piCoeffs, pkCoeffs, aikCoeffs, trigParityI,
                 trigParityK):
        """Initialize a new AlternateCartesianHarmonicField object.
        
        Initialize a new AlternateCartesianHarmonicField object.

        Parameters
        ----------
        piCoeffs : CoefficientExpansion1D
            piCoeffs
        pkCoeffs : CoefficientExpansion1D
            pkCoeffs
        aikCoeffs : CoefficientExpansion2D
            aikCoeffs
        trigParityI : TrigParity
            trigParityI
        trigParityK : TrigParity
            trigParityK
        firstI : int
            firstI
        lastI : int
            lastI
        firstK : int
            firstK
        lastK : int
            lastK
        """
        self.piCoeffs = piCoeffs
        self.pkCoeffs = pkCoeffs
        self.aikCoeffs = aikCoeffs
        self.trigParityI = trigParityI
        self.trigParityK = trigParityK
        self.firstI = aikCoeffs.iLowerBoundIndex
        self.lastI = aikCoeffs.iUpperBoundIndex
        self.firstK = aikCoeffs.jLowerBoundIndex
        self.lastK = aikCoeffs.jUpperBoundIndex

    def evaluateExpansion2D(self, location):
        """Return the full expansion results.
        
        Return the full expansion results.
        
        Parameters
        ----------
        location : VectorIJK
            Location to evaluate expansion.
        
        Returns
        -------
        result : Expansion2D
            Expansion at location.
        """
        x = location.i
        y = location.j
        z = location.k
        expansions = nones((self.aikCoeffs.iSize, self.aikCoeffs.jSize))
        for i in range(self.firstI, self.lastI + 1):
            pi = self.piCoeffs[i]
            sinYpi = self.trigParityI.evaluate(pi*y)
            cosYpi = self.trigParityI.differentiate(pi*y)
            for k in range(self.firstK, self.lastK + 1):
                pk = self.pkCoeffs[k]
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = self.trigParityK.evaluate(pk*z)
                cosZpk = self.trigParityK.differentiate(pk*z)
                aik = self.aikCoeffs[i, k]
                if k == self.lastK:
                    bx = (-aik*exp_*sinYpi*(sqrtP*z*cosZpk +
                          sinZpk*pk*(x + 1.0/sqrtP)))
                    by = -aik*exp_*pi*cosYpi*(z*cosZpk + x*pk*sinZpk/sqrtP)
                    bz = (-aik*exp_*sinYpi*(cosZpk*(1.0 + x*pk*pk/sqrtP)
                                            - z*pk*sinZpk))
                    # Scale the vector, the minus sign comes from the B=-del U.
                    vect = VectorIJK(bx, by, bz)
                    expansions[i - self.firstI][k - self.firstK] = vect
                else:
                    bx = -aik*exp_*sqrtP*sinYpi*sinZpk
                    by = -aik*exp_*pi*cosYpi*sinZpk
                    bz = -aik*exp_*pk*sinYpi*cosZpk
                    # Scale the vector, the minus sign comes from the B=-del U.
                    vect = VectorIJK(bx, by, bz)
                    expansions[i - self.firstI][k - self.firstK] = vect
        return Expansion2Ds.createFromArray(expansions, self.firstI,
                                            self.firstK)

    def evaluateExpansion(self, location):
        """Evaluate the expansion.
        
        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate expansion.
        
        Returns
        -------
        functions : list of function objects
            Functions which make up the expansion.
        """
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for i in range(self.firstI, self.lastI + 1):
            for k in range(self.firstK, self.lastK + 1):
                functions.append(expansions.getExpansion(i, k))
        return functions
