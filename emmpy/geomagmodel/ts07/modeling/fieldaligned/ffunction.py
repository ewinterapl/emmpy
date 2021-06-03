"""emmpy.geomagmodel.ts07.modeling.fieldaligned.ffunction"""

# import static crucible.core.math.CrucibleMath.atan2;
# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.sqrt;

import math

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector

# import crucible.core.math.vectorfields.ScalarField;
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField


class FDerivatives:
    """A class that holds the deformed coordinate F (Tsyganenko 2002 eq. 21)
    and the partial derivatives of F with respect to the original undeformed
    coordinates phi, rho, and y

    author G.K.Stephens
    """

    def __init__(self, f, dF_dPhi, dF_dRho, dF_dy):
        """Constructor"""
        self.f = f
        self.dF_dPhi = dF_dPhi
        self.dF_dRho = dF_dRho
        self.dF_dy = dF_dy

    def getF(self):
        return self.f

    def getdF_dPhi(self):
        return self.dF_dPhi

    def getdF_dRho(self):
        return self.dF_dRho

    def getdF_dy(self):
        return self.dF_dy


class Ffunction(ScalarField):
    """From Tsyganenko 2002, A model of the near magnetosphere with a dawn-dusk
    asymmetry 1.

    Mathematical structure, eq. 21. Defines a stretch transformation that
    deforms the polar angle for the use in deforming the magnetic field of the
    Field aligned currents and the partial derivatives with respect to the
    original coordinates.

    The class FDerivatives holds references to the value F and the partial
    derivates of F with respect to the original coordinates.

    @author G.K.Stephens
    """

    # double rho0 = 7.0; // (see Tsy 2002-1 paragraph 47)
    rho02 = 49.0
    beta = 0.9
    hingeDistance = 10.0
    epsilon = 3.0
    bConst = .5  # These parameters adjust the deformation
    # b = bConst * rho02 / (rho02 + 1);

    def __init__(self, deltaPhi, dipoleTilt):
        self.deltaPhi = deltaPhi
        self.dipoleTilt = dipoleTilt

    def evaluate(self, location):
        """evaluate"""
        if isinstance(location, CylindricalVector):
            # Evaluates the stretch transformation of the polar angle,
            # F(rho, phi, y) where (rho, phi, y) are the original undistorted
            # coordinates (in modified cylindrical coordinates) and the partial
            # derivatives of F with respect to these original coordinates.
            # param location the
            y = location.getHeight()

            # convert to spherical and cylindrical
            rho = location.getCylindricalRadius()
            rho2 = rho*rho
            r = math.sqrt(rho2 + y*y)
            phi = location.getLongitude()
            sinPhi = math.sin(phi)
            cosPhi = math.cos(phi)

            # Implementation of Tsy 2002-1 eq. (21) (with some extra
            # normalization term applied to b?!)
            # the constant has been scaled by the constant rho02 / (rho02 + 1)
            sinPhiCoef = (
                self.deltaPhi + Ffunction.bConst*Ffunction.rho02 /
                (Ffunction.rho02 + 1)*(rho2 - 1)/(Ffunction.rho02 + rho2)
            )
            # the quantity (r-1)/rH
            rRh = (r - 1)/Ffunction.hingeDistance

            # the quantity ((r-1)/rH)^eps
            rRhEps = math.pow(rRh, Ffunction.epsilon)
            fm1 = rRhEps/rRh

            f = 1 + rRhEps

            # Tsy 1998 eq. 10, dipole tilt deformation function Q(r)
            qr = math.pow(f, (1/Ffunction.epsilon))
            dQr = qr*f  # results from the derivative of Q(r)

            psiTerm = Ffunction.beta*self.dipoleTilt/qr

            # "F" in literature
            phiStretched = phi - sinPhiCoef*sinPhi - psiTerm

            # compute derivatives of F with respect to phi, rho, and y
            dF_dPhi = 1 - sinPhiCoef*cosPhi
            dF_dRho = (
                -2*Ffunction.bConst*Ffunction.rho02*rho /
                ((Ffunction.rho02 + rho2)*(Ffunction.rho02 + rho2))*sinPhi +
                Ffunction.beta*self.dipoleTilt*fm1*rho /
                (Ffunction.hingeDistance*r*dQr)
            )
            dF_dy = (
                Ffunction.beta*self.dipoleTilt*fm1*y /
                (Ffunction.hingeDistance*r*dQr)
            )
            return FDerivatives(phiStretched, dF_dPhi, dF_dRho, dF_dy)
        elif isinstance(location, UnwritableVectorIJK):
            x = location.getI()
            y = location.getJ()
            z = location.getK()

            # convert to spherical and cylindrical
            rho2 = x*x + z*z
            rho = math.sqrt(rho2)
            phi = 0.0

            if x == 0 and z == 0:
                phi = 0
            else:
                phi = math.atan2(-z, x)

            return self.evaluate(CylindricalVector(rho, phi, y)).getF()
