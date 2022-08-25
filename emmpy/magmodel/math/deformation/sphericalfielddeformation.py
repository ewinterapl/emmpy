"""Deformation for a spherical field.

Deformation for a spherical field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import sin

from emmpy.magmodel.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.matrices.matrixijk import MatrixIJK


class SphericalFieldDeformation(SphericalVectorField):
    """Deformation for a spherical field.

    Deformation for a spherical field.
    """

    def __init__(self, originalField, coordDeformation):
        """Initialize a new SphericalFieldDeformation object.

        Initialize a new SphericalFieldDeformation object.

        Parameters
        ----------
        originalField : SphericalVectorField
            Original field to deform.
        coordDeformation : DifferentiableSphericalVectorField
            Vector field defining the deformation.
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        originalCoordinate : SphericalVector
            Location to evaluate the field
        SphericalVector
            Deformed spherical field value.
        """
        # Compute the derivatives at the given location.
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # Compute the deformation matrix.
        trans = self.computeMatrix(deformed, originalCoordinate)

        # Evaluate the field at the deformed location.
        bField = self.originalField.evaluate(deformed.f)

        # Evaluate the deformed field.
        v = VectorIJK()
        v[:] = trans.dot(VectorIJK(bField.r, bField.theta, bField.phi))

        return SphericalVector(v.i, v.j, v.k)

    @staticmethod
    def computeMatrix(deformed, originalCoordinate):
        """Compute the deformation matrix.

        Compute the deformation matrix.

        Parameters
        ----------
        deformed : DifferentiableSphericalVectorField.Results
            Derivatives of deformation field.
        originalCoordinate : SphericalVector
            Location to compute the deformation.

        Returns
        -------
        trans : MatrixIJK
            Deformationm transformation matrix.
        """
        r = originalCoordinate.r
        theta = originalCoordinate.theta
        hr = 1
        ht = r
        hp = r*sin(theta)
        hrDef = 1
        htDef = deformed.f.r
        hpDef = deformed.f.r*sin(deformed.f.theta)
        dFrDr = deformed.dFrDr
        dFrDt = deformed.dFrDt
        dFrDp = deformed.dFrDp
        dFtDr = deformed.dFtDr
        dFtDt = deformed.dFtDt
        dFtDp = deformed.dFtDp
        dFpDr = deformed.dFpDr
        dFpDt = deformed.dFpDt
        dFpDp = deformed.dFpDp
        trr = (htDef*hpDef/(ht*hp))*(dFtDt*dFpDp - dFtDp*dFpDt)
        trt = (hrDef*hpDef/(ht*hp))*(dFrDp*dFpDt - dFrDt*dFpDp)
        trp = (hrDef*htDef/(ht*hp))*(dFrDt*dFtDp - dFrDp*dFtDt)
        ttr = (htDef*hpDef/(hr*hp))*(dFtDp*dFpDr - dFtDr*dFpDp)
        ttt = (hrDef*hpDef/(hr*hp))*(dFrDr*dFpDp - dFrDp*dFpDr)
        ttp = (hrDef*htDef/(hr*hp))*(dFrDp*dFtDr - dFrDr*dFtDp)
        tpr = (htDef*hpDef/(hr*ht))*(dFtDr*dFpDt - dFtDt*dFpDr)
        tpt = (hrDef*hpDef/(hr*ht))*(dFrDt*dFpDr - dFrDr*dFpDt)
        tpp = (hrDef*htDef/(hr*ht))*(dFrDr*dFtDt - dFrDt*dFtDr)
        trans = MatrixIJK([[trr, trt, trp],
                           [ttr, ttt, ttp],
                           [tpr, tpt, tpp]])
        return trans
