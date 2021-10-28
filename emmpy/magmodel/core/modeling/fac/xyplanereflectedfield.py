"""Reflect a field about the XY plane.

Reflect a field about the XY plane.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


class XYPlaneReflectedField(VectorField):
    """Reflect a field about the XY plane.

    From T02: "The contribution from the southern currents (symmetric to
    the northern ones for TILT = 0) can be readily represented by rotating
    the northern (N) part by 180deg around the X-axis and changing the
    polarity of the current."

    Attributes
    ----------
    delgate : VectorField
        delgate
    """

    def __init__(self, delgate):
        """Initializen a new XYPlaneReflectedField object.

        Initializen a new XYPlaneReflectedField object.

        Parameters
        ----------
        delgate : VectorField
            delgate
        """
        self.delgate = delgate

    def evaluate(self, location, buffer):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Location to perform the evaluation.
        buffer : VectorIJK
            Buffer to hold result.
        
        Returns
        -------
        buffer : VectorIJK
            Result of field evaluation.
        """
        reflectedLocation = VectorIJK(
            location.i, location.j, -location.k
        )
        self.delgate.evaluate(reflectedLocation, buffer)
        buffer.k = -buffer.k
        return buffer
