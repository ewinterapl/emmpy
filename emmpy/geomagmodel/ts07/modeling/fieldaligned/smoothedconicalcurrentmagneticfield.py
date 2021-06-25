"""emmpy.geomagmodel.ts07.modeling.fieldaligned.smoothedconicalcurrentmagneticfield"""


from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions
)
from emmpy.crucible.core.math.vectorfields.vectorfields import VectorFields
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)
from emmpy.magmodel.core.modeling.fac.conicalcurrentmagneticfield import (
    ConicalCurrentMagneticField
)
from emmpy.utilities.nones import nones


class SmoothedConicalCurrentMagneticField(SphericalVectorField):

    def __init__(self, theta0, deltaTheta, mode, trigParity):
        """Constructor

        param double theta0
        param double deltaTheta
        param int mode
        param TrigParity trigParity
        """
        # double shiftDistance
        shiftDistance = deltaTheta/5.0
        # int numShifts
        numShifts = 5
        # list of VectorField
        shiftedFields = nones((numShifts,))
        for i in range(numShifts):
            # double shiftedTheta0
            shiftedTheta0 = theta0 - 2.0*shiftDistance + i*shiftDistance
            # ConicalCurrentMagneticField
            shiftedFields[i] = ConicalCurrentMagneticField.create(
                shiftedTheta0, deltaTheta, mode, trigParity)
        # VectorField
        self.smoothedField = VectorFields.scale(
            VectorFields.addAll(shiftedFields), 1.0/numShifts
        )

    def evaluate(self, *args):
        if len(args) == 1:
            (location,) = args
            assert(isinstance(location, SphericalVector))
            # UnwritableVectorIJK locationCartesian
            locationCartesian = CoordConverters.convert(location)
            # CartesianVectorFieldValue fieldValue
            # WILL THIS CALL RAISE AN EXCEPTION FROM THE INHERITED
            # SphericalVectorField.evaluate()?
            fieldValue = CartesianVectorFieldValue(
                locationCartesian, self.evaluate(locationCartesian)
            )
            return (
                VectorFieldValueConversions.convertToSpherical(fieldValue).
                getValue()
            )
        elif len(args) == 2:
            (location, buffer) = args
            assert(isinstance(location, UnwritableVectorIJK))
            assert(isinstance(buffer, VectorIJK))
            return self.smoothedField.evaluate(location, buffer)
        else:
            raise Exception

