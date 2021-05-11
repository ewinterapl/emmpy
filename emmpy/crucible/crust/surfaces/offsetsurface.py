"""emmpy.crucible.crust.surfaces.offsetsurface"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.surface import Surface


class OffsetSurface(Surface):

    def __init__(self, delegate, offset):
        """Constructor"""
        Surface.__init__(self)
        self.delegate = Preconditions.checkNotNull(delegate)
        # defensive copy
        self.offset = UnwritableVectorIJK(
            Preconditions.checkNotNull(offset)
        )

    def computeOutwardNormal(self, surfacePoint, buffer):
        offsetSurfacePoint = VectorIJK.add(
            surfacePoint, self.offset, VectorIJK()
        )
        return self.delegate.computeOutwardNormal(offsetSurfacePoint, buffer)

    def intersects(self, source, ray):
        offsetSource = VectorIJK.add(source, self.offset, VectorIJK())
        return self.delegate.intersects(offsetSource, ray)

    def compute(self, source, ray, buffer):
        offsetSource = VectorIJK.add(source, self.offset, VectorIJK())
        return VectorIJK.subtract(
            self.delegate.compute(offsetSource, ray, buffer),
            self.offset, buffer
        )
