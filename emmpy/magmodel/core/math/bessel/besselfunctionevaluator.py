"""emmpy.magmodel.core.math.bessel.besselfunctionevaluator

This interface is for evaluating commonly used forms of Bessel functions of
the first kind.

@author G.K.Stephens
"""

class BesselFunctionEvaluator:

    def besselj0(self, x):
        """Evaluates the Bessel function of the first kind to the order of
        n = 0.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besselj1(self, x):
        """Evaluates the Bessel function of the first kind to the order of
        n = 1.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besseljn(self, n, x):
        """Evaluates the Bessel function of the first kind to the order n.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besselj0jn(self, n, x):
        """Evaluates the Bessel function of the first kind from order 0 to
        order n.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        @return an array containing all the Bessel functions from order 0 to
        order n, the size of the array will be n+1
        """
        raise Exception
