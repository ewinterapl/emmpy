"""emmpy.crucible.crust.surfaces.plane"""


# import crucible.core.designpatterns.Writable;

from emmpy.crucible.core.designpatterns.writable import Writable
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.unwritableplane import UnwritablePlane


class Plane(UnwritablePlane, Writable):
    """Writable subclass of the unwritable 3D plane that completes the
    implementation of the weak immutability design pattern.

    This class contains the mutator methods necessary to set or alter the
    internals of the parent classes fields.

    author F.S.Turner
    """

    def __init__(self, *args):
        if len(args) == 0:
            pass
            # Creates the default plane, whose normal is VectorIJK.K} and
            # contains the origin.
            UnwritablePlane.__init__(self, VectorIJK.K, 0.0)
        elif len(args) == 1:
            (plane,) = args
            # Copy constructor.
            # param plane creates a new plane, copying the contents of the
            # supplied plane.
            UnwritablePlane.__init__(self, plane)
        elif len(args) == 2:
            if isinstance(args[1], float):
                (normal, constant) = args
                # Constructs a plane from the supplied normal vector and
                # constant.
                # A plane can be defined by the expression:
                #    < x, normal > = constant
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # param normal the normal vector
                # param constant the constant
                # throws IllegalArgumentException if normal is zero length.
                UnwritablePlane.__init__(self, normal, constant)
            elif isinstance(args[1], UnwritableVectorIJK):
                (normal, point) = args
                # Constructs a plane from the supplied normal vector and point
                # in the plane.
                # A plane can be defined by the expression:
                #    < x - point, normal > = 0
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # param normal the normal vector
                # param point a point in the plane
                # throws IllegalArgumentException if normal is zero length
                UnwritablePlane.__init__(self, normal, point)
            else:
                raise Exception
        elif len(args) == 3:
            (point, u, v) = args
            # Constructs a plane from the supplied point and two spanning
            # vectors.
            # A plane can be defined by the expression:
            #   point + s * u + t * v
            # where s and t are real numbers, u and v are the linearly
            # independent spanning vectors, and point is an arbitrary point
            # in the plane of interest.
            # param point an arbitrary point in the plane
            # param u one of the two linearly independent spanning vectors
            # param v the other of the spanning vectors
            # throws IllegalArgumentException if u and v are parallel
            UnwritablePlane.__init__(self, point, u, v)
        else:
            raise Exception

    def setTo(self, *args):
        if len(args) == 1:
            (plane,) = args
            # Configures the instance to the value of the supplied plane.
            # param plane the plane to mutate the instance to
            # return a reference to the instance for convenience
            UnwritablePlane.setTo(self, plane)
            return self
        elif len(args) == 2:
            if isinstance(args[1], float):
                (normal, constant) = args
                # Sets the contents of the plane to that of a normal vector and
                # constant.
                # A plane can be defined by the expression:
                #    < x, normal > = constant
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # param normal the normal vector
                # param constant the constant
                # return a reference to the instance for convenience
                # throws IllegalArgumentException if normal is zero length
                UnwritablePlane.setTo(self, normal, constant)
                return self
            elif isinstance(args[1], UnwritableVectorIJK):
                (normal, point) = args
                # Sets the contents of the plane to that of the supplied normal
                # vector and point.
                # A plane can be defined by the expression:
                #    < x - point, normal > = 0
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # param normal the normal vector
                # param point a point in the plane
                # returns a reference to the instance for convenience
                # throws IllegalArgumentException if normal is zero length
                UnwritablePlane.setTo(self, normal, point)
                return self
            else:
                raise Exception
        elif len(args) == 3:
            (point, u, v) = args
            # Sets the contents of the plane from the supplied point and two
            # spanning vectors.
            # A plane can be defined by the expression:
            #   point + s * u + t * v
            # where s and t are real numbers, u and v are the linearly
            # independent spanning vectors, and point is an arbitrary point in
            # the plane of interest.
            # param point an arbitrary point in the plane
            # param u one of the two linearly independent spanning vectors
            # param v the other of the spanning vectors
            # returns a reference to the instance for convenience
            # throws IllegalArgumentException if u and v are parallel
            UnwritablePlane.setTo(self, point, u, v)
            return self
        else:
            raise Exception
