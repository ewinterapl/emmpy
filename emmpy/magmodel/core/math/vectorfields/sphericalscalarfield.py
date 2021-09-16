"""A scalar field in spherical coordinates.

A scalar field in spherical coordinates.

This class was derived from a Java interface, and thus some of the methods
will raise an Exception if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class SphericalScalarField(ScalarField):
    """A scalar field in spherical coordinates.

    A scalar field in spherical coordinates.
    """

    def evaluate(self, location):
        """Evaluate the scalar field at a Cartesian location.

        Evaluate the scalar field at a Cartesian location.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the scalar field.
        
        Returns
        -------
        fieldValue : float
            Value of the scalar field at the location.
        """
        # Convert the Cartesian position to spherical.
        locSphere = CoordConverters.convertToSpherical(location)

        # Evaluate the field value.
        fieldValue = self.evaluateScalar(locSphere)
        return fieldValue

    def evaluateScalar(self, posSph):
        """Evaluate the scalar field at a spherical location.

        Evaluate the scalar field at a spherical location.

        Parameters
        ----------
        posSph : SphericalVector
            Position to evaluate the field.
        
        Returns
        -------
        result : float
            Scalar field value.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
