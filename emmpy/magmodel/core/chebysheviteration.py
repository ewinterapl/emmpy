"""The Chebyshev iteration algorithm.

The Chebyshev iteration algorithm.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

from emmpy.magmodel.core.math.trigparity import TrigParity


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
        """Evaluate the trigonometric expansions.
        
        Evaluate the trigonometric expansions.
        
        Parameters
        ----------
        phi : float
            The angle to evaluate the cos(m*phi) and sin(m*phi).
        sinMphi, cosMphi : list of float
            Buffer arrays to hold sin() and cos() results.
        OR
        phi : float
            The angle to evaluate the cos(m*phi) and sin(m*phi.
        trigMphi, dTrigMphi : list of float
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
            # This method uses the Chebyshev iterative method, to evaluate
            # cos(m*phi) and sin(m*phi) values, and stores the results in the
            # supplied arrays. This is particularly useful for quickly
            # computing an expansion of sines and/or cosines, as the number
            # of trig evaluations is minimal.
            size = len(sinMphi)

            # Compute the m = 1 terms.
            cosPhi = cos(phi)
            sinPhi = sin(phi)

            # The m = 0 terms are cos(0) = 1 and sin(0) = 0.
            cosMphi[0] = 1.0
            sinMphi[0] = 0.0

            # If the number is 0, we are done, so just return.
            if size == 1:
                return

            cosMphi[1] = cosPhi
            sinMphi[1] = sinPhi

            # Apply the recursive algorithm.
            for m in range(2, size):
                cosMphi[m] = 2*cosPhi*cosMphi[m - 1] - cosMphi[m - 2]
                sinMphi[m] = 2*cosPhi*sinMphi[m - 1] - sinMphi[m - 2]

        elif len(args) == 4:
            (phi, trigMphi, dTrigMphi, trigParity) = args
            # This method uses the Chebyshev iterative method, to evaluate
            # sin/cos(m*phi) and its derivative cos/-sin(m*phi) values,
            # and stores the results in the supplied arrays.
            # The TrigParity is used to determine if the arrays are filled
            # with f=sin, df=cos (for ODD parity) or f=cos, df=-sin (for
            # EVEN parity). This is particularly useful for quickly
            # computing an expansion of sines and/or cosines, as the
            # number of trig evaluations is minimal.
            if trigParity is TrigParity.ODD:
                # Fill the expansion with f=sin(m*phi) and df=cos(m*phi).
                ChebyshevIteration.evaluateTrigExpansions(
                    phi, trigMphi, dTrigMphi)
            else:
                # Fill the expansion with f=cos(m*phi) and df=-sin(m*phi).
                ChebyshevIteration.evaluateTrigExpansions(
                    phi, dTrigMphi, trigMphi)
                for i in range(len(dTrigMphi)):
                    dTrigMphi[i] = -dTrigMphi[i]
        else:
            raise TypeError
