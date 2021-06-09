"""The nones() function creates nested lists of None."""


def fillWithNones(shape):
    """Recursively fill a nested list with None.

    param shape - Iterable containing the size of each dimension.
    return noneList - Nested list with shape, filled with None.
    """
    # print("Starting fillWithNones().")
    noneList = [None]*shape[0]
    if len(shape) > 1:
        # print("shape = ", shape)
        for n in range(shape[0]):
            noneList[n] = fillWithNones(shape[1:])
    # print("Returning %s" % noneList)
    return noneList


def nones(shape):
    """Create a nested list of the specified shape, all None.
    
    shape is an iterable of containing the size of each dimension.
    Return a nested list of None, with the specified shape.
    """
    noneList = fillWithNones(shape)
    return noneList
