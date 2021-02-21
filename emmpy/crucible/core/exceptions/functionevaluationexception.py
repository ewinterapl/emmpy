"""Runtime exception to be thrown when a function cannot be evaluated.

@author G.K.Stephens
"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class FunctionEvaluationException(CrucibleRuntimeException):

    # Default serial version UID.
    serialVersionUID = 1

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            s = "The function is not able to evaluate at the supplied value"
        elif len(args) == 1:
            x = args[0]
            s = "The function is not able to evaluate at the value %s" % x
        elif len(args) == 2:
            (x, message) = args
            s = "The function is not able to evaluate at the value %s. %s" % (
                x, message
            )
        else:
            raise CrucibleRuntimeException
        CrucibleRuntimeException.__init__(self, s, **kwargs)
