"""Deformation of a cylindrical basis vector field."""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.MatrixIJK;
# import crucible.core.math.vectorspace.UnwritableMatrixIJK;
# import magmodel.core.math.vectorfields.DifferentiableCylindricalVectorField;

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.deformation.cylindricalfielddeformation import (
    CylindricalFieldDeformation
)
from emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)


class CylindricalBasisFieldDeformation(CylindricalBasisVectorField):
    """Deformation of a cylindrical basis vector field.

    author G.K.Stephens
    """

    # private final CylindricalBasisVectorField originalField;
    # private final DifferentiableCylindricalVectorField coordDeformation;

    def __init__(self, originalField, coordDeformation):
        """Build a new object.

        param CylindricalBasisVectorField originalField
        param DifferentiableCylindricalVectorField coordDeformation
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluateExpansion(self, originalCoordinate):
        """Evaluate the expansion.

        param CylindricalVector originalCoordinate
        return [CylindricalVector]
        """
        # DifferentiableCylindricalVectorField.Results deformed
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        # UnwritableMatrixIJK trans
        trans = CylindricalFieldDeformation.computeMatrix(
            deformed, originalCoordinate
        )
        # [CylindricalVector] bFieldExpansion
        bFieldExpansion = self.originalField.evaluateExpansion(deformed.getF())
        # [CylindricalVector] bFieldExpansionDeformed
        bFieldExpansionDeformed = []
        # CylindricalVector bField
        for bField in bFieldExpansion:
            # VectorIJK v
            v = trans.mxv(
                VectorIJK(bField.getCylindricalRadius(), bField.getLongitude(),
                          bField.getHeight())
            )
            bFieldExpansionDeformed.append(
                CylindricalVector(v.i, v.j, v.getK())
            )
        return bFieldExpansionDeformed

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
