"""A 3-D vector in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent
)
from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'i': 0, 'j': 1, 'k': 2}


class VectorIJK(Vector3D):
    """A 3-D vector in Cartesian (i, j, k) coordinates."""

    def __init__(self, *args):
        """Initialize a new VectorIJK object.

        Initialize a new VectorIJK object.

        Parameters
        ----------
        data : array-like of 3 float, optional, default (None, None, None)
            Values for (i, j, k) coordinates.
        OR
        scale : float
            Scale factor for components to copy.
        data : array-like of 3 float
            Vector components to copy and scale.
        OR
        i, j, k : float
            Values for vector elements.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            self[:] = np.array([None, None, None])
        elif len(args) == 1:
            # Array-like of 3 floats for the components.
            (data,) = args
            self[:] = list(data)
        elif len(args) == 2:
            # Scale factor and array-like of 3 float to scale.
            (scale, data) = args
            self[:] = scale*np.array(data)
        elif len(args) == 3:
            # Scalar values (3) for the components.
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

    def __add__(self, v):
        """Add this vector to another value.
        
        Add this vector to another value, and return a new vector.

        Parameters
        ----------
        v : 3-element np.ndarray
            Values to add to current vector elements.
        
        Returns
        -------
        vsum : VectorIJK
            Sum of both arguments.
        """
        sum = np.ndarray.__add__(self, v)
        vsum = VectorIJK(sum)
        return vsum

    def scale(self, _scale):
        """Scale the vector in-place.

        Scale the vector in-place.

        Parameters
        ----------
        _scale : float
            Scale factor to apply.

        Returns
        -------
        self : VectorIJK
            The current object.
        """
        self[:] *= _scale
        return self

    def unitize(self):
        """Unitize the vector in-place.

        Normalize the vector to unit length in-place.

        Parameters
        ----------
        None

        Returns
        -------
        self : VectorIJK
            The current object.
        """
        length = np.linalg.norm(self)
        self[:] /= length
        return self

    def negate(self):
        """Negate the vector in-place.

        Negate the vector in-place.

        Parameters
        ----------
        None

        Returns
        -------
        self : VectorIJK
            The current object.
        """
        self[:] = -self
        return self

    def createScaled(self, scale):
        """Create a scaled copy of the vector.

        Create a scaled copy of the vector.

        Parameters
        ----------
        scale : float
            Scale factor to apply to the copy.

        Returns
        -------
        v : VectorIJK
            A scaled copy of the current vector.
        """
        v = VectorIJK(scale, self)
        return v

    def setTo(self, *args):
        """Set the vector contents.

        Set the values of all components.

        Parameters
        ----------
        data : array-like of 3 float
            Values to copy to current vector.
        OR
        i, j, k : float
            i, j, k vector components.

        Returns
        -------
        self : VectorIJK
            The current object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            # Copy the components from an array.
            (data,) = args
            self[:] = list(data)
        elif len(args) == 3:
            # Sets the three components of the vector.
            self[:] = args
        else:
            raise ValueError
        return self

    @staticmethod
    def rotate(*args):
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
        if len(args) == 3:
            # Create the buffer, then rotate the vector.
            (vector, axis, angle) = args
            buffer = VectorIJK()
        elif len(args) == 4:
            (vector, axis, angle, buffer) = args
        else:
            raise ValueError

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
        VectorIJK.project(vector, axis, buffer)

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

    @staticmethod
    def project(*args):
        """Compute the projection of one vector onto another.

        Compute the projection of the vector onto another.

        Parameters
        ----------
        vector : VectorIJK
            The vector to project.
        onto : VectorIJK
            The vector onto which the first vector will be projected.
        buffer : VectorIJK (optional)
            Buffer to receive the projected vector.

        Returns
        -------
        buffer : VectorIJK
            The projected vector.

        Raises
        ------
        BugException
            If the rotation axis is zero.
        ValueError:
            If incorrect arguments are provided.

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
        if len(args) == 2:
            # Create a buffer, then perform the projection.
            (vector, onto) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (vector, onto, buffer) = args
        else:
            raise ValueError

        # Scale and project the vector.
        maxVector = absMaxComponent(*vector)
        maxOnto = absMaxComponent(*onto)
        if maxOnto == 0:
            raise BugException("Unable to project vector onto zero vector.")

        # If the vector to project is 0, so is the projection.
        if maxVector == 0:
            buffer[:] = (0, 0, 0)
        else:
            r = onto/maxOnto
            t = vector/maxVector
            scaleFactor = sum(t*r)*maxVector/sum(r*r)
            buffer[:] = r
            buffer.scale(scaleFactor)
        return buffer


# The I basis vector: (1,0,0).
I = VectorIJK(1, 0, 0)

# The J basis vector: (0,1,0).
J = VectorIJK(0, 1, 0)

# The K basis vector: (0,0,1).
K = VectorIJK(0, 0, 1)
