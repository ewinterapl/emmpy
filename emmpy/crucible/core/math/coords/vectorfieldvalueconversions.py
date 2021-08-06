"""Useful vector field value conversions."""


from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.coords.coordconverters import (
    CoordConverters
)
from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)
from emmpy.crucible.core.math.coords.sphericaltocartesianbasistransformation import (
    SphericalToCartesianBasisTransformation
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.matrixijk import (
    MatrixIJK
)


class VectorFieldValueConversions:
    """Useful vector field value conversions.

    This class provides conversions from Cartesian coordinates and vector
    field values to cylindrical and spherical coordinates and vector field
    values, and vice versa.

    @author G.K.Stephens
    """

    CYLINDRICAL = CylindricalToCartesianBasisTransformation()
    SPHERICAL = SphericalToCartesianBasisTransformation()

    def __init__(self):
        """Build a new object."""

    @staticmethod
    def convertToCylindrical(*args):
        """Convert a Cartesian vector to cylindrical coordinates."""
        if len(args) == 1:
            # Converts a Cartesian coordinate and vector field value at that
            # coordinate to a cylindrical coordinate and vector field value
            # @param Cartesian a Cartesian coordinate and vector field value
            # at that coordinate
            # @return a cylindrical coordinate and vector field value at that
            # coordinate
            (cartesian,) = args
            matrix = MatrixIJK()
            position = CoordConverters.convertToCylindrical(
                cartesian.getPosition())
            VectorFieldValueConversions.CYLINDRICAL.getInverseTransformation(
                position, matrix
            )
            value = VectorFieldValueConversions.CYLINDRICAL.mxv(
                matrix, cartesian.getValue()
            )
            return CylindricalVectorFieldValue(position, value)
        elif len(args) == 2:
            # Converts a Cartesian coordinate and vector field value at that
            # coordinate to a cylindrical coordinate and vector field value.
            # @param cartPos a Cartesian coordinate
            # @param cartValue a vector field value at that coordinate
            # @return a cylindrical coordinate and vector field value at that
            # coordinate
            (cartPos, cartValue) = args
            matrix = MatrixIJK()
            position = CoordConverters.convertToCylindrical(cartPos)
            VectorFieldValueConversions.CYLINDRICAL.getInverseTransformation(
                position, matrix
            )
            value = VectorFieldValueConversions.CYLINDRICAL.mxv(
                matrix, cartValue)
            return CylindricalVectorFieldValue(position, value)
        else:
            raise Exception

    @staticmethod
    def convertToSpherical(*args):
        """Convert Cartesian to spherical coordinates."""
        if len(args) == 1:
            # Converts a Cartesian coordinate and vector field value at that
            # coordinate to a spherical coordinate and vector field value
            # @param cartesian a Cartesian coordinate and vector field value at
            # that coordinate
            # @return a spherical coordinate and vector field value at that
            # coordinate
            (cartesian,) = args
            matrix = MatrixIJK()
            position = CoordConverters.convertToSpherical(
                cartesian.getPosition()
            )
            VectorFieldValueConversions.SPHERICAL.getInverseTransformation(
                position, matrix
            )
            value = VectorFieldValueConversions.SPHERICAL.mxv(
                matrix, cartesian.getValue()
            )
            return SphericalVectorFieldValue(position, value)
        elif len(args) == 2:
            # Converts a Cartesian coordinate and vector field value at that
            # coordinate to a spherical coordinate and vector field value.
            # @param cartPos a Cartesian coordinate
            # @param cartValue a vector field value at that coordinate
            # @return a spherical coordinate and vector field value at that
            # coordinate
            (cartPos, cartValue) = args
            matrix = MatrixIJK()
            position = CoordConverters.convertToSpherical(cartPos)
            VectorFieldValueConversions.SPHERICAL.getInverseTransformation(
                position, matrix
            )
            value = VectorFieldValueConversions.SPHERICAL.mxv(
                matrix, cartValue
            )
            return SphericalVectorFieldValue(position, value)
        else:
            raise Exception

    @staticmethod
    def convert(*args):
        """Convert between Cartesian, cylindrical, and spherical."""
        if len(args) == 1:
            if isinstance(args[0], CylindricalVectorFieldValue):
                # Converts a cylindrical coordinate and vector field value at
                # that coordinate to a Cartesian coordinate and vector field
                # value.
                # @param cylindrical a cylindrical coordinate and vector field
                # value at that coordinate
                # @return a Cartesian coordinate and vector field value at that
                # coordinate
                (cylindrical,) = args
                matrix = MatrixIJK()
                position = CoordConverters.convert(cylindrical.getPosition())
                VectorFieldValueConversions.CYLINDRICAL.getTransformation(
                    cylindrical.getPosition(), matrix
                )
                value = VectorFieldValueConversions.CYLINDRICAL.mxv(
                    matrix, cylindrical.getValue()
                )
                return CartesianVectorFieldValue(position, value)
            elif isinstance(args[0], SphericalVectorFieldValue):
                # Converts a spherical coordinate and vector field value at
                # that coordinate to a Cartesian coordinate and vector field
                # value.
                # @param spherical a spherical coordinate and vector field
                # value at that coordinate
                # @return a Cartesian coordinate and vector field value at that
                # coordinate
                (spherical,) = args
                matrix = MatrixIJK()
                position = CoordConverters.convert(spherical.getPosition())
                VectorFieldValueConversions.SPHERICAL.getTransformation(
                    spherical.getPosition(), matrix
                )
                value = VectorFieldValueConversions.SPHERICAL.mxv(
                    matrix, spherical.getValue()
                )
                return CartesianVectorFieldValue(position, value)
            else:
                raise Exception
        elif len(args) == 2:
            if (
                isinstance(args[0], CylindricalVector) and
                isinstance(args[1], CylindricalVector)
            ):
                # Converts a cylindrical coordinate and vector field value at
                # that coordinate to a Cartesian coordinate and vector field
                # value.
                # @param cylPos a cylindrical coordinate
                # @param cylValue a cylindrical vector field value at that
                # coordinate
                # @return a Cartesian coordinate and vector field value at that
                # coordinate
                (cylPos, cylValue) = args
                matrix = MatrixIJK()
                position = CoordConverters.convert(cylPos)
                VectorFieldValueConversions.CYLINDRICAL.getTransformation(
                    cylPos, matrix
                )
                value = VectorFieldValueConversions.CYLINDRICAL.mxv(
                    matrix, cylValue
                )
                return CartesianVectorFieldValue(position, value)
            elif (
                isinstance(args[0], SphericalVector) and
                isinstance(args[1], SphericalVector)
            ):
                # Converts a spherical coordinate and vector field value at
                # that coordinate to a Cartesian coordinate and vector field
                # value.
                # @param sphPos a spherical coordinate
                # @param sphValue a vector field value at that coordinate
                # @return a Cartesian coordinate and vector field value at that
                # coordinate
                (sphPos, sphValue) = args
                matrix = MatrixIJK()
                position = CoordConverters.convert(sphPos)
                VectorFieldValueConversions.SPHERICAL.getTransformation(
                    sphPos, matrix)
                value = VectorFieldValueConversions.SPHERICAL.mxv(
                    matrix, sphValue)
                return CartesianVectorFieldValue(position, value)
            else:
                raise Exception
        else:
            raise Exception
