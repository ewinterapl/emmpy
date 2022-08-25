"""A harmonic field in Cartesian coordinates.

A harmonic field in Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, exp, sin, sqrt

from emmpy.magmodel.math.trigparity import ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
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
        firstK = 0
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
        for i in range(len(self.piCoeffs)):
            pi = self.piCoeffs[i]
            sinYpi = itrig(pi*y)
            cosYpi = idtrig(pi*y)
            for k in range(len(self.pkCoeffs)):
                pk = self.pkCoeffs[k]
                sqrtP = sqrt(pi*pi + pk*pk)
                exp_ = exp(x*sqrtP)
                sinZpk = ktrig(pk*z)
                cosZpk = kdtrig(pk*z)
                aik = self.aikCoeffs[i, k + firstK]
                bx += aik*exp_*sqrtP*sinYpi*sinZpk
                by += aik*exp_*pi*cosYpi*sinZpk
                bz += aik*exp_*pk*sinYpi*cosZpk
        buffer[:] = [-bx, -by, -bz]
        return buffer
