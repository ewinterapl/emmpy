"""A 3-D vector in Cartesian (i, j, k) coordinates.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.tensors.vector3d import Vector3D
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    computeNorm
)
from emmpy.utilities.isrealnumber import isRealNumber


# Map vector component names to indices.
components = {'i': 0, 'j': 1, 'k': 2}


class VectorIJK(Vector3D):
    """A 3-D vector in Cartesian (i, j, k) coordinates.
    """

    def __new__(cls, *args, **kargs):
        """Create a new VectorIJK object.

        Allocate a new VectorIJK object by allocating a new Vector3D
        object on which the VectorIJK will expand.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic constructor.
        kargs : dict of str->object pairs
            Keyword arguments for polymorphic method.
        ijk : list or tuple of float
            Values for (i, j, k) coordinates.
        OR
        vector : VectorIJK
            Existing vector to copy.
        OR
        offset : int
            Offset into data for assignment to vector elements.
        data : list of >=3 float
            Values to use for vector elements, starting at offset.
        OR
        scale : float
            Scale factor for vector to copy.
        vector : VectorIJK
            Existing vector to copy and scale.
        OR
        i, j, k : float
            Values for vector elements.

        Returns
        -------
        v : VectorIJK
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None, None, None)
            v = Vector3D.__new__(cls, *data, **kargs)
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                # List or tuple of 3 values for the components.
                (ijk,) = args
                v = Vector3D.__new__(cls, *ijk, **kargs)
            elif isinstance(args[0], VectorIJK):
                # Copy an existing UnwritableVectorIJK.
                (vector,) = args
                v = Vector3D.__new__(cls, *vector, **kargs)
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], (list, tuple)):
                # Offset and list or tuple of >= (3 + offset + 1) values.
                (offset, data) = args
                v = Vector3D.__new__(cls, data[offset], data[offset + 1],
                                     data[offset + 2], **kargs)
            elif (isRealNumber(args[0]) and
                  isinstance(args[1], VectorIJK)):
                # Scale factor and UnwritableVectorIJK to scale.
                (scale, vector) = args
                v = Vector3D.__new__(cls, scale*vector.i, scale*vector.j,
                                     scale*vector.k, **kargs)
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 3:
            # Scalar values (3) for the components.
            (i, j, k) = args
            v = Vector3D.__new__(cls, i, j, k, **kargs)
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
        self[0|1|2] : float
            Value of specified attribute (i, j, or k).
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

    def createUnitized(self):
        """Create a unitized copy of the vector.

        Create a copy of the vector normalized to unit lenggth.

        Returns
        -------
        v : VectorIJK
            A unitized copy of the current vector.
        """
        length = self.getLength()
        v = VectorIJK(1/length, self)
        return v

    def createNegated(self):
        """Create a negated copy of the vector.

        Create a negated copy of the vector.

        Returns
        -------
        v : VectorIJK
            A negated copy of the current vector.
        """
        v = VectorIJK(-self.i, -self.j, -self.k)
        return v

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
            The current object (for convenience).
        """
        self[:] *= _scale
        return self

    def unitize(self):
        """Unitize the vector in-place.

        Normalize the vector to unit length in-place.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).

        Raises
        ------
        BugException
            If the vector is 0.
        """
        norm = computeNorm(*self)
        if norm == 0:
            raise BugException("Unable to unitize zero-length vector.")
        self[:] /= norm
        return self

    def negate(self):
        """Negate the vector in-place.

        Negate the vector in-place.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).
        """
        self[:] = -self[:]
        return self

    def clear(self):
        """Clear (set to zero) the vector in-place.

        Clear (set to 0) the vector in-place.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).
        """
        self[:] = 0
        return self

    def setI(self, value):
        """Set the ith component of the vector.

        Set the value of component i.

        Parameters
        ----------
        value : float
            New value for component i.

        Returns
        -------
        None
        """
        self[0] = value

    def setJ(self, value):
        """Set the jth component of the vector.

        Set the value of component j.

        Parameters
        ----------
        value : float
            New value for component j.

        Returns
        -------
        None
        """
        self[1] = value

    def setK(self, value):
        """Set the kth component of the vector.

        Set the value of component k.

        Parameters
        ----------
        value : float
            New value for component k.

        Returns
        -------
        None
        """
        self[2] = value

    def set(self, index, value):
        """Set the specified component of the vector.

        Set the value of a component by index.

        Parameters
        ----------
        index : int
            Index (0|1|2) of component to set.
        value : float
            New value for component k.

        Returns
        -------
        None
        """
        self[index] = value

    def setTo(self, *args):
        """Set the vector contents.

        Set the values of all components.

        Parameters
        ----------
        *args : Tuple of arguments.
            Arguments for polymorphic method.
        vector : UnwritableVectorIJK
            Vector to copy to current vector
        OR
        data : list or tuple
            3 values to copy to current vector
        OR
        scale : float
            Scale factor to apply to incoming vector
        vector : UnwritableVectorIJK
            Vector to scale for current vector.
        OR
        offset : int
            Offset into list or tuple.
        data : list or tuple
            Data to copy to current vector.
        OR
        i : float
            First component.
        j : float
            Second component.
        k : float
            Third component.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            if isinstance(args[0], (list, tuple, VectorIJK)):
                # Copy the components from a list or tuple.
                (data,) = args
                self[:] = data[:]
            else:
                raise ValueError('Bad arguments for method!')
        elif len(args) == 2:
            if isRealNumber(args[0]) and isinstance(args[1], VectorIJK):
                # Set the vector components to match another, scaled vector.
                (scale, vector) = args
                self[:] = scale*vector[:]
            elif isinstance(args[0], int) and isinstance(args[1],
                                                         (list, tuple)):
                # Set the vector components to the values from a list or tuple
                # at the offset location.
                (offset, data) = args
                self[:] = data[offset:offset + 3]
            else:
                raise ValueError('Bad arguments for method!')
        elif len(args) == 3:
            # Sets the three components of the vector.
            data = args
            self[:] = data[:]
        else:
            raise ValueError('Bad arguments for method!')
        return self

    def setToUnitized(self, vector):
        """Set the vector to a unitized copy of another.

        Set the vector to a unitized copy of another.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            Vector to unitize and use to set the current vector.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).
        """
        self.setTo(vector)
        self.unitize()
        return self

    def setToNegated(self, vector):
        """Set the vector to a negated copy of another.

        Set the vector to a negated copy of another.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            Vector to negate and use to set the current vector.

        Returns
        -------
        self : VectorIJK
            The current object (for convenience).
        """
        self[:] = -vector[:]
        return self

    @staticmethod
    def rotate(*args):
        """Rotate a copy of a vector.

        Set the vector to a negated copy of another.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            Vector to rotate
        axis : UnwritableVectorIJK
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
            raise ValueError('Bad arguments for method!')

        # Rotate one vector about another by a specified angle.

        # There is one exceptional case, namely if we try to rotate
        # about the zero vector. We can check this by using the project
        # method, as it will throw the desired runtime exception. First
        # cache the contents of vector and axis as input, since we do
        # not know if buffer is equivalent to either of them.
        # (vi, vj, vk) = vector[:]
        v = np.array(vector[:])
        # (ai, aj, ak) = axis[:]
        a = np.array(axis[:])

        # At this point, we are going to build a basis that is
        # convenient for computing the rotated vector. Start by
        # projecting vector onto axis, one of the axes in our basis.
        VectorIJK.project(vector, axis, buffer)

        # Normalize the rotation axis.
        norm = computeNorm(*a)
        a /= norm

        # Store the contents of buffer as this is one of the
        # components of our rotated vector in the new basis.
        p = np.array(buffer[:])

        # To determine one of the other vectors in the basis, simply
        # subtract buffer from vector.
        v -= buffer

        # Now determine the third basis vector by computing the cross
        # product of a unit vector in the direction of axis with
        # buffer.
        buffer[:] = np.cross(a, v)[:]

        # The desired vector projection against this new basis is:
        # {pi,pj,pk} + cos(theta)*{v1i,v1j,v1k} + sin(theta)*buffer
        buffer[:] = p + cos(angle)*v + sin(angle)*buffer
        v = buffer
        return v

    @staticmethod
    def planeProject(*args):
        """Compute the projection of one vector onto a plane.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector to project.
        normal : UnwritableVectorIJK
            The vector defining normal to the plane to project vector onto.
        buffer : VectorIJK (optional)
            Buffer to receive the projected vector.

        Raises
        ------
        BugException:
            If the plane normal vector is 0.
        ValueError
            If incorrect arguments are provided.

        Notes
        -----
        Algebraically, this routine effectively computes:

                                   <vector, to> * to
                          vector - ---------------------
                                      || to ||

        where <> denotes the standard scalar product and ||x|| the norm of x.
        For numeric precision reasons the implementation may vary slightly from
        the above prescription.
        """
        if len(args) == 2:
            # Create the buffer, then perform the projection.
            (vector, normal) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (vector, normal, buffer) = args
        else:
            raise ValueError('Bad arguments for method!')

        # Verify the normal is non-zero.
        if absMaxComponent(*normal) == 0:
            raise BugException('Plane normal vector is zero!')

        # Find the largest vector component magnitude.
        maxVector = absMaxComponent(*vector)

        if maxVector == 0:
            # If maxVector is zero, the vector is a zero vector, and the
            # projection is a zero vector.
            buffer.clear()
        else:

            # Project the vector onto the plane.

            # Create a scaled copy of the input vector to project.
            scaledVector = VectorIJK(vector.i/maxVector, vector.j/maxVector,
                                     vector.k/maxVector)
            VectorIJK.project(scaledVector, normal, buffer)

            # Subtract buffer from the v components to place the result in the
            # plane.
            VectorIJK.subtract(scaledVector, buffer, buffer)

            # Rescale the result.
            buffer.scale(maxVector)

        return buffer

    @staticmethod
    def project(*args):
        """Compute the projection of one vector onto another.

        Project one vector onto another.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector to project.
        onto : UnwritableVectorIJK
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
            v = VectorIJK.project(vector, onto, buffer)
        elif len(args) == 3:
            # Project the first vector onto the second.
            (vector, onto, buffer) = args
            maxVector = absMaxComponent(*vector)
            maxOnto = absMaxComponent(*onto)
            if maxOnto == 0:
                raise BugException(
                    "Unable to project vector onto zero vector.")
                # If the vector to project is 0, so is the projection.
            if maxVector == 0:
                buffer.clear()
            else:
                r = onto/maxOnto
                t = vector/maxVector
                scaleFactor = sum(t*r)*maxVector/sum(r*r)
                buffer[:] = r[:]
                buffer.scale(scaleFactor)
            v = buffer
        else:
            raise ValueError('Bad arguments for method!')
        return v

    @staticmethod
    def combine(*args):
        """Linearly weight and combine vectors.

        For an arbitrary number of vectors, apply scale factors and compute
        the sum.

        The input is an ordered list of (s[0], v[0], s[1], v[1], ...), where
        s[i] is the scale factor for vector v[i].

        Parameters
        ----------
        scale[0] : float
            Scale factor for vector 0.
        vector[0] : UnwritableVectorIJK
            Vector 0
        scale[1|2|...] : float
            Scale factor for vector [1|2|...].
        vector[1|2|...] : UnwritableVectorIJK
            Vector [1|2|...].
        buffer : VectorIJK (optional)
            Buffer to receive the combined vector.

        Returns
        -------
        buffer : VectorIJK
            The weighted sum of all the input vectors.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            raise ValueError('Bad arguments for method!')

        # Convert the args tuple to a list.
        args = list(args)

        # An odd number of arguments indicates the presence of a buffer
        # as the last argument. If none, create one.
        if len(args) % 2 == 1:
            buffer = args.pop()
        else:
            buffer = VectorIJK()

        # Unpack the scale factor/vector pairs.
        scales = args[::2]
        vectors = args[1::2]

        # Clear the buffer, then add up all of the weighted vectors.
        buffer.clear()
        for (s, v) in zip(scales, vectors):
            buffer[:] += s*v[:]
        return buffer

    @staticmethod
    def uCross(*args):
        """Compute the unitized cross product of a and b.

        Compute the unitized cross product of two vectors:

          (a x b)
        -----------
        ||a||*||b||

        Parameters
        ----------
        a : UnwritableVectorIJK
            First vector in cross product.
        b : UnwritableVectorIJK
            Second vector in cross product.
        buffer : VectorIJK (optional)
            Buffer to receive the unitized cross product vector.

        Returns
        -------
        buffer : VectorIJK
            The unitized cross product vector.

        Raises
        ------
        BugException
            If a or b is zero.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args

        # We should scale each vector by its maximal component.
        amax = absMaxComponent(*a)
        if amax == 0:
            raise BugException("The first vector is zero!")
        bmax = absMaxComponent(*b)
        if bmax == 0:
            raise BugException("The second vector is zero!")
        a_scaled = a/amax
        b_scaled = b/bmax
        buffer[:] = np.cross(a_scaled, b_scaled)
        buffer.unitize()
        return buffer

    @staticmethod
    def cross(*args):
        """Compute the cross product of a and b.

        Compute the cross product of two vectors.

        Parameters
        ----------
        a : UnwritableVectorIJK
            First vector in cross product.
        b : UnwritableVectorIJK
            Second vector in cross product.
        buffer : VectorIJK (optional)
            Buffer to receive the cross product vector.

        Returns
        -------
        buffer : VectorIJK
            The cross product vector.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args
        buffer[:] = np.cross(a, b)
        return buffer

    @staticmethod
    def pointwiseMultiply(*args):
        """Create the Pointwise (aka Hadamard, Schur) product of two vectors.

        Compute the pointwise product of two vectors.

        Parameters
        ----------
        a : UnwritableVectorIJK
            First vector in product.
        b : UnwritableVectorIJK
            Second vector in product.
        buffer : VectorIJK (optional)
            Buffer to receive the product vector.

        Returns
        -------
        buffer : VectorIJK
            The product vector.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args
        buffer[:] = a*b
        return buffer

    @staticmethod
    def subtract(*args):
        """Subtract one vector from another.

        Subtract the second vector from the first vector, returning the
        difference as a new vector.

        Parameters
        ----------
        a : UnwritableVectorIJK
            The minuend.
        b : UnwritableVectorIJK
            The subtrahend.
        buffer : VectorIJK (optional)
            Buffer to hold result.

        Returns
        -------
        buffer : VectorIJK
            Vector of the difference (a - b).

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args
        else:
            raise ValueError('Bad arguments for method!')
        buffer[:] = a[:] - b[:]
        return buffer

    @staticmethod
    def add(*args):
        """Add one vector to another.

        Add the second vector from the first vector, returning the
        sum as a new vector.

        Parameters
        ----------
        a : UnwritableVectorIJK
            The first vector.
        b : UnwritableVectorIJK
            The second vector.
        buffer : VectorIJK (optional)
            Buffer to hold result.

        Returns
        -------
        buffer : VectorIJK
            Vector of the sum (a + b).

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args
        else:
            raise ValueError('Bad arguments for method!')
        buffer[:] = a[:] + b[:]
        return buffer

    @staticmethod
    def addAll(*args):
        """Add a set of vectors to produce a sum vector.

        For an arbitrary number of vectors, compute the sum vector.

        Parameters
        ----------
        vectors : List or tuple of UnwritableVectorIJK
            Vectors to add.
        buffer : VectorIJK (optional)
            Buffer to hold result.

        Returns
        -------
        buffer : VectorIJK
            The sum of all the input vectors.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 1:
            (vectors,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (vectors, buffer) = args
        else:
            raise ValueError('Bad arguments for method!')

        # Clear the buffer, then add up the vectors.
        buffer.clear()
        for v in vectors:
            buffer[:] += v[:]
        return buffer

    @staticmethod
    def addRSS(*args):
        """Compute the component-wise RMS sum of two vectors.

        ompute the component-wise root-mean-square sum of two vectors.

        Parameters
        ----------
        a : UnwritableVectorIJK
            First vector to add.
        b : UnwritableVectorIJK
            Second vector to add.
        buffer : VectorIJK (optional)
            Buffer to hold result.

        Returns
        -------
        buffer : VectorIJK
            The component-wise RMS sum of the input vectors.

        Raises
        ------
        ValueError:
            If incorrect arguments are provided.
        """
        if len(args) == 2:
            (a, b) = args
            buffer = VectorIJK()
        elif len(args) == 3:
            (a, b, buffer) = args
        else:
            raise ValueError('Bad arguments for method!')

        # Perform a component wise root sum square of two vectors (add
        # in quadrature).
        i = computeNorm(a.i, b.i)
        j = computeNorm(a.j, b.j)
        k = computeNorm(a.k, b.k)
        buffer.setTo(i, j, k)
        return buffer

    def getI(self):
        """Get the ith component (float)."""
        return self.i

    def getJ(self):
        """Get the jth component (float)."""
        return self.j

    def getK(self):
        """Get the kth component (float)."""
        return self.k

    @staticmethod
    def copyOf(vector):
        """Make an unwritable copy of the supplied vector.

        This method makes an unwritable copy only if necessary. It tries to
        avoid making a copy wherever possible.

        param UnwritableVectorIJK vector a vector to copy.

        return UnwritableVectorIJK either a reference to vector (if vector is
        already only an instance of UnwritableVectorIJK, otherwise an
        unwritable copy of vector's contents
        """
        return VectorIJK(vector)

    def getLength(self):
        """Compute the standard L-2 norm, or length, of the vector.

        return float (i*i + j*j + k*k)^(1/2) without danger of overflow.
        """
        return computeNorm(*self)

# # The ZERO vector.
# ZERO = UnwritableVectorIJK(0, 0, 0)

# The I basis vector: (1,0,0).
I = VectorIJK(1, 0, 0)

# The J basis vector: (0,1,0).
J = VectorIJK(0, 1, 0)

# The K basis vector: (0,0,1).
K = VectorIJK(0, 0, 1)

# # The negative of the I basis vector: (-1,0,0).
# MINUS_I = UnwritableVectorIJK(-1, 0, 0)

# # The negative of the J basis vector: (0,-1,0).
# MINUS_J = UnwritableVectorIJK(0, -1, 0)

# # The negative of the K basis vector: (0,0,-1).
# MINUS_K = UnwritableVectorIJK(0, 0, -1)
