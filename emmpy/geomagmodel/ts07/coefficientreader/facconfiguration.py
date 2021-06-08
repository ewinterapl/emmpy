"""Interface for field-aligned current options."""


class FacConfiguration:

    def __init__(self):
        """Interface for field-aligned current options.

        INTERFACE - DO NOT INSTANTIATE.
        """
        raise Exception

    def createFromCoeffs(self, coeffs):
        """Create the object from a set of coefficients.

        INTERFACE - DO NOT INVOKE."""
        raise Exception

    def getNumberOfFields(self):
        """Get the number of fields.

        INTERFACE - DO NOT INVOKE.
        """
        raise Exception
