"""Deform a vector field.

Deform a vector field using a differentiable vector field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class VectorFieldDeformation(VectorField):
    """Deform a vector field.

    Deform a vector field using a differentiable vector field.
    """

    def __init__(self, originalField, coordDeformation):
        """Initialize a new VectorFieldDeformation object.

        Initialize a new VectorFieldDeformation object.

        Parameters
        ----------
        originalField : VectorField
            The original vector field to deform.
        coordDeformation : DifferentiableVectorField
            The vector field defining the deformation.
        """
        self.originalField = originalField
        self.coordDeformation = coordDeformation

    def evaluate(self, originalCoordinate, buffer):
        """Evaluate the field, then apply the deformation.
        
        Evaluate the field, then apply the deformation.

        Parameters
        ----------
        originalCoordinate : VectorIJK
            Location to evaluate field before deformation.
        buffer : VectorIJK
            Buffer to hold deformed vector field value.
        
        Returns
        -------
        buffer : VectorIJK
            Deformed vector field value at location.
        """
        # Compute the deformation derivatives at the given location.
        deformed = self.coordDeformation.differentiate(originalCoordinate)

        # Compute the deformation matrix.
        trans = self.computeMatrix(deformed)

        # Evaluate the field at the deformed location.
        bField = self.originalField.evaluate(deformed.getF())

        # Evaluate the deformed field.
        v = trans.mxv(VectorIJK(bField.getI(), bField.getJ(), bField.getK()))

        # Return the updated buffer.
        return buffer.setTo(v.getI(), v.getJ(), v.getK())

    @staticmethod
    def computeMatrix(deformed):
        """Compute the deformation matrix from the field derivatives.

        Compute the deformation matrix from the field derivatives.

        Parameters
        ----------
        deformed : DifferentiableVectorField.Results
            Object containing the deformation derivatives.

        Returns
        -------
        trans : MatrixIJK
            The deformation matrix.
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
