"""emmpy.magmodel.core.math.trigparity"""


from math import cos, sin

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)


class TrigParity(DifferentiableUnivariateFunction):
    """A representation of the odd and even parity that exists between the sine
    and cosine function. This type of parity often arises in Fourier series and
    boundary value problems. Solutions to boundary problems are often linear
    combinations of sines and cosines.

    EVEN: f(x) = cos(x), df/dx = -sin(x)
    ODD: f(x) = sin(x), df/dx = cos(x)

    @author G.K.Stephens
    """

    # the even trigonometric parity, the cosine function
    EVEN = DifferentiableUnivariateFunction()
    EVEN.evaluate = lambda t: cos(t)
    EVEN.differentiate = lambda t: -sin(t)

    # the odd trigonometric parity, the sine function
    ODD = DifferentiableUnivariateFunction()
    ODD.evaluate = lambda t: sin(t)
    ODD.differentiate = lambda t: cos(t)

    def __init__(self, function):
        """Constructor"""
        self.function = function

    def evaluate(self, t):
        return self.function.evaluate(t)

    def differentiate(self, t):
        return self.function.differentiate(t)
