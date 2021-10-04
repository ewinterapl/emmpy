"""Interface class for vector field values.

This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class VectorFieldValue:
    """Interface class for vector field values.

    This class was created from a Java interface, and therefore most of
    these methods will raise exceptions if invoked.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new VectorFieldValue object.

        Initialize a new VectorFieldValue object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getPosition(self):
        """Return the position in the vector field.

        Return the position in the vector field.

        Parameters
        ----------
        None

        Returns
        -------
        position : Vector
            Position in the vector field.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getValue(self):
        """Return the value of the vector field.

        Return the value of the vector field.

        Parameters
        ----------
        None

        Returns
        -------
        value : Vector
            Value of the vector field.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
