"""A 2-D array for a coefficient expansion.

A 2-D array of scalar expansion components.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.utilities.nones import nones


class ArrayCoefficientExpansion2D(np.ndarray):
    """A 2-D array of expansion coefficients.
    
    A 2-D array of scalar expansion components.

    Attributes
    ----------
    None
    """

    def __new__(cls, data):
        """Allocate a new ArrayCoefficient2D object.

        Allocate a new ArrayCoefficient2D object by allocating a new
        np.ndarray on which ArrayCoefficient2D will expand.

        Parameters
        ----------
        data : 2-D array-like of float
            The array of expansion coefficients.

        Returns
        -------
        ace2d : ArrayCoefficientExpansion2D
            The newly-allocated object.
        """
        n_rows = len(data)
        n_cols = len(data[0])
        ace2d = super().__new__(cls, shape=(n_rows, n_cols), dtype=float)
        return ace2d

    def __init__(self,  data):
        """Initialize an ArrayCoefficientExpansion2D object.

        Initialize a ArrayCoefficient2D object.

        Parameters
        ----------
        data : 2-D array-like of float
            The array of expansion coefficients.
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
        negation : ArrayCoefficientExpansion2D
            A negated copy of this expansion.
        """
        negation = ArrayCoefficientExpansion2D(-self)
        return negation

    def scale(self, scale_factor):
        """Return a scaled copy of the expansion.

        Return a scaled copy of the expansion.

        Parameters
        ----------
        scale_factor : float
            Scale factor to apply to expansion.

        Returns
        -------
        scaled : ArrayCoefficientExpansion2D
            A scaled copy of this expansion.
        """
        scaled = ArrayCoefficientExpansion2D(scale_factor*self)
        return scaled

    @staticmethod
    def add(a, b):
        """Compute the sum of two expansions.

        Compute the sum of two expansions.

        Parameters
        ----------
        a, b : ArrayCoefficientExpansion2D
            Expansions to add.

        Returns
        -------
        sum : ArrayCoefficientExpansion2D
            Sum of the two expansions.
        """
        sum = ArrayCoefficientExpansion2D(a + b)
        return sum

    @staticmethod
    def createNullExpansion(n_rows, n_cols):
        """Create an expansion of null coefficients.

        Create an expansion of null coefficients using the specified shape.

        Parameters
        ----------
        n_rows, n_cols : int
            Numbers of rows and columns.

        Returns
        -------
        null : ArrayCoefficientExpansion2D
            An expansion with null coefficients.
        """
        data = np.empty((n_rows, n_cols))
        data[...] = np.nan
        null = ArrayCoefficientExpansion2D(data)
        return null

    @staticmethod
    def createUnity(n_rows, n_cols):
        """Create an expansion of unit coefficients.

        Create an expansion of unit coefficients using the specified shape.

        Parameters
        ----------
        n_rows, n_cols : int
            Numbers of rows and columns.

        Returns
        -------
        unity : ArrayCoefficientExpansion2D
            An expansion with unit coefficients.
        """
        data = np.ones((n_rows, n_cols))
        unity = ArrayCoefficientExpansion2D(data)
        return unity
