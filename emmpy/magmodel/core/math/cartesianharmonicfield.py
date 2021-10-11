"""A harmonic field in Cartesian coordinates.

A harmonic field in Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import exp, sqrt

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.utilities.nones import nones


class CartesianHarmonicField(BasisVectorField):
    """A harmonic field in Cartesian coordinates.

    A vector field that is associated with the scalar potential solution
    of Laplace's equation in Cartesian coordinates, where the potential
    exponentially decays as X goes to negative infinity, and the Y and Z
    coordinates are functions of sines or cosines.

    See Section 3.3 of Griffiths or 2.9 of Jackson for further details.

    TODO how to handle negative vs. positive exponentials functions. Is
    this necessary, as one could always negate the input x values.

    These are often used as a building block for representing the
    magnetopause currents in empirical magnetic field models, see
    Tsyganenko [1995, 1996, 1998, 2013].

    Attributes
    ----------
    piCoeffs : CoefficientExpansion1D
        An expansion containing the nonlinear set of coefficients p_i.
    pkCoeffs : CoefficientExpansion1D
        An expansion containing the nonlinear set of coefficients p_k.
    aikCoeffs : CoefficientExpansion2D
        An expansion containing the linear scaling coefficients a_ik.
    trigParityI : TrigParity
        The TrigParity associated with the Y terms (odd=sine,
        even=cosine).
    trigParityK : TrigParity
        The TrigParity associated with the Z terms (odd=sine,
        even=cosine).
    firstI : int
        Lowest index in 1st dimension of aik.
    lastI : int
        Highest index in 1st dimension of aik.
    firstK : int
        Lowest index in 2nd dimension of aik.
    lastK : int
        Highest index in 2nd dimension of aik.
    """

    def __init__(self, piCoeffs, pkCoeffs, aikCoeffs, trigParityI,
                 trigParityK):
        """Initialize a new CartesianHarmonicField object.

        Initialize a new CartesianHarmonicField object.

        Parameters
        ----------
        piCoeffs : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients p_i.
        pkCoeffs : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients p_k.
        aikCoeffs : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients a_ik.
        trigParityI : TrigParity
            The TrigParity associated with the Y terms (odd=sine,
            even=cosine).
        trigParityK : TrigParity
            The TrigParity associated with the Z terms (odd=sine,
            even=cosine).
        """
        self.piCoeffs = piCoeffs
        self.pkCoeffs = pkCoeffs
        self.aikCoeffs = aikCoeffs
        self.trigParityI = trigParityI
        self.trigParityK = trigParityK
        self.firstI = aikCoeffs.getILowerBoundIndex()
        self.lastI = aikCoeffs.getIUpperBoundIndex()
        self.firstK = aikCoeffs.getJLowerBoundIndex()
        self.lastK = aikCoeffs.getJUpperBoundIndex()

    def evaluate(self, location, buffer):
        """Evaluate the field.
        
        Evaluate the field.
        
        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the field.
        buffer : VectorIJK
            Buffer to hold the field result.
        
        Returns
        -------
        buffer : VectorIJK
            THe field result.
        """
        x = location.i
        y = location.j
        z = location.k
        firstI = self.piCoeffs.getLowerBoundIndex()
        lastI = self.piCoeffs.getUpperBoundIndex()
        firstK = self.pkCoeffs.getLowerBoundIndex()
        lastK = self.pkCoeffs.getUpperBoundIndex()
        bx = 0.0
        by = 0.0
        bz = 0.0
        for i in range(firstI, lastI + 1):
            pi = self.piCoeffs.getCoefficient(i)
            sinYpi = self.trigParityI.evaluate(pi*y)
            cosYpi = self.trigParityI.differentiate(pi*y)
            for k in range(firstK, lastK + 1):
                pk = self.pkCoeffs.getCoefficient(k)
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = self.trigParityK.evaluate(pk*z)
                cosZpk = self.trigParityK.differentiate(pk*z)
                aik = self.aikCoeffs.getCoefficient(i, k)
                bx += aik*exp_*sqrtP*sinYpi*sinZpk
                by += aik*exp_*pi*cosYpi*sinZpk
                bz += aik*exp_*pk*sinYpi*cosZpk
        buffer[:] = [-bx, -by, -bz]
        return buffer

    def evaluateExpansion2D(self, location):
        """Return the full expansion results.
        
        Return the full expansion results.
        
        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the field.
        
        Returns
        -------
        result : Expansion2D
            2D expansion at location.
        """
        x = location.i
        y = location.j
        z = location.k
        expansions = nones((self.aikCoeffs.iSize(), self.aikCoeffs.jSize()))
        for i in range(self.firstI, self.lastI + 1):
            pi = self.piCoeffs.getCoefficient(i)
            sinYpi = self.trigParityI.evaluate(pi*y)
            cosYpi = self.trigParityI.differentiate(pi*y)
            for k in range(self.firstK, self.lastK + 1):
                pk = self.pkCoeffs.getCoefficient(k)
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = self.trigParityK.evaluate(pk*z)
                cosZpk = self.trigParityK.differentiate(pk*z)
                aik = self.aikCoeffs.getCoefficient(i, k)
                bx = -aik*exp_*sqrtP*sinYpi*sinZpk
                by = -aik*exp_*pi*cosYpi*sinZpk
                bz = -aik*exp_*pk*sinYpi*cosZpk
                # scale the vector, the minus sign comes from the B=-dell U
                vect = VectorIJK(bx, by, bz)
                expansions[i - self.firstI][k - self.firstK] = vect
        return Expansion2Ds.createFromArray(expansions, self.firstI,
                                            self.firstK)

    def evaluateExpansion(self, location):
        """Evaluate the expansion at a location.
        
        Evaluate the expansion at a location.
        
        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the expansion.
        
        Returns
        -------
        functions : list of functions
            Functions which make up the harmonic field.
        """
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for i in range(self.firstI, self.lastI + 1):
            for k in range(self.firstK, self.lastK + 1):
                functions.append(expansions.getExpansion(i, k))
        return functions
