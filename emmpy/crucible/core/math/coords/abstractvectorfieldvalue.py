"""emmpy.crucible.core.math.coords.abstractvectorfieldvalue"""


# import static com.google.common.base.Preconditions.checkNotNull;

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.coords.vectorfieldvalue import VectorFieldValue


class AbstractVectorFieldValue(VectorFieldValue):
    """AbstractVectorFieldValue"""

    #    * The field containing the buffer that holds the position component of the state.
    #   private final C position;

    #    * The field containing the buffer that holds the value component of the state.
    #   private final C value;

    def __init__(self, position, value):
        """Creates a state.

        @param position the position of one object relative to another.
        @param value the time derivative of the supplied position.
        """
        #   public AbstractVectorFieldValue(C position, C value) {
        self.position = Preconditions.checkNotNull(position)
        self.value = Preconditions.checkNotNull(value)

    def getPosition(self):
        return self.position

    def getValue(self):
        return self.value

    def toString(self):
        return "[position=%s, value=%s]" % (self.position, self.value)

    def hashCode(self):
        """@see java.lang.Object#hashCode()

        (non-Javadoc)
        """
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
        """@see java.lang.Object#equals(java.lang.Object)

        (non-Javadoc)
        """
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
