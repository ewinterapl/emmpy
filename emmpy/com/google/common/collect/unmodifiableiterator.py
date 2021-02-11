""" Python port of the UnmodifiableIterator Java class from Google Guava.

Classes
-------
UnmodifiableIterator
    Provides an unmodifiable iterator.
"""


class UnmodifiableIterator:

    """UnmodifiableIterator

    Based on the original Java UnmodifiableIterator class documented at:
    https://guava.dev/releases/8.0/api/docs/com/google/common/collect/UnmodifiableIterator.html
    """

    def __init__(self):
        """Initialize a new UnmodifiableIterator object.

        The Java constructor for this class is protected.

        Parameters
        ----------
        self : UnmodifiableIterator
            New object to initialize.
        
        Returns
        -------
        self : UnmodifiableIterator
            New object after initialization.
        """
        pass

    def remove(self):
        """Remove an item.

        The method prevents item removal.

        Parameters
        ----------
        self : UnmodifiableIterator
            Object to remove item from.
        
        Returns
        -------
        None

        Raises
        ------
        Exception
            When called.
        """
        raise Exception
