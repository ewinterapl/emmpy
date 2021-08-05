"""A vector field in a 3-dimensional space.

This class represents a vector field in a 3-dimensional vector space. The
only required method is evaluate().

N.B. This class was based on a Java interface, and therefore these methods
will raise exceptions if invoked.

Authors
-------
J. Vanderpool
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class VectorField:
    """A vector field in a 3-dimensional space.

    This class represents a vector field in a 3-dimensional vector space.
    The only required method is evaluate().

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new VectorField object.

        This abstract method must be overridden in a subclass.

        Initialize a new VectorField object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def evaluate(self, *args):
        """Evaluate the vector field at a position.

        This abstract method must be overridden in a subclass.

        Evaluate the vector field at the specified position in a
        3-dimensional space.

        Parameters
        ----------
        location : Vector3D
            The position in 3-dimensional space.

        Returns
        -------
        v : Vector3D
            Value of vector field at the specified location.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
