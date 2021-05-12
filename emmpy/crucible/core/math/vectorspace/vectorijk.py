"""emmpy.crucible.core.math.vectorspace.vectorijk"""


# from math import cos, sin

# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.crucible.core.exceptions.bugexception import BugException
# from emmpy.crucible.core.math.vectorspace.internaloperations import (
#     absMaxComponent,
#     computeNorm
# )
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
# from emmpy.java.lang.illegalargumentexception import IllegalArgumentException
# from emmpy.java.lang.unsupportedoperationexception import (
#     UnsupportedOperationException
# )
# from emmpy.utilities.isrealnumber import isRealNumber


class VectorIJK(UnwritableVectorIJK):
    """Writable subclass of the unwritable 3D vector parent completing the
    implementation of the weak immutability design pattern.

    This class contains the mutator methods necessary to set or alter the
    internals of the parent classes fields.

    author F.S.Turner
    """
    pass

    # # The ZERO vector.
    # ZERO = UnwritableVectorIJK(0, 0, 0)

    # # The I basis vector: (1,0,0).
    # I = UnwritableVectorIJK(1, 0, 0)

    # # The J basis vector: (0,1,0).
    # J = UnwritableVectorIJK(0, 1, 0)

    # # The K basis vector: (0,0,1).
    # K = UnwritableVectorIJK(0, 0, 1)

    # # The negative of the I basis vector: (-1,0,0).
    # MINUS_I = UnwritableVectorIJK(-1, 0, 0)

    # # The negative of the J basis vector: (0,-1,0).
    # MINUS_J = UnwritableVectorIJK(0, -1, 0)

    # # The negative of the K basis vector: (0,0,-1).
    # MINUS_K = UnwritableVectorIJK(0, 0, -1)

    # def __init__(self, *args):
    #     """Constructor"""
    #     if len(args) == 0:
    #         # Construct a vector with an initial value of
    #         # {@link VectorIJK#ZERO}
    #         UnwritableVectorIJK.__init__(self, 0, 0, 0)
    #     elif len(args) == 1:
    #         if isinstance(args[0], list):
    #             # Constructs a vector from the first three elements of an array
    #             # of doubles.
    #             # @param data the array of doubles.
    #             # @throws IndexOutOfBoundsException if the supplied data array
    #             # does not contain at least three elements
    #             (data,) = args
    #             UnwritableVectorIJK.__init__(self, data)
    #         elif isinstance(args[0], UnwritableVectorIJK):
    #             # Copy constructor, creates a vector by copying the values of
    #             # a pre-exisiting one.
    #             # @param vector the vector whose contents are to be copied
    #             (vector,) = args
    #             UnwritableVectorIJK.__init__(self, vector)
    #         else:
    #             raise Exception
    #     elif len(args) == 2:
    #         if isinstance(args[0], int) and isinstance(args[1], list):
    #             # Constructs a vector from the three elements of an array of
    #             # double starting with the offset index.
    #             # @param offset index into the data array to copy into the ith
    #             # component.
    #             # @param data the array of doubles.
    #             # @throws IndexOutOfBoundsException if the supplied data array
    #             # does not contain three elements at indices offset through
    #             # offset + 2
    #             (index, data) = args
    #             UnwritableVectorIJK.__init__(self, index, data)
    #         elif (isRealNumber(args[0]) and
    #               isinstance(args[1], UnwritableVectorIJK)):
    #             # Scaling constructor, creates a new vector by applying a
    #             # scalar multiple to the components of a pre-existing vector.
    #             # This results in (scale*vector) being stored in the newly
    #             # constructed vector.
    #             # @param scale the scale factor to apply
    #             # @param vector the vector whose contents are to be scaled
    #             (scale, vector) = args
    #             UnwritableVectorIJK.__init__(self, scale, vector)
    #         else:
    #             raise Exception
    #     elif len(args) == 3:
    #         # Constructs a vector from three basic components
    #         # @param i the ith component
    #         # @param j the jth component
    #         # @param k the kth component
    #         (i, j, k) = args
    #         UnwritableVectorIJK.__init__(self, i, j, k)
    #     else:
    #         raise Exception

    # def createUnitized(self):
    #     """Note: this method is overridden to return an instance of the
    #     writable subclass rather than the unwritable parent."""
    #     return VectorIJK(self).unitize()

    # def createNegated(self):
    #     """Note: this method is overridden to return an instance of the
    #     writable subclass rather than the unwritable parent."""
    #     return VectorIJK(self).negate()

    # def createScaled(self, scale: float):
    #     """Note: this method is overridden to return an instance of the
    #     writable subclass rather than the unwritable parent."""
    #     return VectorIJK(self).scale(scale)

    # def scale(self, _scale: float):
    #     """Scale the vector.

    #     @param scale the scale factor to apply.
    #     @return a reference to the instance for convenience, which now contains
    #     (scale*this)
    #     """
    #     self.i *= _scale
    #     self.j *= _scale
    #     self.k *= _scale
    #     return self

    # def unitize(self):
    #     """Unitize the vector.

    #     @return a reference to the instance for convenience, which now contains
    #     a vector of unit length in the direction of the original vector.
    #     @throws UnsupportedOperationException if the vector is equal to
    #     {@link VectorIJK#ZERO}
    #     """
    #     norm = computeNorm(self.i, self.j, self.k)
    #     if norm == 0.0:
    #         raise UnsupportedOperationException(
    #             "Unable to unitize vector. Instance is zero length.")
    #     self.i /= norm
    #     self.j /= norm
    #     self.k /= norm
    #     return self

    # def negate(self):
    #     """Negate the vector.

    #     @return a reference to the instance, now containing -vector.
    #     """
    #     self.i *= -1
    #     self.j *= -1
    #     self.k *= -1
    #     return self

    # def clear(self):
    #     """Clear the vector.

    #     @return a reference to the instance, now containing
    #     {@link VectorIJK#ZERO}
    #     """
    #     self.i = 0.0
    #     self.j = 0.0
    #     self.k = 0.0
    #     return self

    # def setI(self, i: float):
    #     """Sets the ith component of the vector.

    #     @param i the ith component
    #     """
    #     self.i = i

    # def setJ(self, j: float):
    #     """Sets the jth component of the vector.

    #     @param j the jth component
    #     """
    #     self.j = j

    # def setK(self, k: float):
    #     """Sets the kth component of the vector.

    #     @param k the kth component
    #     """
    #     self.k = k

    # def set(self, index: int, value: float):
    #     """Sets the specified component of the vector to a supplied value.

    #     @param index the index of the component to set. 0 = ith, 1 = jth,
    #     2 = kth.
    #     @param value the value with which to replace the specified component
    #     @throws IllegalArgumentException if an invalid index, outside the range
    #     [0,2], is specified.
    #     """
    #     Preconditions.checkElementIndex(index, 3, "element")
    #     if index == 0:
    #         self.i = value
    #     elif index == 1:
    #         self.j = value
    #     elif index == 2:
    #         self.k = value
    #     else:
    #         raise BugException

    # def setTo(self, *args):
    #     """Set the vector contents."""
    #     if len(args) == 1:
    #         if isinstance(args[0], UnwritableVectorIJK):
    #             # Set the vector contents to match those of another.
    #             # @param vector the vector whose contents are to be copied into
    #             # the vector
    #             (vector,) = args
    #             self.i = vector.i
    #             self.j = vector.j
    #             self.k = vector.k
    #             return self
    #         elif isinstance(args[0], list):
    #             # Sets the basic components of a vector copying the values from
    #             # the supplied array.
    #             # @param data the array of doubles to copy.
    #             # @return a reference to the instance
    #             (data,) = args
    #             return self.setTo(data[0], data[1], data[2])
    #         else:
    #             raise Exception
    #     elif len(args) == 2:
    #         if isRealNumber(args[0]) and isinstance(args[1],
    #                                                 UnwritableVectorIJK):
    #             # Set the vector contents to match the scale of another.
    #             # @param scale the scale factor to apply to vector
    #             # @param vector the vector whose scaled contents are to be
    #             # copied into the vector
    #             (scale, vector,) = args
    #             self.i = scale*vector.i
    #             self.j = scale*vector.j
    #             self.k = scale*vector.k
    #             return self
    #         elif isinstance(args[0], int) and isinstance(args[1], list):
    #             #  Sets the basic components of a vector copying the values
    #             # from an array at the offset location.
    #             # @param offset the offset into the data array
    #             # @param data array of doubles to copy into vector
    #             # @return a reference to the instance
    #             (offset, data) = args
    #             return self.setTo(data[offset], data[offset + 1],
    #                               data[offset + 2])
    #     elif len(args) == 3:
    #         if (isRealNumber(args[0]) and isRealNumber(args[1])
    #             and isRealNumber(args[2])):
    #             # Sets the basic components of the vector.
    #             # @param i the ith component
    #             # @param j the jth component
    #             # @param k the kth component
    #             (i, j, k) = args
    #             self.i = i
    #             self.j = j
    #             self.k = k
    #             return self
    #     else:
    #         raise Exception

    # def setToUnitized(self, vector):
    #     """Sets the vector content to the a unit length version of another.
    #     @param vector the vector whose contents are to be unitized and stored
    #     in the instance
    #     @return a reference to the instance
    #     @throws UnsupportedOperationException if the supplied vector argument
    #     is {@link VectorIJK#ZERO}
    #     """
    #     self.setTo(vector)
    #     return self.unitize()

    # def setToNegated(self, vector):
    #     """Sets the vector content to a negated version of another.
    #     @param vector the vector whose contents are to be negated and stored in
    #     the instance
    #     @return a reference to the instance
    #     """
    #     self.setTo(vector)
    #     return self.negate()

    # @staticmethod
    # def rotate(*args):
    #     """Rotate the vector."""
    #     if len(args) == 3:
    #         if (isinstance(args[0], UnwritableVectorIJK) and
    #             isinstance(args[1], UnwritableVectorIJK) and
    #             isinstance(args[2], float)):
    #             # Rotate one vector about another by an angle specified in
    #             # radians.
    #             # @param vector the vector to rotate
    #             # @param axis the axis about which to rotate vector
    #             # @param angle the angle, in radians, through which to rotate
    #             # @return a reference to buffer for convenience
    #             # @throws IllegalArgumentException if the axis is equal to
    #             # {@link VectorIJK#ZERO}.
    #             # @see VectorIJK#rotate(UnwritableVectorIJK,
    #             # UnwritableVectorIJK, double, VectorIJK)
    #             (vector, axis, angle) = args
    #             return VectorIJK.rotate(vector, axis, angle, VectorIJK())
    #     elif len(args) == 4:
    #         if (isinstance(args[0], UnwritableVectorIJK) and
    #             isinstance(args[1], UnwritableVectorIJK) and
    #             isinstance(args[2], float) and
    #             isinstance(args[3], VectorIJK)):
    #             # Rotate one vector about another by an angle specified in
    #             # radians. An example is perhaps the most straightforward
    #             # means to explain this methods action. Given an axis (0,0,1)
    #             # and a rotation angle of PI/2, this method does the following:

    #             #    vector         buffer
    #             # ( 1, 2, 3 )   ( -2, 1, 3 )
    #             # ( 1, 0, 0 )   ( 0, 1, 0 )
    #             # ( 0, 1, 0 )   ( -1, 0, 0 )

    #             # @param vector the vector to rotate
    #             # @param axis the axis about which to rotate vector
    #             # @param angle the angle, in radians, through which to rotate
    #             # @param buffer the buffer to receive the contents of the
    #             # rotation
    #             # @return a reference to buffer for convenience
    #             # @throws IllegalArgumentException if the axis is equal to
    #             # {@link VectorIJK#ZERO}.
    #             (vector, axis, angle, buffer) = args

    #             # There is one exceptional case, namely if we try to rotate
    #             # about the zero vector. We can check this by using the project
    #             # method, as it will throw the desired runtime exception. First
    #             # cache the contents of vector and axis as input, since we do
    #             # not know if buffer is equivalent to either of them.
    #             vi = vector.i
    #             vj = vector.j
    #             vk = vector.k
    #             ai = axis.i
    #             aj = axis.j
    #             ak = axis.k

    #             # At this point, we are going to build a basis that is
    #             # convenient for computing the rotated vector. Start by
    #             # projecting vector onto axis, one of the axes in our basis.
    #             VectorIJK.project(vector, axis, buffer)

    #             norm = computeNorm(ai, aj, ak)
    #             ai /= norm
    #             aj /= norm
    #             ak /= norm

    #             #  Store the contents of buffer as this is one of the
    #             # components of our rotated vector in the new basis.
    #             pi = buffer.i
    #             pj = buffer.j
    #             pk = buffer.k

    #             # To determine one of the other vectors in the basis, simply
    #             # subtract buffer from vector.
    #             vi -= buffer.i
    #             vj -= buffer.j
    #             vk -= buffer.k

    #             # Now determine the third basis vector by computing the cross
    #             # product of a unit vector in the direction of axis with
    #             # buffer.
    #             buffer.i = aj*vk - ak*vj
    #             buffer.j = ak*vi - ai*vk
    #             buffer.k = ai*vj - aj*vi

    #             # The desired vector projection against this new basis is:
    #             # {pi,pj,pk} + cos(theta)*{v1i,v1j,v1k} + sin(theta)*buffer
    #             buffer.i = pi + cos(angle)*vi + sin(angle)*buffer.i
    #             buffer.j = pj + cos(angle)*vj + sin(angle)*buffer.j
    #             buffer.k = pk + cos(angle)*vk + sin(angle)*buffer.k

    #             return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def planeProject(*args):
    #     """Compute the projection of one vector onto the plane normal to
    #     another.

    #     Algebraicly, this routine effectively computes:

    #                                <vector, to> * to
    #                       vector - ---------------------
    #                                   || to ||

    #     where <> denotes the standard scalar product and ||x|| the norm of x.
    #     For numeric precision reasons the implementation may vary slightly from
    #     the above prescription.

    #     @param vector the vector to project
    #     @param normal the normal to the plane to project vector onto
    #     @return a new <code>VectorIJK</code> containing the results of the
    #     projection
    #     @throws IllegalArgumentException if normal is equal to
    #     {@link VectorIJK#ZERO}
    #     @see VectorIJK#planeProject(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (vector, normal) = args
    #         return VectorIJK.planeProject(vector, normal, VectorIJK())
    #     elif len(args) == 3:
    #         # @param vector the vector to project
    #         # @param normal the normal to the plane to project vector onto
    #         # @param buffer the buffer to receive the contents of the
    #         # projection
    #         # @return a reference to buffer for convenience
    #         # @throws IllegalArgumentException if normal is equal to
    #         # {@link VectorIJK#ZERO}
    #         (vector, normal, buffer) = args
    #         # If the supplied normal vector is the zero vector, generate the
    #         # necessary exception.
    #         Preconditions.checkArgument(not normal.equals(VectorIJK.ZERO),
    #                                     "Normal must not be the zero vector.")

    #         maxVector = absMaxComponent(vector.i, vector.j, vector.k)

    #         # Check to see if maxVector is zero length. If it is, populate
    #         # buffer with VectorIJK.ZERO.
    #         if maxVector == 0.0:
    #             buffer.clear()
    #             return buffer

    #         # Create a scaled copy of the input vector to project.
    #         scaledVector = VectorIJK(vector.i/maxVector, vector.j/maxVector,
    #                                  vector.k/maxVector)
    #         VectorIJK.project(scaledVector, normal, buffer)

    #         # The second unusual case is when vector itself is zero. This is
    #         # simple enough, the zero vector projects as the zero vector.
    #         if maxVector == 0.0:
    #             buffer.clear()
    #             return buffer

    #         # Subtract buffer from the v components to place the result in the
    #         # plane.
    #         VectorIJK.subtract(scaledVector, buffer, buffer)

    #         # Rescale the result.
    #         buffer.scale(maxVector)
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def project(*args):
    #     """Compute the projection of one vector onto another.

    #     Algebraicly, this routine effectively computes:

    #     <vector, onto> * onto
    #     ---------------------
    #          || onto ||

    #     where <> denotes the standard scalar product and ||x|| the norm of x.
    #     For numeric precision reasons the implementation may vary slightly
    #     from the above prescription.
    #     """
    #     if len(args) == 2:
    #         # @param vector the vector to project
    #         # @param onto the vector onto which vector is to be projected
    #         # @return a new <code>VectorIJK</code> containing the results
    #         # of the projection
    #         # @throws IllegalArgumentException if onto is the equal to
    #         # {@link VectorIJK#ZERO}.
    #         # @see VectorIJK#project(UnwritableVectorIJK,
    #         # UnwritableVectorIJK, VectorIJK)
    #         (vector, onto) = args
    #         return VectorIJK.project(vector, onto, VectorIJK())
    #     elif len(args) == 3:
    #         # @param vector the vector to project
    #         # @param onto the vector onto which vector is to be projected
    #         # @param buffer the buffer to receive the contents of the
    #         # projection
    #         # @return a reference to buffer for convenience
    #         # @throws IllegalArgumentException if onto is the equal to
    #         # {@link VectorIJK#ZERO}.
    #         (vector, onto, buffer) = args
    #         maxVector = absMaxComponent(vector.i, vector.j, vector.k)
    #         maxOnto = absMaxComponent(
    #             onto.i, onto.j, onto.k)
    #         if maxOnto == 0:
    #             raise IllegalArgumentException(
    #                 "Unable to project vector onto the zero vector.")
    #         if maxVector == 0:
    #             buffer.clear()
    #             return buffer
    #         r1 = onto.i/maxOnto
    #         r2 = onto.j/maxOnto
    #         r3 = onto.k/maxOnto
    #         t1 = vector.i/maxVector
    #         t2 = vector.j/maxVector
    #         t3 = vector.k/maxVector
    #         scaleFactor = (
    #             (t1*r1 + t2*r2 + t3*r3)*maxVector/(r1*r1 + r2*r2 + r3*r3)
    #         )
    #         buffer.i = r1
    #         buffer.j = r2
    #         buffer.k = r3
    #         buffer.scale(scaleFactor)
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def combine(*args):
    #     """Linearly combine vectors.

    #     @param scaleA the scale factor for vector a
    #     @param a a vector
    #     @param scaleB the scale vector for vector b
    #     @param b another vector
    #     @param scaleC the scale factor for vector c
    #     @param c the third vector
    #     @param scaleD the scale factor for vector d
    #     @param d the fourth vector
    #     @param scaleE the scale factor for vector e
    #     @param e the fifth vector
    #     @param scaleF the scale factor for vector f
    #     @param f the sixth vector
    #     @param scaleG the scale factor for vector g
    #     @param g the seventh vector
    #     @param scaleH the scale factor for vector h
    #     @param h the eighth vector
    #     @return a new <code>VectorIJK</code> which now contains
    #     ( scaleA*a + scaleB*b + scaleC*c + scaleD*d +
    #       scaleE*e + scaleF*f + scaleG*g + scaleH*h)
    #     @see VectorIJK#combine(double, UnwritableVectorIJK, double,
    #     UnwritableVectorIJK, double, UnwritableVectorIJK, VectorIJK)
    #     """
    #     if len(args) == 4:
    #         (scaleA, a, scaleB, b) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, VectorIJK())
    #     elif len(args) == 5:
    #         (scaleA, a, scaleB, b, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k)
    #         return buffer
    #     elif len(args) == 6:
    #         (scaleA, a, scaleB, b, scaleC, c) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  VectorIJK())
    #     elif len(args) == 7:
    #         (scaleA, a, scaleB, b, scaleC, c, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k)
    #         return buffer
    #     elif len(args) == 8:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  scaleD, d, VectorIJK())
    #     elif len(args) == 9:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i + scaleD*d.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j + scaleD*d.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k + scaleD*d.k)
    #         return buffer
    #     elif len(args) == 10:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  scaleD, d, scaleE, e, VectorIJK())
    #     elif len(args) == 11:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i + scaleD*d.i +
    #                     scaleE*e.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j + scaleD*d.j +
    #                     scaleE*e.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k + scaleD*d.k +
    #                     scaleE*e.k)
    #         return buffer
    #     elif len(args) == 12:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  scaleD, d, scaleE, e, scaleF, f,
    #                                  VectorIJK())
    #     elif len(args) == 13:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i + scaleD*d.i +
    #                     scaleE*e.i + scaleF*f.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j + scaleD*d.j +
    #                     scaleE*e.j + scaleF*f.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k + scaleD*d.k +
    #                     scaleE*e.k + scaleF*f.k)
    #         return buffer
    #     elif len(args) == 14:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f, scaleG, g) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  scaleD, d, scaleE, e, scaleF, f,
    #                                  scaleG, g, VectorIJK())
    #     elif len(args) == 15:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f, scaleG, g, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i + scaleD*d.i +
    #                     scaleE*e.i + scaleF*f.i + scaleG*g.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j + scaleD*d.j +
    #                     scaleE*e.j + scaleF*f.j + scaleG*g.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k + scaleD*d.k +
    #                     scaleE*e.k + scaleF*f.k + scaleG*g.k)
    #         return buffer
    #     elif len(args) == 16:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f, scaleG, g, scaleH, h) = args
    #         return VectorIJK.combine(scaleA, a, scaleB, b, scaleC, c,
    #                                  scaleD, d, scaleE, e, scaleF, f,
    #                                  scaleG, g, scaleH, h, VectorIJK())
    #     elif len(args) == 17:
    #         (scaleA, a, scaleB, b, scaleC, c, scaleD, d, scaleE, e,
    #          scaleF, f, scaleG, g, scaleH, h, buffer) = args
    #         buffer.i = (scaleA*a.i + scaleB*b.i + scaleC*c.i + scaleD*d.i +
    #                     scaleE*e.i + scaleF*f.i + scaleG*g.i + scaleH*h.i)
    #         buffer.j = (scaleA*a.j + scaleB*b.j + scaleC*c.j + scaleD*d.j +
    #                     scaleE*e.j + scaleF*f.j + scaleG*g.j + scaleH*h.j)
    #         buffer.k = (scaleA*a.k + scaleB*b.k + scaleC*c.k + scaleD*d.k +
    #                     scaleE*e.k + scaleF*f.k + scaleG*g.k + scaleH*h.k)
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def uCross(*args):
    #     """Compute the cross product of a and b; unitize the result.

    #     @param a the left hand vector to cross
    #     @param b the right hand vector to cross
    #     @return a new <code>VectorIJK</code> which now contains
    #     (a x b)/||a||/||b||.
    #     @throws IllegalArgumentException if either a or b are equivalent to the
    #     {@link VectorIJK#ZERO}
    #     @throws UnsupportedOperationException if the result of crossing a with
    #     b results in {@link VectorIJK#ZERO}
    #     @see VectorIJK#uCross(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.uCross(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         (a, b, buffer) = args
    #         # We should scale each vector by its maximal component.
    #         amax = absMaxComponent(a.i, a.j, a.k)
    #         bmax = absMaxComponent(b.i, b.j, b.k)
    #         if amax == 0.0 or bmax == 0.0:
    #             raise IllegalArgumentException(
    #                 "At least one input vector is of zero length. Unable to "
    #                 "unitize resultant cross product."
    #             )
    #         ti = (a.j/amax)*(b.k/bmax) - (a.k/amax)*(b.j/bmax)
    #         tj = (a.k/amax)*(b.i/bmax) - (a.i/amax)*(b.k/bmax)
    #         tk = (a.i/amax)*(b.j/bmax) - (a.j/amax)*(b.i/bmax)
    #         buffer.i = ti
    #         buffer.j = tj
    #         buffer.k = tk
    #         return buffer.unitize()
    #     else:
    #         raise Exception

    # @staticmethod
    # def cross(*args):
    #     """Compute the cross product of a and b.
    #     @param a the left hand vector to cross
    #     @param b the right hand vector to cross
    #     @return a new <code>VectorIJK</code> which now contains (a x b)
    #     @see VectorIJK#cross(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.cross(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         (a, b, buffer) = args
    #         ti = a.j*b.k - a.k*b.j
    #         tj = a.k*b.i - a.i*b.k
    #         tk = a.i*b.j - a.j*b.i
    #         buffer.i = ti
    #         buffer.j = tj
    #         buffer.k = tk
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def pointwiseMultiply(*args):
    #     """Create the Pointwise (aka Hadamard aka Schur) product of two vectors
    #     by multiplying their corresponding components

    #     @param a a vector
    #     @param b another vector
    #     @return a new <code>VectorIJK</code> which now contains (a .* b).
    #     @see VectorIJK#pointwiseMultiply(UnwritableVectorIJK,
    #     UnwritableVectorIJK, VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.pointwiseMultiply(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         (a, b, buffer) = args
    #         buffer.i = a.i*b.i
    #         buffer.j = a.j*b.j
    #         buffer.k = a.k*b.k
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def subtract(*args):
    #     """Subtract one vector from another.
    #     @param a the minuend
    #     @param b the subtrahend
    #     @return a new <code>VectorIJK</code> which now contains (a - b)
    #     @see VectorIJK#subtract(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.subtract(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         (a, b, buffer) = args
    #         buffer.i = a.i - b.i
    #         buffer.j = a.j - b.j
    #         buffer.k = a.k - b.k
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def add(*args):
    #     """Add a vector to another.
    #     @param a a vector
    #     @param b another vector
    #     @return a new <code>VectorIJK</code> which now contains (a + b)
    #     @see VectorIJK#add(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.add(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         (a, b, buffer) = args
    #         buffer.i = a.i + b.i
    #         buffer.j = a.j + b.j
    #         buffer.k = a.k + b.k
    #         return buffer
    #     else:
    #         raise Exception

    # @staticmethod
    # def addAll(*args):
    #     """Adds all the vectors in an {@link Iterable} of vectors.
    #     @param vectors an {@link Iterable} of vectors to be added
    #     @param buffer the buffer to receive the results of the addition
    #     @return a reference to buffer for convenience which now contains
    #     (a + b + ... + n).
    #     """
    #     if len(args) == 1:
    #         (vectors,) = args
    #         return VectorIJK.addAll(vectors, VectorIJK())
    #     elif len(args) == 2:
    #         (vectors, buffer) = args
    #         sumI = 0.0
    #         sumJ = 0.0
    #         sumK = 0.0
    #         for vector in vectors:
    #             sumI += vector.i
    #             sumJ += vector.j
    #             sumK += vector.k
    #         return buffer.setTo(sumI, sumJ, sumK)
    #     else:
    #         raise Exception

    # @staticmethod
    # def addRSS(*args):
    #     """Performs a component wise root sum square of two vectors (add in
    #     quadrature).

    #     @param a a vector
    #     @param b another vector

    #     @return a new <code>VectorIJK</code> which now contains
    #     (sqrt(a<sub>i</sub> + b<sub>i</sub> ) ,
    #      sqrt(a<sub>j</sub> + b<sub>j</sub>) ,
    #      sqrt(a<sub>k</sub> + b<sub>k</sub> )).

    #     @see VectorIJK#addRSS(UnwritableVectorIJK, UnwritableVectorIJK,
    #     VectorIJK)
    #     """
    #     if len(args) == 2:
    #         (a, b) = args
    #         return VectorIJK.addRSS(a, b, VectorIJK())
    #     elif len(args) == 3:
    #         # Performs a component wise root sum square of two vectors (add in
    #         # quadrature).
    #         (a, b, buffer) = args
    #         i = computeNorm(a.i, b.i)
    #         j = computeNorm(a.j, b.j)
    #         k = computeNorm(a.k, b.k)
    #         return buffer.setTo(i, j, k)
    #     else:
    #         raise Exception
