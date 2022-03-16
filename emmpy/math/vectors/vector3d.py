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

    def __new__(cls, *args, **kwargs):
        """Allocate a new Vector3D object.

        Allocate a new Vector3D object by allocating a new 3-element
        Vector object on which the Vector3D will expand.

        Parameters
        ----------
        args : tuple of object, optional
            Additional positional arguments to pass to inherited methods.
        kwargs : dictionary of str: object, optional
            Additional keyword arguments to pass to inherited methods.

        Returns
        -------
        v : Vector3D
            The newly-created object.
        """
        v = super().__new__(cls, length=N)
        return v
