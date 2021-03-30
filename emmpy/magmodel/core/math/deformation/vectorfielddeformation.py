"""emmpy.magmodel.core.math.deformation.vectorfielddeformation"""

# import crucible.core.math.vectorfields.DifferentiableVectorField;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.MatrixIJK;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class VectorFieldDeformation(VectorField):
    """TODO please comment

    author G.K.Stephens
    """

    def __init__(self, originalField, coordDeformation):
        """Constructor.

        param originalField
        param coordDeformation
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate, buffer):
        """evaluate"""

        # compute the derivatives at the given location
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # compute the deformation matrix
        trans = self.computeMatrix(deformed)

        # evaluate the field at the deformed location
        bField = self.originalField.evaluate(deformed.getF())

        #  evaluate the deformed field
        v = trans.mxv(VectorIJK(bField.getI(), bField.getJ(), bField.getK()))

        return buffer.setTo(v.getI(), v.getJ(), v.getK())

    def computeMatrix(self, deformed):
        """computeMatrix

        param deformed
        return
        """
        dFxDx = deformed.getdFxDx()
        dFxDy = deformed.getdFxDy()
        dFxDz = deformed.getdFxDz()
        dFyDx = deformed.getdFyDx()
        dFyDy = deformed.getdFyDy()
        dFyDz = deformed.getdFyDz()
        dFzDx = deformed.getdFzDx()
        dFzDy = deformed.getdFzDy()
        dFzDz = deformed.getdFzDz()
        txx = dFyDy*dFzDz - dFyDz*dFzDy
        txy = dFxDz*dFzDy - dFxDy*dFzDz
        txz = dFxDy*dFyDz - dFxDz*dFyDy
        tyx = dFyDz*dFzDx - dFyDx*dFzDz
        tyy = dFxDx*dFzDz - dFxDz*dFzDx
        tyz = dFxDz*dFyDx - dFxDx*dFyDz
        tzx = dFyDx*dFzDy - dFyDy*dFzDx
        tzy = dFxDy*dFzDx - dFxDx*dFzDy
        tzz = dFxDx*dFyDy - dFxDy*dFyDx
        trans = MatrixIJK(txx, tyx, tzx, txy, tyy, tzy, txz, tyz, tzz)
        return trans
