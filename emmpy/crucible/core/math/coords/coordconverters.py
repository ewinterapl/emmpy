"""Useful coordinate conversions."""


from emmpy.crucible.core.math.coords.cylindricalcoordconverter import (
    CylindricalCoordConverter
)
from emmpy.crucible.core.math.coords.cylindricalvector import (
    CylindricalVector
)
from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.coords.polarcoordconverter import (
    PolarCoordConverter
)
from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector
)
from emmpy.crucible.core.math.coords.radeccoordconverter import (
    RaDecCoordConverter
)
from emmpy.crucible.core.math.coords.radecvector import (
    RaDecVector
)
from emmpy.crucible.core.math.coords.sphericalcoordconverter import (
    SphericalCoordConverter
)
from emmpy.crucible.core.math.coords.sphericalvector import (
    SphericalVector
)


class CoordConverters:
    """Useful coordinate conversions.

    author G.K.Stephens
    """

    cylindricalCoordConverter = CylindricalCoordConverter()
    latitudinalCoordConverter = LatitudinalCoordConverter()
    polarCoordConverter = PolarCoordConverter()
    raDecCoordConverter = RaDecCoordConverter()
    sphericalCoordConverter = SphericalCoordConverter()

    def __init__(self):
        """Build a new object."""

    @staticmethod
    def convertToCylindrical(cartesian):
        """Convert a Cartesian position to cylindrical position.

        @param cartesian A {@link UnwritableVectorIJK} holding the Cartesian
        position.
        @param cylindricalBuffer A {@link CylindricalVector} buffer holding the
        cylindrical position;
        @return a reference to buffer for convenience.
        """
        return CoordConverters.cylindricalCoordConverter.toCoordinate(
            cartesian
        )

    @staticmethod
    def convertToLatitudinal(cartesian):
        """Convert from Cartesian coordinates to Latitudinal coordinates.

        @param cartesian
        @param LatitudinalBuffer
        @return
        """
        return CoordConverters.latitudinalCoordConverter.toCoordinate(
            cartesian
        )

    @staticmethod
    def convertToPolar(cartesian):
        """Convert a Cartesian position to polar position.

        @param cartesian A {@link UnwritableVectorIJ} holding the Cartesian
        position.
        @param polarBuffer A {@link PolarVector} buffer holding the polar
        position;
        @return a reference to buffer for convenience.
        """
        return CoordConverters.polarCoordConverter.toCoordinate(cartesian)

    @staticmethod
    def convertToRaDec(cartesian):
        """Convert from Cartesian coordinates to RaDec coordinates.

        @param cartesian
        @param RaDecBuffer
        @return
        """
        return CoordConverters.raDecCoordConverter.toCoordinate(cartesian)

    @staticmethod
    def convertToSpherical(cartesian):
        """Convert a Cartesian position to spherical position.

        @param cartesian A {@link UnwritableVectorIJK} holding the Cartesian
        position.
        @param sphericalBuffer A {@link SphericalVector} buffer holding the
        spherical position;
        @return a reference to buffer for convenience.
        """
        return CoordConverters.sphericalCoordConverter.toCoordinate(cartesian)

    @staticmethod
    def convert(position):
        """Convert back to Cartesian coordinates."""
        if isinstance(position, CylindricalVector):
            # Converts a cylindrical position to a Cartesian position.
            # @param cylindrical A {@link CylindricalVector} holding the
            # cylindrical position.
            # @param cartesianBuffer A {@link VectorIJK} buffer holding the
            # Cartesian position.
            # @return a reference to buffer for convenience.
            cylindrical = position
            return CoordConverters.cylindricalCoordConverter.toCartesian(
                cylindrical
            )
        elif isinstance(position, LatitudinalVector):
            # Converts from Latitudinal coordinates to Cartesian coordinates
            # @param Latitudinal
            # @param cartesianBuffer
            # @return
            latitudinal = position
            return CoordConverters.latitudinalCoordConverter.toCartesian(
                latitudinal
            )
        elif isinstance(position, PolarVector):
            # Converts a polar position to a Cartesian position.
            # @param polar A {@link PolarVector} holding the polar position.
            # @param cartesianBuffer A {@link VectorIJ} buffer holding the
            # Cartesian position.
            # @return a reference to buffer for convenience.
            polar = position
            return CoordConverters.polarCoordConverter.toCartesian(polar)
        elif isinstance(position, RaDecVector):
            # Converts from RaDec coordinates to Cartesian coordinates
            # @param RaDec
            # @param cartesianBuffer
            # @return
            RaDec = position
            return CoordConverters.raDecCoordConverter.toCartesian(RaDec)
        elif isinstance(position, SphericalVector):
            # Converts a spherical position to a Cartesian position.
            # @param spherical A {@link SphericalVector} holding the spherical
            # position.
            # @param cartesianBuffer A {@link VectorIJK} buffer holding the
            # Cartesian position.
            # @return a reference to buffer for convenience.
            spherical = position
            return CoordConverters.sphericalCoordConverter.toCartesian(
                spherical
            )
        else:
            raise Exception
