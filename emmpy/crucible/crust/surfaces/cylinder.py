"""emmpy.crucible.crust.surfaces.cylinder"""


from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.crust.surfaces.circle import Circle
from emmpy.crucible.crust.surfaces.nointersectionexception import (
    NoIntersectionException
)
from emmpy.crucible.crust.surfaces.surface import Surface


class Cylinder(Surface):

    def __init__(self, radius):
        Surface.__init__(self)
        self.circle = Circle(radius)

    def computeOutwardNormal(self, surfacePoint, buffer):
        return buffer.setTo(2*surfacePoint.getI(), 2*surfacePoint.getJ(), 0.0)

    def intersects(self, source, ray):
        return (
            len(self.circle.computeIntersectionsRay(
                VectorIJ(source.getI(), source.getJ()),
                VectorIJ(ray.getI(), ray.getJ()))) != 0
        )

    def compute(self, source, ray, buffer):
        sourceij = VectorIJ(source.getI(), source.getJ())
        rayij = VectorIJ(ray.getI(), ray.getJ())
        if sourceij.equals(rayij):
            raise NoIntersectionException
        bufferij = self.circle.computeFirstIntersectionRay(
            sourceij, rayij, VectorIJ()
        )
        m = ray.getK()/rayij.getLength()
        zIntercept = (
            m*VectorIJ.subtract(bufferij, sourceij).getLength() + source.getK()
        )
        return buffer.setTo(bufferij.getI(), bufferij.getJ(), zIntercept)
