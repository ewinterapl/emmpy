"""Interface for field-aligned current options.

Interface for field-aligned current options.

This class was derived from a Java interface, and therefore mose of the
methods will raise an exception if invoked.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class FacConfiguration:
    """Interface for field-aligned current options.

    Interface for field-aligned current options.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new FacConfiguration object.

        Initialize a new FacConfiguration object.

        Parameters
        ----------
        None
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def createFromCoeffs(self, coeffs):
        """Create a FacConfiguration object from a set of coefficients.

        Create a FacConfiguration object from a set of coefficients.

        Parameters
        ----------
        coeffs : array-like of float
            Coefficients to use.
        
        Returns
        -------
        result : list of FacConfigurationOptions
            Options created from coefficients.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def getNumberOfFields(self):
        """Get the number of fields.

        Get the number of fields.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
