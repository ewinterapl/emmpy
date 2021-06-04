"""A 2-D scalar field."""


class ScalarField2D:
    """A 2-D scalar field.

    @author G.K.Stephens
    """

    def __init__(self, location):
        """Build a new object."""
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
