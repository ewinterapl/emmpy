"""emmpy.crucible.crust.surfaces.surface"""


from emmpy.crucible.crust.surfaces.surfaceintersectioncomputer import (
    SurfaceIntersectionComputer
)
from emmpy.crucible.crust.surfaces.surfacenormalcomputer import (
    SurfaceNormalComputer
)


class Surface(SurfaceNormalComputer, SurfaceIntersectionComputer):

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception
