"""emmpy.magmodel.core.math.bessel.besselfunctionevaluator

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.

This interface is for evaluating commonly used forms of Bessel functions of
the first kind.

@author G.K.Stephens
"""


class BesselFunctionEvaluator:

    def besselj0(self, x):
        """INTERFACE - DO NOT INSTANTIATE

        Evaluates the Bessel function of the first kind to the order of n = 0.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besselj1(self, x):
        """INTERFACE - DO NOT INVOKE

        Evaluates the Bessel function of the first kind to the order of n = 1.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besseljn(self, n, x):
        """INTERFACE - DO NOT INVOKE

        Evaluates the Bessel function of the first kind to the order n.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        """
        raise Exception

    def besselj0jn(self, n, x):
        """INTERFACE - DO NOT INVOKE

        Evaluates the Bessel function of the first kind from order 0 to
        order n.

        @param n the order of the Bessel function.
        @param x the value to compute the Bessel function of.
        @return an array containing all the Bessel functions from order 0 to
        order n, the size of the array will be n+1
        """
        raise Exception
