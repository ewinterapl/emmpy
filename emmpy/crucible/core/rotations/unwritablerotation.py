"""An unwritable rotation interface class."""


class UnwritableRotation:
    """An unwritable rotation interface class.

    Interface encapsulating rotation matrix retrieval from another class.

    author F.S.Turner
    """

    def __init__(self):
        """Build a new object.

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def getRotation(self, buffer):
        """Convert the representation of the rotation into a matrix.

        INTERFACE - DO NOT INVOKE

        param buffer the buffer to capture the result
        return a reference to buffer for convenience
        """
        raise Exception
