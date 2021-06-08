"""Deformation for a basis vector field."""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.deformation.vectorfielddeformation import (
    VectorFieldDeformation
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class BasisVectorFieldDeformation(BasisVectorField):
    """Deformation for a basis vector field."""

    def __init__(self, originalField, coordDeformation):
        """Build a new object."""
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate, buffer):
        """Evaluate the basis vector field deformation."""
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        trans = VectorFieldDeformation.computeMatrix(deformed)   # STATIC?
        bField = self.originalField.evaluate(deformed.getF())
        v = trans.mxv(VectorIJK(bField.getI(), bField.getJ(), bField.getK()))
        return buffer.setTo(v.getI(), v.getJ(), v.getK())

    def evaluateExpansion(self, originalCoordinate):
        """Evaluate the expansion at the specified location."""
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        trans = VectorFieldDeformation.computeMatrix(deformed)
        bFieldExpansion = self.originalField.evaluateExpansion(deformed.getF())
        bFieldExpansionDeformed = []
        for bField in bFieldExpansion:
            v = trans.mxv(
                VectorIJK(bField.getI(), bField.getJ(), bField.getK())
            )
            bFieldExpansionDeformed.append(
                UnwritableVectorIJK(v.getI(), v.getJ(), v.getK())
            )
        return bFieldExpansionDeformed

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions."""
        return self.originalField.getNumberOfBasisFunctions()
