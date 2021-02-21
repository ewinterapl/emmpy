"""Interface describing an exception factory, designed to convert one type of
exceptions to another for abdicating control of exception generation to the
user or implementor of an interface.

TODO: Provide a simple example.

@author F.S.Turner

@param <I> Input exception type
@param <O> Output exception type
"""


# NOTE: THIS EXCEPTION CLASS IS PROBABLY NOT NEEDED.


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class ExceptionFactory:

    def __init__(self, *args, **kwargs):
        raise CrucibleRuntimeException
