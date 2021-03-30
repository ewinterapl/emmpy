"""emmpy.crucible.core.math.vectorfields.vectorfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class VectorField:
    """Represents a 3 dimensional vector field, which maps a VectorIJK to
    another VectorIJK.

    author vandejd1
    author G.K.Stephens
    """

    def __init__(self):
        """Interface - do not instantiate"""
        raise Exception

    def evaluate(self, *args):
        """Interface - do not invoke.

        Evaluate the field at the given position

        units and such are up to the implementors

        throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        if len(args) == 1:
            # param location VectorIJK, often location
            # return the resultant VectorIJK
            (location,) = args
            return self.evaluate(location, VectorIJK())
        elif len(args) == 2:
            # Evaluate the field at the given position, put the result into the
            # buffer and return the buffer
            # param location VectorIJK, often location
            # param buffer a VectorIJK buffer that will hold the result of the
            # evaluation
            # return the buffer
            (location, buffer) = args
            raise Exception
        else:
            raise Exception
