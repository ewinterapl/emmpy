"""A scalar field in a 3-dimensional space.

This class represents a scalar field in a 3-dimensional vector space. The
only required method is evaluate().

N.B. This class was based on a Java interface, and therefore these methods
will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class ScalarField:
    """A scalar field in a 3-dimensional space.

    This class represents a scalar field in a 3-dimensional vector space.
    The only required method is evaluate().

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new ScalarField object.

        This abstract method must be overridden in a subclass.

        Initialize a new ScalarField object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def evaluate(self, location):
        """Evaluate the scalar field at a position.

        This abstract method must be overridden in a subclass.

        Evaluate the scalar field at the specified position in a
        3-dimensional space.

        Parameters
        ----------
        location : Vector3D
            The position in 3-dimensional space.

        Returns
        -------
        v : float
            Value of scalar field at the specified location.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
