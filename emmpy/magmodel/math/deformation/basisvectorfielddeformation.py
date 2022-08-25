"""Define a deformation for a basis vector field.

Define a deformation for a basis vector field.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.math.deformation.vectorfielddeformation import (
    VectorFieldDeformation
)
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class BasisVectorFieldDeformation(BasisVectorField):
    """Define a deformation for a basis vector field.

    Define a deformation for a basis vector field.
    """

    def __init__(self, originalField, coordDeformation):
        """Initialize a new BasisVectorFieldDeformation object.

        Initialize a new BasisVectorFieldDeformation object.

        Parameters
        ----------
        originalField : BasisVectorField
            Original basis vector field to deform.
        coordDeformation : DifferentiableVectorField
            Vector field defining the deformation.
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluateExpansion(self, originalCoordinate):
        """Evaluate and deform the expansion at the specified location.
        
        Evaluate and deform the expansion at the specified location.

        Parameters
        ----------
        originalCoordinate : VectorIJK
            Location for expansion evaluation.
        
        Returns
        -------
        bFieldExpansionDeformed : list of VectorIJK
            Deformed expansion terms at location.
        """
        deformed = self.coordDeformation.differentiate(originalCoordinate)
        trans = VectorFieldDeformation.computeMatrix(deformed)
        bFieldExpansion = self.originalField.evaluateExpansion(deformed.f)
        bFieldExpansionDeformed = []
        for bField in bFieldExpansion:
            v = VectorIJK()
            v[:] = trans.dot(VectorIJK(bField.i, bField.j, bField.k))
            bFieldExpansionDeformed.append(VectorIJK(v.i, v.j, v.k))
        return bFieldExpansionDeformed

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions.
        
        Return the number of basis functions.

        Parameters
        ----------
        None

        Returns
        -------
        getNumberOfBasisFunctions() : int
            The number of basis functions in the expansion.
        """
        return self.originalField.getNumberOfBasisFunctions()
