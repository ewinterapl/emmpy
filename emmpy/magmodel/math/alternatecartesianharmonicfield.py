"""A specialized version of a Cartesian harmonic field.

A specialized version of a Cartesian harmonic field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.magmodel.math.expansions.arrayexpansion2d import ArrayExpansion2D
from emmpy.magmodel.math.trigparity import ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
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
        """
        self.piCoeffs = piCoeffs
        self.pkCoeffs = pkCoeffs
        self.aikCoeffs = aikCoeffs
        self.trigParityI = trigParityI
        self.trigParityK = trigParityK

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
        if self.trigParityI is ODD:
            itrig = np.sin
            idtrig = np.cos
        else:
            itrig = np.cos
            idtrig = lambda x: -np.sin(x)
        if self.trigParityK is ODD:
            ktrig = np.sin
            kdtrig = np.cos
        else:
            ktrig = np.cos
            kdtrig = lambda x: -np.sin(x)
        expansions = nones((len(self.aikCoeffs), len(self.aikCoeffs[0])))
        sinYpi = itrig(self.piCoeffs*y)
        cosYpi = idtrig(self.piCoeffs*y)
        sinZpk = ktrig(self.pkCoeffs*z)
        cosZpk = kdtrig(self.pkCoeffs*z)
        sqrtP = np.sqrt(np.array([[pi**2 + pk**2 for pk in self.pkCoeffs] for pi in self.piCoeffs]))
        exp_ = np.exp(x*sqrtP)
        aik = np.array(self.aikCoeffs[...])
        pi = np.array(self.piCoeffs)
        pk = np.array(self.pkCoeffs)
        sinYpiXsinZpk = np.outer(sinYpi, sinZpk)
        sinYpiXcosZpk = np.outer(sinYpi, cosZpk)
        cosYpiXsinZpk = np.outer(cosYpi, sinZpk)
        ni = len(self.piCoeffs)
        nk = len(self.pkCoeffs)
        bx = np.empty((ni, nk))
        bx[:, :-1] = -aik[:, :-1]*exp_[:, :-1]*sqrtP[:, :-1]*sinYpiXsinZpk[:, :-1]
        bx[:, -1] = (
            -aik[:, -1]*exp_[:, -1]*sinYpi *
            (sqrtP[:, -1]*z*cosZpk[-1] + sinZpk[-1]*pk[-1]*(x + 1.0/sqrtP[:, -1]))
        )
        by = np.empty((ni, nk))
        by[:, :-1] = (
            -aik[:, :-1]*exp_[:, :-1]*np.broadcast_to(pi, (nk, ni)).T[:, :-1]*cosYpiXsinZpk[:, :-1]
        )
        by[:, -1] = (
            -aik[:, -1]*exp_[:, -1]*np.broadcast_to(pi, (nk, ni)).T[:, -1] *
            np.broadcast_to(cosYpi, (nk, ni)).T[:, -1] *
            (z*cosZpk[-1] + x*pk[-1]*sinZpk[-1]/sqrtP[:, -1])
        )
        bz = np.empty((ni, nk))
        bz[:, :-1] = -aik[:, :-1]*exp_[:, :-1]*pk[:-1]*sinYpiXcosZpk[:, :-1]
        bz[:, -1] = (
            -aik[:, -1]*exp_[:, -1] * sinYpi * 
            (cosZpk[-1]*(1.0 + x*pk[-1]*pk[-1]/sqrtP[:, -1]) - z*pk[-1]*sinZpk[-1])
        )
        for i in range(ni):
            for k in range(nk):
                vect = VectorIJK(bx[i, k], by[i, k], bz[i, k])
                expansions[i][k] = vect
        return ArrayExpansion2D(expansions)

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
        for i in range(len(self.aikCoeffs)):
            for k in range(len(self.aikCoeffs[0])):
                functions.append(expansions[i][k])
        return functions
