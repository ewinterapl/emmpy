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
