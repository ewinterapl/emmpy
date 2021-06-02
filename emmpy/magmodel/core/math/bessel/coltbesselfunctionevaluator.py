"""emmpy.magmodel.core.math.bessel.coltbesselfunctionevaluator"""

from emmpy.magmodel.core.math.bessel.besselfunctionevaluator import (
    BesselFunctionEvaluator
)
from emmpy.magmodel.core.math.bessel.coltbessel import ColtBessel


class ColtBesselFunctionEvaluator(BesselFunctionEvaluator):
    """An implementation of a {@link BesselFunctionEvaluator} using the Colt
    library.

    @author G.K.Stephens
    """

    @staticmethod
    def besselj0(x):
        return ColtBessel.j0(x)

    @staticmethod
    def besselj1(x):
        return ColtBessel.j1(x)

    @staticmethod
    def besseljn(n, x):
        """besseljn

        TODO Ugh, when x is small but non-zero, the Colt evaluator will often
        return NaNs. This is a bug in their algorithm, that looks like the
        recursive algorithm gets so small that it is smaller than the smallest
        double. Tsyganenko's code has the same problem, so Sasha fixed it with
        the following change. This is a hack though, the algorithm should be
        fixed.
        """
        if abs(n) > 1 and abs(x) < 1.0E-12:
            return 0.0
        return ColtBessel.jn(n, x)

    @staticmethod
    def besselj0jn(n, x):
        bessels = [None]*(n + 1)
        for nn in range(n + 1):
            bessels[nn] = ColtBesselFunctionEvaluator.besseljn(nn, x)
        return bessels
