"""A polar angle transformation for twisting and warping."""


# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.CrucibleMath.sin;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import geomagmodel.ts07.modeling.fieldaligned.Ffunction.FDerivatives;
# import magmodel.core.math.deformation.CylindricalFieldDeformation;
# import magmodel.core.math.vectorfields.BasisVectorField;
# import magmodel.core.math.vectorfields.CylindricalBasisVectorField;
# import magmodel.core.math.vectorfields.CylindricalVectorField;

from math import cos, sin

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.magmodel.core.math.coords.cylindricalcoordsxaligned import (
    CylindricalCoordsXAligned
)
from emmpy.magmodel.core.math.deformation.cylindricalbasisfielddeformation import (
    CylindricalBasisFieldDeformation
)
from emmpy.magmodel.core.math.vectorfields.differentiablecylindricalvectorfield import (
    DifferentiableCylindricalVectorField, Results
)


class TwistWarpFfunction(DifferentiableCylindricalVectorField):
    """A polar angle transformation for twisting and warping.

    Defines a transformation that deforms the polar angle to introduce a
    twisting of the tail current sheet and a tilt warping in the Y-Z plane and
    its partial derivatives with respect to the original coordinates
    cylindrical coordinates.

    From Tsgyanenko 1998, Modeling of twisted/warped magnetospheric
    configurations using the general deformation method, eq. 14.
    where in this implementation, L(X) is just a constant L=20.0, and
    phi_t = -T*X, where T is the twist parameter.

    The class FDerivatives holds references to the value F and the partial
    derivatives of F with respect to the original coordinates.

    author G.K.Stephens
    """

    dG_dx = 0
    xL = 20
    dxL_dx = 0

    def __init__(self, warpParam, twistParam, dipoleTilt):
        """Build a new object.

        Constructs the following function (from Tsyganenko 1998 eq. 14) and
        its derivatives:

        where in this implementation, L(X) is just a constant L=20.0, and
        phi_t = -T*X, where T is the twist parameter.

        param warpParam the double parameter G in the function
        param twistParam the double parameter
        param double dipoleTilt
        """
        self.warpParam = warpParam
        self.twistParam = twistParam
        self.sinDipoleTilt = sin(dipoleTilt)

    # @staticmethod
    # def deformField(dipoleTilt, warpParam, twistParam, undeformedField):
    #     """deformFIeld

    #     param double dipoleTilt
    #     param double warpParam
    #     param double twistParam
    #     param VectorField undeformedField - assumed Cartesian
    #     return VectorField
    #     """

    #     # Convert the supplied undeformed field to cylindrical coordinates
    #     # CylindricalVectorField
    #     undeformedFieldCyl = CylindricalCoordsXAligned.convertField(
    #         undeformedField)

    #     // Construct the deformation
    #     TwistWarpFfunction deformation = new TwistWarpFfunction(warpParam, twistParam, dipoleTilt);

    #     // Deform the cylindrical field
    #     CylindricalFieldDeformation deformedFieldCyl =
    #         new CylindricalFieldDeformation(undeformedFieldCyl, deformation);

    #     // Convert the deformed field back to Cartesian coordinates
    #     VectorField deformedField = CylindricalCoordsXAligned.convertField(deformedFieldCyl);

    #     return deformedField;
    #   }

    @staticmethod
    def deformBasisField(dipoleTilt, warpParam, twistParam, undeformedField):
        """Deform the basis field.

        param double dipoleTilt
        param double warpParam
        param double twistParam
        param BasisVectorField undeformedField
        return BasisVectorField
        """
        # Convert the supplied undeformed field to cylindrical coordinates
        # CylindricalBasisVectorField
        undeformedFieldCyl = CylindricalCoordsXAligned.convertBasisField(
            undeformedField)

        # Construct the deformation
        # TwistWarpFfunction
        deformation = TwistWarpFfunction(warpParam, twistParam, dipoleTilt)

        # Deform the cylindrical field
        # CylindricalBasisFieldDeformation
        deformedFieldCyl = CylindricalBasisFieldDeformation(
            undeformedFieldCyl, deformation)

        # Convert the deformed field back to Cartesian coordinates
        # BasisVectorField
        deformedField = CylindricalCoordsXAligned.convertBasisField(
            deformedFieldCyl)

        return deformedField

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    #     // convert the Cartesian position to cylindrical
    #     CylindricalVector locCyl = CylindricalCoordsXAligned.convert(location);

    #     // evaluate the cylindrical vector field value for the given position
    #     CylindricalVector cylValue = evaluate(locCyl);

    #     // convert the vector field value to Cartesian
    #     UnwritableVectorIJK value = CylindricalCoordsXAligned.convert(cylValue);

    #     return buffer.setTo(value);
    #   }

    #   @Override
    #   public CylindricalVector evaluate(CylindricalVector location) {

    #     double x = location.getHeight();

    #     double rho = location.getCylindricalRadius();
    #     // TODO
    #     if (rho == 0.0) {
    #       rho = 1.0E-14;
    #     }
    #     double rho2 = rho * rho;

    #     double phi = location.getLongitude();
    #     // double sinPhi = sin(phi);
    #     double cosPhi = cos(phi);

    #     double rho4L4 = rho / (rho2 * rho2 + (xL * xL * xL * xL));

    #     // Calculate F (the adjusted phi measurement) and its derivatives
    #     double F = phi + warpParam * rho2 * rho4L4 * cosPhi * sinDipoleTilt + twistParam * x;

    #     return new CylindricalVector(rho, F, x);
    #   }

    def differentiate(self, location):
        """Evaluate the twist and warp transformation of the polar angle.

        F(rho, phi, x) where (rho, phi, x) are the original undistorted
        coordinates (in modified cylindrical coordinates) and the partial
        derivatives of F with respect to these original coordinates

        param CylindricalVector location
        return Results
        """
        # float x, rho, rho2, phi, sinPhi, cosPhi, rho4L4
        x = location.z
        rho = location.rho
        # TODO
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
        # float F
        F = (
            phi + self.warpParam*rho2*rho4L4*cosPhi*self.sinDipoleTilt +
            self.twistParam*x
        )

        # compute derivatives of F with respect to phi, rho, and x
        # float dRho_dPhi, dRho_dRho, dRho_dx
        dRho_dPhi = 0.0
        dRho_dRho = 1.0
        dRho_dx = 0.0

        # float dF_dPhi, dF_dRho, dF_dx
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

        # float dx_dPhi, dx_dRho, dx_dx
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
