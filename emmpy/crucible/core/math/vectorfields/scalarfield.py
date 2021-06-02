"""emmpy.crucible.core.math.vectorfields.scalarfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class ScalarField:
    """Represents a 3 dimensional scalar field, which maps a VectorIJK to a
    scalar (double).

    @author G.K.Stephens
    """

    def __init__(self, location):
        """INTERFACE - DO NOT INSTANTIATE"""
        raise Exception

    def evaluate(self, location):
        """Evaluate the field at the given position, and return a scalar value

        INTERFACE - DO NOT INVOKE.

        units and such are up to the implementors

        @param location {@link VectorIJK}, often location
        @return the scalar value
        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        raise Exception
