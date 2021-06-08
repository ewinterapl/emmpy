"""Base class for vector field values."""


from emmpy.crucible.core.math.coords.vectorfieldvalue import VectorFieldValue


class AbstractVectorFieldValue(VectorFieldValue):
    """Base class for vector field values."""

    def __init__(self, position, value):
        """Create a state.

        @param position the position of one object relative to another.
        @param value the time derivative of the supplied position.
        """
        self.position = position
        self.value = value

    def getPosition(self):
        """Return the position."""
        return self.position

    def getValue(self):
        """Return the value."""
        return self.value
