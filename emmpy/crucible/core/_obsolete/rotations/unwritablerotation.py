"""emmpy.crucible.core.rotations.unwritablerotation"""


class UnwritableRotation:
    """Interface encapsulating rotation matrix retrieval from another class.

    author F.S.Turner
    """

    def __init__(self):
        """Constructor

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
