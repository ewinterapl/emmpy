"""Utility methods for other vectorspace classes.

Module providing various static methods that support the implementation
of methods of the various other classes provided in this package.

<b>Maintainer Note:</b>This class is an implementation detail of the
classes and methods provided by this package as a whole. Functionality
present here should not be exposed outside of this package. Further, as
methods defined here may be invoked from any class in this package, it must
remain free of references to all other classes in this package. In other
words, it is at the absolute bottom of the package layering structure.

@author F.S.Turner
"""


import numpy as np
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


def absMaxComponent(*args) -> float:
    """Compute the absolute value of the largest component .

    @param i the ith component
    @param j the jth component
    @param k the kth component
    @return the absolute value of the largest, in magnitude, component of
    the vector [i,j,k].
    """
    if len(args) not in (2, 3):
        raise Exception
    return max(abs(x) for x in args)


def checkRotation(*args) -> None:
    """Determine if a 3x3 matrix is a rotation.

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
        testVal = np.linalg.norm([ii, ji])
        if (testVal < 1.0 - normTolerance) or (testVal > 1.0 + normTolerance):
            raise MalformedRotationException(
                "Matrix's ith column is not sufficiently close to unit " +
                "length.")
        testVal = np.linalg.norm([ij, jj])
        if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                normTolerance)):
            raise MalformedRotationException(
                "Matrix's jth column is not sufficiently close to unit " +
                "length.")
        testVal = np.linalg.det(np.array([ii, ij, ji, jj])).reshape((2, 2))
        if ((testVal < 1.0 - detTolerance) or (testVal > 1.0 + detTolerance)):
            raise MalformedRotationException(
                "Matrix's determinant is not sufficiently close to unity.")
    elif len(args) == 11:
        (ii, ji, ki, ij, jj, kj, ik, jk, kk,
            normTolerance, detTolerance) = args
        testVal = np.linalg.norm([ii, ji, ki])
        if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                normTolerance)):
            raise MalformedRotationException(
                "Matrix's ith column is not sufficiently close to unit " +
                "length.")
        testVal = np.linalg.norm([ij, jj, kj])
        if ((testVal < 1.0 - normTolerance) or (testVal > 1.0 +
                                                normTolerance)):
            raise MalformedRotationException(
                "Matrix's jth column is not sufficiently close to unit " +
                "length."
            )
        testVal = np.linalg.norm([ik, jk, kk])
        if (testVal < 1.0 - normTolerance) or (testVal > 1.0 + normTolerance):
            raise MalformedRotationException(
                "Matrix's kth column is not sufficiently close to unit " +
                "length."
            )
        testVal = np.linalg.det(np.array([ii, ij, ik, ji, jj, jk, ki, kj, kk]).reshape((3, 3)))
        if ((testVal < 1.0 - detTolerance) or (testVal > 1.0 + detTolerance)):
            raise MalformedRotationException(
                "Matrix's determinant is not sufficiently close to unity.")
