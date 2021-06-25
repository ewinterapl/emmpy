"""emmpy.geomagmodel.ts07.modeling.fieldaligned.stretchedfield"""


from math import atan2, cos, sin, sqrt

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.geomagmodel.ts07.modeling.fieldaligned.ffunction import (
    FDerivatives, Ffunction
)


class StretchedField(VectorField):
    """Performs a stretching deformation on the input VectorField.
    
    This stretching is accounting for 3 effects as described in
    "A model of the near magnetosphere with a dawn-dusk asymmetry 1.
    Mathematical structure" by N. A. Tsyganenko.
    See eq. (21, 22, 23, 24, and 25) in section 2.3.3.

    1: the noon-midnight asymmetry in the R1 and R2 field aligned currents.
    2: dipole tilt angle
    3: a spatial scaling that can account for the equatorward expansion of the
    Birkeland current ovals.

    see http://onlinelibrary.wiley.com/doi/10.1029/2001JA000219/abstract
    (Tsyganenko, 2002)

    author Nicholas Sharp
    author G.K.Stephens
    """

    # float rho02, beta, hingeDistance, epsilon, bConst
    rho02 = 49.0
    beta = 0.9
    hingeDistance = 10.0
    epsilon = 3.0
    bConst = 0.5  # These parameters adjust the deformation

    def __init__(self, unstretchedField, dipoleTilt, deltaPhi):
        """Constructor

        param VectorField unstretchedField the input unstretched field that
        will be stretched
        param double dipoleTilt the dipole tilt angle
        param deltaPhi deltaPhi determines the amount of shift of the center
        of the FAC region to the nightside
        """
        # VectorField unstretchedField
        self.unstretchedField = unstretchedField
        # double deltaPhi
        self.deltaPhi = deltaPhi
        # double dipoleTilt
        self.dipoleTilt = dipoleTilt
        # Ffunction fFunction
        self.fFunction = Ffunction(deltaPhi, dipoleTilt)

    def evaluate(self, location, buffer):
        """evaluate

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """

        # float x, y, z, rho2, rho, phi, sinPhi, cosPhi
        x = location.i
        y = location.j
        z = location.k
        # convert to spherical and cylindrical
        rho2 = x*x + z*z
        rho = sqrt(rho2)
        phi = 0.0
        if x == 0 and z == 0:
            phi = 0
        else:
            phi = atan2(-z, x)
        sinPhi = sin(phi)
        cosPhi = cos(phi)

        # Tsy 2002-1 eqn 21, evaluates the stretch transformation function that
        # is used for the FAC field along with the partial derivatives with
        # respect to phi, rho, and y
        # FDerivatives fValues
        fValues = self.fFunction.evaluate(CylindricalVector(rho, phi, y))

        # the derivatives
        # float dF_dPhi, dF_dRho, dF_dy, sinF, cosF, xStar, yStar, zStar
        dF_dPhi = fValues.getdF_dPhi()
        dF_dRho = fValues.getdF_dRho()
        dF_dy = fValues.getdF_dy()
        sinF = sin(fValues.getF())
        cosF = cos(fValues.getF())
        xStar = rho*cosF
        yStar = y
        zStar = -rho*sinF

        # UnwritableVectorIJK unstretchedVector
        unstretchedVector = self.unstretchedField.evaluate(
            VectorIJK(xStar, yStar, zStar)
        )

        # Tsy 2002-1 eqn 22, B* the original undeformed field evaluated with
        # the deformed coordinates
        # float bRhoStar, bPhiStar
        bRhoStar = (
            unstretchedVector.i*cosF - unstretchedVector.k*sinF
        )
        bPhiStar = (
            -unstretchedVector.i*sinF - unstretchedVector.k*cosF
        )

        # Tsy 2002-1 eqn 23, B' apply the transformation matrix
        # float bRho, bPhi, by
        bRho = bRhoStar*dF_dPhi
        bPhi = bPhiStar - rho*(unstretchedVector.j*dF_dy +
                               bRhoStar*dF_dRho)
        by = unstretchedVector.j*dF_dPhi

        # Tsy 2002-1 eqn 24, and now convert B' from cylindrial to Cartesian
        # float bx, bz
        bx = bRho*cosPhi - bPhi*sinPhi
        bz = -bRho*sinPhi - bPhi*cosPhi

        return buffer.setTo(bx, by, bz)

    def evaluate2(self, location, buffer):
        """evaluate2

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """

        # float x, y, z
        x = location.getI()
        y = location.getJ()
        z = location.getK()

        # convert to spherical and cylindrical
        # float rho2, rho, rSph, phi, sinPhi, cosPhi
        rho2 = x*x + z*z
        rho = sqrt(rho2)
        rSph = sqrt(x*x + y*y + z*z)
        phi = 0.0
        if x == 0 and z == 0:
            phi = 0
        else:
            phi = atan2(-z, x)
        sinPhi = sin(phi)
        cosPhi = cos(phi)

        # Implementation of Tsy 2002-1 eq. (21) (with some extra normalization
        # term applied to b?!)
        # the constant has been scaled by the constant rho02 / (rho02 + 1)
        # float sinPhiCoef, r1Rh, f, fm1, psiTerm
        sinPhiCoef = (
            self.deltaPhi + StretchedField.bConst*StretchedField.rho02 /
            (StretchedField.rho02 + 1)*(rho2 - 1)/(StretchedField.rho02 + rho2)
        )
        r1Rh = (rSph - 1)/StretchedField.hingeDistance
        f = (1 + pow(r1Rh, StretchedField.epsilon))
        fm1 = pow(r1Rh, StretchedField.epsilon - 1)
        psiTerm = (
            StretchedField.beta*self.dipoleTilt /
            pow(f, 1/StretchedField.epsilon)
        )

        # "F" in literature
        # float phiStretched
        phiStretched = phi - sinPhiCoef*sinPhi - psiTerm

        # compute derivatives of F with respect to phi, rho, and y
        # float dF_dPhi, dF_dRho, dF_dy, sinF, cosF, xStar, yStar, zStar
        dF_dPhi = 1 - sinPhiCoef*cosPhi
        dF_dRho = (
            -2*StretchedField.bConst*StretchedField.rho02*rho /
            (StretchedField.rho02 + rho2)*(StretchedField.rho02 + rho2)*sinPhi +
            StretchedField.beta*self.dipoleTilt*fm1*rho /
            (self.hingeDistance*rSph*pow(f, 1/StretchedField.epsilon + 1))
        )
        dF_dy = (
            StretchedField.beta*self.dipoleTilt*fm1*y /
            (self.hingeDistance*rSph*pow(f, 1/StretchedField.epsilon + 1))
        )
        sinF = sin(phiStretched)
        cosF = cos(phiStretched)
        xStar = rho*cosF
        yStar = y
        zStar = -rho*sinF

        # UnwritableVectorIJK unstretchedVector
        unstretchedVector = (
            self.unstretchedField.evaluate(VectorIJK(xStar, yStar, zStar))
        )

        # Tsy 2002-1 eqn 22, B* the original undeformed field evaluated with
        # the deformed coordinates
        # float bRhoStar, bPhiStar
        bRhoStar = (
            unstretchedVector.getI()*cosF - unstretchedVector.getK()*sinF
        )
        bPhiStar = (
            -unstretchedVector.getI()*sinF - unstretchedVector.getK()*cosF
        )

        # Tsy 2002-1 eqn 23, B' apply the transformation matrix
        # float bRho, bPhi, by
        bRho = bRhoStar*dF_dPhi
        bPhi = bPhiStar - rho*(unstretchedVector.getJ()*dF_dy +
                               bRhoStar*dF_dRho)
        by = unstretchedVector.getJ()*dF_dPhi

        # Tsy 2002-1 eqn 24, and now convert B' from cylindrial to Cartesian
        # float bx, bz
        bx = bRho*cosPhi - bPhi*sinPhi
        bz = -bRho*sinPhi - bPhi*cosPhi

        return buffer.setTo(bx, by, bz)
