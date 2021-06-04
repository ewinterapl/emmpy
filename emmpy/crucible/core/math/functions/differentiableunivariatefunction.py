"""A differentiable univariate function.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.functions.univariatefunction import (
    UnivariateFunction
)


class DifferentiableUnivariateFunction(UnivariateFunction):
    """A single variable, differentiable function.

    author F.S.Turner
    """

    def __init__(self):
        """Build a new object.

        INTERFACE - DO NOT INSTANTIATE
        """

    def differentiate(self, t):
        """Evaluate the derivative of the univariate function.

        INTERFACE - DO NOT INVOKE

        @param t the value of interest
        @return the derivative of the function evaluated at t
        """
        raise Exception
