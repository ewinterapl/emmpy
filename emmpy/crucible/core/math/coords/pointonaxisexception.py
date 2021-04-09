"""emmpy.crucible.core.math.coords.pointonaxisexception"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class PointOnAxisException(CrucibleRuntimeException):
    """PointOnAxisException"""

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            pass
        elif len(args) == 1:
            # args[0] can be message or cause
            CrucibleRuntimeException.__init__(self, args[0])
        elif len(args) == 2:
            (message, cause) = args
            CrucibleRuntimeException.__init__(self, message, cause)
