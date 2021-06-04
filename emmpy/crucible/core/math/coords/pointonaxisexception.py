"""Exception for point-on-axis conditions."""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class PointOnAxisException(CrucibleRuntimeException):
    """Exception for point-on-axis conditions."""

    def __init__(self, *args):
        """Build a new object."""
        if len(args) == 0:
            pass
        elif len(args) == 1:
            # args[0] can be message or cause
            CrucibleRuntimeException.__init__(self, args[0])
        elif len(args) == 2:
            (message, cause) = args
            CrucibleRuntimeException.__init__(self, message, cause)
