"""A 2-D array of scalar expansion components.

A 2-D array of scalar expansion components. The index of the first valid
row (iLowerBoundIndex) and the first valid column (jLowerBoundIndex) are
not required to be 0. The stored array is padded with unused rows before
the first valid row, and unused elements at the head of each column. This
allows the non-0-based indexing to work directly, at the expense of some
unused memory. This approach is faster than indexing with offsets at
each access, and allows the expansion to be used as a numpy array directly
using slicing, e.g. expansion[iJlowerBoundIndex:, jLowerBoundIndex:.]

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class ScalarExpansion2D(np.ndarray):
    """A 2-D array of scalar expansion components.

A 2-D array of scalar expansion components. The index of the first valid
row (iLowerBoundIndex) and the first valid column (jLowerBoundIndex) are
not required to be 0. The stored array is padded with unused rows before
the first valid row, and unused elements at the head of each column. This
allows the non-0-based indexing to work directly, at the expense of some
unused memory. This approach is faster than indexing with offsets at
each access, and allows the expansion to be used as a numpy array directly
using slicing, e.g. expansion[iJlowerBoundIndex:, jLowerBoundIndex:.]

    valid_components = expansion[iLowerBoundIndex:, jLowerBoundIndex:]

    Attributes
    ----------
    iLowerBoundIndex : int
        Index of first valid row.
    iUpperBoundIndex : int
        Index of last valid row.
    jLowerBoundIndex : int
        Index of first valid column.
    jUpperBoundIndex : int
        Index of last valid column.
    """

    def __new__(cls, data, iLowerBoundIndex, jLowerBoundIndex):
        """Allocate a new ScalarExpansion2D object.

        Allocate a new ScalarExpansion2D object by allocating a new
        np.ndarray object on which this class will expand. Extra, unused
        rows are padded at the head of the array, and extra unused
        elements are padded at the start of each row. This allows
        non-0-based indexing in each dimensions.

        Parameters
        ----------
        data : array-like of float
            2-D array of scalar expansion components.
        iLowerBoundIndex : int
            Index of first valid row.
        jLowerBoundIndex : int
            Index of first valid column.

        Returns
        -------
        se2d : ScalarExpansion2D
            The newly-allocated object.
        """
        n_rows = len(data) + iLowerBoundIndex
        n_cols = len(data[0]) + jLowerBoundIndex
        se2d = super().__new__(cls, shape=(n_rows, n_cols))
        return se2d

    def __init__(self, data, iLowerBoundIndex, jLowerBoundIndex):
        """Initialize a new ScalarExpansion2D object.

        Initialize a new ScalarExpansion2D object. Note that the padding
        rows at the start of the array (equal to iLowerBoundIndex rows),
        and the padding elements at the start of each row (equal to
        jLowerBoundIndex elements per row), are ignored.

        Parameters
        ----------
        data : array-like of float
            2-D array of scalar expansion components.
        iLowerBoundIndex : int
            Index of first valid row.
        jLowerBoundIndex : int
            Index of first valid column.
        """
        self[iLowerBoundIndex:, jLowerBoundIndex:] = np.array(data)
        self.iLowerBoundIndex = iLowerBoundIndex
        self.iUpperBoundIndex = iLowerBoundIndex + len(data) - 1
        self.jLowerBoundIndex = jLowerBoundIndex
        self.jUpperBoundIndex = jLowerBoundIndex + len(data[0]) - 1
