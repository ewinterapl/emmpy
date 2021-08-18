"""Base class for coordinate transformations.

This class defines the methods needed for coordinate transformations.

This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class Transformation:
    """Base class for coordinate transformations.

    This interface assists with the manipulation of Jacobians. A Jacobian is
    the matrix of all first order partial derivatives of a vector with respect
    to another vector. In this package, it is meant to represent the first
    order partial derivatives of some coordinate system with respect to
    Cartesian. A Jacobian can obviously be identified with simply a
    MatrixIJK, however, this eliminates all context.

    Note: for a completely symmetric interface, getInverseJacobian would take a
    VectorIJK, however, this is not done, because it allows the implementor to
    use the inversion of the getJacobian method. This is not the most generic
    way, but it allows for only a single definition of the Jacobian and not
    two. Spice also follows this convention.

    TODO Within this package, implementations of this interface are assumed to
    be thread safe, and in practice are so because they are stateless. Perhaps
    this restriction should be lifted, and the threading issues present in this
    package be solved in a more robust way.
    """

    def __init__(self):
        """Initialize a new Transformation object.

        Initialize a new Transformation object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getTransformation(self, coordPosition, buffer):
        """Get the Jacobian from the coordinate system to Cartesian.

        Get the Jacobian from the coordinate system to Cartesian at the
        specified location.

        Parameters
        ----------
        coordPosition : Vector3D
            The coordinate position at which the Jacobian will be calculated.
        buffer : MatrixIJK
            The Jacobian from the specified coordinate system to Cartesian.

        Returns
        -------
        buffer : MatrixIJK
            The Jacobian from the specified coordinate system to Cartesian.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getInverseTransformation(self, coordPosition, buffer):
        """Get the Jacobian from Cartesian to the coordinate system.

        Get the Jacobian from Cartesian to the coordinate system at the
        specified location.

        Parameters
        ----------
        coordPosition : Vector3D
            The coordinate position at which the Jacobian will be
            calculated.
        buffer : MatrixIJK
            The Jacobian from Cartesian to the specified coordinate
            system.

        Returns
        -------
        buffer : MatrixIJK
            The Jacobian from Cartesian to the specified coordinate
            system.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def mxv(self, *args):
        """Multiply a vector by a matrix.

        Multiply a vector by a matrix.

        Parameters
        ----------
        *args : tuple of object
            Defined by subclass.

        Returns
        -------
        result : object
            Defined by subclass.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
