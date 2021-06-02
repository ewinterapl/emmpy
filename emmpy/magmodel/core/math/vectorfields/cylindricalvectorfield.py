"""emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield

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

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class CylindricalVectorFieldView:

    def __init__(self, cvf):
        self.cvf = cvf


class CylindricalVectorField(VectorField):
    # public interface CylindricalVectorField extends VectorField {
    """Represents a {@link VectorField} in cylindrical coordinates and provides
    the conversion from a {@link CylindricalVector} field to a Cartesian vector
    field.

    where r is the cylindrical radius, &#966; is the longitude (or aziumuth)
    angle, and z is the height

    @author G.K.Stephens
    """

    def __init__(self):
        """INTERFACE - DO NOT INSTANTIATE."""
        raise Exception

    @staticmethod
    def asCylindrical(field):
        """asCylindrical"""
        if isinstance(field, CylindricalVectorField):
            return field
        else:
            pass
            # cvfv = CylindricalVectorFieldView(a)
            # cvfv.evaluate = lambda XXX: -a.getCoefficient(index)

#     // override this default method to improve the performance of the code, we already have the
#     // field as a Cartesian field, so there is no need to jump through the conversions
#     @Override
#     public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
#         return field.evaluate(location, buffer);
#     }

#     @Override
#     public CylindricalVector evaluate(CylindricalVector location) {

#         // convert the Cartesian position to spherical
#         UnwritableVectorIJK locCart = CoordConverters.convert(location);

#         // evaluate the field value
#         UnwritableVectorIJK fieldValue = field.evaluate(locCart);

#         // construct the spherical vector field value for the given position
#         CartesianVectorFieldValue cart = new CartesianVectorFieldValue(locCart, fieldValue);

#         // convert the vector field value back to Cartesian
#         CylindricalVector valueSphere =
#             VectorFieldValueConversions.convertToCylindrical(cart).getValue();

#         // return the value
#         return valueSphere;
#     }
#     };
# }
# }

    #   @Override
    #   public default VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    #     // convert the Cartesian position to cylindrical
    #     CylindricalVector locCyl = convertToCylindrical(location);

    #     // evaluate the cylindrical vector field value for the given position
    #     CylindricalVectorFieldValue cyl = new CylindricalVectorFieldValue(locCyl, evaluate(locCyl));

    #     // convert the vector field value to Cartesian
    #     UnwritableVectorIJK valueCyl = convert(cyl).getValue();

    #     return buffer.setTo(valueCyl);
    #   }

    #   /**
    #    * Evaluate the field at the given position in spherical coordinates
    #    *
    #    * units and such are up to the implementors
    #    *
    #    * @param location {@link CylindricalVector}, often location
    #    * @return the resultant {@link CylindricalVector}
    #    *
    #    * @throws FunctionEvaluationException if the function cannot perform the evaluation
    #    */
    #   public CylindricalVector evaluate(CylindricalVector location);

    # }
