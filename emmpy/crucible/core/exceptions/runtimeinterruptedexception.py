"""emmpy.crucible.core.exceptions.runtimeinterruptedexception

A {@link RuntimeException} intended to perform the same function as
{@link InterruptedException} in cases where the API can not declare the
checked variant provided by the JDK.

@author turnefs1
"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class RuntimeInterruptedException(CrucibleRuntimeException):
    pass
