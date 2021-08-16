"""Bug exception for Crucible code.

Exception generated as a result of something failing that should never
fail.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class BugException(CrucibleRuntimeException):
    """Bug exception for Crucible code."""
