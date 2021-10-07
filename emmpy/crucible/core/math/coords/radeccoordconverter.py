"""Convert to and from celestial coordinates.

This class provides methods that convert between celestial (right
ascension and declination) and Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import pi

from emmpy.crucible.core.math.coords.coordconverter import CoordConverter
from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.math.coordinates.latitudinalvector import LatitudinalVector
from emmpy.math.coordinates.radecvector import RaDecVector


class RaDecCoordConverter(CoordConverter):
    """Convert to and from celestial coordinates.

    This class provides methods that convert between celestial (right
    ascension and declination) and Cartesian coordinates.
    """

    LAT_CONVERTER = LatitudinalCoordConverter()

    def __init__(self):
        """Initialize a new RaDecCoordConverter object.

        Initialize a new RaDecCoordConverter object.

        Parameters
        ----------
        None
        """

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to celestial coordinates.

        Convert a Cartesian vector to celestial coordinates.

        Parameters
        ----------
        cartesian : VectorIJK
            Vector in Cartesian coordinates.

        Returns
        -------
        celestial : RaDecVector
            Input vector converted to celestial coordinates.
        """
        latitudinal = RaDecCoordConverter.LAT_CONVERTER.toCoordinate(cartesian)
        r = latitudinal.r
        ra = latitudinal.lon
        dec = latitudinal.lat
        if ra < 0.0:
            ra += 2*pi
        return RaDecVector(r, ra, dec)

    def toCartesian(self, celestial):
        """Convert a celestial vector to Cartesian coordinates.

        Convert a celestial vector to Cartesian coordinates.

        Parameters
        ----------
        celestial : RaDecVector
            Vector in celestial coordinates.

        Returns
        -------
        cartesian : VectorIJK
            Input vector converted to Cartesian coordinates.
        """
        latitudinal = LatitudinalVector(celestial.r, celestial.ra, celestial.dec)
        return RaDecCoordConverter.LAT_CONVERTER.toCartesian(latitudinal)
