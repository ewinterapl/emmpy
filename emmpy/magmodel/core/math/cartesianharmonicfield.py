"""A harmonic field in Cartesian coordinates."""


from math import exp, sqrt

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.utilities.nones import nones


class CartesianHarmonicField(BasisVectorField):
    """A harmonic field in Cartesian coordinates.

    A vector field that is associated with the scalar potential solution of
    Laplace's equation in Cartesian coordinates, where the potential
    exponentially decays as X goes to negative infinity, and the Y and Z
    coordinates are functions of sines or cosines.

    See Section 3.3 of Griffiths or 2.9 of Jackson for further details.

    TODO how to handle negative vs. positive exponentials functions. Is this
    necessary, as one could always negate the input x values.

    These are often used as a building block for representing the magnetopause
    currents in empirical magnetic field models, see Tsyganenko [1995, 1996,
    1998, 2013].

    author G.K.Stephens
    """

    def __init__(self, piCoeffs, pkCoeffs, aikCoeffs, trigParityI,
                 trigParityK):
        """Build a new object.

        param pkCoeffs an expansion containing the nonlinear set of
        coefficients p_k
        param piCoeffs an expansion containing the nonlinear set of
        coefficients p_i
        param aikCoeffs an expansion containing the linear scaling
        coefficients a_ik
        param trigParityI the TrigParity associated with the Y terms
        (odd=sine, even=cosine)
        param trigParityK the TrigParity associated with the Z terms
        (odd=sine, even=cosine)
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
        """Evaluate the field."""
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
        """Return the full expansion results."""
        x = location.getI()
        y = location.getJ()
        z = location.getK()
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

    def getFistIexpansionNumber(self):
        """Get the first dimension lowest index."""
        return self.firstI

    def getLastIexpansionNumber(self):
        """Get the first dimension highest index."""
        return self.lastI

    def getFistKexpansionNumber(self):
        """Get the second dimension first index."""
        return self.firstK

    def getLastKexpansionNumber(self):
        """Get the second dimension last index."""
        return self.lastK

    def evaluateExpansion(self, location):
        """Evaluate the expansion at a location."""
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for i in range(self.firstI, self.lastI + 1):
            for k in range(self.firstK, self.lastK + 1):
                functions.append(expansions.getExpansion(i, k))
        return functions

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions."""
        return self.aikCoeffs.iSize()*self.aikCoeffs.jSize()
