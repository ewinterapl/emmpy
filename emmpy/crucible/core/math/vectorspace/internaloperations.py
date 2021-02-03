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
#com.google.common.base.Preconditions.checkElementIndex