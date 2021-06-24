"""Generic class for 2-dimensional vectors.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.tensors.vector import Vector


class Vector2D(Vector):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed.

    This object may be directly used as a Numpy array.
    """

    def __new__(cls, *args):
        """Create a new Vector2D object.

        Allocate a new Vector2D object by allocating a new Vector object
        on which the Vector2D will expand.

        Parameters
        ----------
        args : tuple of 2 float (optional)
            First and second vector elements.

        Returns
        -------
        v : Vector2D
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None, None)
        elif len(args) == 2:
            data = args
        else:
            raise ValueError('Exactly 0 or 2 numeric arguments are required!')
        v = Vector.__new__(cls, shape=(2,))
        v[:] = data[:]
        return v
