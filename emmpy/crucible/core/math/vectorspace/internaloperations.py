"""Utility methods for other vectorspace classes.

This module provides functions that support the implementation
of methods of the various other classes provided in this package.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


def absMaxComponent(*args):
    """Compute the absolute value of the largest of a group of numbers.

    Determine the largest component by magnitude, and return its absolute
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


def checkRotation(*args):
    """Determine if the values of matrix are a rotation.

    Determine if the values of a column-major matrix composed of the
    arguments constitute a valid rotation matrix. If so, take no action.
    If not, raise a MalformedRotationException.

    A matrix is a valid rotation matrix if the determinant is unity, and
    each column has unit norm.

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
        # Convert the individual values to a 2x2 np.ndarray.
        a = np.array([ii, ij, ji, jj]).reshape(2, 2)
    elif len(args) == 11:
        # 3-D matrix.
        (ii, ji, ki, ij, jj, kj, ik, jk, kk,
         normTolerance, detTolerance) = args
        # Convert the individual values to a 3x3 np.ndarray.
        a = np.array([ii, ij, ik, ji, jj, jk, ki, kj, kk]).reshape(3, 3)
    else:
        raise ValueError

    # Verify the matrix has unit determinant, within tolerance.
    det = np.linalg.det(a)
    if abs(det) > 1 + detTolerance:
        raise MalformedRotationException

    # Verify each column has unit norm.
    for col in range(len(a)):
        norm = np.linalg.norm(a[:, col])
        if abs(norm) > 1 + normTolerance:
            raise MalformedRotationException
