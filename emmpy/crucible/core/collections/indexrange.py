"""Author : vandejd1 Created : Apr 19, 2010

Copyright (C) 2010 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved
"""


class IndexRange:
    """captures a range of indices specified by a low index and a high index;
    both end points are considered to be included in the range

    NOTES for future development: If you want to add methods, look at the
    crucible.math.intervals package and make sure that any method names you
    use are consistent with the (non-integer) interval processing class there.
    After discussion, we decided that its probably easier to duplicate code
    for the integer interval mechanisms (if we ever need it) rather than try
    to come up with a convoluted framework for handling (unwritable and
    writable) intervals of multiple types.

    If you want to make this class writable: create a new parent class that is
    unwritable: UnwritableIndexRange, and then move the getter methods there.
    Then this class becomes the writable versions and you can add the setters
    here.

    This class is one instance of a larger concept - that of index mapping or
    index translation (as in sub-setting, or selecting a sub-range). There is
    already a class in the timeseries library that will eventually be moved
    into crucible that this class will eventually implement: IIndexTranslator.

    @author vandejd1
    """

    def __init__(self, lowIndexInclusive: int, highIndexInclusive: int):
        self.__lowIndex = lowIndexInclusive
        self.__highIndex = highIndexInclusive

    def getLowIndex(self) -> int:
        """Return the lower index in the range; this index value is included
        in the range"""
        return self.__lowIndex

    def getHighIndex(self) -> int:
        """Return the upper index in the range; this index is included in the
        range"""
        return self.__highIndex

    def getNumIndicesIncluded(self) -> int:
        """Return the total number of indices in the range, including the
        lower and upper endpoints"""
        return self.__highIndex - self.__lowIndex + 1

    def contains(self, idx: int) -> bool:
        """Returns true if the given index is inside this range, i.e., if
        {@code lowIndex <= idx <= highIndex}

        @param idx the index to test

        @return true if contained in the range
        """
        return idx >= self.__lowIndex and idx <= self.__highIndex

    def hashCode(self) -> int:
        prime = 31
        result = 1
        result = prime*result + self.__highIndex
        result = prime*result + self.__lowIndex
        return result

    def equals(self, obj) -> bool:
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.__highIndex != other.__highIndex:
            return False
        if self.__lowIndex != other.__lowIndex:
            return False
        return True

    def toString(self) -> str:
        return "IndexRange [lowIndex=%d, highIndex=%d]" % (self.__lowIndex,
                                                           self.__highIndex)
