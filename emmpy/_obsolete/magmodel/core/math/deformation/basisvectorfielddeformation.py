"""emmpy.magmodel.core.math.deformation.basisvectorfielddeformation"""


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
    """BasisVectorFieldDeformation"""

    def __init__(self, originalField, coordDeformation):
        """Constructor"""
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate, buffer):
        """evaluate"""
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        trans = VectorFieldDeformation.computeMatrix(deformed)   # STATIC?
        bField = self.originalField.evaluate(deformed.getF())
        v = trans.mxv(VectorIJK(bField.getI(), bField.getJ(), bField.getK()))
        return buffer.setTo(v.getI(), v.getJ(), v.getK())

    def evaluateExpansion(self, originalCoordinate):
        """evaluateExpansion"""
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
        return self.originalField.getNumberOfBasisFunctions()
