"""Compute the magnetic field from a smoothed conical current sheet.

Compute the magnetic field from a smoothed conical current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import emmpy.math.vectorfields.vectorfields as vectorfields
from emmpy.magmodel.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)
from emmpy.magmodel.modeling.fac.conicalcurrentmagneticfield import (
    ConicalCurrentMagneticField
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.utilities.nones import nones


class SmoothedConicalCurrentMagneticField(SphericalVectorField):
    """Compute the magnetic field from a smoothed conical current sheet.

    Compute the magnetic field from a smoothed conical current sheet.

    Attributes
    ----------
    smoothedField : VectorField
        The smoothed vector field.
    """

    def __init__(self, theta0, deltaTheta, mode, trigParity):
        """Initialize a new SmoothedConicalCurrentMagneticField object.

        Initialize a new SmoothedConicalCurrentMagneticField object.

        Parameters
        ----------
        theta0 : float
            theta0
        deltaTheta : float
            deltaTheta
        mode : int
            mode
        trigParity : TrigParity
            trigParity
        """
        shiftDistance = deltaTheta/5.0
        numShifts = 5
        shiftedFields = nones((numShifts,))
        for i in range(numShifts):
            shiftedTheta0 = theta0 - 2.0*shiftDistance + i*shiftDistance
            shiftedFields[i] = ConicalCurrentMagneticField.create(
                shiftedTheta0, deltaTheta, mode, trigParity)
        self.smoothedField = vectorfields.scale(
            vectorfields.addAll(shiftedFields), 1.0/numShifts
        )

    def evaluate(self, *args):
        """Evaluate the magnetic field.
        
        Evaluate the magnetic field.
        
        Parameters
        ----------
        location : SphericalVector or VectorIJK
            Location for evaluation.
        buffer : VectorIJK, optional
            Buffer to hold result.

        Returns
        -------
        result : SphericalVector or VectorIJK
            Field evaluated at location.

        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if len(args) == 1:
            (location,) = args
            assert(isinstance(location, SphericalVector))
            locationCartesian = CoordConverters.convert(location)
            fieldValue = CartesianVectorFieldValue(
                locationCartesian, self.evaluate(locationCartesian)
            )
            return (
                VectorFieldValueConversions.convertToSpherical(fieldValue).
                getValue()
            )
        elif len(args) == 2:
            (location, buffer) = args
            assert(isinstance(location, VectorIJK))
            assert(isinstance(buffer, VectorIJK))
            return self.smoothedField.evaluate(location, buffer)
        else:
            raise TypeError
