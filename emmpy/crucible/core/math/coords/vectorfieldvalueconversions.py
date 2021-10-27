"""Useful vector field value conversions.

This class provides conversions from Cartesian coordinates and vector
field values to cylindrical and spherical coordinates and vector field
values, and vice versa.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.sphericalvector import SphericalVector, sphericalToCartesian
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector, cylindricalToCartesian, cartesianToCylindrical,
    getCylindricalBasisToCartesianBasisTransformation
)
from emmpy.math.coordinates.sphericalvector import (
    SphericalVector, sphericalToCartesian, cartesianToSpherical,
    getSphericalBasisToCartesianBasisTransformation
)
from emmpy.math.matrices.matrixijk import MatrixIJK
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.math.vectorfields.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)
from emmpy.math.vectorfields.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)


class VectorFieldValueConversions:
    """Useful vector field value conversions.

    This class provides conversions from Cartesian coordinates and vector
    field values to cylindrical and spherical coordinates and vector field
    values, and vice versa.
    """

    @staticmethod
    def convertToSpherical(*args):
        """Convert a Cartesian vector field value to spherical.

        Parameters
        ----------
        cartesian : CartesianVectorFieldValue
            Vector field value to convert.
        OR
        cartesianPosition, cartesianValue : CartesianVector
            Cartesian position and vector value.

        Returns
        -------
        spherical : SphericalVectorFieldValue
            Input vector field value converted to spherical coordinates.
        """
        if len(args) == 1:
            # Convert a Cartesian vector field value to a spherical
            # vector field value.
            (cartesian,) = args
            cartesianPosition = cartesian.position
            cartesianValue = cartesian.value
        elif len(args) == 2:
            # Convert a Cartesian position vector and a Cartesian value
            # vector to a spherical vector field value.
            (cartesianPosition, cartesianValue) = args
        else:
            raise TypeError

        # Convert the Cartesian position to spherical.
        sphericalPosition = cartesianToSpherical(
            CartesianVector(cartesianPosition)
        )

        # Get the Cartesian-to-spherical transformation matrix at
        # the current spherical position.
        cartToSphMatrix = getSphericalBasisToCartesianBasisTransformation(sphericalPosition).T

        # Convert the Cartesian vector value to spherical.
        sphericalValue = SphericalVector(cartToSphMatrix.dot(cartesianValue))

        # Create and return the new spherical vector field value.
        spherical = SphericalVectorFieldValue(
            sphericalPosition, sphericalValue)
        return spherical

    @staticmethod
    def convert(*args):
        """Convert a cylindrical or spherical vector field value to Cartesian.

        Parameters
        ----------
        vfv : CylindricalVectorFieldValue or SphericalVectorFieldValue
            Vector field value to convert.
        OR
        position, value : CylindricalVector or SphericalVector
            Cylindrical or spherical position and vector value.

        Returns
        -------
        cartesian : CartesianVectorFieldValue
            Input vector field value converted to Cartesian coordinates.
        """
        if len(args) == 1:
            # Convert a vector field value in cylindrical or spherical
            # coordinates to Cartesian.
            (vfv,) = args
            position = vfv.position
            value = vfv.value
        elif len(args) == 2:
            # Convert an input position/value pair to a Cartesian
            # vector field value.
            (position, value) = args
        else:
            raise TypeError

        # Convert the input position to Cartesian.
        if isinstance(position, CylindricalVector):
            raise Exception
        elif isinstance(position, SphericalVector):
            cartesianPosition = sphericalToCartesian(position)
        else:
            raise TypeError

        # Convert the input vector value to Cartesian.
        toCartMatrix = MatrixIJK()
        if (isinstance(args[0], (CylindricalVectorFieldValue,
                                 CylindricalVector))):
            raise Exception
        elif (isinstance(args[0], (SphericalVectorFieldValue,
                                   SphericalVector))):
            toCartMatrix = getSphericalBasisToCartesianBasisTransformation(position)
        else:
            raise TypeError
        cartesianValue = CartesianVector(toCartMatrix.dot(value))

        # Create and return the new Cartesian vector field value.
        cartesian = CartesianVectorFieldValue(
            cartesianPosition, cartesianValue)
        return cartesian
