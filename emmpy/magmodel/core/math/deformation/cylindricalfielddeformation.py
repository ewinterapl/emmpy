"""Deformation for a cylindrical field."""


import sys
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class CylindricalFieldDeformation(CylindricalVectorField):
    """Deformation for a cylindrical field.

    author G.K.Stephens
    """

    def __init__(self, originalField, coordDeformation):
        """Build a new object.

        param CylindricalVectorField originalField
        param DifferentiableCylindricalVectorField coordDeformation
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate):
        """Evaluate the field.

        param CylindricalVector originalCoordinate
        return CylindricalVector
        """
        # compute the derivatives at the given location
        # DifferentiableCylindricalVectorField.Results deformed
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # compute the deformation matrix
        # MatrixIJK trans
        trans = self.computeMatrix(deformed, originalCoordinate)

        # evaluate the field at the deformed location
        # CylindricalVector bField
        bField = self.originalField.evaluate(deformed.getF())

        # evaluate the deformed field
        # VectorIJK v
        v = trans.mxv(VectorIJK(
            bField.getCylindricalRadius(), bField.getLongitude(),
            bField.getHeight())
        )

        return CylindricalVector(v.getI(), v.getJ(), v.getK())

    @staticmethod
    def computeMatrix(deformed, originalCoordinate):
        """Compute the deformation matrix.

        param DifferentiableCylindricalVectorField.Results deformed
        param CylindricalVector originalCoordinate
        return MatrixIJK
        """
        # float r, hr, hp, hz, hrDef, hpDef, hzDef
        r = originalCoordinate.rho
        hr = 1.0
        hp = r
        hz = 1.0
        hrDef = 1.0
        hpDef = deformed.getF().rho
        hzDef = 1.0

        # float dFrDr, dFrDp, dFrDz
        dFrDr = deformed.getdFrDr()
        dFrDp = deformed.getdFrDp()
        dFrDz = deformed.getdFrDz()

        # float dFpdr, dFpDp, dFpDz
        dFpDr = deformed.getdFpDr()
        dFpDp = deformed.getdFpDp()
        dFpDz = deformed.getdFpDz()

        # float dFzDr, dFzDp, dFzDz
        dFzDr = deformed.getdFzDr()
        dFzDp = deformed.getdFzDp()
        dFzDz = deformed.getdFzDz()

        # float trr, trp, trz
        trr = (hpDef*hzDef/(hp*hz))*(dFpDp*dFzDz - dFpDz*dFzDp)
        trp = (hrDef*hzDef/(hp*hz))*(dFrDz*dFzDp - dFrDp*dFzDz)
        trz = (hrDef*hpDef/(hp*hz))*(dFrDp*dFpDz - dFrDz*dFpDp)

        # float tpr, tpp, tpz
        tpr = (hpDef*hzDef/(hr*hz))*(dFpDz*dFzDr - dFpDr*dFzDz)
        tpp = (hrDef*hzDef/(hr*hz))*(dFrDr*dFzDz - dFrDz*dFzDr)
        tpz = (hrDef*hpDef/(hr*hz))*(dFrDz*dFpDr - dFrDr*dFpDz)

        # float tzr, tzp, tzz
        tzr = (hpDef*hzDef/(hr*hp))*(dFpDr*dFzDp - dFpDp*dFzDr)
        tzp = (hrDef*hzDef/(hr*hp))*(dFrDp*dFzDr - dFrDr*dFzDp)
        tzz = (hrDef*hpDef/(hr*hp))*(dFrDr*dFpDp - dFrDp*dFpDr)

        # MatrixIJK trans
        trans = MatrixIJK(trr, tpr, tzr, trp, tpp, tzp, trz, tpz, tzz)

        # TODO ugh, what do I do here
        if hp == 0:
            trr = (1*hzDef/(1*hz))*(dFpDp*dFzDz - dFpDz*dFzDp)
            trp = sys.float_info.max*(dFrDz*dFzDp - dFrDp*dFzDz)
            trz = (hrDef*1/(1*hz))*(dFrDp*dFpDz - dFrDz*dFpDp)
            tpr = (hpDef*hzDef/(hr*hz))*(dFpDz*dFzDr - dFpDr*dFzDz)
            tpp = (hrDef*hzDef/(hr*hz))*(dFrDr*dFzDz - dFrDz*dFzDr)
            tpz = (hrDef*hpDef/(hr*hz))*(dFrDz*dFpDr - dFrDr*dFpDz)
            tzr = (1*hzDef/(hr*1))*(dFpDr*dFzDp - dFpDp*dFzDr)
            tzp = sys.float_info.max*(dFrDp*dFzDr - dFrDr*dFzDp)
            tzz = (hrDef*1/(hr*1))*(dFrDr*dFpDp - dFrDp*dFpDr)
            trans = MatrixIJK(trr, tpr, tzr, trp, tpp, tzp, trz, tpz, tzz)

        return trans
