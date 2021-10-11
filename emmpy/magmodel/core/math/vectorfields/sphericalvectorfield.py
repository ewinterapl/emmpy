"""A vector field in spherical coordinates.

A vector field in spherical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions
)
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D
from emmpy.math.coordinates.sphericalvector import cartesianToSpherical


class SphericalVectorField(VectorField):
    """A vector field in spherical coordinates.

    Represents a VectorField in spherical coordinates and provides the
    conversion from a SphericalVector field to a Cartesian vector field.
    """

    def evaluate(self, location, buffer):
        """Evaluate the field at a given Cartesian location.
        
        Evaluate the field at a given Cartesian location.
        
        Parameters
        ----------
        location : VectorIJK
            Cartesian location to evaluate the field.
        buffer : VectorIJK
            Buffer to hold the Cartesian result.
        
        Returns
        -------
        buffer : VectorIJK
            Cartesian field value.
        """
        # Convert the Cartesian position to spherical.
        locSphere = cartesianToSpherical(CartesianVector3D(location))

        # Evaluate the field value.
        fieldValue = self.evaluate(locSphere)

        # Construct the spherical vector field value for the given
        # position.
        sphere = SphericalVectorFieldValue(locSphere, fieldValue)

        # Convert the vector field value back to Cartesian.
        valueSphere = VectorFieldValueConversions.convert(sphere).value

        # Return the value.
        buffer[:] = valueSphere
        return buffer
