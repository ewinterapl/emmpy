"""Abstract base class for n-dimensional vectors."""


from emmpy.exceptions.abstractclassexception import AbstractClassException


class Vector:
    """Abstract base class for n-dimensional vectors.

    This class must be subclassed to be used.

    This class is like a Java interface - it specifies all of the methods that
    must be defined in a subclass. But since the entire class is abstract
    (must be subclassed), the constructor __init__() will raise
    AbstractClassException if invoked, and all other methods will raise
    AbstractMethodException if invoked.

    author Eric Winter (eric.winter@jhuapl.edu)
    """

    def __init__(self):
        """Initialize a new Vector object."""
        raise AbstractClassException
