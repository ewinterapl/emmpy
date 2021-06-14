"""Base class for Emmpy exceptions.

author Eric Winter (eric.winter@jhuapl.edu)
"""


class EmmpyException(Exception):
    """Base class for all Emmpy exceptions."""

    # The default message to attach to the exception when no message is
    # provided.
    _default_message = 'An EmmpyException has been raised!'

    def __init__(self, *args):
        """Initialize a new EmmpyException.

        param (str, optional) message - Message to attach to exception.
        A default will be used if not provided.
        """
        if len(args) == 0:
            message = EmmpyException._default_message
        elif len(args) == 1:
            message = args[0]
        else:
            raise Exception
        self.message = message
