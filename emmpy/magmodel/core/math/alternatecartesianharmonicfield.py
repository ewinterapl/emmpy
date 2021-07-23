"""A specialized version of a Cartesian harmonic field."""


from math import exp, sqrt

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.utilities.nones import nones


class AlternateCartesianHarmonicField(BasisVectorField):
    """A specialized version of a Cartesian harmonic field.

    This class is very similar to CartesianHarmonicField which represents
    scalar potential solution of Laplace's equation in Cartesian coordinate.

    The difference is that the last K expansion is the 'derivative' term of the
    expansion. See Tsyganenko 2002, A model of the near magnetosphere with a
    dawn-dusk asymmetry 1. Mathematical structure Eq. 31 and 32, as he
    explains:

    "The potentials (equation (31)) were obtained by taking a derivative of
    equation (30) with respect to 1/rk; combining the potentials (equations
    (30) and (31)) was found necessary in order to avoid the tendency of the
    parameters rk to cluster in close pairs, accompanied by an unlimited growth
    of the corresponding linear coefficients in the course of the iterative
    minimization of Bn^2"

    TODO Using SVD to solve for the coefficients may alleviate the issue
    described above.

    author G.K.Stephens
    """

    def __init__(self, piCoeffs, pkCoeffs, aikCoeffs, trigParityI,
                 trigParityK):
        """Build a new object."""
        self.piCoeffs = piCoeffs
        self.pkCoeffs = pkCoeffs
        self.aikCoeffs = aikCoeffs
        self.trigParityI = trigParityI
        self.trigParityK = trigParityK
        self.firstI = aikCoeffs.getILowerBoundIndex()
        self.lastI = aikCoeffs.getIUpperBoundIndex()
        self.firstK = aikCoeffs.getJLowerBoundIndex()
        self.lastK = aikCoeffs.getJUpperBoundIndex()

    # def evaluate(self, location, buffer):
    #     x = location.getI()
    #     y = location.getJ()
    #     z = location.getK()
    #     firstI = self.piCoeffs.getLowerBoundIndex()
    #     lastI = self.piCoeffs.getUpperBoundIndex()
    #     firstK = self.pkCoeffs.getLowerBoundIndex()
    #     lastK = self.pkCoeffs.getUpperBoundIndex()
    #     bx = 0.0
    #     by = 0.0
    #     bz = 0.0
    #     for i in range(firstI, lastI + 1):
    #         pi = self.piCoeffs.getCoefficient(i)
    #         sinYpi = self.trigParityI.evaluate(pi*y)
    #         cosYpi = self.trigParityI.differentiate(pi*y)
    #         for k in range(firstK, lastK + 1):
    #             pk = self.pkCoeffs.getCoefficient(k)
    #             sqrtP = sqrt(pi*pi + pk*pk)
    #             exp_ = exp(x*sqrtP)
    #             sinZpk = self.trigParityK.evaluate(pk*z)
    #             cosZpk = self.trigParityK.differentiate(pk*z)
    #             aik = self.aikCoeffs.getCoefficient(i, k)
    #             if k == lastK:
    #                 bx += aik*exp_*sinYpi*(sqrtP*z*cosZpk +
    #                                        sinZpk*pk*(x + 1.0/sqrtP))
    #                 by += aik*exp_*pi*cosYpi*(z*cosZpk + x*pk*sinZpk/sqrtP)
    #                 bz += aik*exp_*sinYpi*(cosZpk*(1.0 + x*pk*pk/sqrtP) -
    #                                        z*pk*sinZpk)
    #             else:
    #                 bx += aik*exp_*sqrtP*sinYpi*sinZpk
    #                 by += aik*exp_*pi*cosYpi*sinZpk
    #                 bz += aik*exp_*pk*sinYpi*cosZpk
    #     return buffer.setTo(-bx, -by, -bz)

    def evaluateExpansion2D(self, location):
        """Return the full expansion results."""
        x = location.i
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
                if k == self.lastK:
                    bx = (-aik*exp_*sinYpi*(sqrtP*z*cosZpk +
                          sinZpk*pk*(x + 1.0/sqrtP)))
                    by = -aik*exp_*pi*cosYpi*(z*cosZpk + x*pk*sinZpk/sqrtP)
                    bz = (-aik*exp_*sinYpi*(cosZpk*(1.0 + x*pk*pk/sqrtP)
                                            - z*pk*sinZpk))
                    # scale the vector, the minus sign comes from the B=-dell U
                    vect = VectorIJK(bx, by, bz)
                    expansions[i - self.firstI][k - self.firstK] = vect
                else:
                    bx = -aik*exp_*sqrtP*sinYpi*sinZpk
                    by = -aik*exp_*pi*cosYpi*sinZpk
                    bz = -aik*exp_*pk*sinYpi*cosZpk
                    # scale the vector, the minus sign comes from the B=-dell U
                    vect = VectorIJK(bx, by, bz)
                    expansions[i - self.firstI][k - self.firstK] = vect
        return Expansion2Ds.createFromArray(expansions, self.firstI,
                                            self.firstK)

    # def getFistIexpansionNumber(self):
    #     return self.firstI

    # def getLastIexpansionNumber(self):
    #     return self.lastI

    # def getFistKexpansionNumber(self):
    #     return self.firstK

    # def getLastKexpansionNumber(self):
    #     return self.lastK

    def evaluateExpansion(self, location):
        """Evaluate the expansion."""
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for i in range(self.firstI, self.lastI + 1):
            for k in range(self.firstK, self.lastK + 1):
                functions.append(expansions.getExpansion(i, k))
        return functions

    # def getNumberOfBasisFunctions(self):
    #     return self.aikCoeffs.iSize()*self.aikCoeffs.jSize()
