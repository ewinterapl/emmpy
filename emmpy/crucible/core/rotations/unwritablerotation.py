"""Abstract class representing an unwritable rotation matrix.

N.B. This class was based on a Java interface, and therefore these methods
will raise exceptions if invoked.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class UnwritableRotation:
    """Abstract class representing an unwritable rotation matrix.

    N.B. This class was based on a Java interface, and therefore these
    methods will raise exceptions if invoked.
    """

    def __init__(self):
        """Initialize a new UnwritableRotation object.

        This abstract method must be overridden in a subclass.

        Initialize a new UnwritableRotation object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getRotation(self, buffer):
        """Convert the representation of the rotation into a matrix.

        Convert the representation of the rotation into a matrix.

        Parameters
        ----------
        buffer : Matrix
            Matrix to capture the result.

        Returns
        -------
        buffer : Matrix
            The rotation matrix.
        """
        raise AbstractMethodException
