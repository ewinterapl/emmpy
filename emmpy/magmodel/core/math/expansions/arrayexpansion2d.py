"""A 2-D array of expansion values.

A 2-D array of expansion values.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.utilities.nones import nones


class ArrayExpansion2D(list):
    """A 2-D array of expansion values.
    
    A 2-D array of expansion values.

    Attributes
    ----------
    data : 2-D list of object
        Expansion values. Can be float, or other objects such as VectorIJK
        or nested ArrayExpansion1D or ArrayExpansion2D objects.
    """

    def __init__(self, data):
        """Initialize a new ArrayExpansion2D object.

        Initialize a new ArrayExpansion2D object.

        Parameters
        ----------
        data : 2-D list of object
            Expansion values. Can be float, or other objects such as VectorIJK
            or nested ArrayExpansion1D or ArrayExpansion2D objects.
        """
        self[:] = data[:]

    @staticmethod
    def add(a, b):
        """Add two expansions of CartesianVectors.

        Add two expansions of CartesianVectors.

        Parameters
        ----------
        a, b : ArrayExpansion2D of CartesianVector
            Expansions to add.

        Returns
        -------
        ae2d : ArrayExpansion2D
            Object for expansion sum.
        """
        numAzimuthalExpansions = len(a)
        numRadialExpansions = len(a[0])
        array = nones((numAzimuthalExpansions, numRadialExpansions))
        for i in range(numAzimuthalExpansions):
            for j in range(numRadialExpansions):
                array[i][j] = CartesianVector(a[i][j] + b[i][j])
        ae2d = ArrayExpansion2D(array)

        return ae2d
