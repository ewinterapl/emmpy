"""Generic class for 2-dimensional vectors.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectors.vector import Vector


class Vector2D(Vector):
    """Generic class for 2-dimensional vectors.

    This class implements a generic 2-dimensional vector. No coordinate
    system information is assumed.
    """

    def __new__(cls, *args):
        """Create a new Vector2D object.

        Allocate a new Vector2D object by allocating a new Vector object
        on which the Vector2D will expand.

        Parameters
        ----------
        args : Tuple of 2 floats
            First and second vector elements.

        Returns
        -------
        v : Vector2D
            The newly-created object.

        Raises
        ------
        ValueError
            If other than 2 arguments are provided.
        """
        if len(args) != 2:
            raise ValueError('Exactly 2 numeric arguments are required!')
        v = Vector.__new__(cls, shape=(2,))
        v[0] = args[0]
        v[1] = args[1]
        return v
