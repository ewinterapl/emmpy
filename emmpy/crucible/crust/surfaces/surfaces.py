"""emmpy.crucible.crust.surfaces.surfaces"""


from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)
from emmpy.crucible.crust.surfaces.cylinder import Cylinder
from emmpy.crucible.crust.surfaces.ellipsoid import Ellipsoid
from emmpy.crucible.crust.surfaces.offsetsurface import OffsetSurface
from emmpy.crucible.crust.surfaces.rotatedsurface import RotatedSurface
from emmpy.crucible.crust.surfaces.sphere import Sphere


class Surfaces:

    ROTATE_Z_TO_X = UnwritableRotationMatrixIJK(
        0.0, 0.0, 1.0, 0.0, 1.0, 0.0, -1.0, 0.0, 0.0
    )

    ROTATE_Z_TO_Y = UnwritableRotationMatrixIJK(
        1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0, 0.0
    )

    def __init__(self):
        """Constructor"""
        pass

    @staticmethod
    def createEllipsoidalSurface(a, b, c):
        if a == b and a == c:
            return Sphere(a)
        return Ellipsoid(a, b, c)

    @staticmethod
    def createSphere(radius):
        return Sphere(radius)

    @staticmethod
    def offset(surface, offset):
        return OffsetSurface(surface, offset)

    @staticmethod
    def createCylinderAlongX(radius):
        return RotatedSurface(Cylinder(radius), Surfaces.ROTATE_Z_TO_X)

    @staticmethod
    def createCylinderAlongY(radius):
        return RotatedSurface(Cylinder(radius), Surfaces.ROTATE_Z_TO_Y)

    @staticmethod
    def createCylinderAlongZ(radius):
        return Cylinder(radius)
