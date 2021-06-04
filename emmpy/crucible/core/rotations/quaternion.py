"""emmpy.crucible.core.rotations.quaternion"""


from math import acos, cos, sin, sqrt

from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)
from emmpy.crucible.core.rotations.privilegedrotationmatrixijk import (
    PrivilegedRotationMatrixIJK
)
from emmpy.crucible.core.rotations.rotation import Rotation
from emmpy.utilities.doubletolongbits import doubleToLongBits


class Quaternion(Rotation):
    """Implementation of a rotational quaternion and the corresponding
    arithmetic algorithms.

    Note: this is not a general implementation of a quaternion, this class is
    solely focused on quaternions of unit length used to capture rotations.

    The quaternions constructed and presented by this class encapsulate
    rotations. As such, they are necessarily of length unity. The constructors
    normalize input to preserve this property to the best precision available
    in the Java native double type. Further, this class is writable for
    performance considerations. In an ideal world, it would be unwritable and
    each method resulting in a quaternion would be static and construct a new
    quaternion to encapsulate the output.

    The following text is taken from NAIF's QXQ routine (Note: this class
    implements the SPICE quaternion.)

    There are (at least) two popular "styles" of quaternions; these differ in
    the layout of the quaternion elements, the definition of the multiplication
    operation, and the mapping between the set of unit quaternions and
    corresponding rotation matrices.

    SPICE-style quaternions have the scalar part in the first component and the
    vector part in the subsequent components. The SPICE convention, along with
    the multiplication rules for SPICE quaternions, are those used by William
    Rowan Hamilton, the inventor of quaternions.

    Another common quaternion style places the scalar component last. This
    style is often used in engineering applications.

    The correspondence between SPICE quaternions and rotation matrices is
    defined as follows: Let R be a rotation matrix that transforms vectors from
    a right-handed, orthogonal reference frame F1 to a second right-handed,
    orthogonal reference frame F2. If a vector V has components x, y, z in the
    frame F1, then V has components x', y', z' in the frame F2, and R satisfies
    the relation:

        [ x' ]     [       ] [ x ]
        | y' |  =  |   R   | | y |
        [ z' ]     [       ] [ z ]

    Letting Q = (q0, q1, q2, q3) be the SPICE unit quaternion representing R,
    we have the relation:

            +-                                                          -+
            |           2    2                                           |
            | 1 - 2 ( q2 + q3 )    2 (q1 q2 - q0 q3)   2 (q1 q3 + q0 q2) |
            |                                                            |
            |                                                            |
            |                                2    2                      |
        R = | 2 (q1 q2 + q0 q3)    1 - 2 ( q1 + q3 )   2 (q2 q3 - q0 q1) |
            |                                                            |
            |                                                            |
            |                                                    2    2  |
            | 2 (q1 q3 - q0 q2)    2 (q2 q3 + q0 q1)   1 - 2 ( q1 + q2 ) |
            |                                                            |
            +-                                                          -+

    To map the rotation matrix R to a unit quaternion, we start by decomposing
    the rotation matrix as a sum of symmetric and skew-symmetric parts:

        R = [ I  +  (1-cos(theta)) OMEGA  ] + [ sin(theta) OMEGA ]
                     symmetric                   skew-symmetric

    OMEGA is a skew-symmetric matrix of the form:

                  +-             -+
                  |  0   -n3   n2 |
                  |               |
        OMEGA  =  |  n3   0   -n1 |
                  |               |
                  | -n2   n1   0  |
                  +-             -+

    The vector N of matrix entries (n1, n2, n3) is the rotation axis of R and
    theta is R's rotation angle. Note that N and theta are not unique.

    Let
        C = cos(theta/2)
        S = sin(theta/2)

    Then the unit quaternions Q corresponding to R are

        Q = +/- ( C, S*n1, S*n2, S*n3 )

    The mappings between quaternions and the corresponding rotations are
    carried out by the methods on this class:

    Quaternion.getRotation(RotationMatrixIJK) {quaternion to matrix}
    Quaternion.setTo(UnwritableRotationMatrixIJK) {matrix to quaternion}

    Quaternion.setTo(UnwritableRotationMatrixIJK)} always returns a quaternion
    with scalar part greater than or equal to zero.

    author F.S. Turner (APL)
    """

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Construct an identity quaternion.
            self.q0 = 1.0
            self.q1 = 0.0
            self.q2 = 0.0
            self.q3 = 0.0
        elif len(args) == 1:
            if isinstance(args[0], Quaternion):
                # Construct a copy of an existing quaternion.
                # param q the quaternion to copy.
                (q,) = args
                self.q0 = q.q0
                self.q1 = q.q1
                self.q2 = q.q2
                self.q3 = q.q3
            elif isinstance(args[0], UnwritableRotationMatrixIJK):
                # Construct a quaternion from a rotation matrix.
                # Note: as of the current release of this class, this method
                # does no checking to enforce that the input matrix is in fact
                # a rotation matrix.
                # If matrix rotates vectors by an angle of r radians about a
                # unit vector A, where r is in [0, pi], then if h = r/2,
                #    Q = ( cos(h), sin(h)A ,  sin(h)A ,  sin(h)A ).
                #                         1          2          3
                # The restriction that r must be in the range [0, pi]
                # determines the output quaternion Q uniquely except when
                # r = pi; in this special case, both of the quaternions:
                #    Q = ( 0,  A ,  A ,  A  )
                #               1    2    3
                # and:
                #    Q = ( 0, -A , -A , -A  )
                #               1    2    3
                # are possible outputs, if A is a choice of rotation axis for
                # matrix.
                # param matrix the rotation matrix from which to construct the
                # quaternion.
                (matrix,) = args
                self.setTo(matrix)
            else:
                raise Exception
        elif len(args) == 2:
            # Construct a quaternion from a rotation axis and angle specified
            # in radians.
            # Note: the rotation axis is normalized to unit length before
            # creating the quaternion.
            # param axis a vector containing the desired rotation axis.
            # param angle an angle, specified in radians, that determines the
            # magnitude of the rotation about axis.
            (axis, angle) = args
            self.setTo(axis, angle)
        elif len(args) == 4:
            # Construct a quaternion from a scalar and 3 vector components.
            # Note: this constructor normalizes the input components to enforce
            # the unity restriction.
            # param scalar the scalar component
            # param vector1 the ith vector component
            # param vector2 the jth vector component
            # param vector3 the kth vector component
            (scalar, vector1, vector2, vector3) = args
            self.setTo(scalar, vector1, vector2, vector3)
        else:
            raise Exception

    @staticmethod
    def multiply(*args):
        """Multiply two quaternions and store the result in a buffer.

        Quaternion r = Quaternion.multiply(a, b, new Quaternion());
        has the effect:
        r = a * b
        where a and b are represented as the sums of scalar (real) and vector
        (imaginary) parts as follows:
        a = as + av
        b = bs + bv
        then the resultant output quaternion stored in q is:
        r = os + ov
        where:
        os = as * bs + &lt;av, bv&gt;
        ov = as * bv + bs * av + av x bv
        and the notation <,> denotes the inner product operator and x denotes
        the cross product operator.

        param a the quaternion on the left of the multiplication operator
        param b the quaternion on the right of the multiplication operator
        param buffer a buffer to capture the results of the multiplication.
        Note: buffer may be a reference to either a or b.
        return a reference to buffer for convenience.
        """
        if len(args) == 2:
            (a, b) = args
            # Multiply two quaternions together and store the results in a
            # newly created quaternion.
            # param a the quaternion on the left of the multiplication operator
            # param b the quaternion on the right of the multiplication
            # operator
            # return a newly created quaternion containing the result of a*b.
            return Quaternion.multiply(a, b, Quaternion())
        elif len(args) == 3:
            # NAIF's quaternion implementation requires multiplication to be
            # carried out in the following manner:
            # q = ab
            # q0 = a0*b0 - <aV,bV> qV = a0*bV + b0*aV + (aV x bV)
            # where q0, a0, and b0 are the scalar components of q, a, and b
            # respectively; and qV, aV, and bV are the vector components of q,
            # a, and b respectively.
            (a, b, buffer) = args
            t0 = a.q0*b.q0 - a.q1*b.q1 - a.q2*b.q2 - a.q3*b.q3
            t1 = a.q0*b.q1 + b.q0*a.q1 + a.q2*b.q3 - a.q3*b.q2
            t2 = a.q0*b.q2 + b.q0*a.q2 - a.q1*b.q3 + a.q3*b.q1
            t3 = a.q0*b.q3 + b.q0*a.q3 + a.q1*b.q2 - a.q2*b.q1

            # Normalize the resultant output quaternion.
            scale = Quaternion.computeNorm(t0, t1, t2, t3)
            if scale == 0.0:
                buffer.q0 = 0.0
                buffer.q1 = 0.0
                buffer.q2 = 0.0
                buffer.q3 = 0.0
            # SHOULD BE AN else HERE
            buffer.q0 = t0/scale
            buffer.q1 = t1/scale
            buffer.q2 = t2/scale
            buffer.q3 = t3/scale
            return buffer
        else:
            raise Exception

    @staticmethod
    def computeNorm(q0, q1, q2, q3):
        """Computes the norm of four quaternion components in an overflow safe
        way.

        param q0 the scalar component
        param q1 the ith component
        param q2 the jth component
        param q3 the kth component
        return the length of the quaternion [q0,q1,q2,q3]
        """
        max_ = max(abs(q0), abs(q1), abs(q2), abs(q3))
        if max_ == 0.0:
            return 0.0
        q0 /= max_
        q1 /= max_
        q2 /= max_
        q3 /= max_
        return max_*sqrt(q0*q0 + q1*q1 + q2*q2 + q3*q3)

    def getScalar(self):
        """Retrieve the scalar component of the quaternion.

        return the scalar component of the quaternion which is the cosine of
        half the rotation angle.
        """
        return self.q0

    def getVector(self, buffer):
        """Retrieve the vector components of the quaternion.

        param buffer the vector memory to store the results. The vector
        components are simply the sine of half the rotation angle
        multiplied by the rotation axis.
        return a reference to the input vector for convenience.
        """
        buffer.setTo(self.q1, self.q2, self.q3)
        return buffer

    def getRotationAxis(self, buffer):
        """Extract the rotation axis from the quaternion.

        param buffer is the vector used to store the resultant axis of rotation
        represented by the quaternion. This axis is the axis of the smaller
        angle rotation, namely assuming that the angle of the rotation is
        bounded to [0, Pi]. Note: if the quaternion is the identity quaternion,
        this method simply selects the rotation axis to be (0, 0, 1). If the
        quaternion encodes a rotation of Pi radians, then both axis and -axis
        may be regarded as the rotational axis.
        return a reference to the input vector, axis for convenience.
        """

        # The vector components {q1, q2, q3} store the rotation axis, but have
        # been scaled by the sine of half the rotation angle. Just inject the
        # vector components into a vector and normalize to restore the unit
        # length rotation axis.
        buffer.setTo(self.q1, self.q2, self.q3)

        # Check to see if this is the identity quaternion, i.e. all of the
        # vector components are the zero vector.
        if buffer.getLength() == 0.0:
            buffer.setTo(0.0, 0.0, 1.0)
        else:
            buffer.unitize()

        # Lastly, check the sign of q0. If it is negative, then we have an axis
        # and a rotation of greater than Pi radians, flip the axis.
        if self.q0 < 0:
            buffer.negate()

        return buffer

    def getRotationAngle(self):
        """Retrieve the rotation angle from the quaternion.

        return the rotation angle, specified in radians. The angle returned is
        bounded between [0, Pi].
        """

        # The leading component of the quaternion is the cosine of half the
        # rotation angle. However, we need to account for the fact that a
        # quaternion and it's negative encode the same rotation. Return the
        # angle between [0,Pi].
        if self.q0 < 0:
            return 2*acos(-self.q0)
        else:
            return 2*acos(self.q0)

    def conjugate(self):
        """Conjugate a quaternion.

        The results are stored in the original instance.

        Conjugation negates the vector components of the quaternion,
        effectively altering the sense of the encapsulated rotation. In the
        rotation matrix world, it is the same as an inverse or transpose.
        return a reference to the quaternion for convenience.
        """

        # Just negate the vector components.
        self.q1 = -self.q1
        self.q2 = -self.q2
        self.q3 = -self.q3
        return self

    def negate(self):
        """Negate the entire quaternion.

        return a reference to the instance for convenience
        """
        self.q0 = -self.q0
        self.q1 = -self.q1
        self.q2 = -self.q2
        self.q3 = -self.q3
        return self

    def setTo(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Quaternion):
                # Copy the contents of one quaternion to another.
                # param q the quaternion to copy.
                # return a reference to the copied quaternion for convenience.
                (q,) = args
                self.q0 = q.q0
                self.q1 = q.q1
                self.q2 = q.q2
                self.q3 = q.q3
                return self
            elif isinstance(args[0], UnwritableRotationMatrixIJK):
                # The mathematics behind this routine are described here for
                # the convenience of the reader. The details are largely
                # unimportant, but it provides a framework for understanding
                # the implementation provided here. Note: this text is adapted
                # almost directly from NAIF's M2Q module.

                # If our quaternion is C, S1, S2, S3 (the S's being the
                # imaginary part) and we let

                #    CSi = C  * Si
                #    Sij = Si * Sj

                # then the rotation matrix corresponding to our quaternion is:

                #    R(1,1)      = 1.0D0 - 2*S22 - 2*S33
                #    R(2,1)      =         2*S12 + 2*CS3
                #    R(3,1)      =         2*S13 - 2*CS2
                #    R(1,2)      =         2*S12 - 2*CS3
                #    R(2,2)      = 1.0D0 - 2*S11 - 2*S33
                #    R(3,2)      =         2*S23 + 2*CS1
                #    R(1,3)      =         2*S13 + 2*CS2
                #    R(2,3)      =         2*S23 - 2*CS1
                #    R(3,3)      = 1.0D0 - 2*S11 - 2*S22

                # From the above we can see that:

                # TRACE = 3 - 4 * (S11 + S22 + S33)

                # so that

                #    1.0D0 + TRACE = 4 - 4*(S11 + S22 + S33)
                #                  = 4*(CC + S11 + S22 + S33)
                #                  - 4*(S11 + S22 + S33)
                #                  = 4*CC

                # Thus up to sign

                #    C = 0.5D0 * DSQRT( 1.0D0 + TRACE )

                # But we also have

                #    1.0D0 + TRACE - 2.0D0*R(i,i) = 4.0D0
                #                                 - 4.0D0(Sii + Sjj + Skk)
                #                                 - 2.0D0 + 4.0D0(Sjj + Skk)
                #                                 = 2.0D0 - 4.0D0*Sii

                # So that

                #    1.0D0 - TRACE + 2.0D0*R(i,i) = 4.0D0*Sii

                # and so up to sign

                #    Si = 0.5D0*DSQRT( 1.0D0 - TRACE + 2.0D0*R(i,i) )

                # in addition to this observation, we note that all of the
                # product pairs can easily be computed

                #     CS1 = (R(3,2) - R(2,3))/4.0D0
                #     CS2 = (R(1,3) - R(3,1))/4.0D0
                #     CS3 = (R(2,1) - R(1,2))/4.0D0
                #     S12 = (R(2,1) + R(1,2))/4.0D0
                #     S13 = (R(3,1) + R(1,3))/4.0D0
                #     S23 = (R(2,3) + R(3,2))/4.0D0

                # But taking sums or differences of numbers that are nearly
                # equal or nearly opposite results in a loss of precision. As a
                # result we should take some care in which terms to select when
                # computing C, S1, S2, S3. However, by simply starting with one
                # of the large quantities cc, S11, S22, or S33 we can make sure
                # that we use the best of the 6 quantities above when computing
                # the remaining components of the quaternion.

                # see Quaternion.Quaternion(UnwritableRotationMatrixIJK)
                (matrix,) = args
                trace = matrix.getII() + matrix.getJJ() + matrix.getKK()
                mtrace = 1.0 - trace
                cc4 = 1.0 + trace
                s114 = mtrace + 2*matrix.getII()
                s224 = mtrace + 2*matrix.getJJ()
                s334 = mtrace + 2*matrix.getKK()

                # Note that if you simply add:
                # cc4 + s114 + s224 + s334
                # you get four. Thus at least one of the terms is greater
                # than 1.
                if 1.0 <= cc4:
                    c = sqrt(cc4*0.25)
                    factor = 1.0/(c*4.0)
                    s1 = (matrix.getKJ() - matrix.getJK())*factor
                    s2 = (matrix.getIK() - matrix.getKI())*factor
                    s3 = (matrix.getJI() - matrix.getIJ())*factor
                elif 1.0 <= s114:
                    s1 = sqrt(s114*0.25)
                    factor = 1.0/(s1*4.0)
                    c = (matrix.getKJ() - matrix.getJK())*factor
                    s2 = (matrix.getIJ() + matrix.getJI())*factor
                    s3 = (matrix.getIK() + matrix.getKI())*factor
                elif 1.0 <= s224:
                    s2 = sqrt(s224*0.25)
                    factor = 1.0/(s2*4.0)
                    c = (matrix.getIK() - matrix.getKI())*factor
                    s1 = (matrix.getIJ() + matrix.getJI())*factor
                    s3 = (matrix.getJK() + matrix.getKJ())*factor
                else:
                    s3 = sqrt(s334*0.25)
                    factor = 1.0/(s3*4.0)
                    c = (matrix.getJI() - matrix.getIJ())*factor
                    s1 = (matrix.getIK() + matrix.getKI())*factor
                    s2 = (matrix.getJK() + matrix.getKJ())*factor

                # If the magnitude of this quaternion is not one, polish it up
                # a bit.
                l2 = c*c + s1*s1 + s2*s2 + s3*s3
                if l2 != 1.0:
                    polish = 1.0/sqrt(l2)
                    c = c*polish
                    s1 = s1*polish
                    s2 = s2*polish
                    s3 = s3*polish

                # Return a quaternion with the scalar component that is
                # positive. Other software in the rotations package may rely on
                # this. This does exactly what NAIF's M2Q routine does, but
                # should the boolean expression be: (c >= 0.0)? This results in
                # -0.0 being generated if the matrix would have a zero scalar
                # component.
                if c > 0.0:
                    self.q0 = c
                    self.q1 = s1
                    self.q2 = s2
                    self.q3 = s3
                else:
                    self.q0 = -c
                    self.q1 = -s1
                    self.q2 = -s2
                    self.q3 = -s3

                return self
            else:
                raise Exception
        elif len(args) == 2:
            # Construct a quaternion from a rotation axis and angle; store the
            # resultant quaternion in an existing one.
            # Note: the rotation axis is normalized to unit length before
            # assigning the components to the quaternion.
            # param axis a vector containing the desired rotation axis.
            # param angle an angle, specified in radians, that determines the
            # magnitude of the rotation about axis.
            # return a reference to the quaternion for convenience.
            (axis, angle) = args
            scale = sin(angle/2)/axis.getLength()
            self.q0 = cos(angle/2)
            self.q1 = scale*axis.getI()
            self.q2 = scale*axis.getJ()
            self.q3 = scale*axis.getK()
            return self
        elif len(args) == 4:
            # Sets the contents of the quaternion to match the supplied
            # quaternion components.
            # Note: the supplied components are normalized to ensure that the
            # quaternion is of unit length.
            # param q0 the scalar component
            # param q1 the ith component
            # param q2 the jth component
            # param q3 the kth component
            # return a reference to the instance for convenience
            (q0, q1, q2, q3) = args

            # Normalize the inputs to force the quaternion to be as close as
            # possible to unit length.
            factor = Quaternion.computeNorm(q0, q1, q2, q3)

            # Handle the zero quaternion case.
            if factor == 0.0:
                factor = 1.0

            self.q0 = q0/factor
            self.q1 = q1/factor
            self.q2 = q2/factor
            self.q3 = q3/factor
            return self
        else:
            raise Exception

    def getRotation(self, buffer):
        """Get the rotation matrix

        If a quaternion, Q, satisfies the equality:

            || Q ||   =  1

        * or equivalently

                  2          2          2          2
            Q(0)   +   Q(1)   +   Q(2)   +   Q(3)   =  1,

        then we can always find a unit vector A and a scalar r such that:

            Q = ( cos(r/2), sin(r/2)A(1), sin(r/2)A(2), sin(r/2)A(3) ).

        We can interpret A and r as the axis and rotation angle of a rotation
        in 3-space. If we restrict r to the range [0, pi], then r and A are
        uniquely determined, except if r = pi. In this special case, A and -A
        are both valid rotation axes.

        Every rotation is represented by a unique orthogonal matrix; this
        routine returns that unique rotation matrix corresponding to Q.
        Note: if the supplied quaternion is of zero length, the identity matrix
        is returned.

        The underlying mathematics employed by the implementation is spelled
        out in detail here for reference, but in practice may be ignored. The
        text and the method are adapted almost directly from NAIF's Q2M
        routine.

        If a matrix R represents a rotation of r radians about the unit vector
        n, we know that R can be represented as

                                               2
            I  +  sin(r) N  +  [ 1 - cos(r) ] N ,

        where N is the matrix that satisfies

            Nv = n x v

        for all vectors v, namely

                 +-                -+
                 |  0    -n     n   |
                 |         3     2  |
                 |                  |
            N =  |  n     0    -n   |.
                 |   3           1  |
                 |                  |
                 | -n     n     0   |
                 |   2     1        |
                 +-                -+

        Define S as

            sin(r/2) N,

        and let our input quaternion Q be

            ( q ,  q ,  q ,  q ).
               0    1    2    3

        Using the facts that

                                2
            1 - cos(r)  =  2 sin (r/2)

        and

            sin(r)      =  2 cos(r/2) sin(r/2),

        we can express R as

                                         2
            I  +  2 cos(r/2) S    +   2 S,

        or

                                   2
            I  +  2 q  S    +   2 S.
                     0

        Since S is just

            +-                -+
            |  0    -q     q   |
            |         3     2  |
            |                  |
            |  q     0    -q   |,
            |   3           1  |
            |                  |
            | -q     q     0   |
            |   2     1        |
            +-                -+

        our expression for R comes out to

            +-                                                         -+
            |          2   2                                            |
            | 1 - 2 ( q + q  )    2( q q  -  q q )     2 ( q q  + q q ) |
            |          2   3          1 2     0 3           1 3    0 2  |
            |                                                           |
            |                              2   2                        |
            | 2( q q  +  q q )    1 - 2 ( q + q  )     2 ( q q  - q q ) |.
            |     1 2     0 3              1   3            2 3    0 1  |
            |                                                           |
            |                                                   2   2   |
            | 2( q q  -  q q )    2 ( q q  + q q )     1 - 2 ( q + q  ) |
            |     1 3     0 2          2 3    0 1               1   2   |
            +-                                                         -+
        """
        q01 = self.q0*self.q1
        q02 = self.q0*self.q2
        q03 = self.q0*self.q3
        q12 = self.q1*self.q2
        q13 = self.q1*self.q3
        q23 = self.q2*self.q3
        q1s = self.q1*self.q1
        q2s = self.q2*self.q2
        q3s = self.q3*self.q3

        # Sharpen the computation by effectively converting this quaternion to
        # a unit quaternion if it is not already one.
        l2 = self.q0*self.q0 + q1s + q2s + q3s
        if l2 != 1.0 and l2 != 0.0:
            sharpen = 1.0/l2
            q01 = q01*sharpen
            q02 = q02*sharpen
            q03 = q03*sharpen
            q12 = q12*sharpen
            q13 = q13*sharpen
            q23 = q23*sharpen
            q1s = q1s*sharpen
            q2s = q2s*sharpen
            q3s = q3s*sharpen

        # Now inject the results into the public fields of matrix directly.
        # Note that the individual components of matrix are laid out in this
        # fashion: +- -+ | ii ij ik | buffer = | ji jj jk | | ki kj kk | +- -+
        assigner = PrivilegedRotationMatrixIJK()
        assigner.setToWithoutCheck(
            1.0 - 2.0*(q2s + q3s), 2.0*(q12 + q03), 2.0*(q13 - q02),
            2.0*(q12 - q03), 1.0 - 2.0*(q1s + q3s), 2.0*(q23 + q01),
            2.0*(q13 + q02), 2.0*(q23 - q01), 1.0 - 2.0*(q1s + q2s))
        buffer.setTo(assigner)
        return buffer

    def hashCode(self):
        prime = 31
        result = 1
        temp = doubleToLongBits(self.q0)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.q1)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.q2)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.q3)
        result = prime*result + temp ^ (temp >> 32)
        return result

    def equals(self, obj):
        """Equality test

        Note: this considers the equality of the components only in the
        comparison. It is possible that the components, while different capture
        precisely the same rotation. This method only evaluates whether the
        individual components are identical. Note, classes that derive from
        this class may be considered equal to instances of the parent if they
        have identical fields. This method uses instanceof in its determination
        of whether to proceed, not Class comparison.
        """
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, Quaternion):
            return False
        other = obj
        if (doubleToLongBits(self.q0) !=
            doubleToLongBits(other.q0)):
            return False
        if (doubleToLongBits(self.q1) !=
            doubleToLongBits(other.q1)):
            return False
        if (doubleToLongBits(self.q2) !=
            doubleToLongBits(other.q2)):
            return False
        if (doubleToLongBits(self.q3) !=
            doubleToLongBits(other.q3)):
            return False
        return True

    def toString(self):
        return "[%s %s %s %s]" % (self.q0, self.q1, self.q2, self.q3)
