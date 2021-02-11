"""Python port of the Java class
crucible.core.collections.AbstractIndexedIterator

Classes
-------
AbstractIndexedIterator
    Python version of the AbstractIndexedIterator Java class
"""


from emmpy.com.google.common.collect.unmodifiableiterator import UnmodifiableIterator


class AbstractIndexedIterator(UnmodifiableIterator):
    """AbstractIndexedIterator

    Based on the original Java class:
    crucible.core.collections.AbstractIndexedIterator

    Since this was designed as an abstract Java class, this class must not be
    instantiated. Subclasses must implement the elements() and element()
    methods.

    From the original Java file:

    /**
    * Simple abstract class that implements the {@link Iterator} interface from a source that is
    * organized by index. Simply supply implementations for the two abstract methods and you'll have an
    * {@link Iterator} that works properly.
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
        self.index = 0

    def hasNext(self):
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
        return self.index < self.elements()

    def next(self):
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
        if self.index < self.elements():
            # Post-increment index after retrieval.
            e = self.element(index)
            self.index = self.index + 1
            return e
        raise Exception("Unable to access element at index:" + self.index
                    + "from indexed elements of length:" + self.elements());

    def elements(self):
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
        raise Exception

    def element(self, index):
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
        raise Exception