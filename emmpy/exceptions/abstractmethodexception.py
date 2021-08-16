"""Exception for invoking abstract methods.

This exception should be raised when an abstract method (a method that
must be overridden) is invoked.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.emmpyexception import EmmpyException


class AbstractMethodException(EmmpyException):
    """Raise this exception when an abstract method is invoked."""

    # The default message to attach to the exception when no message is
    # provided.
    _default_message = 'Do not invoke an abstract method!'

    def __init__(self, message=_default_message):
        """Initialize a new AbstractMethodException.

        Parameters
        ----------
        message : str, optional default = _default_message
            Message to display when exception is raised.

        Returns
        -------
        None
        """
        super().__init__(message)
