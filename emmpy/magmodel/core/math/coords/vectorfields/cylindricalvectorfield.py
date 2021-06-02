"""emmpy.magmodel.core.math.vectorfields.cylindricalbectorfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""

# import static crucible.core.math.coords.CoordConverters.convertToCylindrical;
# import static crucible.core.math.coords.VectorFieldValueConversions.convert;
# import crucible.core.exceptions.FunctionEvaluationException;
# import crucible.core.math.coords.CartesianVectorFieldValue;
# import crucible.core.math.coords.CoordConverters;
# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.coords.CylindricalVectorFieldValue;
# import crucible.core.math.coords.VectorFieldValueConversions;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions
)
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)


class CylindricalVectorFieldWrapper:

    def __init__(self, field):
        self.field = field

    def evaluate(self, *args):
        """override this default method to improve the performance of the code,
        we already have the field as a Cartesian field, so there is no need to
        jump through the conversions"""
        if len(args) == 1:
            (location,) = args
            # N.B. ORIGINAL COMMENTS ARE INCORRECT - SHOULD BE CYLINDRICAL.
            # convert the Cartesian position to spherical
            locCart = CoordConverters.convert(location)

            # evaluate the field value
            fieldValue = self.field.evaluate(locCart)

            # construct the spherical vector field value for the given position
            cart = CartesianVectorFieldValue(locCart, fieldValue)

            # convert the vector field value back to Cartesian
            valueSphere = (
                VectorFieldValueConversions.convertToCylindrical(cart).
                getValue()
            )

            # return the value
            return valueSphere
        elif len(args) == 2:
            (location, buffer) = args
            return self.field.evaluate(location, buffer)
        else:
            raise Exception


class CylindricalVectorField(VectorField):
    """Represents a VectorField in cylindrical coordinates and provides the
    conversion from a CylindricalVector field to a Cartesian vector field.

    where r is the cylindrical radius, &#966; is the longitude (or aziumuth)
    angle, and z is the height

    @author G.K.Stephens
    """

    def __init__(self):
        """Constructor"""
        pass

    @staticmethod
    def asCylindrical(field):
        if isinstance(field, CylindricalVectorField):
            return field
        else:
            cvfw = CylindricalVectorFieldWrapper(field)
            return cvfw

    @staticmethod
    def evaluate(*args):
        if len(args) == 1:
            # Evaluate the field at the given position in spherical coordinates
            # units and such are up to the implementors
            # @param location {@link CylindricalVector}, often location
            # @return the resultant {@link CylindricalVector}
            # @throws FunctionEvaluationException if the function cannot
            # perform the evaluation
            pass
        elif len(args) == 2:
            (location, buffer) = args
            raise Exception  # THIS METHOD DOES NOT WORK

            # convert the Cartesian position to cylindrical
            # locCyl = CoordConverters.convertToCylindrical(location)

            # evaluate the cylindrical vector field value for the given
            # position
            # cyl = CylindricalVectorFieldValue(locCyl, self.evaluate(locCyl))

            # convert the vector field value to Cartesian
            # valueCyl = CoordConverters.convert(cyl).getValue()

            # return buffer.setTo(valueCyl)
