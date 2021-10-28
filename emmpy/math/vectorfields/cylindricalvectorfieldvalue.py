"""Vector field in a 3-D cylindrical space.

A cylindrical vector field value contains a position in the vector field,
and a value for the vector field, both in cylindrical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector,
    cartesianToCylindrical, cylindricalToCartesian,
    getCylindricalBasisToCartesianBasisTransformation
)
from .cartesianvectorfieldvalue import CartesianVectorFieldValue
from .vectorfieldvalue import VectorFieldValue


class CylindricalVectorFieldValue(VectorFieldValue):
    """Vector field in a 3-D cylindrical space.

    A cylindrical vector field value contains a position in the vector
    field, and a value for the vector field, both in cylindrical
    coordinates.
    """


def convertToCylindrical(*args):
    """Convert a Cartesian vector field value to cylindrical.

    Parameters
    ----------
    cartesian : CartesianVectorFieldValue
        Vector field value to convert.
    OR
    cartesianPosition, cartesianValue : CartesianVector
        Cartesian position and vector value.

    Returns
    -------
    cylindrical : CylindricalVectorFieldValue
        Input vector field value converted to cylindrical coordinates.
    """
    if len(args) == 1:
        # Convert a Cartesian vector field value to a cylindrical
        # vector field value.
        (cartesian,) = args
        cartesianPosition = cartesian.position
        cartesianValue = cartesian.value
    elif len(args) == 2:
        # Convert a Cartesian position vector and a Cartesian value
        # vector to a cylindrical vector field value.
        (cartesianPosition, cartesianValue) = args
    else:
        raise TypeError

    # Convert the Cartesian position to cylindrical.
    cylindricalPosition = cartesianToCylindrical(
        CartesianVector(cartesianPosition)
    )

    # Get the Cartesian-to-cylindrical transformation matrix at
    # the current cylindrical position.
    cartToCylMatrix = getCylindricalBasisToCartesianBasisTransformation(cylindricalPosition).T

    # Convert the Cartesian vector value to cylindrical.
    cylindricalValue = CylindricalVector(cartToCylMatrix.dot(cartesianValue))

    # Create and return the new cylindrical vector field value.
    cylindrical = CylindricalVectorFieldValue(
        cylindricalPosition, cylindricalValue
    )
    return cylindrical


def convertToCartesian(*args):
    """Convert a cylindrical vector field value to Cartesian.

    Parameters
    ----------
    vfv : CylindricalVectorFieldValue
        Vector field value to convert.
    OR
    position, value : CylindricalVector
        Cylindrical position and vector value.

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
    cartesianPosition = cylindricalToCartesian(position)

    # Convert the input vector value to Cartesian.
    toCartMatrix = getCylindricalBasisToCartesianBasisTransformation(position)
    cartesianValue = CartesianVector(toCartMatrix.dot(value))

    # Create and return the new Cartesian vector field value.
    cartesian = CartesianVectorFieldValue(
        cartesianPosition, cartesianValue)
    return cartesian
