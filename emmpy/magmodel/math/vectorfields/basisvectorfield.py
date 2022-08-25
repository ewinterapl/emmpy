"""Base interface for a basis vector field.

N.B. This class was created from a Java interface, and therefore most of
these methods will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""

from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


class BasisVectorField(VectorField):
    """Base interface for a basis vector field.

    An interface that represents a VectorField that can decomposed into a
    linear expansion of vector fields.
    """

    def evaluate(self, *args):
        """Evaluate the field.
        
        Evaluate the field.
        
        Parameters
        ----------
        location : VectorIJK
            Location to evaluate field.
        buffer : VectorIJK (optional)
            Buffer to hold result.

        Returns
        -------
        buffer : VectorIJK
            Vector value of basis vector field.
        
        Raises
        ------
        TypeError
            If incorrect parameters are provided.
        """
        if len(args) == 1:
            (location,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (location, buffer) = args
        else:
            raise TypeError
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
