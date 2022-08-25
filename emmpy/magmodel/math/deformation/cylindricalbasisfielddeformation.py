"""Deformation of a cylindrical basis vector field.

Deformation of a cylindrical basis vector field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.math.deformation.cylindricalfielddeformation import (
    CylindricalFieldDeformation
)
from emmpy.magmodel.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.vectorijk import VectorIJK


class CylindricalBasisFieldDeformation(CylindricalBasisVectorField):
    """Deformation of a cylindrical basis vector field.

    Deformation of a cylindrical basis vector field.
    """

    def __init__(self, originalField, coordDeformation):
        """Initialize a new CylindricalBasisVectorFieldDeformation object.

        Initialize a new CylindricalBasisVectorFieldDeformation object.

        Parameters
        ----------
        originalField : CylindricalBasisVectorField
            Original field to deform.
        coordDeformation : DifferentiableCylindricalVectorField
            Vector field defining the deformation.
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluateExpansion(self, originalCoordinate):
        """Evaluate and deform the expansion.

        Evaluate and deform the expansion.

        Parameters
        ----------
        originalCoordinate : CylindricalVector
            Location to compute deformed field.

        Returns
        -------
        bFieldExpansionDeformed : list of CylindricalVector
            Deformed expansion components.
        """
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        trans = CylindricalFieldDeformation.computeMatrix(
            deformed, originalCoordinate
        )
        bFieldExpansion = self.originalField.evaluateExpansion(deformed.f)
        bFieldExpansionDeformed = []
        for bField in bFieldExpansion:
            v = VectorIJK()
            vcyl = VectorIJK(bField.rho, bField.phi, bField.z)
            v[:] = trans.dot(vcyl)
            bFieldExpansionDeformed.append(CylindricalVector(v.i, v.j, v.k))
        return bFieldExpansionDeformed
