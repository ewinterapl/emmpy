"""emmpy.crucible.core.math.functions.univariatefunction

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class UnivariateFunction:
    """Simple interface describing a function of a single variable.

    @author F.S.Turner
    """

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE.
        """
        raise Exception

    def evaluate(self, t):
        """Evaluates the function at the specified value.

        INTERFACE - DO NOT INVOKE

        @param t the value of interest
        @return the value of the function at t
        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        raise Exception
