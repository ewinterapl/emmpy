"""A basis vector field in cylindrical coordinates."""


# import static crucible.core.math.coords.CoordConverters.convertToCylindrical;
# import static crucible.core.math.coords.VectorFieldValueConversions.convert;
# import com.google.common.collect.ImmutableList;
# import crucible.core.exceptions.FunctionEvaluationException;
# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.coords.CylindricalVectorFieldValue;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class CylindricalBasisVectorField(CylindricalVectorField):
    """A basis vector field in cylindrical coordinates.

    Represents a VectorField in cylindrical coordinates and provides the
    conversion from a CylindricalVector field to a Cartesian vector field.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephens
    """

    def __init__(self):
        """Build a new object.

        INTERFACE - DO NOT INSTANTIATE
        """

    #   @Override
    #   public default VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #     // convert the Cartesian position to cylindrical
    #     CylindricalVector locCyl = convertToCylindrical(location);
    #     // evaluate the field value
    #     CylindricalVector fieldValue = evaluate(locCyl);
    #     // construct the cylindrical vector field value for the given position
    #     CylindricalVectorFieldValue cyl = new CylindricalVectorFieldValue(locCyl, fieldValue);
    #     // convert the vector field value back to Cartesian
    #     UnwritableVectorIJK valueCyl = convert(cyl).getValue();
    #     // return the value
    #     return buffer.setTo(valueCyl);
    #   }

    def evaluateExpansion(self, location):
        """Evaluate the expansion.

        Evaluate the field expansion at the given position, and returns an
        ImmutableList  results of each individual field in the expansion in
        cylindrical coordinates

        INTERFACE - DO NOT INVOKE

        param location CylindricalVector, often location
        return the resultant CylindricalVector as a list

        throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        raise Exception

    #   /**
    #    * @return the number of individual vector fields in the expansion
    #    */
    #   public int getNumberOfBasisFunctions();
