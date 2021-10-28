"""A vector field in a space of arbitrary dimension.

This class represents a vector field in a space of arbitrary dimension.
A vector field is defined as a mapping from a vector position in the
field to a vector value in the field. The position and value vectors are
assumed to have the same dimensionality as the space.

Authors
-------
J. Vanderpool
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.vectorijk import VectorIJK


class VectorField:
    """A vector field in a space of arbitrary dimension.

    This class represents a vector field in a space of arbitrary dimension.
    A vector field is defined as a mapping from a vector position in the
    field to a vector value in the field. The position and value vectors are
    assumed to have the same dimensionality as the space.

    Attributes
    ----------
    None
    """

    def evaluate(self, position):
        """Evaluate the vector field at a position.

        This abstract method must be overridden in a subclass.

        Evaluate the vector field at the specified position in the vector
        space.

        Parameters
        ----------
        position : Vector
            The position for evaluation in the vector space.

        Returns
        -------
        value : Vector
            Value of vector field at the specified position.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException


def add(a, b):
    """Create a vector field by adding two vector fields.

    Create a vector field by adding two vector fields. The two fields
    maintain their separate nature, and are only added when this sum field
    is evaluated.

    Parameters
    ----------
    a, b : VectorField
        The vector fields to add.
    
    Returns
    -------
    sumVectorField : VectorField
        A VectorField that computes the component-wise sum (a + b).
    """
    sumVectorField = VectorField()

    # This custom evaluate() method dynamically sums the individual vector
    # fields and stores the sum in the buffer.
    def my_evaluate(location, buffer):
        va = a.evaluate(location, VectorIJK())
        vb = b.evaluate(location, VectorIJK())
        buffer[:] = va + vb
        return buffer

    sumVectorField.evaluate = my_evaluate
    return sumVectorField


def addAll(fields):
    """Create a vector field by adding multiple vector fields.

    Create a vector field by adding multiple vector fields. The fields
    maintain their separate nature, and are only added when this sum field
    is evaluated.

    Parameters
    ----------
    fields : array-like of VectorField
        The vector fields to add.
    
    Returns
    -------
    vf : VectorField
        A VectorField that computes the component-wise sum of the fields.
    """
    vf = VectorField()

    # This custom evaluate() method dynamically sums the individual vector
    # fields and stores the sum in the buffer.
    def my_evaluate(location, buffer):
        vsum = np.zeros((3,))
        for field in fields:
            field.evaluate(location, buffer)
            vsum[:] += buffer
        buffer[:] = vsum
        return buffer

    vf.evaluate = my_evaluate
    return vf


def negate(vectorField):
    """Create the negation of a vector field.

    Create the negation of a vector field. The original field maintains
    its separate nature, and is only negated when this negated field is
    evaluated.

    This method works on any VectorField-based object in any coordinate
    system.

    Parameters
    ----------
    vectorField : VectorField
        The vector field to negate.
    
    Returns
    -------
    negation : VectorField
        A VectorField that computes the negation of the original field.
    """
    negation = VectorField()

    # This custom evaluate() method dynamically negates the original vector
    # field and stores the result in the buffer.
    def my_evaluate(location, buffer):
        vectorField.evaluate(location, buffer)
        buffer[:] = -buffer
        return buffer

    negation.evaluate = my_evaluate
    return negation


def scaleLocation(vectorField, scaleFactor):
    """Create a vector field by scaling the location of a field.

    Create a vector field by scaling the location of a field.

    Parameters
    ----------
    vectorField : VectorField
        The vector field for which to scale locations.
     scaleFactor : float
        Scale factor for vector field locations.
    
    Returns
    -------
    scaledLocationField : VectorField
        A vector field that computes the value at a scaled location.
    """
    scaledLocationField = VectorField()

    # This custom evaluate() method dynamically scales the location of the
    # original vector field and stores the result in the buffer.
    def my_evaluate(location, buffer):
        scaledLocation = scaleFactor*VectorIJK(location)
        vectorField.evaluate(scaledLocation, buffer)
        return buffer

    scaledLocationField.evaluate = my_evaluate
    return scaledLocationField
