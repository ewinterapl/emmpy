"""A vector location and field value there.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class VectorFieldValue:
    """A vector location and field value there."""

    def __init__(self):
        """INTERFACE - DO NOT INSTANTIATE."""
        raise Exception

    def getPosition(self):
        """Get the position component.

        INTERFACE - DO NOT INVOKE.

        @return the position component
        """
        raise Exception

    def getValue(self):
        """Get the value associated with that position.

        INTERFACE - DO NOT INVOKE.

        @return the value associated with that position
        """
        raise Exception
