"""emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield"""


# import static crucible.core.math.coords.CoordConverters.convertToCylindrical;
# import static crucible.core.math.coords.VectorFieldValueConversions.convert;
# import com.google.common.collect.ImmutableList;
# import crucible.core.exceptions.FunctionEvaluationException;
# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.coords.CylindricalVectorFieldValue;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;


class CylindricalBasisVectorField:

    # /**
    #  * Represents a {@link VectorField} in cylindrical coordinates and provides the conversion from a
    #  * {@link CylindricalVector} field to a Cartesian vector field.
    #  * <p>
    #  * <img src="doc-files/cylindricalVectorField.png" />
    #  * <p>
    #  * where r is the radius, &#952; is the co-latitude angle, and &#966; is the longitude (or aziumuth)
    #  * angle
    #  * 
    #  * @author G.K.Stephens
    #  *
    #  */
    # public interface CylindricalBasisVectorField extends CylindricalVectorField {

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

    #   /**
    #    * Evaluate the field expansion at the given position, and returns an {@link ImmutableList} of the
    #    * results of each individual field in the expansion in cylindrical coordinates
    #    * 
    #    * @param location {@link CylindricalVector}, often location
    #    * @return the resultant {@link CylindricalVector}
    #    * 
    #    * @throws FunctionEvaluationException if the function cannot perform the evaluation
    #    */
    #   public ImmutableList<CylindricalVector> evaluateExpansion(CylindricalVector location);

    #   /**
    #    * @return the number of individual vector fields in the expansion
    #    */
    #   public int getNumberOfBasisFunctions();

    # }
