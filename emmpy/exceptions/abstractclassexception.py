"""Exception for instantiating abstract classes.

author Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.emmpyexception import EmmpyException


class AbstractClassException(EmmpyException):
    """Raise this exception when an abstract class is instantiated."""

    def __init__(self, *args):
        """Initialize a new AbstractClassException.

        param (str, optional) message - Message to attach to exception.
        A default will be created if not provided.
        """
        message = 'Do not instantiate an abstract class!'
        if len(args) == 0:
            pass
        elif len(args) == 1:
            message = args[0]
        else:
            raise Exception
        self.message = message
