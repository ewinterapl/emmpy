"""A 2-D vector in Cartesian (i, j) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    computeNorm
)
from emmpy.math.vectors.vector2d import Vector2D
from emmpy.utilities.isrealnumber import isRealNumber


# Map vector component names to indices.
components = {'i': 0, 'j': 1}


class VectorIJ(Vector2D):
    """A 2-D vector in Cartesian (i, j) coordinates."""

    def __init__(self, *args):
        """Initialize a new VectorIJ object.

        Initialize a new VectorIJ object.

        Parameters
        ----------
        iter : iterable of 2 float
            Values for (i, j) coordinates.
        OR
        offset : int
            Offset into data for assignment to vector elements.
        iterable : list of >=2 float
            Values to use for vector elements, starting at offset.
        OR
        scale : float
            Scale factor for components to copy.
        iter : Iterable of 2 float
            Existing vector to copy and scale.
        OR
        i, j : float
            Values for vector elements.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            self[:] = (None, None)
        elif len(args) == 1:
            # Iterable of 2 values for the components.
            (iter,) = args
            self[:] = list(iter)
        elif len(args) == 2:
            if isinstance(args[0], int) and not isRealNumber(args[1]):
                # Offset and iterable of >= (2 + offset + 1) values.
                (offset, iter) = args
                self[:] = list(iter[offset:offset + 2])
            elif isRealNumber(args[0]) and not isRealNumber(args[1]):
                # Scale factor and np.ndarray to scale.
                (scale, a) = args
                self[:] = scale*a
            else:
                # Scalar values (2) for the components.
                self[:] = args
        else:
            raise ValueError

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to get.

        Returns
        -------
        self[0|1] : float
            Value of specified attribute (i or j).
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of a computed attribute.

        Set the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        None
        """
        self[components[name]] = value
