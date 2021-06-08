"""A scalar field in spherical coordinates."""


from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField


class SphericalScalarField(ScalarField):
    """A scalar field in spherical coordinates.

    author G.K.Stephens
    """

    def __init__(self):
        """Build a new object.

        INTERFACE - DO NOT INSTNTIATE
        """
        raise Exception

    def evaluate(self, location):
        """Evaluate the scalar field at a Cartesian location.

        param UnwritableVectorIJK location
        return double
        """
        # convert the Cartesian position to spherical
        # SphericalVector locSphere
        locSphere = CoordConverters.convertToSpherical(location)

        # evaluate the field value
        # double fieldValue
        fieldValue = self.evaluateScalar(locSphere)
        return fieldValue

    def evaluateScalar(self, posSph):
        """Evaluate the scalar field at a spherical location.

        INTERFACE - DO NOT INVOKE

        param SphericalVector posSph
        return double
        """
        raise Exception
