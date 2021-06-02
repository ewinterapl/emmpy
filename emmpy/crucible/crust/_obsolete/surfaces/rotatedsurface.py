"""emmpy.crucible.crust.surfaces.rotatedsurface"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)
from emmpy.crucible.crust.surfaces.surface import Surface


class RotatedSurface(Surface):

    def __init__(self, delegate, rotationMatrix):
        """Constructor"""
        Surface.__init__(self)
        self.delegate = Preconditions.checkNotNull(delegate)
        self.rotationMatrix = UnwritableRotationMatrixIJK(
            Preconditions.checkNotNull(rotationMatrix)
        )

    def computeOutwardNormal(self, surfacePoint, buffer):
        return self.rotationMatrix.mtxv(
            self.delegate.computeOutwardNormal(self.rotationMatrix.mxv(surfacePoint),
                                               buffer),
            buffer
        )

    def intersects(self, source, ray):
        return self.delegate.intersects(
            self.rotationMatrix.mxv(source),
            self.rotationMatrix.mxv(ray)
        )

    def compute(self, source, ray, buffer):
        return self.rotationMatrix.mtxv(
            self.delegate.compute(self.rotationMatrix.mxv(source),
                                  self.rotationMatrix.mxv(ray), buffer),
            buffer
        )
