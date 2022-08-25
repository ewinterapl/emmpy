"""A polar angle transformation for twisting and warping.

A polar angle transformation for twisting and warping.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

from emmpy.math.coordinates.cylindricalcoordsxaligned import (
    CylindricalCoordsXAligned
)
from emmpy.magmodel.math.deformation.cylindricalbasisfielddeformation import (
    CylindricalBasisFieldDeformation
)
from emmpy.magmodel.math.vectorfields.differentiablecylindricalvectorfield import (
    Results
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


# Module constants
xL = 20.0


class TwistWarpFfunction:
    """A polar angle transformation for twisting and warping.

    Defines a transformation that deforms the polar angle to introduce a
    twisting of the tail current sheet and a tilt warping in the Y-Z plane
    and its partial derivatives with respect to the original cylindrical
    coordinates.

    From Tsgyanenko 1998, Modeling of twisted/warped magnetospheric
    configurations using the general deformation method, eq. 14.
    where in this implementation, L(X) is just a constant L=20.0, and
    phi_t = -T*X, where T is the twist parameter.

    The class FDerivatives holds references to the value F and the partial
    derivatives of F with respect to the original coordinates.

    Attributes
    ----------
    warpParam : float
        The double parameter G in the function.
    twistParam : float
        twistParam
    dipoleTilt : float
        Sine of the dipole tilt angle.
    """

    dG_dx = 0
    xL = 20
    dxL_dx = 0

    def __init__(self, warpParam, twistParam, dipoleTilt):
        """Initialize a new TwistWarpFfunction object.

        Constructs the following function (from Tsyganenko 1998 eq. 14)
        and its derivatives.

        In this implementation, L(X) is just a constant L=20.0, and
        phi_t = -T*X, where T is the twist parameter.

        Parameters
        ----------
        warpParam : float
            The double parameter G in the function.
        twistParam : float
            twistParam
        dipoleTilt : float
            Dipole tilt angle (radians).
        """
        self.warpParam = warpParam
        self.twistParam = twistParam
        self.sinDipoleTilt = sin(dipoleTilt)

    def evaluate(self, location, buffer):
        """Evaluate the function at the specified location.
        
        Parameters
        ----------
        location : VectorIJK
            Location of evaluation.
        buffer : VectorIJK
            Buffer to hold result.
        
        Returns
        -------
        buffer : VectorIJK
            Result of computation.
        """
        # Convert the Cartesian position to cylindrical.
        locCyl = CylindricalCoordsXAligned.convert(location)

        # Evaluate the cylindrical vector field value for the given position.
        x = locCyl.z
        rho = locCyl.rho
        if rho == 0.0:
            rho = 1.0E-14
        rho2 = rho**2
        phi = locCyl.phi
        cosPhi = cos(phi)
        rho4L4 = rho/(rho2**2 + xL**4)

        # Calculate F (the adjusted phi measurement) and its derivatives.
        F = phi + self.warpParam*rho2*rho4L4*cosPhi*self.sinDipoleTilt + self.twistParam*x

        cylValue =  CylindricalVector(rho, F, x)

        # Convert the vector field value to Cartesian.
        value = CylindricalCoordsXAligned.convert(cylValue);
        buffer[...] = value[...]
        return buffer

    def differentiate(self, location):
        """Evaluate the twist and warp transformation of the polar angle.

        F(rho, phi, x) where (rho, phi, x) are the original undistorted
        coordinates (in modified cylindrical coordinates) and the partial
        derivatives of F with respect to these original coordinates.

        Parameters
        ----------
        location : CylindricalVector
            Location to perform the differentiation.
        
        Returns
        -------
        result : Results
            Result of the differentiation.
        """
        x = location.z
        rho = location.rho
        if rho == 0.0:
            rho = 1.0E-14
        rho2 = rho*rho
        phi = location.phi
        sinPhi = sin(phi)
        cosPhi = cos(phi)
        rho4L4 = (
            rho/(rho2*rho2 + (TwistWarpFfunction.xL*TwistWarpFfunction.xL *
                              TwistWarpFfunction.xL*TwistWarpFfunction.xL))
        )

        # Calculate F (the adjusted phi measurement) and its derivatives
        F = (
            phi + self.warpParam*rho2*rho4L4*cosPhi*self.sinDipoleTilt +
            self.twistParam*x
        )

        # Compute derivatives of F with respect to phi, rho, and x.
        dRho_dPhi = 0.0
        dRho_dRho = 1.0
        dRho_dx = 0.0
        dF_dPhi = 1 - self.warpParam*rho2*rho4L4*sinPhi*self.sinDipoleTilt
        dF_dRho = (
            self.warpParam*rho4L4*rho4L4 *
            (3*TwistWarpFfunction.xL*TwistWarpFfunction.xL *
             TwistWarpFfunction.xL*TwistWarpFfunction.xL - rho2*rho2) *
            cosPhi*self.sinDipoleTilt
        )
        dF_dx = (
            rho4L4*cosPhi*self.sinDipoleTilt *
            (TwistWarpFfunction.dG_dx*rho2 - self.warpParam*rho*rho4L4*4 *
             pow(TwistWarpFfunction.xL, 3)*TwistWarpFfunction.dxL_dx) +
            self.twistParam
        )
        dx_dPhi = 0.0
        dx_dRho = 0.0
        dx_dx = 1.0

        # CylindricalVector deformed
        deformed = CylindricalVector(rho, F, x)

        return Results(
            deformed,
            dRho_dRho, dRho_dPhi, dRho_dx,
            dF_dRho, dF_dPhi, dF_dx,
            dx_dRho, dx_dPhi, dx_dx
        )

    @staticmethod
    def deformBasisField(dipoleTilt, warpParam, twistParam, undeformedField):
        """Deform the basis field.

        Deform the basis field.

        Parameters
        ----------
        dipoleTilt : float
            dipoleTilt
        warpParam : float
            warpParam
        twistParam : float
            twistParam
        undeformedField : BasisVectorField
            undeformedField
        
        Returns
        -------
        deformedField : BasisVectorField
            deformedField
        """
        # Convert the supplied undeformed field to cylindrical coordinates.
        undeformedFieldCyl = CylindricalCoordsXAligned.convertBasisField(
            undeformedField)

        # Construct the deformation.
        deformation = TwistWarpFfunction(warpParam, twistParam, dipoleTilt)

        # Deform the cylindrical field.
        deformedFieldCyl = CylindricalBasisFieldDeformation(
            undeformedFieldCyl, deformation)

        # Convert the deformed field back to Cartesian coordinates.
        deformedField = CylindricalCoordsXAligned.convertBasisField(
            deformedFieldCyl)

        return deformedField
