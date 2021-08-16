"""Utility functions for vector fields.

Utility functions for vector fields.

Authors
-------
Jon Vanderpool (27 February 2012)
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.deformation.sphericalfielddeformation import (
    SphericalFieldDeformation
)
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


def add(a, b):
    """Create a vector field by adding the two vector fields.

    Create a vector field by adding the two vector fields. The two fields
    maintain their separate nature, and are only added when this sum field
    is evaluated.

    Parameters
    ----------
    a, b : VectorField
        The vector fields to add.
    
    Returns
    -------
    vf : VectorField
        A VectorField that computes the component-wise sum (a + b).
    """
    vf = VectorField()

    # This custom evaluate() method dynamically sums the individual vector
    # fields and stores the sum in the buffer.
    def my_evaluate(location, buffer):
        va = a.evaluate(location, VectorIJK())
        vb = b.evaluate(location, VectorIJK())
        buffer[:] = va + vb
        return buffer

    vf.evaluate = my_evaluate
    return vf


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


def negate(field):
    """Create a vector field by negating a vector field.

    Create a vector field by negating a vector field. The original field
    maintains its separate nature, and is only negated when this negated
    field is evaluated.

    Parameters
    ----------
    field : VectorField
        The vector field to negate.
    
    Returns
    -------
    vf : VectorField
        A VectorField that computes the negation of the original field
    """
    vf = VectorField()

    # This custom evaluate() method dynamically negates the original vector
    # field and stores the result in the buffer.
    def my_evaluate(location, buffer):
        field.evaluate(location, buffer)
        buffer *= -1
        return buffer

    vf.evaluate = my_evaluate
    return vf


def scale(field, scaleFactor):
    """Create a vector field by scaling a vector field.

    Create a vector field by scaling a vector field. The original field
    maintains its separate nature, and is only scaled when this scaled
    field is evaluated.

    Parameters
    ----------
    field : VectorField
        The vector field to negate.
    scaleFactor : float
        Scale factor to apply to vector field value.

    Returns
    -------
    vf : VectorField
        A VectorField that computes the scaled version of the original.
        field.
    """
    vf = VectorField()

    # This custom evaluate() method dynamically scales the original vector
    # field and stores the result in the buffer.
    def my_evaluate(*my_args):
        if len(my_args) == 1:
            (location,) = my_args
            buffer = VectorIJK()
        else:
            (location, buffer) = my_args
        if isinstance(field, SphericalFieldDeformation):
            fe = SphericalVectorField.evaluate(field, location, buffer)
        else:
            fe = field.evaluate(location, buffer)
        fe *= scaleFactor
        return fe

    vf.evaluate = my_evaluate
    return vf


def scaleLocation(field, scaleFactor):
    """Create a vector field by scaling the location of a field.

    Create a vector field by scaling the location of a field.

    Parameters
    ----------
    field : VectorField
        The vector field for which to scale locations.
     scaleFactor : float
        Scale factor for vector field locations.
    
    Returns
    -------
    vf : VectorField
        A vector field that computes the value at a scaled location.
    """
    vf = VectorField()

    # This custom evaluate() method dynamically scales the location of the
    # original vector field and stores the result in the buffer.
    def my_evaluate(location, buffer):
        v = VectorIJK(scaleFactor, location)
        field.evaluate(v, buffer)
        return buffer

    vf.evaluate = my_evaluate
    return vf
