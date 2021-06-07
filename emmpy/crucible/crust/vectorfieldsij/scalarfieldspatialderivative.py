"""An interface for the derivative of a 2-D scalar field."""


class ScalarFieldIJSpatialDerivative:
    """An interface for the derivative of a 2-D scalar field."""

    def __init__(self, location):
        """Build a new object.

        INTERFACE - DO NOT INSTANTIATE.

        param (UnwritableVectorIJK) location
        """
        raise Exception

    def differentiateFDi(self, location):
        """Get the 1st gradient component.

        INTERFACE - DO NOT INVOKE.

        param (UnwritableVectorIJK) location
        return (float)
        """
        raise Exception

    def differentiateFDj(self, location):
        """Get the 2nd gradient component.

        INTERFACE - DO NOT INVOKE.

        param (UnwritableVectorIJK) location
        return (float)
        """
        raise Exception
