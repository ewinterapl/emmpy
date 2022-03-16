"""Scale the position and value of a vector field.

Scale the position and value of a vector field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectorfields.vectorfield import VectorField


class ScaledField(VectorField):
    """Scale the position and value of a vector field.

    Scale a VectorField by scaling both the position and the output
    vector by a scalar value.

    Attributes
    ----------
    unscaledField : VectorField
        The unscaled field.
    kappaScale : float
        The scale factor.
    """

    def __init__(self, unscaledField, kappaScale):
        """Initialize a new ScaledField object.

        Construct a scaled VectorField by scaling both the position and
        the output vector by a scalar value.

        B'(r) = a B(a r)

        where B' is the resulting scaled field.
        B and r are the original unscaled and a is the scale factor.

        Parameters
        ----------
        unscaledField : VectorField
            The unscaled field.
        kappaScale : float
            The scale factor.
        """
        self.unscaledField = unscaledField
        self.kappaScale = kappaScale

    def evaluate(self, location, buffer):
        """Evaluate the scaled field at a given location.

        Evaluate the scaled field at a given location.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        buffer : VectorIJK
            Buffer to hold the evaluation result.
        
        Returns
        -------
        buffer : VectorIJK
            Field evaluated at location.
        """
        # Perform spatial scaling, eq. (25).
        scaledLocation = location*self.kappaScale
        self.unscaledField.evaluate(scaledLocation, buffer)

        # Apply the kappa scaling factor eq. (25).
        buffer *= self.kappaScale
        return buffer
