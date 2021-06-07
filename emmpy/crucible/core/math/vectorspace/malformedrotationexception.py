"""Exception to use for a malformed rotation matrix."""


class MalformedRotationException(Exception):
    """Exception for the specification of an invalod rotation matrix.

    @author F.S.Turner
    """

    def __init__(self, *args):
        """Build the object."""
        if len(args) == 0:
            pass
        elif len(args) == 1:
            Exception(self, args[0])
        elif len(args) == 2:
            Exception(self, args[0], args[1])
        else:
            raise Exception
