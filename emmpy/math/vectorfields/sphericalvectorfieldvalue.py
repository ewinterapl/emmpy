"""Vector field in a 3-D spherical space.

A spherical vector field value contains a position in the vector field,
and a value for the vector field, both in spherical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.sphericalvector import SphericalVector, cartesianToSpherical, getSphericalBasisToCartesianBasisTransformation, sphericalToCartesian
from emmpy.math.coordinates.sphericalvector import (
    SphericalVector,
    cartesianToSpherical, sphericalToCartesian,
    getSphericalBasisToCartesianBasisTransformation
)
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.math.vectorfields.vectorfieldvalue import VectorFieldValue


class SphericalVectorFieldValue(VectorFieldValue):
    """Vector field in a 3-D spherical space.

    A spherical vector field value contains a position in the vector field,
    and a value for the vector field, both in spherical coordinates.
    """


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


def convertToCartesian(*args):
    """Convert a spherical vector field value to Cartesian.

    Parameters
    ----------
    vfv : SphericalVectorFieldValue
        Vector field value to convert.
    OR
    position, value : SphericalVector
        Spherical position and vector value.

    Returns
    -------
    cartesian : CartesianVectorFieldValue
        Input vector field value converted to Cartesian coordinates.
    """
    if len(args) == 1:
        (vfv,) = args
        position = vfv.position
        value = vfv.value
    elif len(args) == 2:
        (position, value) = args
    else:
        raise TypeError

    # Convert the input position to Cartesian.
    cartesianPosition = sphericalToCartesian(position)

    # Convert the input vector value to Cartesian.
    toCartMatrix = getSphericalBasisToCartesianBasisTransformation(position)
    cartesianValue = CartesianVector(toCartMatrix.dot(value))

    # Create and return the new Cartesian vector field value.
    cartesian = CartesianVectorFieldValue(
        cartesianPosition, cartesianValue)
    return cartesian
