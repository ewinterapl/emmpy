"""Magnetic field from 2 conical current sheets.

Magnetic field from 2 conical current sheets.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import emmpy.math.vectorfields.vectorfields as vectorfields
from emmpy.magmodel.modeling.fac.xyplanereflectedfield import (
    XYPlaneReflectedField
)
from emmpy.math.vectorfields.vectorfield import (
    VectorField, add, negate
)


class TwoConicalFields(VectorField):
    """Magnetic field from 2 conical current sheets.

    Represents the magnetic field of two deformed azimuthal harmonic of a
    finite thickness conical current sheet.

    As described in "A model of the near magnetosphere with a dawn-dusk
    asymmetry 1. Mathematical structure" by N. A. Tsyganenko. See eq.
    (20). The cones' axis is the +/-Z axis.

    see http://onlinelibrary.wiley.com/doi/10.1029/2001JA000219/abstract
    (Tsyganenko, 2002

    Attributes
    ----------
    field : VectorField
        field
    """

    def __init__(self, field):
        """Initialize a new TwoConicalFields object.

        Initialize a new TwoConicalFields object.

        Parameters
        ----------
        field : VectorField
            field
        """
        self.field = add(field, XYPlaneReflectedField(negate(field)))

    def evaluate(self, location, buffer):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the field.
        buffer : VectorIJK
            Buffer to hold the result.
        
        Returns
        -------
        buffer : VectorIJK
            Result of evaluation.
        """
        return self.field.evaluate(location, buffer)
