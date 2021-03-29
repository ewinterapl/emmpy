"""vectorfield"""

# package crucible.core.math.vectorfields;

# import crucible.core.exceptions.FunctionEvaluationException;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

class VectorField:
    """Represents a 3 dimensional vector field, which maps a {@link VectorIJK}
    to another {@link VectorIJK}.

    @author vandejd1
    @author G.K.Stephens
    """

    # def __init__(self):
    #     """Interface - do not instantiate"""
    #     raise Exception

    def evaluate(self, *args):
        """Evaluate the field at the given position

        units and such are up to the implementors

        @throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        if len(args) == 1:
            # @param location {@link VectorIJK}, often location
            # @return the resultant {@link VectorIJK}
            (location,) = args
            return self.evaluate(location, VectorIJK())
        elif len(args) == 2:
            # Evaluate the field at the given position, put the result into the
            # buffer and return the buffer
            # @param location {@link VectorIJK}, often location
            # @param buffer a {@link VectorIJK} buffer that will hold the result of the evaluation
            # @return the buffer
            raise Exception
