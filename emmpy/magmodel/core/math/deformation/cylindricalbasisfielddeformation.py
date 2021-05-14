"""emmpy.magmodel.core.math.deformation.cylindricalbasisfielddeformation"""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.vectorspace.MatrixIJK;
# import crucible.core.math.vectorspace.UnwritableMatrixIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import magmodel.core.math.vectorfields.DifferentiableCylindricalVectorField;

from emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)


class CylindricalBasisFieldDeformation(CylindricalBasisVectorField):
    """author G.K.Stephens"""

    # private final CylindricalBasisVectorField originalField;
    # private final DifferentiableCylindricalVectorField coordDeformation;

    def __init__(self, originalField, coordDeformation):
        """Constructor.

        param CylindricalBasisVectorField originalField
        param DifferentiableCylindricalVectorField coordDeformation
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    #   @Override
    #   public ImmutableList<CylindricalVector> evaluateExpansion(CylindricalVector originalCoordinate) {
    #     DifferentiableCylindricalVectorField.Results deformed =
    #         coordDeformation.differentiate(originalCoordinate);
    #     UnwritableMatrixIJK trans =
    #         CylindricalFieldDeformation.computeMatrix(deformed, originalCoordinate);
    #     ImmutableList<CylindricalVector> bFieldExpansion =
    #         originalField.evaluateExpansion(deformed.getF());
    #     ImmutableList.Builder<CylindricalVector> bFieldExpansionDeformed = ImmutableList.builder();
    #     for (CylindricalVector bField : bFieldExpansion) {
    #       VectorIJK v = trans.mxv(
    #           new VectorIJK(bField.getCylindricalRadius(), bField.getLongitude(), bField.getHeight()));
    #       bFieldExpansionDeformed.add(new CylindricalVector(v.getI(), v.getJ(), v.getK()));
    #     }
    #     return bFieldExpansionDeformed.build();
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return originalField.getNumberOfBasisFunctions();
    #   }

    #   @Override
    #   public CylindricalVector evaluate(CylindricalVector originalCoordinate) {
    #     // compute the derivatives at the given location
    #     DifferentiableCylindricalVectorField.Results deformed =
    #         coordDeformation.differentiate(originalCoordinate);
    #     // compute the deformation matrix
    #     MatrixIJK trans = CylindricalFieldDeformation.computeMatrix(deformed, originalCoordinate);
    #     // evaluate the field at the deformed location
    #     CylindricalVector bField = originalField.evaluate(deformed.getF());
    #     // evaluate the deformed field
    #     VectorIJK v = trans.mxv(
    #         new VectorIJK(bField.getCylindricalRadius(), bField.getLongitude(), bField.getHeight()));
    #     return new CylindricalVector(v.getI(), v.getJ(), v.getK());
    #   }
