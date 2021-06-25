"""Jacobian matrix for the cylindrical-to-cartesian transformation."""


from math import cos, sin

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class CylindricalToCartesianJacobian(Transformation):
    """Jacobian matrix for the cylindrical-to-cartesian transformation."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Return the transformation matrix.

        .-                                  -.
        |  dx/dr     dx/dlong       dx/dz    |
        |                                    |
        |  dy/dr     dy/dlong       dy/dz    |
        |                                    |
        |  dz/dr     dz/dlong       dz/dz    |
        `-                                  -'

        .-                                  -.
        |  cos(long)  -sin(long)*r    0      |
        |                                    |
        |  sin(long)   cos(long)*r    0      |
        |                                    |
        |     0           0           1      |
        `-                                  -'
        """
        # from SPICE's routine in drdcyl.f
        # JACOBI (DX,DR) = DCOS( LONG )
        # JACOBI (DY,DR) = DSIN( LONG )
        # JACOBI (DZ,DR) = 0.0D0
        # JACOBI (DX,DLON) = -DSIN( LONG ) * R
        # JACOBI (DY,DLON) = DCOS( LONG ) * R
        # JACOBI (DZ,DLON) = 0.0D0
        # JACOBI (DX,DZ) = 0.0D0
        # JACOBI (DY,DZ) = 0.0D0
        # JACOBI (DZ,DZ) = 1.0D0
        r = coordPosition.getCylindricalRadius()
        lon = coordPosition.getLongitude()
        cosLon = cos(lon)
        sinLon = sin(lon)
        j_DX_DR = cosLon
        j_DY_DR = sinLon
        j_DZ_DR = 0.0
        j_DX_DLON = -sinLon*r
        j_DY_DLON = cosLon*r
        j_DZ_DLON = 0.0
        j_DX_DZ = 0.0
        j_DY_DZ = 0.0
        j_DZ_DZ = 1.0
        return buffer.setTo(j_DX_DR, j_DY_DR, j_DZ_DR,
                            j_DX_DLON, j_DY_DLON, j_DZ_DLON,
                            j_DX_DZ, j_DY_DZ, j_DZ_DZ)

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the inverse transformation."""
        try:
            return self.getTransformation(coordPosition, buffer).invort()
        except Exception as e:
            raise PointOnAxisException(e)

    def mxv(self, *args):
        """Multiply a velocity by the jacobian."""
        if isinstance(args[1], CylindricalVector):
            (jacobian, coordVelocity) = args
            return MatrixIJK.mxv(jacobian, coordVelocity.getVectorIJK())
        elif isinstance(args[1], UnwritableVectorIJK):
            (inverseJacobian, cartVelocity) = args
            vect = MatrixIJK.mxv(inverseJacobian, cartVelocity)
            return CylindricalVector(vect.getI(), vect.getJ(), vect.getK())
        else:
            raise Exception
