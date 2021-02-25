from emmpy.java.util.arrays import Arrays


class ArrayUtilities:
    """From the original Java file:

    This class consists exclusively of static methods that operate on or
    return arrays. It is much like the Arrays class in the java.util
    package, only it provides other useful methods.

    TODO: Flush out the class with the remaining primitive array search
    methods

    @author F.S.Turner

    Determine the index of the last element less than or equal to the
    specified key. The list must be sorted into ascending order
    {@link Arrays#sort(double[])}. If it is not sorted, the results
    are undefined. If the list contains multiple elements equal to the
    specified one, the last one is guaranteed to be extracted.

    The method utilizes {@link Arrays#binarySearch(double[], int, int,
    double)} so its performance characteristics are closely related.

    @param list the list containing sorted doubles over which to search
    @param key the key to locate the last element less than or equal to
    in the list

    @return the range returned is [-1,list.length-1], where -1 indicates
    that key precedes all elements in the list.
    """

    @classmethod
    def lastLessThanOrEqualTo(cls, *args):
        """Determine the index of the last element less than or equal to the
        specified key. The list must be sorted into ascending order
        {@link Arrays#sort(double[])}. If it is not sorted, the results
        are undefined. If the list contains multiple elements equal to the
        specified one, the last one is guaranteed to be extracted.

        The method utilizes {@link Arrays#binarySearch(double[], int, int,
        double)} so its performance characteristics are closely related.

        @param list the list containing sorted doubles over which to search
        @param key the key to locate the last element less than or equal to
        in the list
        OR
        @param list the list over which a subset of values is to be searched
        @param startIndex the starting position to perform the search
        @param length the length over which to perform the search
        @param key the key to locate

        @return the index of the element last less than or equal to the
        supplied key in the sublist. The range returned is
        [pos-1,pos+length-1] where pos-1 indicates that key precedes all
        elements in the specified range within list.
        """
        if len(args) == 2:
            (alist, key) = args
            startIndex = 0
            length = len(alist)
        elif len(args) == 4:
            (alist, startIndex, length, key) = args
        else:
            raise Exception

        result = Arrays.binarySearch(alist, startIndex, startIndex + length,
                                     key)
        # If the result was located in the list directly, locate the last
        # element equal to it and return that index.
        if result >= 0:
            lastEqualIndex = cls.__locateLastElementEqualTo(result, alist,
                                                            startIndex
                                                            + length)
            return lastEqualIndex
        return cls.convertIndexForLessThan(result)

    @classmethod
    def lastLessThan(cls, *args):
        """Determine the index of the last element strictly less than the
        specified key. The list must be sorted into ascending order
        {@link Arrays#sort(double[])}. If it is not sorted, the results are
        undefined. If the list contains multiple equal elements to the
        specified one, the last one is guaranteed to be extracted.

        This method utilizes {@link Arrays#binarySearch(double[], int, int,
        double)} so its performance characteristics are closely related.

        @param list the list containing sorted doubles over which to search
        @param key the key to locate the last element strictly less than in
        the list
        OR
        @param list the list over which a subset of values is to be searched
        @param startIndex the starting position from which to perform the
        search
        @param length the length over which to perform the search
        @param key the key to locate

        @return the index of the last element strictly less than the
        supplied key in the sublist. The range returned is [pos-1,
        pos+length-1] where pos-1 indicates that key preceds all
        elements in the specified range within the list.
        """
        if len(args) == 2:
            (alist, key) = args
            startIndex = 0
            length = len(alist)
        elif len(args) == 4:
            (alist, startIndex, length, key) = args
        else:
            raise Exception

        result = Arrays.binarySearch(list, startIndex, startIndex + length,
                                     key)

        # If the result was located in the list directly, locate the first
        # element equal to it and return that index less 1.
        if result >= 0:
            lastEqualIndex = cls.locateFirstElementEqualTo(result, alist,
                                                           startIndex)
            return lastEqualIndex - 1
        return cls.onvertIndexForLessThan(result)

    @classmethod
    def firstGreaterThanOrEqualTo(cls, *args):
        """Determine the index of the first element greater than or equal to
        the specified key. The list must be sorted into ascending order
        {@link Arrays#sort(double[])}. If it is not sorted, the results
        are undefined. If the list contains multiple elements equal to the
        specified key, the first one is guaranteed to be located.

        This method utilizes {@link Arrays#binarySearch(double[], int, int,
        double)} so its performance characteristics are closely related.

        @param list the sorted list containing the values to be searched
        @param key the key to locate
        OR
        @param list the list from which the range is to be searched
        @param startIndex the start index of the search range
        @param length the length of the search range
        @param key the key to locate

        @return the range returned is [pos, pos+length], where pos+length
        indicates that key follows all elements in the range.
        """
        if len(args) == 2:
            (alist, key) = args
            # This is just as simple as invoking the corresponding
            # lastLessThan method and adding one.
            return cls.lastLessThan(alist, key) + 1
        elif len(args) == 4:
            (alist, startIndex, length, key) = args
            return cls.lastLessThan(alist, startIndex, length, key) + 1

    @classmethod
    def firstGreaterThan(cls, *args):
        """Determine the index of the first element strictly greater than the
        specified key. The list must be sorted into ascending order:
        {@link Arrays#sort(double[])}. If it is not sorted, the results are
        undefined. If the list contains multiple elements equal to the
        specified object, the first one is guaranteed to be located.

        This method utilizes {@link Arrays#binarySearch(double[], int, int,
        double)} so its performance characteristics are closely related.

        @param list the list over which to perform the search
        @param key the value to locate
        OR
        @param list the list from which the range is to be searched
        @param startIndex the start index of the search range
        @param length the length of the search range
        @param key the key to locate

        @return the range returned is [0, list.length], where list.length
        indicates that key follows all elements in the list.
        """
        if len(args) == 2:
            (alist, key) = args
            # This is just as simple as invoking the corresponding
            # lastLessThan method and adding one.
            return cls.lastLessThanOrEqualTo(alist, key) + 1
        elif len(args) == 4:
            (alist, startIndex, length, key) = args
            return cls.lastLessThanOrEqualTo(alist, startIndex, length,
                                             key) + 1

    @staticmethod
    def __locateLastElementEqualTo(index, alist, maxIndex):
        """Locate the last element in the list equal to the element by the
        supplied index.

        @param index the index at which to start the search. It should be an
        index to an existing element of the list that is of interest.
        @param list the list over which the search is to be performed
        @param maxIndex the maximum index which is to be considered

        @return the index of the last element equal to list[index] in the
        sorted list.
        """

        # If we are already at the end of the list, just return.
        if index == len(alist) - 1:
            return index

        result = index

        # Loop over elements in the list incrementing result as long as they
        # are equal to list[index].
        # while ((result < maxIndex) && (list[++result] == list[index])) {}
        while result < maxIndex:
            result += 1
            if alist[result] == alist[index]:
                continue

        # Result will have been incremented one past the desired index,
        # decrement it.
        result -= 1
        return result

    @staticmethod
    def __locateFirstElementEqualTo(index, alist, firstIndex):
        """Locate the first element in the list equal to the element at
        position index.

        @param index the index at which to start the search for the first
        value.
        @param list the list over which the search is to be performed.
        @param firstIndex the minimum index over which the search is to happen

        @return the index of the first element equal to list[index] in the
        sorted list.
        """

        # If we are already at the start of the range, just return.
        if index == firstIndex:
            return index

        result = index

        # Loop over the previous elements in the list as long as they
        # continue to compare with equality to the element at list[index].
        # while ((result > firstIndex) && (list[--result] == list[index])) {}
        while result > firstIndex:
            result -= 1
            if alist[result] == alist[index]:
                continue

        # Result will have been decremented one past the desired index,
        # increment it.
        result += 1
        return result

    @staticmethod
    def __convertIndexForLessThan(result):
        """In the event that the binarySearch algorithm from the Collections
        class is unable to turn up a matched element, locate the index of the
        element that is strictly less than the one sought.

        @param result a negative result from either
        {@link Arrays#binarySearch(byte[], byte)}
        @param listSize the size of the list over which the binary search was
        performed at the time of the search

        @return the index of the element strictly less than the one sought
        after in the binary search.
        """
        insertionPoint = -result - 1

        # Since the insertion point is defined as the index at which everyone
        # will be shifted to the right:

        # value: 10 20 30 40 index: 0 1 2 3

        # If insertion point is 1, then that means the result of inserting
        # this element into the list will result:

        # value: 10 15 20 30 40 index: 0 1 2 3 4

        # would be the result, and 15 would have reduced to an insertion point
        # of 1. So, long story short, if we reach here then just subtract one
        # and we'll get the answer we desire.
        return insertionPoint - 1

    @staticmethod
    def isRagged(r):
        """Checks if an array is ragged, e.g:

        This is a ragged array
          { {1, 2, 3} }
          { {3, 4}    }

        This is not a ragged array
          { {1, 2, 3} }
          { {3, 4, 5} }

        @param r input array
        @param <R> the array type parameter

        @return true if the input is a ragged array, false if it is
        'rectangular'
        """
        if len(r) > 0 and len(r[0]) > 0:
            width0 = len(r[0])
            depth0 = len(r[0][0])
            for i in range(len(r)):
                if len(r[i]) != width0:
                    return True
                for j in range(len(r[0])):
                    if len(r[i][j]) != depth0:
                        return True
        return False
