"""Deformation for a spherical field."""


from math import sin

from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class SphericalFieldDeformation(SphericalVectorField):
    """Deformation for a spherical field.

    author G.K.Stephens
    """

    def __init__(self, originalField, coordDeformation):
        """Build a new object.

        param SphericalVectorField originalField
        param DifferentiableSphericalVectorField coordDeformation
        """
        # SphericalVectorField originalField
        self.originalField = originalField
        # DifferentiableSphericalVectorField coordDeformation
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate):
        """Evaluate the field.

        param SphericalVector originalCoordinate
        return SphericalVector
        """
        # compute the derivatives at the given location
        # Results deformed
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # compute the deformation matrix
        # MatrixIJK trans
        trans = self.computeMatrix(deformed, originalCoordinate)

        # evaluate the field at the deformed location
        # SphericalVector bField
        bField = self.originalField.evaluate(deformed.getF())

        # evaluate the deformed field
        # VectorIJK v
        v = VectorIJK()
        v[:] = trans.dot(
            VectorIJK(bField.getRadius(), bField.getColatitude(),
                      bField.getLongitude())
        )

        return SphericalVector(v.i, v.j, v.k)

    @staticmethod
    def computeMatrix(deformed, originalCoordinate):
        """Compute the deformation matrix.

        param Results deformed
        param SphericalVector originalCoordinate
        return MatrixIJK
        """
        # float r, theta, hr, ht, hp, hrDef, htDef, hpDef
        r = originalCoordinate.getRadius()
        theta = originalCoordinate.getColatitude()
        hr = 1
        ht = r
        hp = r*sin(theta)
        hrDef = 1
        htDef = deformed.getF().getRadius()
        hpDef = (
            deformed.getF().getRadius()*sin(deformed.getF().getColatitude())
        )

        # float dFrDr, dFrDt, dFrDp, dFtDr, dFtDt, dFtDp, dFpDr, dFpDt, dFpDp
        dFrDr = deformed.getdFrDr()
        dFrDt = deformed.getdFrDt()
        dFrDp = deformed.getdFrDp()
        dFtDr = deformed.getdFtDr()
        dFtDt = deformed.getdFtDt()
        dFtDp = deformed.getdFtDp()
        dFpDr = deformed.getdFpDr()
        dFpDt = deformed.getdFpDt()
        dFpDp = deformed.getdFpDp()

        # float trr, trt, trp, ttr, ttt, ttp, tpr, tpt, tpp
        trr = (htDef*hpDef/(ht*hp))*(dFtDt*dFpDp - dFtDp*dFpDt)
        trt = (hrDef*hpDef/(ht*hp))*(dFrDp*dFpDt - dFrDt*dFpDp)
        trp = (hrDef*htDef/(ht*hp))*(dFrDt*dFtDp - dFrDp*dFtDt)
        ttr = (htDef*hpDef/(hr*hp))*(dFtDp*dFpDr - dFtDr*dFpDp)
        ttt = (hrDef*hpDef/(hr*hp))*(dFrDr*dFpDp - dFrDp*dFpDr)
        ttp = (hrDef*htDef/(hr*hp))*(dFrDp*dFtDr - dFrDr*dFtDp)
        tpr = (htDef*hpDef/(hr*ht))*(dFtDr*dFpDt - dFtDt*dFpDr)
        tpt = (hrDef*hpDef/(hr*ht))*(dFrDt*dFpDr - dFrDr*dFpDt)
        tpp = (hrDef*htDef/(hr*ht))*(dFrDr*dFtDt - dFrDt*dFtDr)

        # MatrixIJK trans
        trans = MatrixIJK(trr, ttr, tpr, trt, ttt, tpt, trp, ttp, tpp)
        return trans
