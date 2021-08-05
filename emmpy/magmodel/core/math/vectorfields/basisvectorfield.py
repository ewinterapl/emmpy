"""Base interface for a basis vector field.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class BasisVectorField(VectorField):
    """Base interface for a basis vector field.

    An interface that represents a VectorField that can decomposed into a
    linear expansion of vector fields.

    returns the results of the vector field expansion in an ImmutableList.

    The coefficients a_i are considered an implementation detail.

    author G.K.Stephens
    """

    def __init__(self):
        """Build a new object."""

    def evaluate(self, *args):
        """Evaluate the field."""
        if len(args) == 1:
            (location,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (location, buffer) = args
        else:
            raise Exception
        basisVectors = self.evaluateExpansion(location)
        fx = 0.0
        fy = 0.0
        fz = 0.0
        for basisVector in basisVectors:
            fx += basisVector.i
            fy += basisVector.j
            fz += basisVector.k
        buffer[:] = [fx, fy, fz]
        return buffer

