"""An unwritable 3-D vector in Cartesian (i, j, k) coordinates.

A weakly immutable 3-dimensional vector designed to properly support a writable
subclass.

Note: Subclass implementers, you should only use the protected fields in this
class to store the contents of the vector components, otherwise all of the
methods here and in the operations class may break.

The basic data fields on this class are marked as protected to allow direct
access to them through subclassing. This will get around any performance issues
that one may have in using this vector arithmetic toolkit due to the
enforcement of access to the component values through accessor methods.

Note, the equals and hashcode implementations in this class support proper
comparisons between subclasses of this class and this class. The reason this
works, is because by design the only member variables of this class live in the
parent class. If one subclasses this class and defines additional members then
this will most certainly break the implementation presented here.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import asin, pi

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.tensors.vector3d import Vector3D
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.utilities.isrealnumber import isRealNumber


# Map vector component names to indices.
components = {'i': 0, 'j': 1, 'k': 2}


class UnwritableVectorIJK(Vector3D):
    """UnwritableVectorIJK.

    This class implements a 3-dimensional vector in Cartesian (i, j, k)
    coordinates, with many additional useful methods.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    i : float
        Value of i-coordinate.
    j : float
        Value of j-coordinate.
    k : float
        Value of k-coordinate.
    """

    def __new__(cls, *args):
        """Create a new UnwritableVectorIJK object.

        Allocate a new UnwritableVectorIJK object by allocating a new
        Vector3D object on which the UnwritableVectorIJK will expand.

        Parameters
        ----------
        args : tuple of object
            Arguments for polymorphic constructor.
        SUCH AS:
        ijk : list or tuple of float
            Values for (i, j, k) coordinates.
        OR
        vector : UnwritableVectorIJK
            Existing vector to copy.
        OR
        offset : int
            Offset into data for assignment to vector elements.
        data : list of >=3 float
            Values to use for vector elements, starting at offset.
        OR
        scale : float
            Scale factor for vector to copy.
        vector : UnwritableVectorIJK
            Existing vector to copy and scale.
        OR
        i, j, k : float
            Values for vector elements.

        Returns
        -------
        v : UnwritableVectorIJK
            The newly-created object.

        Raises
        ------
        ValueError
            If incorrect arguments are provided.
        """
        if len(args) == 0:
            data = (None, None, None)
            v = Vector3D.__new__(cls, *data)
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                # List or tuple of 3 values for the components.
                (ijk,) = args
                v = Vector3D.__new__(cls, *ijk)
            elif isinstance(args[0], UnwritableVectorIJK):
                # Copy an existing UnwritableVectorIJK.
                (vector,) = args
                v = Vector3D.__new__(cls, *vector)
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], (list, tuple)):
                # Offset and list or tuple of >= (3 + offset + 1) values.
                (offset, data) = args
                v = Vector3D.__new__(cls, data[offset], data[offset + 1],
                                     data[offset + 2])
            elif (isRealNumber(args[0]) and
                  isinstance(args[1], UnwritableVectorIJK)):
                # Scale factor and UnwritableVectorIJK to scale.
                (scale, vector) = args
                v = Vector3D.__new__(cls, scale*vector.i, scale*vector.j, scale*vector.k)
            else:
                raise ValueError('Bad arguments for constructor!')
        elif len(args) == 3:
            # Scalar values (3) for the components.
            (i, j, k) = args
            v = Vector3D.__new__(cls, i, j, k)
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

    def createUnitized(self):
        """Create a new, unit-length copy of the vector.

        Make a unit-length copy of the vector by scaling by the reciprocal
        of the length.

        Returns
        -------
        v : UnwritableVectorIJK
            A unit-length copy of the vector.
        """
        length = self.getLength()
        v = UnwritableVectorIJK(1/length, self)
        return v

    def createNegated(self):
        """Create a negated copy of an the vector.

        Create a negated copy of the vector by negating each individual
        element.

        Returns
        -------
        v : UnwritableVectorIJK
            A negated copy of the vector.
        """
        v = UnwritableVectorIJK(-self.i, -self.j, -self.k)
        return v

    def createScaled(self, scale):
        """Create a scaled copy of an the vector.

        Convenience method for UnwritableVectorIJK(scale, this).

        Parameters
        ----------
        scale : float
            The scale factor to apply to the vector.

        Returns
        -------
        v : UnwritableVectorIJK
            A scaled copy of the vector.
        """
        v = UnwritableVectorIJK(scale, self)
        return v

    def getI(self):
        """Get the ith component.

        Returns
        -------
        self.i : float
            The value of component i.
        """
        return self.i

    def getJ(self):
        """Get the jth component.

        Returns
        -------
        self.j : float
            The value of component j.
        """
        return self.j

    def getK(self):
        """Get the kth component.

        Returns
        -------
        self.k : float
            The value of component k.
        """
        return self.k

    def get(self, index):
        """Get the specified component.

        Return the specified vector component, by index.

        Parameters
        ----------
        index : int (0|1|2)
            The index of the component to retrieve.

        Returns
        -------
        self[0|1|2] : float
            The value for the requested component.
        """
        return self[index]

    def getLength(self):
        """Compute the standard L-2 norm, or length, of the vector.

        Compute the length of the vector.

        Returns
        -------
        length : float
            Length of the vector.
        """
        length = computeNorm(self.i, self.j, self.k)
        return length

    def getDot(self, vector):
        """Compute the dot product of this vector with another vector.

        Compute the dot (scalar) product of this vector with another.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector to dot with the current vector.

        Returns
        -------
        dot : float
            The dot product of this vector with the supplied vector.
        """
        dot = self.dot(vector)
        return dot

    def getSeparation(self, vector):
        """Compute the angular separation between this and another vector.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector from which the angle is measured.

        Returns
        -------
        angle : float
            The angular separation between vector and this instance in
            radians.

        Raises
        ------
        BugException
            If either this instance or the supplied vector are zero.
        """
        thisNorm = self.getLength()
        if thisNorm == 0:
            raise BugException("Unable to compute angular separation. "
                               "This vector is the zero vector.")
        vectorNorm = vector.getLength()
        if vectorNorm == 0:
            raise BugException("Unable to compute angular separation. "
                               "The argument supplied is the zero vector.")
        dotProduct = self.getDot(vector)
        if dotProduct > 0:
            v = self/thisNorm - vector/vectorNorm
            norm = computeNorm(v[0], v[1], v[2])
            angle = 2*asin(0.5*norm)
        elif dotProduct < 0:
            v = self/thisNorm + vector/vectorNorm
            norm = computeNorm(v[0], v[1], v[2])
            angle = pi - 2*asin(0.5*norm)
        else:
            angle = pi/2
        return angle

    def getSeparationOutOfPlane(self, normal):
        """Compute the angle between this vector and a plane.

        Positive values lie on the same side as normal, negative on the
        other side.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector normal to the plane.

        Returns
        -------
        angle : float
            The angular separation between vector and the plane in
            radians.
        """
        angle = pi/2 - self.getSeparation(normal)
        return angle

    @staticmethod
    def copyOf(vector):
        """Make an unwritable copy of the supplied vector.

        This method makes an copy of the existing vector.

        Parameters
        ----------
        vector : UnwritableVectorIJK
            The vector to copy.

        Returns
        -------
        v : UnwritableVectorIJK
            A copy of the vector.
        """
        v = UnwritableVectorIJK(vector)
        return v
