"""Generic class for 3-dimensional vectors.

Note that we use __new__ in addition to __init__ to enforce the 3-element
size of the vector.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector import Vector


# Number of elements in a 3-D vector.
N = 3


class Vector3D(Vector):
    """Generic class for 3-dimensional vectors.

    This class implements a generic 3-dimensional vector. No coordinate
    system information is assumed.
    """

    def __new__(cls, *args, **kargs):
        """Allocate a new Vector3D object.

        Allocate a new Vector3D object by allocating a new 3-element
        Vector object on which the Vector3D will expand.

        Returns
        -------
        v : Vector3D
            The newly-created object.
        """
        v = super().__new__(cls, length=N)
        return v

    def __init__(self, *args, **kargs):
        """Initialize a new Vector3D object.

        Initialize a new Vector3D object.

        Parameters
        ----------
        data : array-like, optional, default (None)*3.
            Values for 1st, 2nd, and 3rd elements.
        OR
        data[0], data[1], data[2] : float, optional.
            Values for 1st, 2nd, and 3rd elements.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None,)*N
        elif len(args) == 1:
            (data,) = args
        elif len(args) == N:
            data = args
        else:
            raise ValueError
        self[:] = data
