"""Abstract base class for n-dimensional vectors.

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

    def __new__(cls, *args, **kargs):
        """Create a new Vector object.

        Allocate a new Vector object by allocating a new ndarray on which
        the Vector will expand.

        Note that this method should only be called from the __new__()
        method of subclasses.

        Parameters
        ----------
        args : tuple of object
            Positional arguments for polymorphic method.
        kargs : dict of str->object pairs
            Keyword arguments for polymorphic method.

        Returns
        -------
        v : Vector
            The newly-created object.
        """
        v = np.ndarray.__new__(cls, *args, **kargs)
        return v
