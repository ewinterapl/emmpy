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

    def toString(self):
        """Convert the object to a string."""
        return "[position=%s, value=%s]" % (self.position, self.value)

    def hashCode(self):
        """Compute the object hash code."""
        prime = 31
        result = 1
        result = prime*result
        if self.position is not None:
            result += self.position.hashCode()
        result = prime*result
        if self.value is not None:
            result += self.value.hashCode()
        return result

    def equals(self, obj):
        """Check the object for equality with another object."""
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.position is None:
            if other.position is not None:
                return False
        elif not self.position.equals(other.position):
            return False
        if self.value is None:
            if other.value is not None:
                return False
        elif not self.value.equals(other.value):
            return False
        return True
