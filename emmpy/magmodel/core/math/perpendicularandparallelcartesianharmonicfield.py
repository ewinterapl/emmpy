"""emmpy.magmodel.core.math.perpendicularandparallelcartesianharmonicfield"""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.RotationMatrixIJK;
# import crucible.core.math.vectorspace.UnwritableRotationMatrixIJK;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.vectorfields.BasisVectorFields;

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.rotations.axisandangle import AxisAndAngle
from emmpy.magmodel.core.math.cartesianharmonicfield import (
    CartesianHarmonicField
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class PerpendicularAndParallelCartesianHarmonicField(BasisVectorField):
    """Represents the linear combination of a perpendicular and parallel
    Cartesian harmonic vector field.
    
    This is often useful because a VectorField can be decomposed into the sum
    of a vertical and horizontal vector field.

    This formulation has shown to be effective for representing the
    magnetopause currents that can be used to contain the magnetic field within
    the magnetosphere: e.g. Tsyganenko 1998].

    author G.K.Stephens
    author Nicholas Sharp
    """
    #   private final BasisVectorField perpendicularField;
    #   private final BasisVectorField parallelField;

    def __init__(self, perpendicularField, parallelField):
        """Constructor"""
        self.perpendicularField = perpendicularField
        self.parallelField = parallelField

    @staticmethod
    def create(trigParityI, p, r, perpCoeffs, q, s, parrCoeffs):
        """Creates a PerpendicularAndParallelCartesianHarmonicField

        param trigParityI the TrigParity associated with the Y terms
        (odd=sine, even=cosine)
        param p an expansion containing the nonlinear set of coefficients p_i
        param r an expansion containing the nonlinear set of coefficients r_k
        param perpCoeffs an expansion containing the linear scaling
        coefficients a_ik
        param q an expansion containing the nonlinear set of coefficients q_i
        param s an expansion containing the nonlinear set of coefficients s_k
        param parrCoeffs an expansion containing the linear scaling
        coefficients b_ik
        return a newly constructed
        PerpendicularAndParallelCartesianHarmonicField
        """
        perpendicularVectorField = CartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, TrigParity.ODD)
        parallelDipoleShieldingField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, TrigParity.EVEN)
        return PerpendicularAndParallelCartesianHarmonicField(
            perpendicularVectorField, parallelDipoleShieldingField)

    def createWithRotation(trigParityI, perpendicularTiltAngle, p, r,
                           perpCoeffs, parallelTiltAngle, q, s, parrCoeffs):
        """Creates a PerpendicularAndParallelCartesianHarmonicField where each
        field is rotated by an arbitrary angle about the y-axis

        Described in detail in the appendix of Tsyganenko [1998].

        param trigParityI the TrigParity associated with the Y terms
        (odd=sine, even=cosine)
        param perpendicularTiltAngle the angle to rotate the perpendicular
        field about the y-axis
        param p an expansion containing the nonlinear set of coefficients p_i
        param r an expansion containing the nonlinear set of coefficients r_k
        param perpCoeffs an expansion containing the linear scaling
        coefficients a_ik
        param parallelTiltAngle the angle to rotate the parallel field about
        the y-axis
        param q an expansion containing the nonlinear set of coefficients q_i
        param s an expansion containing the nonlinear set of coefficients s_k
        param parrCoeffs an expansion containing the linear scaling
        coefficients b_ik
        return a newly constructed
        PerpendicularAndParallelCartesianHarmonicField
        """
        # construct the unrotated fields
        perpField = CartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, TrigParity.ODD)
        paraField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, TrigParity.EVEN)

        # the rotation matrices about Y axis
        perpendicularRotation = AxisAndAngle(
            VectorIJK.J,
            -perpendicularTiltAngle).getRotation(RotationMatrixIJK())
        parallelRotation = AxisAndAngle(
            VectorIJK.J,
            -parallelTiltAngle).getRotation(RotationMatrixIJK())

        # // now rotate the fields
        # BasisVectorField rotatedPerpField = BasisVectorFields.rotate(perpField, perpendicularRotation);
        # BasisVectorField rotatedParaField = BasisVectorFields.rotate(paraField, parallelRotation);

        # return new PerpendicularAndParallelCartesianHarmonicField(rotatedPerpField, rotatedParaField);

    #   /**
    #    * Creates a {@link PerpendicularAndParallelCartesianHarmonicField} where each field is rotated by
    #    * an arbitrary angle about the y-axis, i.e.:
    #    * <p>
    #    * <img src="doc-files/perpAndParrWithRotation.png" />
    #    * <p>
    #    * Described in detail in the appendix of Tsyganenko [1998].
    #    * 
    #    * @param trigParityI the {@link TrigParity} associated with the Y terms (odd=sine, even=cosine)
    #    * @param perpendicularTiltAngle the angle to rotate the perpendicular field about the y-axis
    #    * @param p an expansion containing the nonlinear set of coefficients p<sub>i</sub>
    #    * @param r an expansion containing the nonlinear set of coefficients r<sub>k</sub>
    #    * @param perpCoeffs an expansion containing the linear scaling coefficients (a<sub>ik</sub>)
    #    * @param parallelTiltAngle the angle to rotate the parallel field about the y-axis
    #    * @param q an expansion containing the nonlinear set of coefficients q<sub>i</sub>
    #    * @param s an expansion containing the nonlinear set of coefficients s<sub>k</sub>
    #    * @param parrCoeffs an expansion containing the linear scaling coefficients (b<sub>ik</sub>)
    #    * 
    #    * @return a newly constructed {@link PerpendicularAndParallelCartesianHarmonicField}
    #    */
    #   public static PerpendicularAndParallelCartesianHarmonicField createWithRotationAndAlternate(
    #       TrigParity trigParityI, double perpendicularTiltAngle, CoefficientExpansion1D p,
    #       CoefficientExpansion1D r, CoefficientExpansion2D perpCoeffs, double parallelTiltAngle,
    #       CoefficientExpansion1D q, CoefficientExpansion1D s, CoefficientExpansion2D parrCoeffs) {

    #     // construct the unrotated fields
    #     BasisVectorField perpField =
    #         new AlternateCartesianHarmonicField(p, r, perpCoeffs, trigParityI, TrigParity.ODD);
    #     BasisVectorField paraField =
    #         new CartesianHarmonicField(q, s, parrCoeffs, trigParityI, TrigParity.EVEN);

    #     // the rotation matrices about Y axis
    #     UnwritableRotationMatrixIJK perpendicularRotation =
    #         new AxisAndAngle(VectorIJK.J, -perpendicularTiltAngle).getRotation(new RotationMatrixIJK());
    #     UnwritableRotationMatrixIJK parallelRotation =
    #         new AxisAndAngle(VectorIJK.J, -parallelTiltAngle).getRotation(new RotationMatrixIJK());

    #     // now rotate the fields
    #     BasisVectorField rotatedPerpField = BasisVectorFields.rotate(perpField, perpendicularRotation);
    #     BasisVectorField rotatedParaField = BasisVectorFields.rotate(paraField, parallelRotation);

    #     return new PerpendicularAndParallelCartesianHarmonicField(rotatedPerpField, rotatedParaField);
    #   }

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    #     VectorIJK perpField = perpendicularField.evaluate(location);
    #     VectorIJK parField = parallelField.evaluate(location, buffer);

    #     VectorIJK.add(perpField, parField, buffer);

    #     return buffer;
    #   }

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {

    #     ImmutableList<UnwritableVectorIJK> perpFields = perpendicularField.evaluateExpansion(location);
    #     ImmutableList<UnwritableVectorIJK> parFields = parallelField.evaluateExpansion(location);

    #     ImmutableList.Builder<UnwritableVectorIJK> expansions = ImmutableList.builder();

    #     expansions.addAll(perpFields);
    #     expansions.addAll(parFields);

    #     return expansions.build();
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return (perpendicularField.getNumberOfBasisFunctions()
    #         + parallelField.getNumberOfBasisFunctions());
    #   }

    #   /**
    #    * @return the perpendicular field
    #    */
    #   public BasisVectorField getPerpendicularField() {
    #     return perpendicularField;
    #   }

    #   /**
    #    * @return the parallel field
    #    */
    #   public BasisVectorField getParallelField() {
    #     return parallelField;
    #   }

    # }
