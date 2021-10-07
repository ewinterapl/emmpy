"""Useful coordinate conversion methods.

This class contains several useful coordinate conversion methods.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.cylindricalcoordconverter import (
    CylindricalCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.coords.polarcoordconverter import (
    PolarCoordConverter
)
from emmpy.crucible.core.math.coords.radeccoordconverter import (
    RaDecCoordConverter
)
from emmpy.crucible.core.math.coords.sphericalcoordconverter import (
    SphericalCoordConverter
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.coordinates.latitudinalvector import LatitudinalVector
from emmpy.math.coordinates.polarvector import PolarVector
from emmpy.math.coordinates.radecvector import RaDecVector


class CoordConverters:
    """Useful coordinate conversion methods.

    This class contains several useful coordinate conversion methods.

    Attributes
    ----------
    cylindricalCoordConverter : CylindricalCoordConverter
        Converts between Cartesian and cylindrical coordinates.
    latitudinalCoordConverter : LatitudinalCoordConverter
        Converts between Cartesian and latitudinal coordinates.
    raDecCoordConverter : RaDecCoordConverter
        Converts between Cartesian and ra-dec coordinates.
    polarCoordConverter : PolarCoordConverter
        Converts between Cartesian and polar coordinates.
    sphericalCoordConverter : SphericalCoordConverter
        Converts between Cartesian and spherical coordinates.
    """

    # Create the standard converters.
    cylindricalCoordConverter = CylindricalCoordConverter()
    latitudinalCoordConverter = LatitudinalCoordConverter()
    polarCoordConverter = PolarCoordConverter()
    raDecCoordConverter = RaDecCoordConverter()
    sphericalCoordConverter = SphericalCoordConverter()

    def __init__(self):
        """Initialize a new CoordConverters object.

        Initialize a new CoordConverters object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    @staticmethod
    def convertToCylindrical(cartesian):
        """Convert a 3-D Cartesian vector to a cylindrical vector.

        Convert a 3-D Cartesian vector to a cylindrical vector.

        Parameters
        ----------
        cartesian : VectorIJK
            A Cartesian vector.

        Returns
        -------
        cylindrical : CylindricalVector
            The input vector converted to cylindrical coordinates.
        """
        cylindrical = CoordConverters.cylindricalCoordConverter.toCoordinate(
            cartesian
        )
        return cylindrical

    @staticmethod
    def convertToLatitudinal(cartesian):
        """Convert a 3-D Cartesian vector to a latitudinal vector.

        Convert a 3-D Cartesian vector to a latitudinal vector.

        Parameters
        ----------
        cartesian : VectorIJK
            A Cartesian vector.

        Returns
        -------
        latitudinal : LatitudinalVector
            The input vector converted to latitudinal coordinates.
        """
        latitudinal = CoordConverters.latitudinalCoordConverter.toCoordinate(
            cartesian
        )
        return latitudinal

    @staticmethod
    def convertToPolar(cartesian):
        """Convert a 2-D Cartesian vector to a polar vector.

        Convert a 2-D Cartesian vector to a polar vector.

        Parameters
        ----------
        cartesian : VectorIJ
            A Cartesian vector.

        Returns
        -------
        polar : PolarVector
            The input vector converted to polar coordinates.
        """
        polar = CoordConverters.polarCoordConverter.toCoordinate(cartesian)
        return polar

    @staticmethod
    def convertToRaDec(cartesian):
        """Convert a 3-D Cartesian vector to a RA/DEC vector.

        Convert a 3-D Cartesian vector to a RA/DEC vector.

        Parameters
        ----------
        cartesian : VectorIJK
            A Cartesian vector.

        Returns
        -------
        radec : RaDecVector
            The input vector converted to RA/DEC coordinates.
        """
        radec = CoordConverters.raDecCoordConverter.toCoordinate(
            cartesian
        )
        return radec

    @staticmethod
    def convertToSpherical(cartesian):
        """Convert a 3-D Cartesian vector to a spherical vector.

        Convert a 3-D Cartesian vector to a spherical vector.

        Parameters
        ----------
        cartesian : VectorIJK
            A Cartesian vector.

        Returns
        -------
        spherical : SphericalVector
            The input vector converted to spherical coordinates.
        """
        spherical = CoordConverters.sphericalCoordConverter.toCoordinate(
            cartesian
        )
        return spherical

    @staticmethod
    def convert(position):
        """Convert an input vector to Cartesian coordinates.

        Convert a cylindrical, latitudinal, polar, RA/DEC, or spherical
        vector to Cartesian coordinates.

        Parameters
        -----------
        position : Vector
            A vector in cylindrical, latitudinal, polar, RA/DEC, or spherical
            coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        if isinstance(position, CylindricalVector):
            cartesian = CoordConverters.cylindricalCoordConverter.toCartesian(
                position)
        elif isinstance(position, LatitudinalVector):
            cartesian = CoordConverters.latitudinalCoordConverter.toCartesian(
                position)
        elif isinstance(position, PolarVector):
            cartesian = CoordConverters.polarCoordConverter.toCartesian(
                position)
        elif isinstance(position, RaDecVector):
            cartesian = CoordConverters.raDecCoordConverter.toCartesian(
                position)
        elif isinstance(position, SphericalVector):
            cartesian = CoordConverters.sphericalCoordConverter.toCartesian(
                position)
        else:
            raise ValueError
        return cartesian
