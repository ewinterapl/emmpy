"""emmpy.magmodel.core.math.vectorfields.sphericalscalarfield"""


from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField


class SphericalScalarField(ScalarField):
    """author G.K.Stephens"""

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTNTIATE
        """
        raise Exception

    def evaluate(self, location):
        """evaluate

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
        """evaluateScalar

        INTERFACE - DO NOT INVOKE

        param SphericalVector posSph
        return double
        """
        raise Exception
