"""This class assumes the lists provided to it are sorted in asceding order.
"""

from collections.abc import Iterator

from emmpy.java.util.collections import Collections
# from emmpy.crucible.core import collections
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class CollectionUtilities:
    """This class consists exclusively of static methods that operate on or
    return collections. It contains polymorphic algorithms that operate on
    collections. It is much like the Collections class in the java.util
    package, only it provides other useful generic methods.

    The methods of this class all throw a NullPointerException if the
    collections or class objects provided to them are null.

    @author F.S.Turner (APL)
    """

    @staticmethod
    def lastLessThanOrEqualTo(*args) -> int:
        """Determine the index of the last element less than or equal to the
        specified key. The list must be sorted into ascending order according
        to the natural ordering specified by the implementation of the
        Comparable interface. If it is not sorted, the results are undefined.
        If the list contains multiple elements equal to the specified object,
        the last one is guaranteed to be extracted.

        The method utilizes {@link java.util.Collections#binarySearch(List,
        Object)} so its performance characteristics are closely related.

        @param <T> the parameterized type of the key
        @param list the list containing objects capable of being compared to
        an instance of T, sorted in an order consistent with the comparison
        @param key the key to locate the last element less than or equal to in
        the list
        OR
        @param <T> the parameterized type of the key
        @param list the list containing objects to be compared against key
        with the supplied comparator, sorted in an ordering consistent with
        the comparator
        @param key the key to locate the last element less than or equal to in
        the list
        @param c the comparator defining the ordering to be utilized in the
        search

        @return the range returned is [-1,list.size()-1], where -1 indicates
        that key precedes all elements in the list.
        """
        if len(args) == 2:
            (alist, key) = args
        elif len(args) == 3:
            # The comparator object c is ignored.
            (alist, key, c) = args
        else:
            raise CrucibleRuntimeException

        # Check to see if the key itself exists in the list.
        # If binarySearch() returns >=0, that is the position of the key in
        # the list. If < 0, the result of binarySearch() is
        # (-insertionPoint - 1), where insertionPoint is the index in the
        # sorted list where the key would be inserted to maintain sort order.
        result = Collections.binarySearch(alist, key)

        # If the result was located in the list directly, locate the *last*
        # element equal to it and return that index.
        if result >= 0:
            # Start search at the index of the *first* (maybe only) appearance
            # of the key.
            lastEqualIndex = CollectionUtilities.locateLastElementEqualTo(
                result, key, alist)
            return lastEqualIndex

        # The key was not found in the list, so convert the negative result
        # from binarySearch() to the correct insertion point.
        return CollectionUtilities.convertIndexForLessThan(result, len(alist))

    @staticmethod
    def lastLessThan(*args) -> int:
        """Determine the index of the last element less than the specified
        key. The list must be sorted into ascending order according to the
        natural ordering specified by the implementation of the Comparable
        interface. If it is not sorted, the results are undefined. If the list
        contains multiple elements equal to the specified object, the last
        one is guaranteed to be extracted.

        The method utilizes
        {@link java.util.Collections#binarySearch(List, Object)} so its
        performance characteristics are closely related.

        @param <T> the parameterized type of the key
        @param list the list containing objects capable of being compared to
        an instance of T, sorted in an order consistent with the comparison
        @param key the key to locate the last element less than in the list

        @return the range returned is [-1,list.size()-1], where -1 indicates
        that key precedes all elements in the list.
        """
        if len(args) == 2:
            (alist, key) = args
        elif len(args) == 3:
            # This case ignores c.
            (alist, key, c) = args
        else:
            raise CrucibleRuntimeException

        # Check to see if the key itself exists in the list.
        # If binarySearch() returns >=0, that is the position of the key in
        # the list. If < 0, the result of binarySearch() is
        # (-insertionPoint - 1), where insertionPoint is the index in the
        # sorted list where the key would be inserted to maintain sort order.
        result = Collections.binarySearch(alist, key)

        # If the result was located in the list directly, locate the first
        # element equal to it and return that index less 1.
        if result >= 0:
            lastEqualIndex = CollectionUtilities.locateFirstElementEqualTo(
                result, key, alist)
            return lastEqualIndex - 1

        # The key was not found in the list, so convert the negative result
        # from binarySearch() to the correct insertion point.
        return CollectionUtilities.convertIndexForLessThan(result, len(alist))

    @staticmethod
    def firstGreaterThanOrEqualTo(*args) -> int:
        if len(args) == 2:
            (alist, key) = args
        elif len(args) == 3:
            # This case ignores c.
            (alist, key, c) = args
        else:
            raise CrucibleRuntimeException
        return CollectionUtilities.lastLessThan(alist, key) + 1

    @staticmethod
    def firstGreaterThan(*args) -> int:
        if len(args) == 2:
            (alist, key) = args
        elif len(args) == 3:
            # This case ignores c.
            (alist, key, c) = args
        else:
            raise CrucibleRuntimeException
        return CollectionUtilities.lastLessThanOrEqualTo(alist, key) + 1

    @staticmethod
    def locateFirstElementEqualTo(*args) -> int:
        """Locate the first element equal to the supplied key,
        starting at index. This expectation is that index is already
        pointing at an element of the list that is equal to the supplied
        key from the implementation of the Comparable interface's
        perspective.

        Supplying the key is necessary in the event that the list itself
        implements Comparable of an unrelated type, of which key is an
        instance of a subclass.

        @param <T> the parameterized type of key
        @param index the index at which to start the search. It should be
        such that: list.get(index).compareTo(key) == 0.
        @param key the key to compare against for equality
        @param list the list containing objects to be compared against
        key, sorted in an order consistent with the natural ordering
        defined by Comparable

        @return the index of the first element in the list that is equal
        to the supplied key.
        """
        if len(args) == 3:
            if isinstance(args[1], int):
                (index, key, alist) = args
            else:
                (index, alist, c) = args
        else:
            raise CrucibleRuntimeException

        # If we are already at the head of the list, then just return.
        if index == 0:
            return index

        # Search up to the specified index.
        result = alist.index(key, 0, index + 1)
        return result

    @staticmethod
    def locateLastElementEqualTo(*args) -> int:
        """Locate the last element equal to the supplied key, starting at
        index. This expectation is that index is already pointing at an
        element of the list that is equal to the supplied key from the
        implementation of the Comparable interface's perspective.

        Supplying the key is necessary in the event that the list itself
        implements Comparable of an unrelated type, of which key is an instance
        of a subclass.

        @param <T> the parameterized type of key
        @param index the index at which to start the search. It should be such
        that:
        list.get(index).compareTo(key) == 0.
        @param key the key to compare against for equality
        @param list the list containing objects to be compared against key,
        sorted in an order consistent with the natural ordering defined by
        Comparable

        @return the index of the last element in the list that is equal to the
        supplied key.
        """
        if len(args) == 3:
            if isinstance(args[1], int):
                (index, key, alist) = args
            else:
                (index, alist, c) = args
        else:
            raise CrucibleRuntimeException

        # If we are already at the end of the list, just return.
        if index == len(alist) - 1:
            return index

        # Search backward from the end of the list.
        for i in range(len(alist) - 1, index - 1, -1):
            if alist[i] == key:
                return i
        raise ValueError

    @staticmethod
    def convertIndexForLessThan(result: int, listSize: int) -> int:
        """In the event that the binarySearch algorithm from the Collections
        class is unable to turn up a matched element, locate the index of the
        element that is strictly less than the one sought

        @param result a negative result from either
        {@link java.util.Collections#binarySearch(List, Object)} or
        {@link java.util.Collections#binarySearch(List, Object, Comparator)}

        @param listSize the size of the list over which the binary search was
        performed at the time of the search

        @return the index of the element strictly less than the one sought
        after in the binary search. Range of returned values is [-1,listSize],
        where -1 indicates the value sought after precedes all elements in the
        list.
        """
        insertionPoint = -result - 1

        # Since the insertion point is defined as the index at which everyone
        # will be shifted to the right:

        # value: 10 20 30 40 index: 0 1 2 3

        # If insertion point is 1, then that means the result of inserting this
        # element into the list will result:

        # value: 10 15 20 30 40 index: 0 1 2 3 4

        # would be the result, and 15 would have reduced to an insertion point
        # of 1. So, long story short, if we reach here then just subtract one
        # and we'll get the answer we desire.
        return insertionPoint - 1

    @staticmethod
    def addAll(*args) -> list:
        """Adds the contents of an iterator to the supplied collection.

        Elements are added to the collection via the
        {@link Collection#add(Object)} method in the order that the iterator
        produces them.

        @param <T> the element type of the iterator
        @param <C> the collection type
        @param iterable the iterator, producing elements of type T
        @param collection the collection to receive elements of type T

        @return a reference to collection for the convenience of method
        chaining
        """
        if len(args) == 2:
            if isinstance(args[0], Iterator):
                (iterable, collection) = args
            else:
                (iterator, collection) = args
        else:
            raise CrucibleRuntimeException

        # Add each new item to the end of the list.
        for obj in iterator:
            collection.append(obj)
        return collection

    @staticmethod
    def convertToListOfSuperclass(listOfChildren: list) -> list:
        """allows an ImmutableList of children objects to be converted to an
        ImmutableList of parent objects; for an ordinary Java List, this would
        be dangerous because of the ability to potentially ADD diverse objects
        into the list. But since this method deals with an immutable list,
        nothing can be added. Note that the requirement that S extends T is
        not needed - the compiler will let this through even if S does not
        extend T, but that's probably something you don't want to do, so the
        S extends T is there to remind you of this fact. As long as S extends
        T, the casting that goes on inside this method is safe.

        @param <T> the type of the child
        @param <S> the type of the parent
        @param listOfChildren the children to convert

        @return the same list cast as a list of parent objects (type T)
        """

        # This is really a no-op.
        # recast as list of parent objects:
        return listOfChildren
