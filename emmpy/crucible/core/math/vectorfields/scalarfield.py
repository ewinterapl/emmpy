"""A 3-D scalar field.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class ScalarField:
    """A 3-D scalar field.

    @author G.K.Stephens
    """

    def __init__(self, location):
        """Build a new object."""
        raise Exception

    def evaluate(self, location):
        """Evaluate the field at a position.

        INTERFACE - DO NOT INVOKE.

        units and such are up to the implementors

        @param location {@link VectorIJK}, often location
        @return the scalar value
        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        raise Exception
