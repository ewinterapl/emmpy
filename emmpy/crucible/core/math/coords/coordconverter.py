"""Abstract base class for coordinate converters.

This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class CoordConverter:
    """Abstract base class for coordinate converters.

    This class defines the methods required by coordinate converter
    classes.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new CoordConverter object.

        Initialize a new CoordConverter object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def toCoordinate(self, cartesian):
        """Convert a Cartesian vector to the coordinate system.

        Converts a Cartesian vector to this coordinate system.

        Parameters
        ----------
        cartesian : Vector
            A Cartesian vector.
        
        Returns
        -------
        coordinate : Vector
            The input vector converted to the current coordinate system.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def toCartesian(self, coordinate):
        """Convert a coordinate vector to the Cartesian system.

        Converts a coordinate vector to this Cartesian system.

        Parameters
        ----------
        coordinate : Vector
            A vector in the current coordinate system.
        
        Returns
        -------
        cartesian : Vector
            The input vector converted to the Cartesian coordinate system.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
