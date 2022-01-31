"""A 2-D array of expansion values.

A 2-D array of expansion values.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.utilities.nones import nones


class ArrayExpansion2D(Expansion2D):
    """A 2-D array of expansion values.
    
    A 2-D array of expansion values.

    Attributes
    ----------
    data : 2-D list of float
        Expansion values.
    lastAzimuthalExpansionNumber : int
        Last index of expansion values in 1st dimension.
    lastRadialExpansionNumber : int
        Last index of expansion values in 2nd dimension.
    """

    def __init__(self, data):
        """Initialize a new ArrayExpansion2D object.

        Initialize a new ArrayExpansion2D object.

        Parameters
        ----------
        data : 2-D list of float
            Expansion values.
        """
        self.data = data
        self.lastAzimuthalExpansionNumber = len(data) - 1
        self.lastRadialExpansionNumber = len(data[0]) - 1

    @staticmethod
    def add(a, b):
        """Add two expansions using a wrapper object.

        Add two expansions using a wrapper object.

        Parameters
        ----------
        a, b : ArrayExpansion2D
            Expansions to add.

        Returns
        -------
        ae2d : ArrayExpansion2D
            Object for expansion sum.
        """
        numAzimuthalExpansions = len(a.data)
        numRadialExpansions = len(a.data[0])
        array = nones((numAzimuthalExpansions, numRadialExpansions))
        for i in range(numAzimuthalExpansions):
            for j in range(numRadialExpansions):
                array[i][j] = CartesianVector(
                    a.data[i][j] + b.data[i][j]
                )
        ae2d = ArrayExpansion2D(array)

        return ae2d
