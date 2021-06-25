"""Generic class for 3-dimensional vectors.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.tensors.vector import Vector


class Vector3D(Vector):
    """Generic class for 3-dimensional vectors.

    This class implements a generic 3-dimensional vector. No coordinate
    system information is assumed.

    This object may be directly used as a Numpy array.
    """

    def __new__(cls, *args, **kargs):
        """Create a new Vector3D object.

        Allocate a new Vector3D object by allocating a new Vector object
        on which the Vector3D will expand.

        Parameters
        ----------
        args : tuple of 3 float (optional)
            First, second, and third vector elements.
        kargs : dict of str->object pairs
            Keyword arguments for polymorphic method.

        Returns
        -------
        v : Vector3D
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None, None, None)
        elif len(args) == 3:
            data = args
        else:
            raise ValueError('Exactly 0 or 3 numeric arguments are required!')
        v = Vector.__new__(cls, shape=(3,), **kargs)
        v[:] = data[:]
        return v
