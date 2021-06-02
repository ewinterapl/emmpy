"""emmpy.magmodel.core.math.vectorfields.basisvectorfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class BasisVectorField(VectorField):
    """An interface that represents a VectorField that can decomposed into a
    linear expansion of vector fields.

    returns the results of the vector field expansion in an ImmutableList.

    The coefficients a_i are considered an implementation detail.

    author G.K.Stephens
    """

    def __init__(self):
        pass

    def evaluate(self, *args):
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
            fx += basisVector.getI()
            fy += basisVector.getJ()
            fz += basisVector.getK()
        return buffer.setTo(fx, fy, fz)
