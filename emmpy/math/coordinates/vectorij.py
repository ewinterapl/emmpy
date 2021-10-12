"""A 2-D vector in Cartesian (i, j) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.vectors.vector2d import Vector2D


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

        Parameters
        ----------
        name : str
            Name of attribute to set.
        value : float
            Value to assign to attribute.

        Returns
        -------
        None
        """
        self[components[name]] = value
