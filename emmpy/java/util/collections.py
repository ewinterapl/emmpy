import bisect


class Collections:

    @staticmethod
    def binarySearch(alist, key):
        """Python version of java.util.collections binarySearch() method.

        The algorithm is taken from the documentation for the original
        Java method, available at:

        https://docs.oracle.com/javase/7/docs/api/java/util/Collections.html#binarySearch(java.util.List,%20T)

        From that documentation:
        *****
        public static <T> int binarySearch(List<? extends Comparable<? super T>> list, T key)
        Searches the specified list for the specified object using the binary
        search algorithm. The list must be sorted into ascending order
        according to the natural ordering of its elements (as by the
        sort(List) method) prior to making this call. If it is not sorted,
        the results are undefined. If the list contains multiple elements equal
        to the specified object, there is no guarantee which one will be found.
        This method runs in log(n) time for a "random access" list (which
        provides near-constant-time positional access). If the specified list
        does not implement the RandomAccess interface and is large, this method
        will do an iterator-based binary search that performs O(n) link
        traversals and O(log n) element comparisons.
        *****

        Translated: Search the list alist (already sorted in increasing order)
        for the key. If found, return the index of the *first* list item equal
        to the key (note this is different from the undefined result for this
        case in the Java version of this method). If the key is not found in
        the list, determine the index where the key should be inserted to
        maintain increasing list order, and return the negative of that index,
        minus 1 (negative results indicate the need to insert).

        NOTE: This method will only work reliably for a list of integers, or
        other objects that can be compared exactly. It will not work reliably
        for a list of floats, due to finite-precision equality checks.
        """

        # If the key is in the array, return the index of its first appearance.
        try:
            pos = alist.index(key)
            return pos
        except ValueError as e:
            pass # Key not found in list, so look for insertion point.

        # The insertion point is the index of the first element in the sorted
        # list that is greater than the key. This means:

        # * None of the list elements are equal to the key.
        # * If the key is less than the first (least) element of the list, the
        #   insertion_point is 0.
        # * If the key falls between two list elements at indices i and i+1,
        #   insertion_point is i+1.
        # * If the key is greater than the last (greatest) element of the list,
        #   insertion_point is len(alist).

        # For a list with n ordered elements, the possible values of
        # insertion_point are:
        # 0, 1, ..., len(alist)
        # Thus the possible return values at this point are:
        # -len(alist)-1, -len(alist), ..., -1
        insertion_point = bisect.bisect_left(alist, key)
        return -insertion_point - 1
