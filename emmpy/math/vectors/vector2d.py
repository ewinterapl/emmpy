"""Generic class for 2-dimensional vectors.

Note that we use __new__ in addition to __init__ to enforce the 2-element
size of the vector.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector import Vector


# Number of elements in a 2-D vector.
N = 2


class Vector2D(Vector):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed.
    """

    def __new__(cls, *args, **kargs):
        """Allocate a new Vector2D object.

        Allocate a new Vector2D object by allocating a new 2-element
        Vector object on which the Vector2D will expand.

        The initial contents of the Vector are undefined.

        Returns
        -------
        v : Vector2D
            The newly-created object.
        """
        v = super().__new__(cls, length=N)
        return v

    def __init__(self, *args, **kargs):
        """Initialize a new Vector2D object.

        Initialize a new Vector2D object.

        Parameters
        ----------
        data : array-like, optional, default (None)*2.
            Values for 1st and 2nd elements.
        OR
        data[0], data[1] : float, optional.
            Values for 1st and 2nd elements.

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
