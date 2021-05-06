"""emmpy.magmodel.core.math.cartesianharmonicfield"""


# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;
# import static crucible.core.math.CrucibleMath.exp;
# import static crucible.core.math.CrucibleMath.sqrt;
# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.Expansion2D;

from math import exp, sqrt

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class CartesianHarmonicField(BasisVectorField):
    """A vector field that is associated with the scalar potential solution of
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
        """Constructor

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
        self.trigParityI = TrigParity.trigParityI
        self.trigParityK = TrigParity.trigParityK
        self.firstI = aikCoeffs.getILowerBoundIndex()
        self.lastI = aikCoeffs.getIUpperBoundIndex()
        self.firstK = aikCoeffs.getJLowerBoundIndex()
        self.lastK = aikCoeffs.getJUpperBoundIndex()

    def evaluate(self, location, buffer):
        x = location.getI()
        y = location.getJ()
        z = location.getK()
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
        return buffer.setTo(-bx, -by, -bz)

    def evaluateExpansion2D(self, location):
        """Returns the full expansion results."""
        x = location.getI()
        y = location.getJ()
        z = location.getK()
        expansions = [[None]*self.aikCoeffs.jSize()]*self.aikCoeffs.iSize()
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
        return self.firstI

    def getLastIexpansionNumber(self):
        return self.lastI

    def getFistKexpansionNumber(self):
        return self.firstK

    def getLastKexpansionNumber(self):
        return self.lastK

    def evaluateExpansion(self, location):
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for i in range(self.firstI, self.lastI + 1):
            for k in range(self.firstK, self.lastK + 1):
                functions.append(expansions.getExpansion(i, k))
        return functions

    def getNumberOfBasisFunctions(self):
        return self.aikCoeffs.iSize()*self.aikCoeffs.jSize()
