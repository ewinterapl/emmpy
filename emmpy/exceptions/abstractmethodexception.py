"""Exception for invoking abstract methods.

author Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.emmpyexception import EmmpyException


class AbstractMethodxception(EmmpyException):
    """Raise this exception when an abstract method is invoked."""

    # The default message to attach to the exception when no message is
    # provided.
    _default_message = 'Do not invoke an abstract method!'

    def __init__(self, *args):
        """Initialize a new AbstractMethodException.

        param (str, optional) message - Message to attach to exception.
        A default will be created if not provided.
        """
        message = AbstractMethodxception._default_message
        if len(args) == 0:
            pass
        elif len(args) == 1:
            message = args[0]
        else:
            raise Exception
        EmmpyException.__init__(self, message)
