"""A 1-D array of expansion values.

A 1-D array of expansion values.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.cartesianvector import CartesianVector


class ArrayExpansion1D(list):
    """A 1-D array of expansion values.

    A 1-D array of expansion values.

    Attributes
    ----------
    array : array-like of float
        Expansion values.
    """

    def __init__(self, array):
        """Initialize a new ArrayEpansion1D object.

        Initialize a new ArrayEpansion1D object.

        Parameters
        ----------
        array : list of float
            Expansion values.
        """
        self[:] = array[:]

    @staticmethod
    def add(a, b):
        """Add 2 1-D expansions.

        Add 2 1-D expansions.

        Parameters
        ----------
        a, b : ArrayExpansion1D
            Expansions to add.

        Returns
        -------
        ae1d : ArrayExpansion1D
            An expansion that is the sum of a and b.
        """
        array = []
        for i in range(len(a)):
            array.append(CartesianVector(a[i] + b[i]))
        ae1d = ArrayExpansion1D(array)

        return ae1d
