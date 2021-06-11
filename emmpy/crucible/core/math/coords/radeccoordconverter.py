"""Convert between Ra/Dec and Cartesian coordinates."""

from emmpy.crucible.core.math.coords.coordconverter import CoordConverter
from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.coords.radecvector import RaDecVector


class RaDecCoordConverter(CoordConverter):
    """Convert between Ra/Dec and Cartesian coordinates."""

    LAT_CONVERTER = LatitudinalCoordConverter()

    def __init__(self):
        """Build a new object."""

    def toCoordinate(self, cartesian):
        """Convert Cartesian to Ra/Dec coordinates."""
        workCoord = RaDecCoordConverter.LAT_CONVERTER.toCoordinate(cartesian)
        r = workCoord.getRadius()
        lat = workCoord.getLatitude()
        lon = workCoord.getLongitude()
        if lon < 0.0:
            lon += 2*pi
        return RaDecVector(r, lon, lat)

    def toCartesian(self, coordinate):
        """Convert Ra/Dec to Cartesian coordinates."""
        workCoord = LatitudinalVector(
            coordinate.getRadius(), coordinate.getDeclination(),
            coordinate.getRightAscension()
        )
        return RaDecCoordConverter.LAT_CONVERTER.toCartesian(workCoord)
