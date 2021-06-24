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
    """

    def __new__(cls, *args):
        """Create a new Vector3D object.

        Allocate a new Vector3D object by allocating a new Vector object
        on which the Vector3D will expand.

        Parameters
        ----------
        args : Tuple of 3 floats
            First, second, and third vector elements.

        Returns
        -------
        v : Vector3D
            The newly-created object.

        Raises
        ------
        ValueError
            If other than 3 arguments are provided.
        """
        if len(args) == 0:
            data = (None, None, None)
        elif len(args) == 3:
            data = args
        else:
            raise ValueError('Exactly 0 or 3 numeric arguments are required!')
        v = Vector.__new__(cls, shape=(3,))
        v[:] = data[:]
        return v
