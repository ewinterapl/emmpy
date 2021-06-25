"""A 3-D vector in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.tensors.vector2d import Vector2D
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    computeNorm
)
from emmpy.utilities.isrealnumber import isRealNumber


# Map vector component names to indices.
components = {'i': 0, 'j': 1}


class VectorIJ(Vector2D):
    """A 2-D vector in Cartesian (i, j, k) coordinates.
    """

    def __new__(cls, *args, **kargs):
        """Create a new VectorIJ object.

        Allocate a new VectorIJ object by allocating a new Vector2D
        object on which the VectorIJ will expand.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic constructor.
        kargs : dict of str->object pairs
            Keyword arguments for polymorphic method.
        ij : list or tuple of float
            Values for (i, j) coordinates.
        OR
        vector : VectorIJ
            Existing vector to copy.
        OR
        offset : int
            Offset into data for assignment to vector elements.
        data : list of >=2 float
            Values to use for vector elements, starting at offset.
        OR
        scale : float
            Scale factor for vector to copy.
        vector : VectorIJ
            Existing vector to copy and scale.
        OR
        i, j : float
            Values for vector elements.

        Returns
        -------
        v : VectorIJ
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None, None)
            v = Vector2D.__new__(cls, *data, **kargs)
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                # List or tuple of 3 values for the components.
                (ij,) = args
                v = Vector2D.__new__(cls, *ij, **kargs)
            elif isinstance(args[0], VectorIJ):
                # Copy an existing VectorIJ.
                (vector,) = args
                v = Vector2D.__new__(cls, *vector, **kargs)
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], (list, tuple)):
                # Offset and list or tuple of >= (2 + offset + 1) values.
                (offset, data) = args
                v = Vector2D.__new__(cls, data[offset], data[offset + 1],
                                     **kargs)
            elif (isRealNumber(args[0]) and isinstance(args[1], VectorIJ)):
                # Scale factor and VectorIJ to scale.
                (scale, vector) = args
                v = Vector2D.__new__(cls, scale*vector.i, scale*vector.j, **kargs)
            else:
                # Scalar values (2) for the components.
                (i, j) = args
                v = Vector2D.__new__(cls, i, j, **kargs)
        else:
            raise ValueError('Bad arguments for constructor!')
        return v

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
