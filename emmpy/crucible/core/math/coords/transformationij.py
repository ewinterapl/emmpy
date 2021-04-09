"""emmpy.crucible.core.math.coords.transformationij

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.coords.abstractvectorij import AbstractVectorIJ


class TransformationIJ(AbstractVectorIJ):
    """This interface assists with the manipulation of Jacobians.

    A Jacobian is the matrix of all first order partial derivatives of a vector
    with respect to another vector. In this package, it is meant to represent
    the first order partial derivatives of some coordinate system with respect
    to Cartesian. A Jacobian can obviously be identified with simply a
    {@link MatrixIJ}, however, this eliminates all context.

    Note: for a completely symmetric interface, getInverseJacobian would take a
    VectorIJ, however, this is not done, because it allows the implementor to
    use the inversion of the getJacobian method. This is not the most generic
    way, but it allows for only a single definition of the Jacobian and not
    two. Spice also follows this convention.

    TODO Within this package, implementations of this interface are assumed to
    be thread safe, and in practice are so because they are stateless. Perhaps
    this restriction should be lifted, and the threading issues present in this
    package be solved in a more robust way.

    @author G.K.Stephens
    @param <C> an {@link AbstractVectorIJ} type
    """

    def __init__(self):
        """INTERFACE - DO NOT INSTANTIATE."""
        raise Exception

    def getTransformation(self, coordPosition, buffer):
        """Gets the Jacobian from the Coordinate system to Cartesian

        INTERFACE - DO NOT INVOKE.

        @param coordPosition The coordinate position in which the Jacobian will
        be calculated.
        @param buffer A {@link MatrixIJ} containing the Jacobian from the
        specified Coordinate system to Cartesian.
        @return A {@link MatrixIJ} containing the Jacobian from the specified
        Coordinate system to Cartesian.
        """
        raise Exception

    def getInverseTransformation(self, coordPosition, buffer):
        """Returns the Jacobian from Cartesian to the specified Coordinate
        system.

        INTERFACE - DO NOT INVOKE.
        
        Note, that this takes a coordinate position and not the Cartesian
        position, allowing the implementor to leverage the other method.

        @param coordPosition The coordinate position in which the inverse
        Jacobian will be calculated.
        @param buffer A {@link MatrixIJ} containing the Jacobian from Cartesian
        to the specified Coordinate system.
        @return A {@link MatrixIJ} containing the Jacobian from Cartesian to
        the specified Coordinate system.
        """
        raise Exception

    def mxv(self, *args):
        """INTERFACE - DO NOT INVOKE

        Arguments can be:
        (jacobian, coordVelocity)
        (inverseJacobian, cartVelocity)
        """
        raise Exception
