"""Abstract base class for n-dimensional floating-point vectors.

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

    This abstract class should not be instantiated directly. Doing so will
    usually raise an Exception of some type.

    This class is derived from the numpy.ndarray class, to allow a single
    entry point for Numpy code to be used in the vector classes.
    Therefore, if we decide to use a new representation for vectors
    (other than numpy), fewer classes will need to be changed. This
    approach also allows all of the numpy.ndarray methods to be available
    to subclasses of Vector.
    """

    def __new__(cls, length, *args, **kwargs):
        """Allocate a new Vector object.

        Allocate a new Vector object by allocating a new np.ndarray on
        which the Vector will expand.

        The initial contents of the Vector are undefined.

        Parameters
        ----------
        length : integer
            Number of elements in vector.
        args : tuple of object, optional
            Additional positional arguments to pass to inherited methods.
        kwargs : dictionary of str: object, optional
            Additional keyword arguments to pass to inherited methods.

        Returns
        -------
        v : Vector
            The newly-created object.
        """
        v = super().__new__(cls, shape=(length,), dtype=float)
        return v

    def __init__(self, *args, **kargs):
        """Initialize a new Vector object.

        Initialize a new Vector object.

        Parameters
        ----------
        data : array-like, optional, default None.
            Values for vector elements.
        OR
        *data : array-like of float, optional.
            Values for vector elements.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = None
        elif len(args) == 1:
            (data,) = args
        else:
            data = args
        self[:] = data
