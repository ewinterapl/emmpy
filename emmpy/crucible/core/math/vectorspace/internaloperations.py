from math import sqrt

# Class providing various static methods that support the implementation of methods of the various
# other classes provided in this package.
# <p>
# <b>Maintainer Note:</b>This class is an implementation detail of the classes and methods provided
# by this package as a whole. Functionality present here should not be exposed outside of this
# package. Further, as methods defined here may be invoked from any class in this package, it must
# remain free of references to all other classes in this package. In other words, it is at the
# absolute bottom of the package layering structure.
# </p>
# 
# @author F.S.Turner

class InternalOperations:

    # Computes the absolute value of the largest, magnitude, component of a vector expressed in three
    # individual components.
    # @param i the ith component
    # @param j the jth component
    # @param k the kth component
    # @return the absolute value of the largest, in magnitude, component of the vector [i,j,k].
    @staticmethod
    def absMaxComponent(i, j, k):
        return max(abs(i), max(abs(j), abs(k)))

    # Method that computes the norm of a vector expressed as three separate components. This method
    # is marked with package access to allow other classes in the vector arithmetic toolkit to
    # utilize it.
    # @param i the ith component
    # @param j the jth component
    # @param k the kth component
    # @return the length of the [i,j,k] vector
    @staticmethod
    def computeNorm(i, j, k):
        max = InternalOperations.absMaxComponent(i, j, k)

        # If max is 0, then vector is clearly the zero vector.
        if max == 0.0:
            return 0.0

        i /= max
        j /= max
        k /= max

        # Since we're trying to avoid overflow in the square root:
        return max * sqrt(i * i + j * j + k * k)

    #   /**
    #    * Determine if the components of a three by three matrix constitute a rotation.
    #    * 
    #    * @param ii ith row, ith column element
    #    * @param ji jth row, ith column element
    #    * @param ki kth row, ith column element
    #    * @param ij ith row, jth column element
    #    * @param jj jth row, jth column element
    #    * @param kj kth row, jth column element
    #    * @param ik ith row, kth column element
    #    * @param jk jth row, kth column element
    #    * @param kk kth row, kth column element
    #    * @param normTolerance tolerance off of unity for the magnitude of the column vectors
    #    * @param detTolerance tolerance off of unity for the determinant of the matrix
    #    * 
    #    * @throws MalformedRotationException if the supplied components do not adequately describe a
    #    *         rotation given the supplied tolerances
    #    */
    @classmethod
    def checkRotation(cls, ii, ji, ki, ij, jj, kj, ik, jk, kk, normTolerance, detTolerance):
        #       throws MalformedRotationException {

        testVal = cls.computeNorm(ii, ji, ki)
        if (testVal < 1.0 - normTolerance) or (testVal > 1.0 + normTolerance):
            raise Exception("Matrix's ith column is not sufficiently close to unit length.")
            # throw new MalformedRotationException(
                # "Matrix's ith column is not sufficiently close to unit length.");

        #     testVal = computeNorm(ij, jj, kj);
        #     if ((testVal < 1.0 - normTolerance) || (testVal > 1.0 + normTolerance)) {
        #       throw new MalformedRotationException(
        #           "Matrix's jth column is not sufficiently close to unit length.");
        #     }

        #     testVal = computeNorm(ik, jk, kk);
        #     if ((testVal < 1.0 - normTolerance) || (testVal > 1.0 + normTolerance)) {
        #       throw new MalformedRotationException(
        #           "Matrix's kth column is not sufficiently close to unit length.");
        #     }

        #     testVal = computeDeterminant(ii, ji, ki, ij, jj, kj, ik, jk, kk);

        #     if ((testVal < 1.0 - detTolerance) || (testVal > 1.0 + detTolerance)) {
        #       throw new MalformedRotationException(
        #           "Matrix's determinant is not sufficiently close to unity.");
        #     }

        #   }
