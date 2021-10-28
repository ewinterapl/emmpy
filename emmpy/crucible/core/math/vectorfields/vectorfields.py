"""Utility functions for vector fields.

Utility functions for vector fields.

Authors
-------
Jon Vanderpool (27 February 2012)
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.magmodel.core.math.deformation.sphericalfielddeformation import (
    SphericalFieldDeformation
)
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


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
        v = scaleFactor*VectorIJK(location)
        field.evaluate(v, buffer)
        return buffer

    vf.evaluate = my_evaluate
    return vf
