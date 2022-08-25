"""The Chebyshev iteration algorithm.

The Chebyshev iteration algorithm.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.magmodel.math.trigparity import ODD


class ChebyshevIteration:
    """The Chebyshev iteration algorithm.

    Implements Chebyshev's iterative algorithm for fast computation of
    sines and cosines.

    This is particularly useful for quickly computing an expansion of
    sines and/or cosines, as the number of trig evaluations is minimal.

    Attributes
    ----------
    None
    """

    @staticmethod
    def evaluateTrigExpansions(*args):
        """Compute the trigonometric expansion components.

        Compute the trigonometric expansion components. The components are
        the sines and cosines of the integral multiples of phi:

        sinMphi = [sin(0*phi), sin(1*phi), sin(2*phi), ..., sin(m*phi)]
        cosMphi = [cos(0*phi), cos(1*phi), cos(2*phi), ..., cos(m*phi)]

        where m is size - 1, and size is the length of sinMphi and cosMphi
        (which must be of identical length).

        If 3 parameters are provided, then just copy the sine and cosine
        components to the corresponding buffers.

        If 4 parameters are provided, assign the expansions based on the
        trigonometric parity:

        ODD:  trigMphi = sinMphi, dTrigMphi =  cosMphi
        EVEN: trigMphi = cosMphi, dTrigMphi = -sinMphi

        Parameters
        ----------
        phi : float
            The angle to use for computing the expansions.
        sinMphi, cosMphi : ndarray of float
            Buffer arrays to hold sin() and cos() results.
        OR
        trigMphi, dTrigMphi : ndarray of float
            Buffer arrays to store the results.
        trigParity : TrigParity
            Odd or even.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            If incorrect parameters are provided.
        """
        if len(args) == 3:
            (phi, sinMphi, cosMphi) = args
        elif len(args) == 4:
            (phi, trigMphi, dTrigMphi, trigParity) = args
        else:
            raise TypeError
        size = len(args[1])
        sizes = np.array(range(0, size))
        phis = phi*sizes
        sines = np.sin(phis)
        cosines = np.cos(phis)
        if len(args) == 3:
            sinMphi[:] = sines
            cosMphi[:] = cosines
        else:
            if trigParity is ODD:
                trigMphi[:] = sines
                dTrigMphi[:] = cosines
            else:
                trigMphi[:] = cosines
                dTrigMphi[:] = -sines
