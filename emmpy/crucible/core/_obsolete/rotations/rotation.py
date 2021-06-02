"""emmpy.crucible.core.rotations.rotation"""


from emmpy.crucible.core.rotations.unwritablerotation import (
    UnwritableRotation
)


class Rotation(UnwritableRotation):
    """Interface describing the two, minimal methods to implement a rotation.

    author F.S.Turner
    """

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def setTo(self, matrix):
        """Set the representation to the value of the supplied matrix.

        param matrix the rotation matrix to capture
        return a reference to the instance for convenience
        """
        raise Exception
