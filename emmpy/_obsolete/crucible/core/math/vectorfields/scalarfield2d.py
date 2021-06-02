"""emmpy.crucible.core.math.vectorfields.scalarfield2d"""


class ScalarField2D:
    """Represents a 2 dimensional scalar field, which maps a VectorIJ to a
    scalar (double).

    @author G.K.Stephens
    """

    def __init__(self, location):
        """Interface - do not instantiate."""
        raise Exception

    def evaluate(self, location):
        """Evaluate the scalar at the given position, return the double.

        units and such are up to the implementors

        @param location {@link VectorIJ}, often location
        @return the scalar
        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        # Interface - do not invoke.
        raise Exception
