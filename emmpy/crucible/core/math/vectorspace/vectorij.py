"""A 2-D vector in Cartesian (i, j) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

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
        data : array-like of 2 float, optional, default (None, None)
            Values for (i, j) coordinates.
        OR
        offset : int
            Offset into array data for assignment to (i, j) coordinates.
        data : array-like of >=2 float
            Values to assign to (i, j) coordinates, starting at offset.
        OR
        scale : float
            Scale factor for components to copy.
        data : array-like of 2 float
            Existing array of values to copy and scale.
        OR
        i, j : float
            Values for vector elements.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            self[:] = np.array([None, None])
        elif len(args) == 1:
            # Array-like of 2 values for the components.
            (data,) = args
            self[:] = np.array(data)
        elif len(args) == 2:
            if isinstance(args[0], int) and not isRealNumber(args[1]):
                # Offset and array-like of >= (2 + offset + 1) values.
                (offset, data) = args
                self[:] = np.array(data)[offset:offset + 2]
            elif isRealNumber(args[0]) and not isRealNumber(args[1]):
                # Scale factor and array-like of 2 values to scale.
                (scale, data) = args
                self[:] = scale*np.array(data)
            else:
                # Scalar values (i, j) for the components.
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

    def scale(self, scale):
        """Scale the vector.

        Apply a scale factor to the vector.

        Parameters
        ----------
        scale : float
            Scale factor to apply.

        Returns
        -------
        self : VectorIJ
            The current object.
        """
        self[:] *= scale
        return self

    def unitize(self):
        """Unitize the vector.

        Normalize the vector to unit length.

        Parameters
        ----------
        None

        Returns
        -------
        self : VectorIJ
            The current vector, normalized to unit length.
        """
        length = np.linalg.norm(self)
        self[:] /= length
        return self

    def setTo(self, *args):
        """Set the vector components.

        Set the values of the vector components.

        Parameters
        ----------
        data : array-like of 2 float, optional, default (None, None)
            Values for (i, j) coordinates.
        OR
        offset : int
            Offset into array data for assignment to (i, j) coordinates.
        data : array-like of >=2 float
            Values to assign to (i, j) coordinates, starting at offset.
        OR
        scale : float
            Scale factor for components to copy.
        data : array-like of 2 float
            Existing array of values to copy and scale.
        OR
        i, j : float
            Values for vector elements.

        Returns
        -------
        self : VectorIJ
            The current object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            # Array-like of 2 float.
            (data,) = args
            self[:] = data
        elif len(args) == 2:
            if isinstance(args[0], int) and not isRealNumber(args[1]):
                # Set by offset into array.
                (offset, data) = args
                self[:] = np.array(data)[offset:offset + 2]
            elif isRealNumber(args[0]) and not isRealNumber(args[1]):
                # Set by scaling an existing vector.
                (scale, data) = args
                self[:] = scale*np.array(data)
            elif isRealNumber(args[0]) and isRealNumber(args[1]):
                # Explicit component values.
                (i, j) = args
                self[:] = (i, j)
        else:
            raise TypeError
        return self


# The ZERO vector.
ZERO = VectorIJ(0, 0)

# The I basis vector: (1,0).
I = VectorIJ(1, 0)

# The J basis vector: (0,1).
J = VectorIJ(0, 1)

# The negative of the I basis vector: (-1,0).
MINUS_I = VectorIJ(-1, 0)

# The negative of the J basis vector: (0,-1).
MINUS_J = VectorIJ(0, -1)
