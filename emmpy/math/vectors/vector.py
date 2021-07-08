"""Abstract base class for n-dimensional vectors.

Note that we use __new__ in addition to __init__ to enforce the specified
size of the vector.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np


class Vector(np.ndarray):
    """Abstract base class for n-dimensional vectors.

    This class is the base class for all vector classes in all
    coordinate systems.

    This abstract class must not be instantiated directly. Doing so will
    usually raise an Exception of some type.

    This class is derived from the numpy.ndarray class, to allow a single
    entry point for Numpy code to be used in the vector classes.
    Therefore, if we decide to use a new representation for vectors
    (other than numpy), fewer classes will need to be changed. This
    approach also allows all of the numpy.ndarray methods to be available
    to subclasses of Vector.
    """

    def __new__(cls, length, *args, **kargs):
        """Create a new Vector object.

        Allocate a new Vector object by allocating a new ndarray on which
        the Vector will expand.

        Note that this method should only be called from the __new__()
        method of subclasses.

        The initial contents of the Vector are nan.

        Parameters
        ----------
        length : integer
            Number of elements in vector.

        Returns
        -------
        v : Vector
            The newly-created object.
        """
        v = super().__new__(cls, shape=(length,), dtype=float)
        v[:] = np.nan  # This works if dtype is float, but not if int.
        return v
