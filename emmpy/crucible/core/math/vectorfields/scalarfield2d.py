"""A scalar field in a 2-dimensional space.

This class represents a scalar field in a 2-dimensional vector space. The
only required method is evaluate().

N.B. This class was based on a Java interface, and therefore these methods
will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class ScalarField2D:
    """A scalar field in a 2-dimensional space.

    This class represents a scalar field in a 2-dimensional vector space.
    The only required method is evaluate().

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new ScalarField2D object.

        This abstract method must be overridden in a subclass.

        Initialize a new ScalarField2D object.

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
        2-dimensional space.

        Parameters
        ----------
        location : Vector2D
            The position in 2-dimensional space.

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
