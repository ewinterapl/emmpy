"""Python port of the Java class
crucible.core.collections.AbstractSequentialReadOnlyList

From the original Java source file:

--------------------------------------------------------------------------
package crucible.core.collections;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.NoSuchElementException;

/**
 * abstract base class for making a list view of objects; you just need the
 * size() and get(i) methods;
 *
 * Note that this list does not implement the marker interface RandomAccess,
 * meaning that the collections will not assume fast random access. (There is
 * a subclass that does have random access if that's what you want.)
 *
 * All methods that add or modify elements throw runtime exceptions.
 *
 * @author vandejd1
 */
--------------------------------------------------------------------------

Classes
-------
AbstractSequentialReadOnlyList
    DESCRIBE
"""


from emmpy.java.lang.indexoutofboundsexception import IndexOutOfBoundsException
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)
from emmpy.java.util.iterator import Iterator
from emmpy.java.util.list import List
from emmpy.java.util.listiterator import ListIterator
from emmpy.java.util.nosuchelementexception import NoSuchElementException


class AbstractSequentialReadOnlyList(List):
    """AbstractSequentialReadOnlyList

    DESCRIBE

    Since this was designed as an abstract Java class, this class must not be
    instantiated.
    """

    def add(self, *args):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def addAll(self, *args):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def clear(self):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def contains(self, o):
        """A very simple implementation that does linear search
        """
        for i in range(self.size()):
            if self.get(i).equals(o):
                return True
        return False

    def containsAll(self, c):
        """Does linear search on every element in the list
        """
        for o in c:
            if not self.contains(o):
                return False
        return True

    def indexOf(self, o):
        """A very simple implementation that does linear search to find the
         index of the element that .equals() the given object
        """
        for i in range(self.size()):
            if self.get(i).equals(o):
                return i
        return -1

    def isEmpty(self):
        return self.size() == 0

    def iterator(self):
        return self.listIterator()

    def lastIndexOf(self, o):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def listIterator(self, *args):
        return None
        # return listIterator(0)
        # or
        # return new ListItr(index);

    def remove(self, *args):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def removeAll(self, c):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def retainAll(self, c):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def set(self, index, element):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def subList(self, fromIndex, toIndex):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    def toArray(self, *args):
        raise UnsupportedOperationException(
            "Unsupported method called on a read-only list.")

    class Itr(Iterator):
        """DESCRIBE
        """

        def __init__(self):
            # Index of element to be returned by subsequent call to next.
            self.cursor = 0
            # Index of element returned by most recent call to next or
            # previous. Reset to -1 if this element is deleted by a call to
            # remove.
            self.lastRet = -1

        def hasNext(self):
            return self.cursor != self.size()

        def next(self):
            # checkForComodification();
            try:
                next = self.get(self.cursor)
                self.lastRet = self.cursor
                self.cursor += 1
                return next
            except IndexOutOfBoundsException:
                raise NoSuchElementException()

        def remove(self):
            raise UnsupportedOperationException(
                "Unsupported method called on a read-only list.")

    class ListItr(ListIterator, Iterator):

        def __init__(self, index):
            self.cursor = index

        def hasPrevious(self):
            return self.cursor != 0

        def previous(self):
            try:
                i = self.cursor - 1
                previous = self.get(i)
                self.lastRet = self.cursor = i
                return previous
            except IndexOutOfBoundsException:
                raise NoSuchElementException

        def nextIndex(self):
            return self.cursor

        def previousIndex(self):
            return self.cursor - 1

        def set(self, o):
            raise UnsupportedOperationException(
                "Unsupported method called on a read-only list.")

        def add(self, o):
            raise UnsupportedOperationException(
                "Unsupported method called on a read-only list.")
