"""emmpy.crucible.core.math.vectorfields.scalarfield"""


class ScalarField:
    """Represents a 3 dimensional scalar field, which maps a VectorIJK to a
    scalar (double).

    @author G.K.Stephens
    """

    def __init__(self, location):
        """Interface - do not instantiate."""
        raise Exception

    def evaluate(self, location):
        """Evaluate the field at the given position, and return a scalar value

        units and such are up to the implementors

        @param location {@link VectorIJK}, often location
        @return the scalar value
        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        # Interface - do not invoke.
        raise Exception
