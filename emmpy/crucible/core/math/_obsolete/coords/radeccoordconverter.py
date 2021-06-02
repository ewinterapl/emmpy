"""emmpy.crucible.core.math.coords.radeccoordconverter.py"""

# import static crucible.core.units.FundamentalPhysicalConstants.TWOPI;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
from emmpy.crucible.core.math.coords.coordconverter import CoordConverter
from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector
)
from emmpy.crucible.core.math.coords.radecvector import RaDecVector
from emmpy.crucible.core.units.fundamentalphysicalconstants import (
    FundamentalPhysicalConstants
)


class RaDecCoordConverter(CoordConverter):

    LAT_CONVERTER = LatitudinalCoordConverter()

    def __init__(self):
        """Constructor"""
        pass

    def toCoordinate(self, cartesian):
        workCoord = RaDecCoordConverter.LAT_CONVERTER.toCoordinate(cartesian)
        r = workCoord.getRadius()
        lat = workCoord.getLatitude()
        lon = workCoord.getLongitude()
        if lon < 0.0:
            lon += FundamentalPhysicalConstants.TWOPI
        return RaDecVector(r, lon, lat)

    def toCartesian(self, coordinate):
        workCoord = LatitudinalVector(
            coordinate.getRadius(), coordinate.getDeclination(),
            coordinate.getRightAscension()
        )
        return RaDecCoordConverter.LAT_CONVERTER.toCartesian(workCoord)
