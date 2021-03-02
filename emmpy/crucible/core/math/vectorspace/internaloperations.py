"""internaloperations.py
"""


from math import sqrt

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class InternalOperations:
    """Class providing various static methods that support the implementation
    of methods of the various other classes provided in this package.

    <b>Maintainer Note:</b>This class is an implementation detail of the
    classes and methods provided by this package as a whole. Functionality
    present here should not be exposed outside of this package. Further, as
    methods defined here may be invoked from any class in this package, it must
    remain free of references to all other classes in this package. In other
    words, it is at the absolute bottom of the package layering structure.

    @author F.S.Turner
    """

    @staticmethod
    def absMaxComponent(*args) -> float:
        """Computes the absolute value of the largest, magnitude, component of
        a vector expressed in three individual components.
        @param i the ith component
        @param j the jth component
        @param k the kth component
        @return the absolute value of the largest, in magnitude, component of
        the vector [i,j,k].
        """
        if len(args) not in (2, 3):
            raise Exception
        return max(abs(x) for x in args)

    @staticmethod
    def computeNorm(*args) -> float:
        """Method that computes the norm of a vector expressed as three
        separate components. This method is marked with package access to allow
        other classes in the vector arithmetic toolkit to utilize it.
        @param i the ith component
        @param j the jth component
        @param k the kth component
        @return the length of the [i,j,k] vector
        """
        if len(args) == 2:
            (i, j) = args
            max = InternalOperations.absMaxComponent(i, j)
            # If max is 0, then vector is clearly the zero vector.
            if max == 0.0:
                return 0.0
            i /= max
            j /= max
            # Since we're trying to avoid overflow in the square root:
            return max*sqrt(i*i + j*j)
        elif len(args) == 3:
            (i, j, k) = args
            max = InternalOperations.absMaxComponent(i, j, k)
            # If max is 0, then vector is clearly the zero vector.
            if max == 0.0:
                return 0.0
            i /= max
            j /= max
            k /= max
            # Since we're trying to avoid overflow in the square root:
            return max*sqrt(i*i + j*j + k*k)
        else:
            raise Exception

    @staticmethod
    def checkRotation(*args) -> None:
        """Determine if the components of a three by three matrix constitute a
        rotation.

        @param ii ith row, ith column element
        @param ji jth row, ith column element
        @param ki kth row, ith column element
        @param ij ith row, jth column element
        @param jj jth row, jth column element
        @param kj kth row, jth column element
        @param ik ith row, kth column element
        @param jk jth row, kth column element
        @param kk kth row, kth column element
        @param normTolerance tolerance off of unity for the magnitude of the
        column vectors
        @param detTolerance tolerance off of unity for the determinant of the
        matrix

        @throws MalformedRotationException if the supplied components do not
        adequately describe a rotation given the supplied tolerances
        """
        if len(args) == 8:
            (ii, ji, ij, jj, normTolerance, detTolerance) = args
            testVal = InternalOperations.computeNorm(ii, ji)
            if (testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                   normTolerance):
                raise MalformedRotationException(
                    "Matrix's ith column is not sufficiently close to unit " +
                    "length.")
            testVal = InternalOperations.computeNorm(ij, jj)
            if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                    normTolerance)):
                raise MalformedRotationException(
                    "Matrix's jth column is not sufficiently close to unit " +
                    "length.")
            testVal = InternalOperations.computeDeterminant(ii, ji, ij, jj)
            if ((testVal < 1.0 - detTolerance) or (testVal > 1.0 +
                                                   detTolerance)):
                raise MalformedRotationException(
                    "Matrix's determinant is not sufficiently close to unity.")
        elif len(args) == 11:
            (ii, ji, ki, ij, jj, kj, ik, jk, kk,
             normTolerance, detTolerance) = args
            testVal = InternalOperations.computeNorm(ii, ji, ki)
            if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                    normTolerance)):
                raise MalformedRotationException(
                    "Matrix's ith column is not sufficiently close to unit " +
                    "length.")
            testVal = InternalOperations.computeNorm(ij, jj, kj)
            if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                    normTolerance)):
                raise MalformedRotationException(
                    "Matrix's jth column is not sufficiently close to unit " +
                    "length."
                )
            testVal = InternalOperations.computeNorm(ik, jk, kk)
            if (testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                   normTolerance):
                raise MalformedRotationException(
                    "Matrix's kth column is not sufficiently close to unit " +
                    "length."
                )
            testVal = InternalOperations.computeDeterminant(ii, ji, ki,
                                                            ij, jj, kj,
                                                            ik, jk, kk)
            if ((testVal < 1.0 - detTolerance) or (testVal > 1.0 +
                                                   detTolerance)):
                raise MalformedRotationException(
                    "Matrix's determinant is not sufficiently close to unity.")

    def computeDeterminant(*args) -> float:
        """Computes the determinant of a three by three matrix described by the
        supplied components.

        @param ii ith row, ith column element
        @param ji jth row, ith column element
        @param ki kth row, ith column element
        @param ij ith row, jth column element
        @param jj jth row, jth column element
        @param kj kth row, jth column element
        @param ik ith row, kth column element
        @param jk jth row, kth column element
        @param kk kth row, kth column element

        @return the determinant of the matrix described by the supplied
        components.

        TODO: Consider scaling the components by the largest component and then
        evaluating the determinant function. This may enhance numerical
        precision.
        """
        if len(args) == 4:
            (ii, ji, ij, jj) = args
            # TODO: Consider scaling the components by the largest component
            # and then evaluating the determinant function. This may enhance
            # numerical precision.
            return ii*jj - ji*ij
        elif len(args) == 9:
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            return ii*(jj*kk - jk*kj) - ij*(ji*kk - jk*ki) + ik*(ji*kj - jj*ki)
