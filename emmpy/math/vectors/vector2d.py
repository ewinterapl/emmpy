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

    def __new__(cls, *args, **kwargs):
        """Allocate a new Vector2D object.

        Allocate a new Vector2D object by allocating a new 2-element
        Vector object on which the Vector2D will expand.

        The initial contents of the Vector are undefined.

        Parameters
        ----------
        args : tuple of object, optional
            Additional positional arguments to pass to inherited methods.
        kwargs : dictionary of str: object, optional
            Additional keyword arguments to pass to inherited methods.

        Returns
        -------
        v : Vector2D
            The newly-created object.
        """
        v = super().__new__(cls, length=N)
        return v
