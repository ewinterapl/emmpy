"""A 3-D vector in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'i': 0, 'j': 1, 'k': 2}


class VectorIJK(Vector3D):
    """A 3-D vector in Cartesian (i, j, k) coordinates."""

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
        self[0|1|2] : float
            Value of specified attribute (i, j, or k).
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


# The I basis vector: (1,0,0).
I = VectorIJK(1, 0, 0)

# The J basis vector: (0,1,0).
J = VectorIJK(0, 1, 0)

# The K basis vector: (0,0,1).
K = VectorIJK(0, 0, 1)


def rotate(vector, axis, angle):
    """Rotate a copy of a vector.

    Make a copy of the vector, and rotate the copy by the specified
    angle around the specified axis vector.

    Parameters
    ----------
    vector : VectorIJK
        Vector to rotate
    axis : VectorIJK
        Veector defining the rotation axis.
    angle : float
        Rotation angle (radians).
    buffer : VectorIJK (optional)
        Buffer to receive the rotated vector.

    Returns
    -------
    v : VectorIJK
        A rotated copy of the original vector.

    Raises
    ------
    ValueError
        If incorrect arguments are provided.

    Notes
    -----
    An example is perhaps the most straightforward means to explain
    computation. Given an axis (0,0,1) and a rotation angle of pi/2,
    this method does the following:

        vector         buffer
    ( 1, 2, 3 )   ( -2, 1, 3 )
    ( 1, 0, 0 )   ( 0, 1, 0 )
    ( 0, 1, 0 )   ( -1, 0, 0 )
    """
    buffer = VectorIJK()

    # Rotate one vector about another by a specified angle.

    # There is one exceptional case, namely if we try to rotate
    # about the zero vector. We can check this by using the project
    # method, as it will throw the desired runtime exception. First
    # cache the contents of vector and axis as input, since we do
    # not know if buffer is equivalent to either of them.
    v = np.array(vector)
    a = np.array(axis)

    # At this point, we are going to build a basis that is
    # convenient for computing the rotated vector. Start by
    # projecting vector onto axis, one of the axes in our basis.
    buffer[:] = project(vector, axis)

    # Normalize the rotation axis.
    norm = np.linalg.norm(a)
    a /= norm

    # Store the contents of buffer as this is one of the
    # components of our rotated vector in the new basis.
    p = np.array(buffer)

    # To determine one of the other vectors in the basis, simply
    # subtract buffer from vector.
    v -= buffer

    # Now determine the third basis vector by computing the cross
    # product of a unit vector in the direction of axis with
    # buffer.
    buffer[:] = np.cross(a, v)

    # The desired vector projection against this new basis is:
    # {pi,pj,pk} + cos(theta)*{v1i,v1j,v1k} + sin(theta)*buffer
    buffer[:] = p + cos(angle)*v + sin(angle)*buffer
    v = buffer
    return v


def project(vector, onto):
    """Compute the projection of one vector onto another.

    Compute the projection of the vector onto another.

    Parameters
    ----------
    vector : VectorIJK
        The vector to project.
    onto : VectorIJK
        The vector onto which the first vector will be projected.

    Returns
    -------
    v : VectorIJK
        The projected vector.

    Notes
    -----
    Algebraically, this routine effectively computes:

    <vector, onto> * onto
    ---------------------
         || onto ||

    where <> denotes the standard scalar product and ||x|| the norm of x.
    For numeric precision reasons the implementation may vary slightly
    from the above prescription.
    """
    projection = vector.dot(onto)/onto.dot(onto)*onto
    return VectorIJK(projection)
