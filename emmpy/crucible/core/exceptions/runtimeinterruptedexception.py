"""A {@link RuntimeException} intended to perform the same function as
{@link InterruptedException} in cases where the API can not declare the
checked variant provided by the JDK.

@author turnefs1
"""

# NOTE: THIS EXCEPTION CLASS IS PROBABLY NOT NEEDED.


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class RuntimeInterruptedException(CrucibleRuntimeException):

    serialVersionUID = 1

    def __init__(self, *args, **kwargs):
        raise CrucibleRuntimeException
