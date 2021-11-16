"""A 2-D array of scalar expansion components.

A 2-D array of scalar expansion components. This is just a lightweight
extension of a 2-D np.ndarray.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.utilities.nones import nones


class ScalarExpansion2D(np.ndarray):
    """A 2-D array of scalar expansion components.

    This class represents a 2-D expansion of scalars. This class can be
    used directly as an np.ndarray.

    Attributes
    ----------
    None
    """

    def __new__(cls, data):
        """Allocate a new ScalarExpansion2D object.

        Allocate a new ScalarExpansion2D object by allocating a new
        np.ndarray object on which this class will expand.

        Parameters
        ----------
        data : array-like of float
            2-D array of scalar expansion components.

        Returns
        -------
        se2d : ScalarExpansion2D
            The newly-allocated object.
        """
        se2d = super().__new__(cls, shape=(len(data), len(data[0])))
        return se2d

    def __init__(self, data):
        """Initialize a new ScalarExpansion2D object.

        Initialize a new ScalarExpansion2D object.

        Parameters
        ----------
        data : array-like of float
            2-D array of scalar expansion components.
        """
        self[...] = data

    def negate(self):
        """Return a negated copy of the expansion.

        Return a negated copy of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        negation : ScalarExpansion2D
            A negated copy of this expansion.
        """
        negation = ScalarExpansion2D(-self)
        return negation

    def scale(self, scaleFactor):
        """Create a scaled copy of the expansion.

        Create a scaled copy of the expansion.

        Parameters
        ----------
        scaleFactor : float
            Scale factor to apply to expansion.

        Returns
        -------
        scaled : ScalarExpansion2D
            A scaled copy of the expansion.
        """
        scaled = ScalarExpansion2D(scaleFactor*self)
        return scaled

    @staticmethod
    def add(a, b):
        """Compute the sum of two expansions.

        Compute the sum of two expansions. The expansions are assumed to have
        the same shape.

        Parameters
        ----------
        a, b : ScalarExpansion2D
            Expansions to add.

        Returns
        -------
        exp_sum : ScalarExpansion2D
            Sum of the two expansions.
        """
        data = a + b
        expansionSum = ScalarExpansion2D(a + b)
        return expansionSum

    @staticmethod
    def createNullExpansion(n_rows, n_cols):
        """Create an expansion of null coefficients.

        Create an expansion of null coefficients using the specified shape.

        Parameters
        ----------
        n_rows, n_cols : int
            Counts for rows and columns.

        Returns
        -------
        null : ScalarExpansion2D
            An expansion with null coefficients.
        """
        nulls = nones((n_rows, n_cols))
        data = np.array(nulls)
        null = ScalarExpansion2D(data)
        return null

    @staticmethod
    def createUnity(n_rows, n_cols):
        """Create an expansion of unit coefficients.

        Create an expansion of unit coefficients using the specified shape.

        Parameters
        ----------
        n_rows, n_cols : int
            Counts for rows and columns.

        Returns
        -------
        unity : ScalarExpansion2D
            An expansion with unit coefficients.
        """
        ones = np.ones((n_rows, n_cols))
        data = np.array(ones)
        unity = ScalarExpansion2D(data)
        return unity
