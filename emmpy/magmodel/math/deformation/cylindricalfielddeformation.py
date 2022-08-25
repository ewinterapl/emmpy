"""Deformation for a cylindrical field.

Deformation for a cylindrical field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import sys

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.matrices.matrixijk import MatrixIJK


class CylindricalFieldDeformation:
    """Deformation for a cylindrical field.

    Deformation for a cylindrical field.
    """

    def __init__(self, originalField, coordDeformation):
        """Initialize a new CylindricalFieldDeformation object.

        Initialize a new CylindricalFieldDeformation object.

        Parameters
        ----------
        originalField : CylindricalVectorField
            Original field to deform.
        coordDeformation : DifferentiableCylindricalVectorField
            Vector field defining the deformation.
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        originalCoordinate : CylindricalVector
            Location to evaluate the field.

        Returns
        -------
        result : CylindricalVector
            The deformed field value.
        """
        # Compute the derivatives at the given location.
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # Compute the deformation matrix.
        trans = self.computeMatrix(deformed, originalCoordinate)

        # Evaluate the field at the deformed location.
        bField = self.originalField.evaluate(deformed.getF())

        # Evaluate the deformed field.
        v = trans.mxv(VectorIJK(bField.rho, bField.phi, bField.z))

        return CylindricalVector(v.i, v.j, v.k)

    @staticmethod
    def computeMatrix(deformed, originalCoordinate):
        """Compute the deformation matrix.

        Compute the deformation matrix.

        Parameters
        ----------
        deformed : DifferentiableCylindricalVectorField.Results
            Derivatives of deformation field.
        originalCoordinate : CylindricalVector 
            Deformation matrix at the location.
        
        Returns
        -------
        trans : MatrixIJK
            The transformation matrix for the deformation.
        """
        r = originalCoordinate.rho
        hr = 1.0
        hp = r
        hz = 1.0
        hrDef = 1.0
        hpDef = deformed.f.rho
        hzDef = 1.0
        dFrDr = deformed.dFrDr
        dFrDp = deformed.dFrDp
        dFrDz = deformed.dFrDz
        dFpDr = deformed.dFpDr
        dFpDp = deformed.dFpDp
        dFpDz = deformed.dFpDz
        dFzDr = deformed.dFzDr
        dFzDp = deformed.dFzDp
        dFzDz = deformed.dFzDz
        trr = (hpDef*hzDef/(hp*hz))*(dFpDp*dFzDz - dFpDz*dFzDp)
        trp = (hrDef*hzDef/(hp*hz))*(dFrDz*dFzDp - dFrDp*dFzDz)
        trz = (hrDef*hpDef/(hp*hz))*(dFrDp*dFpDz - dFrDz*dFpDp)
        tpr = (hpDef*hzDef/(hr*hz))*(dFpDz*dFzDr - dFpDr*dFzDz)
        tpp = (hrDef*hzDef/(hr*hz))*(dFrDr*dFzDz - dFrDz*dFzDr)
        tpz = (hrDef*hpDef/(hr*hz))*(dFrDz*dFpDr - dFrDr*dFpDz)
        tzr = (hpDef*hzDef/(hr*hp))*(dFpDr*dFzDp - dFpDp*dFzDr)
        tzp = (hrDef*hzDef/(hr*hp))*(dFrDp*dFzDr - dFrDr*dFzDp)
        tzz = (hrDef*hpDef/(hr*hp))*(dFrDr*dFpDp - dFrDp*dFpDr)
        trans = MatrixIJK([[trr, trp, trz],
                           [tpr, tpp, tpz],
                           [tzr, tzp, tzz]])

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
            trans = MatrixIJK([[trr, tpr, tzr], [trp, tpp, tzp], [trz, tpz, tzz]])

        return trans
