"""Bug exception for Crucible code.

Exception generated as a result of something failing that should never fail.

author F.S.Turner
"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class BugException(CrucibleRuntimeException):
    """Bug exception for Crucible code."""
