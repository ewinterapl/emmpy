"""Python port of the Java abstract class
crucible.core.collections.AbstractIndexedIterator

Classes
-------
AbstractIndexedIterator
    Python version of the AbstractIndexedIterator Java class
"""


# from emmpy.java.util.iterator import Iterator
from emmpy.com.google.common.collect.unmodifiableiterator import (
    UnmodifiableIterator
)
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.java.util.nosuchelementexception import NoSuchElementException


class AbstractIndexedIterator(UnmodifiableIterator):
    """AbstractIndexedIterator

    Based on the original Java class:
    crucible.core.collections.AbstractIndexedIterator

    Since this was designed as an abstract Java class, this class must not be
    instantiated. Subclasses must implement the elements() and element()
    methods.

    From the original Java file:

    /**
    * Simple abstract class that implements the {@link Iterator} interface
    * from a source that is organized by index. Simply supply implementations
    * for the two abstract methods and you'll have an {@link Iterator} that
    * works properly.
    *
    * @author F.S.Turner
    *
    * @param <E> the element over which iteration is to be performed
    */
    """

    def __init__(self):
        """Initialize a new AbstractIndexedIterator object.

        Parameters
        ----------
        self : AbstractIndexedIterator
            Current object

        Returns
        -------
        self : AbstractIndexedIterator
            Current object
        """
        self.__index = 0

    def hasNext(self) -> bool:
        """Check if there are elements remaining.

        Parameters
        ----------
        self : AbstractIndexedIterator
            Current object

        Returns
        -------
        bool
            True if elements remain, else False.
        """
        return self.__index < self.elements()

    def next(self) -> object:
        """Return the next element.

        Parameters
        ----------
        self : AbstractIndexedIterator
            Current object

        Returns
        -------
        object
            Next object in list.
        """
        if self.__index < self.elements():
            # Post-increment index after retrieval.
            e = self.element(self.__index)
            self.__index += 1
            return e
        raise NoSuchElementException(
            "Unable to access element at index:" + self.__index
            + "from indexed elements of length:" + self.elements())

    def elements(self) -> int:
        """Provide the number of elements in the indexed list.

        Parameters
        ----------
        self : AbstractIndexedIterator
            Current object

        Returns
        -------
        int
            Number of elements in list.

        Raises
        ------
        Exception
            When called.
        """
        raise CrucibleRuntimeException

    def element(self, index) -> object:
        """Supplies the element associated with a particular index in the
        range [0, elements()-1] respectively.

        Parameters
        ----------
        self
            Current object
        index : int
            Index of element to return.

        Returns
        -------
        object
            The element at index.

        Raises
        ------
        Exception
            If called.
        """
        raise CrucibleRuntimeException
