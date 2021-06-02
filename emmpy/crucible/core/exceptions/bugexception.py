"""emmpy.crucible.core.exceptions.bugexception

Runtime exception generated as a result of something failing that should
never fail.

Prototypical example would be invoking the string constructor:
new String(new byte[] {32, 32}, "ISO-8859-1")
the constructor may throw an exception due to an unsupported character
encoding, but this should never happen in practice.

@author F.S.Turner
"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class BugException(CrucibleRuntimeException):
    pass
