"""emmpy.crucible.core.math.vectorspace.vectorij"""


from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    computeNorm
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.utilities.isrealnumber import isRealNumber


class VectorIJ(UnwritableVectorIJ):
    """Writable subclass of the unwritable 2D vector parent completing the
    implementation of the weak immutability design pattern.

    This class contains the mutator methods necessary to set or alter the
    internals of the parent classes fields.

    This was a simple copy and paste of the {@link VectorIJK} class. The cross
    product methods return a {@link VectorIJK}.

    TODO add rotation methods if when needed

    @author G.K.Stephens copy and extension of F.S.Turner
    """

    # The ZERO vector.
    ZERO = UnwritableVectorIJ(0, 0)

    # The I basis vector: (1,0).
    I = UnwritableVectorIJ(1, 0)

    # The J basis vector: (0,1).
    J = UnwritableVectorIJ(0, 1)

    # The negative of the I basis vector: (-1,0).
    MINUS_I = UnwritableVectorIJ(-1, 0)

    # The negative of the J basis vector: (0,-1).
    MINUS_J = UnwritableVectorIJ(0, -1)

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Construct a vector with an initial value of 0.
            UnwritableVectorIJ.__init__(self, 0.0, 0.0)
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a vector from the first two elements of an array
                # of doubles.
                (data,) = args
                UnwritableVectorIJ.__init__(self, data)
            elif isinstance(args[0], VectorIJ):
                # Copy constructor, creates a vector by copying the values of
                # a pre-exisiting one.
                (vector,) = args
                UnwritableVectorIJ.__init__(self, vector)
            else:
                raise Exception
        elif len(args) == 2:
            if isRealNumber(args[0]) and isRealNumber(args[1]):
                # Constructs a vector from two basic components.
                (i, j) = args
                UnwritableVectorIJ.__init__(self, i, j)
            elif isinstance(args[0], int) and isinstance(args[1], list):
                # Constructs a vector from the two elements of an array of
                # double starting with the offset index.
                (offset, data) = args
                UnwritableVectorIJ.__init__(self, offset, data)
            elif isRealNumber(args[0]) and isinstance(args[1], VectorIJ):
                # Scaling constructor, creates a new vector by applying a
                # scalar multiple to the components of a pre-existing vector.
                # This results in (scale*vector) being stored in the newly
                # constructed vector.
                (scale, vector) = args
                UnwritableVectorIJ.__init__(self, scale, vector)
            else:
                raise Exception
        else:
            raise CrucibleRuntimeException

    def createUnitized(self):
        """Note: this method is overridden to return an instance of the
        writable subclass rather than the unwritable parent.
        """
        return VectorIJ(self).unitize()

    def createNegated(self):
        """Note: this method is overridden to return an instance of the
        writable subclass rather than the unwritable parent."""
        return VectorIJ(self).negate()

    def scale(self, scale: float):
        """Scale the vector.

        @param scale the scale factor to apply.
        @return a reference to the instance for convenience, which now contains
        (scale*this)
        """
        self.i *= scale
        self.j *= scale
        return self

    def unitize(self):
        """Unitize the vector.

        @return a reference to the instance for convenience, which now contains
        a vector of unit length in the direction of the original vector.
        @throws UnsupportedOperationException if the vector is equal to
        {@link VectorIJ#ZERO}
        """
        norm = computeNorm(self.i, self.j)
        if norm == 0.0:
            raise Exception(
                "Unable to unitize vector. Instance is zero length.")
        self.i /= norm
        self.j /= norm
        return self

    def negate(self):
        """Negate the vector.

        @return a reference to the instance, now containing -vector.
        """
        self.i *= -1
        self.j *= -1
        return self

    def clear(self):
        """Clear the vector.

        @return a reference to the instance, now containing
        {@link VectorIJ#ZERO}
        """
        self.i = 0
        self.j = 0
        return self

    def setI(self, i: float):
        """Sets the ith component of the vector.

        @param i the ith component
        """
        self.i = i

    def setJ(self, j: float):
        """Sets the jth component of the vector.

        @param j the jth component
        """
        self.j = j

    def set(self, index: int, value: float):
        """Sets the specified component of the vector to a supplied value.

        @param index the index of the component to set. 0 = ith, 1 = jth.
        @param value the value with which to replace the specified component
        @throws IndexOutOfBoundsException if an invalid index, outside the
        range [0,1], is specified.
        """
        if index == 0:
            self.i = value
        elif index == 1:
            self.j = value
        else:
            raise BugException

    def setTo(self, *args):
        """Set the vector contents to match those of another."""
        if len(args) == 1:
            if isinstance(args[0], VectorIJ):
                # Copy values from existing vector.
                (vector,) = args
                self.i = vector.i
                self.j = vector.j
                return self
            elif isinstance(args[0], list):
                # Copy values from first 2 elements of a list.
                (data,) = args
                self.setTo(data[0], data[1])
                return self
            else:
                raise Exception
        elif len(args) == 2:
            if isRealNumber(args[0]) and isinstance(args[1], VectorIJ):
                # Set by scaling an existing vector.
                (scale, vector) = args
                self.i = scale*vector.i
                self.j = scale*vector.j
                return self
            elif isinstance(args[0], int) and isinstance(args[1], list):
                # Set with 2 values at index into a list.
                (index, data) = args
                self.setTo(data[index], data[index + 1])
                return self
            elif isRealNumber(args[0]) and isRealNumber(args[1]):
                (i, j) = args
                self.i = i
                self.j = j
                return self
            else:
                raise Exception
        else:
            raise CrucibleRuntimeException

    def setToUnitized(self, vector):
        """Sets the vector content to the a unit length version of another.

        @param vector the vector whose contents are to be unitized and stored
        in the instance
        @return a reference to the instance
        @throws UnsupportedOperationException if the supplied vector argument
        is {@link VectorIJ#ZERO}
        """
        self.setTo(vector)
        self.unitize()
        return self

    def setToNegated(self, vector):
        """Sets the vector content to a negated version of another.

        @param vector the vector whose contents are to be negated and stored
        in the instance
        @return a reference to the instance
        """
        self.setTo(vector)
        return self.negate()

    def asVectorIJK(self, *args):
        """Wraps this vector as a new {@link VectorIJK}. K is zero.
        @return a new {@link VectorIJK}
        """
        if len(args) == 0:
            return self.asVectorIJK(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            buffer.setI(self.i)
            buffer.setJ(self.j)
            buffer.setK(0)
            return buffer
        else:
            raise Exception

    @staticmethod
    def lineProject(*args):
        """Compute the projection of one vector onto the line normal to
        another.

        Algebraicly, this routine effectively computes:

                                   <vector, to> * to
                          vector - -----------------
                                      || to ||

        where <> denotes the standard scalar product and ||x|| the norm of x.
        For numeric precision reasons the implementation may vary slightly from
        the above prescription.

        @param vector the vector to project
        @param normal the normal to the line to project vector onto
        @return a new <code>VectorIJ</code> containing the results of the
        projection
        @throws IllegalArgumentException if normal is equal to {@link ZERO}
        @see lineProject
        """
        if len(args) == 2:
            (vector, normal) = args
            return VectorIJ.lineProject(vector, normal, VectorIJ())
        elif len(args) == 3:
            (vector, normal, buffer) = args
            maxVector = absMaxComponent(vector.i, vector.j)

            # There are two unusual cases that require special treatment. The
            # first is if the normal vector is the zero vector. Fortunately,
            # the necessary exception is generated by the project() method. So,
            # start by performing the necessary projection. Buffer the
            # components of vector, in case buffer and vector are the same
            # object.
            vi = vector.i
            vj = vector.j

            VectorIJ.project(vector, normal, buffer)

            # The second unusual case is when vector itself is zero. This is
            # simple enough, the zero vector projects as the zero vector.
            if maxVector == 0.0:
                buffer.clear()
                return buffer

            # Scale buffer and the v components by 1.0/maxVector to bring them
            # closer to similar magnitudes.
            vi /= maxVector
            vj /= maxVector
            buffer.i /= maxVector
            buffer.j /= maxVector

            # Subtract buffer from the v components to place the result in the
            # line.
            buffer.i = vi - buffer.i
            buffer.j = vj - buffer.j

            # Rescale the result.
            buffer.scale(maxVector)
            return buffer
        else:
            raise Exception

    @staticmethod
    def project(*args):
        """Compute the projection of one vector onto another.

        Algebraically, this routine effectively computes:

                          <vector, onto> * onto
                          ---------------------
                               || onto ||

        where <> denotes the standard scalar product and ||x|| the norm of x.
        For numeric precision reasons the implementation may vary slightly from
        the above prescription.

        @param vector the vector to project
        @param onto the vector onto which vector is to be projected
        @return a new <code>VectorIJ</code> containing the results of the
        projection
        OR
        @param buffer the buffer to receive the contents of the projection

        @throws IllegalArgumentException if onto is the equal to {@link ZERO}.
        @see project
        """
        if len(args) == 2:
            (vector, onto) = args
            return VectorIJ.project(vector, onto, VectorIJ())
        elif len(args) == 3:
            (vector, onto, buffer) = args
            maxVector = absMaxComponent(vector.i, vector.j)
            maxOnto = absMaxComponent(onto.i, onto.j)
            if maxOnto == 0:
                raise Exception(
                    "Unable to project vector onto the zero vector.")
            if maxVector == 0:
                buffer.clear()
                return buffer
            r1 = onto.i/maxOnto
            r2 = onto.j/maxOnto
            t1 = vector.i/maxVector
            t2 = vector.j/maxVector
            scaleFactor = (t1*r1 + t2*r2)*maxVector/(r1*r1 + r2*r2)
            buffer.i = r1
            buffer.j = r2
            buffer.scale(scaleFactor)
            return buffer
        else:
            raise BugException

    @staticmethod
    def combine(*args):
        """Linearly combine vectors.

        @param scaleA the scale factor for vector a
        @param a a vector
        @param scaleB the scale vector for vector b
        @param b another vector
        @param scaleC the scale factor for vector c
        @param c the third vector
        @param buffer the buffer to receive the results of the combination

        @return a new <code>VectorIJ</code> which now contains
        ( scaleA*a + scaleB*b + scaleC*c )

        @see combine
        """
        if len(args) == 4:
            (scaleA, a, scaleB, b) = args
            return VectorIJ.combine(scaleA, a, scaleB, b, VectorIJ())
        elif len(args) == 5:
            (scaleA, a, scaleB, b, buffer) = args
            buffer.i = scaleA*a.i + scaleB*b.i
            buffer.j = scaleA*a.j + scaleB*b.j
            return buffer
        elif len(args) == 6:
            (scaleA, a, scaleB, b, scaleC, c) = args
            return VectorIJ.combine(scaleA, a, scaleB, b, scaleC, c,
                                    VectorIJ())
        elif len(args) == 7:
            (scaleA, a, scaleB, b, scaleC, c, buffer) = args
            buffer.i = scaleA*a.i + scaleB*b.i + scaleC*c.i
            buffer.j = scaleA*a.j + scaleB*b.j + scaleC*c.j
            return buffer
        else:
            raise Exception

    @staticmethod
    def uCross(*args):
        """Compute the cross product of a and b; unitize the result.

        @param a the left hand vector to cross
        @param b the right hand vector to cross
        @param buffer the buffer to receive the contents of the unitized cross
        product

        @return a new <code>VectorIJ</code> which now contains
        (a x b)/||a||/||b||.

        @throws IllegalArgumentException if either a or b are equivalent to
        the {@link ZERO}
        @throws UnsupportedOperationException if the result of crossing a with
        b results in {@link ZERO}

        @see uCross
        """
        if len(args) == 2:
            (a, b) = args
            return VectorIJ.uCross(a, b, VectorIJK())
        elif len(args) == 3:
            (a, b, buffer) = args
            # We should scale each vector by its maximal component.
            amax = absMaxComponent(a.i, a.j)
            bmax = absMaxComponent(b.i, b.j)
            if amax == 0.0 or bmax == 0.0:
                raise Exception(
                    "At least one input vector is of zero" +
                    " length. Unable to unitize resultant" +
                    " cross product.")
            ti = 0.0
            tj = 0.0
            tk = (a.i/amax)*(b.j/bmax) - (a.j/amax)*(b.i/bmax)
            buffer.setI(ti)
            buffer.setJ(tj)
            buffer.setK(tk)
            return buffer.unitize()
        else:
            raise Exception

    @staticmethod
    def cross(*args):
        """Compute the cross product of a and b.

        @param a the left hand vector to cross
        @param b the right hand vector to cross
        @param buffer the buffer to receive the contents of the cross product

        @return a new <code>VectorIJK</code> which now contains (a x b)

        @see cross
        """
        if len(args) == 2:
            (a, b) = args
            return VectorIJ.cross(a, b, VectorIJK())
        elif len(args) == 3:
            (a, b, buffer) = args
            ti = 0.0
            tj = 0.0
            tk = a.i*b.j - a.j*b.i
            buffer.setI(ti)
            buffer.setJ(tj)
            buffer.setK(tk)
            return buffer
        else:
            raise Exception

    @staticmethod
    def subtract(*args):
        """Subtract one vector from another.

        @param a the minuend
        @param b the subtrahend
        @param buffer the buffer to receive the results of the subtraction

        @return a new <code>VectorIJ</code> which now contains (a - b)

        @see subtract
        """
        if len(args) == 2:
            (a, b) = args
            return VectorIJ.subtract(a, b, VectorIJ())
        elif len(args) == 3:
            (a, b, buffer) = args
            buffer.i = a.i - b.i
            buffer.j = a.j - b.j
            return buffer
        else:
            raise Exception

    @staticmethod
    def add(*args):
        """Add two vectors.

        @param a a vector
        @param b another vector
        @param buffer the buffer to receive the results of the addition

        @return a new <code>VectorIJ</code> which now contains (a + b).

        @see add
        """
        if len(args) == 2:
            (a, b) = args
            return VectorIJ.add(a, b, VectorIJ())
        elif len(args) == 3:
            (a, b, buffer) = args
            buffer.i = a.i + b.i
            buffer.j = a.j + b.j
            return buffer
        else:
            raise Exception

    @staticmethod
    def addAll(*args):
        """Adds all the vectors in an {@link Iterable} of vectors.

        @param vectors an {@link Iterable} of vectors to be added
        @param buffer the buffer to receive the results of the addition

        @return a reference to buffer for convenience which now contains
        (a + b + ... + n).
        """
        if len(args) == 1:
            (vectors,) = args
            return VectorIJ.addAll(vectors, VectorIJ())
        elif len(args) == 2:
            (vectors, buffer) = args
            sumI = 0.0
            sumJ = 0.0
            for vector in vectors:
                sumI += vector.i
                sumJ += vector.j
            return buffer.setTo(sumI, sumJ)
        else:
            raise Exception

    @staticmethod
    def addRSS(*args):
        """Performs a component wise root sum square of two vectors (add in
        quadrature).

        @param a a vector
        @param b another vector
        @param buffer the buffer to receive the results of the root sum square

        @return a new <code>VectorIJ</code> which now contains
        (sqrt(a.i + b.i) , sqrt(a.j + b.j).

        @see VectorIJ#addRSS(UnwritableVectorIJ, UnwritableVectorIJ, VectorIJ)
        """
        if len(args) == 2:
            (a, b) = args
            return VectorIJ.addRSS(a, b, VectorIJ())
        elif len(args) == 3:
            (a, b, buffer) = args
            i = computeNorm(a.i, b.i)
            j = computeNorm(a.j, b.j)
            return buffer.setTo(i, j)
        else:
            raise Exception
