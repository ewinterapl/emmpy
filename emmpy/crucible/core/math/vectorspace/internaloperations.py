"""Utility methods for other vectorspace classes.

This module provides functions that support the implementation
of methods of the various other classes provided in this package.

Maintainer Note: This class is an implementation detail of the classes and
methods provided by this package as a whole. Functionality present here
should not be exposed outside of this package. Further, as methods defined
here may be invoked from any class in this package, it must remain free of
references to all other classes in this package. In other words, it is at
the absolute bottom of the package layering structure.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


def absMaxComponent(*args) -> float:
    """Compute the absolute value of the largest of a group of numbers.

    Determine the largest component by magnitude, and return it absolte
    value.

    Parameters
    ----------
    *args : float
        Arbitrary number of floats.

    Returns
    -------
    max(abs(x)) : float
        Absolute value of the largest number in args.
    """
    return max(abs(x) for x in args)


def checkRotation(*args) -> None:
    """Determine if the values of matrix are a rotation.

    Determine if the values of a column-major matrix composed of the
    arguments constitute a valid rotation matrix. If so, take no action.
    If not, raise a MalformedRotationException.

    Parameters
    ----------
    ii, ji, ij, jj : float
        2-D matrix components in column-major order.
    OR
    ii, ji, ki, ij, jj, kj, ik, jk, kk : float
        3-D matrix components in column-major order.
    normTolerance : float
        Tolerance relative to unity for matrix norm calculation.
    detTolerance : float
        Tolerance relative to unity for determinant calculation.
    
    Returns
    -------
    None

    Raises
    ------
    MalformedRotationException
        If the supplied components do not form a valid rotation matrix
        under the specified tolerances.
    ValueError
        If incorrect parameters are provided.
    """
    if len(args) == 6:
        # 2-D matrix
        (ii, ji, ij, jj, normTolerance, detTolerance) = args
        # Verify the first column has unit norm.
        norm = np.linalg.norm([ii, ji])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
        # Verify the second column has unit norm.
        norm = np.linalg.norm([ij, jj])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
        # Verify the matrix has unit determinant.
        a = np.array([ii, ij, ji, jj]).reshape(2, 2)
        det = np.linalg.det(a)
        if abs(det) > 1 + normTolerance:
            raise MalformedRotationException
    elif len(args) == 11:
        # 3-D matrix.
        (ii, ji, ki, ij, jj, kj, ik, jk, kk,
         normTolerance, detTolerance) = args
        # Verify the first column has unit norm.
        norm = np.linalg.norm([ii, ji, ki])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
        # Verify the second column has unit norm.
        norm = np.linalg.norm([ij, jj, kj])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
        # Verify the third column has unit norm.
        norm = np.linalg.norm([ik, jk, kk])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
        # Verify the matrix has unit determinant.
        a = np.array([ii, ij, ik, ji, jj, jk, ki, kj, kk]).reshape(3, 3)
        det = np.linalg.det(a)
        if abs(det) > 1 + normTolerance:
            raise MalformedRotationException
    else:
        raise ValueError
