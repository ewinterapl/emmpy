"""Abstract class representing a rotation matrix.

N.B. This class was based on a Java interface, and therefore these methods
will raise exceptions if invoked.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class Rotation:
    """Abstract class representing a rotation matrix.

    N.B. This class was based on a Java interface, and therefore these
    methods will raise exceptions if invoked.
    """

    def __init__(self):
        """Initialize a new Rotation object.

        This abstract method must be overridden in a subclass.

        Initialize a new Rotation object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def setTo(self, matrix):
        """Set the representation to the value of the supplied matrix.

        Set the representation to the value of the supplied matrix.

        Parameters
        ----------
        matrix : Matrix
            Matrix of values for the rotation matrix.

        Returns
        -------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
