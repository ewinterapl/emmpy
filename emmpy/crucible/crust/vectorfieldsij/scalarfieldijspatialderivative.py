"""An interface for the derivatives of a 2-D scalar field.

This class defines the interface for the derivatives of a 2-D scalar
field.
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class ScalarFieldIJSpatialDerivative:
    """An interface for the derivatives of a 2-D scalar field."""

    def __init__(self, location):
        """Initialize a new ScalarFieldIJSpatialDerivative object.

        Parameters
        ----------
        location : VectorIJ
            Location in 2-D Cartesian space.

        Raises
        ------
        AbstractMethodException
            When invoked.

        """
        raise AbstractMethodException

    def differentiateFDi(self, location):
        """Get the 1st gradient component.

        Return the derivative of the scalar field wrt the 1st
        coordinate.

        Parameters
        ----------
        location : VectorIJ
            Location in 2-D Cartesian space.

        Returns
        -------
        val : float
            1st-coordinate derivative of field at location.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFDj(self, location):
        """Get the 2nd gradient component.

        Return the derivative of the scalar field wrt the 2nd
        coordinate.

        Parameters
        ----------
        location : VectorIJ
            Location in 2-D Cartesian space.

        Returns
        -------
        val : float
            2nd-coordinate derivative of field at location.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
