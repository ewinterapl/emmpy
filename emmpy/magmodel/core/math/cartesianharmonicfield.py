"""A harmonic field in Cartesian coordinates.

A harmonic field in Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, exp, sin, sqrt

from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.trigparity import ODD
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK
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
        self.firstI = aikCoeffs.iLowerBoundIndex
        self.lastI = aikCoeffs.iUpperBoundIndex
        self.firstK = aikCoeffs.jLowerBoundIndex
        self.lastK = aikCoeffs.jUpperBoundIndex

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
        firstI = 0
        lastI = len(self.piCoeffs) - 1
        firstK = 1
        lastK = len(self.pkCoeffs)
        bx = 0.0
        by = 0.0
        bz = 0.0
        if self.trigParityI is ODD:
            itrig = sin
            idtrig = cos
        else:
            itrig = cos
            idtrig = lambda x: -sin(x)
        if self.trigParityK is ODD:
            ktrig = sin
            kdtrig = cos
        else:
            ktrig = cos
            kdtrig = lambda x: -sin(x)
        for i in range(lastI - firstI + 1):
            pi = self.piCoeffs[i]
            sinYpi = itrig(pi*y)
            cosYpi = idtrig(pi*y)
            for k in range(lastK - firstK + 1):
                pk = self.pkCoeffs[k]
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = ktrig(pk*z)
                cosZpk = kdtrig(pk*z)
                aik = self.aikCoeffs[i + firstI, k + firstK]
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
        if self.trigParityI is ODD:
            itrig = sin
            idtrig = cos
        else:
            itrig = cos
            idtrig = lambda x: -sin(x)
        if self.trigParityK is ODD:
            ktrig = sin
            kdtrig = cos
        else:
            ktrig = cos
            kdtrig = lambda x: -sin(x)
        expansions = nones((self.aikCoeffs.iSize(), self.aikCoeffs.jSize()))
        for i in range(self.lastI - self.firstI + 1):
            pi = self.piCoeffs.getCoefficient(i + self.firstI)
            sinYpi = itrig(pi*y)
            cosYpi = idtrig(pi*y)
            for k in range(self.lastK - self.firstK + 1):
                pk = self.pkCoeffs.getCoefficient(k + self.firstK)
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = ktrig(pk*z)
                cosZpk = kdtrig(pk*z)
                aik = self.aikCoeffs.getCoefficient(i + self.firstI, k + self.firstK)
                bx = -aik*exp_*sqrtP*sinYpi*sinZpk
                by = -aik*exp_*pi*cosYpi*sinZpk
                bz = -aik*exp_*pk*sinYpi*cosZpk
                # scale the vector, the minus sign comes from the B=-dell U
                vect = VectorIJK(bx, by, bz)
                expansions[i][k] = vect
        return Expansion2Ds.createFromArray(expansions, self.firstI, self.firstK)

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
        for i in range(self.lastI - self.firstI + 1):
            for k in range(self.lastK - self.firstK + 1):
                functions.append(expansions.getExpansion(i + self.firstI, k + self.firstK))
        return functions
