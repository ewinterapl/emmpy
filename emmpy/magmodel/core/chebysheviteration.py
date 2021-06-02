"""emmpy.magmodel.core.chebysheviteration"""


from math import cos, sin

from emmpy.magmodel.core.math.trigparity import TrigParity


class ChebyshevIteration:
    """Implements Chebyshev's iterative algorithm for fast computation of sines
    and cosines.
    
    This is particularly useful for quickly computing an expansion of sines
    and/or cosines, as the number of trig evaluations is minimal.

    author G.K.Stephens
    """

    @staticmethod
    def evaluateTrigExpansions(*args):
        if len(args) == 3:
            (phi, sinMphi, cosMphi) = args
            # This method uses the Chebyshev iterative method, to evaluate
            # cos(m*phi) and sin(m*phi) values, and stores the results in the
            # supplied arrays. This is particularly useful for quickly
            # computing an expansion of sines and/or cosines, as the number
            # of trig evaluations is minimal.
            # Chebyshev's iteration algorithm is:
            # <img src="doc-files/chebyshevMethod.png" />
            # param float phi the angle to evaluate the cos(m*phi) and
            # sin(m*phi)
            # param [float] sinMphi a supplied array where the sin(m*phi)
            # values will be stored
            # param [float] cosMphi a supplied array where the cos(m*phi)
            # values will be stored, must be the same length
            # return None

            # int size
            size = len(sinMphi)

            # compute the m = 1 terms
            # float cosPhi, sinPhi
            cosPhi = cos(phi)
            sinPhi = sin(phi)

            # the m = 0 terms are cos(0) = 1 and sin(0) = 0
            cosMphi[0] = 1.0
            sinMphi[0] = 0.0

            # if the number is 0, we are done, so just return
            if size == 1:
                return

            cosMphi[1] = cosPhi
            sinMphi[1] = sinPhi

            # apply the recursive algorithm
            for m in range(2, size):
                cosMphi[m] = 2*cosPhi*cosMphi[m - 1] - cosMphi[m - 2]
                sinMphi[m] = 2*cosPhi*sinMphi[m - 1] - sinMphi[m - 2]

        elif len(args) == 4:
            (phi, trigMphi, dTrigMphi, trigParity) = args
            # This method uses the Chebyshev iterative method, to evaluate
            # sin/cos(m*phi) and its derivative cos/-sin(m*phi) values, and
            # stores the results in the supplied arrays.
            # The TrigParity is used to determine if the arrays are filled
            # with f=sin, df=cos (for ODD parity) or f=cos, df=-sin (for
            # EVEN parity). This is particularly useful for quickly
            # computing an expansion of sines and/or cosines, as the number
            # of trig evaluations is minimal.
            # param float phi the angle to evaluate the cos(m*phi) and
            # sin(m*phi)
            # param [float] trigMphi a supplied array where the
            # sin/cos(m*phi) values will be stored
            # param [float] dTrigMphi a supplied array where the
            # cos/-sin(m*phi) values will be stored, must be the same
            # length
            # param TrigParity trigParity is used to determine if the
            # arrays are filled with f=sin, df=cos (for ODD parity) or
            # f=cos, df=-sin (for EVEN parity)
            # return None
            if trigParity is TrigParity.ODD:
                # fill the expansion with f=sin(m*phi) and df=cos(m*phi)
                ChebyshevIteration.evaluateTrigExpansions(phi, trigMphi, dTrigMphi)
            else:
                # fill the expansion with f=cos(m*phi) and df=-sin(m*phi)
                ChebyshevIteration.evaluateTrigExpansions(phi, dTrigMphi, trigMphi)
                for i in range(len(dTrigMphi)):
                    dTrigMphi[i] = -dTrigMphi[i]
        else:
            raise Exception
