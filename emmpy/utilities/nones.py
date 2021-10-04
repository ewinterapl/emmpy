"""Return a nested list full of None.

The nones() function creates a nested list with the specified shape, and
fills it with the value None.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


def nones(shape):
    """Create a nested list filled with None.

    Create a nested list with the specified shape, and fill it with None.
    Construction of the nested list is done by recursive invocation of
    this function.

    Parameters
    ----------
    shape : list of int
        The size of each dimension in the nested list.

    Returns
    -------
    noneList : list
        Return a nested list of None, with the specified shape.
    """
    noneList = [None]*shape[0]
    if len(shape) > 1:
        for n in range(shape[0]):
            noneList[n] = nones(shape[1:])
    return noneList
