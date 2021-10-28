"""Perform a stretching deformation on a vector field.

Perform a stretching deformation on a vector field.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, sin, sqrt

from emmpy.geomagmodel.ts07.modeling.fieldaligned.ffunction import Ffunction
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


class StretchedField(VectorField):
    """Perform a stretching deformation on a vector field.
    
    This stretching is accounting for 3 effects as described in "A model
    of the near magnetosphere with a dawn-dusk asymmetry 1. Mathematical
    structure" by N. A. Tsyganenko. See eq. (21, 22, 23, 24, and 25) in
    section 2.3.3.

    1: the noon-midnight asymmetry in the R1 and R2 field aligned
       currents.
    2: dipole tilt angle
    3: a spatial scaling that can account for the equatorward expansion
       of the Birkeland current ovals.

    See http://onlinelibrary.wiley.com/doi/10.1029/2001JA000219/abstract
    (Tsyganenko, 2002).

    Attributes
    ----------
    unstretchedField : VectorField
        The input unstretched field that will be stretched.
    dipoleTilt : float
        The dipole tilt angle.
    deltaPhi : float
        Determines the amount of shift of the center of the FAC region to
        the nightside.
    fFunction : Ffunction
        Stretching function.
    """

    rho02 = 49.0
    beta = 0.9
    hingeDistance = 10.0
    epsilon = 3.0
    bConst = 0.5  # These parameters adjust the deformation

    def __init__(self, unstretchedField, dipoleTilt, deltaPhi):
        """Initialize a new StretchedField object.

        Initialize a new StretchedField object.

        Parameters
        ----------
        unstretchedField : VectorField
            The input unstretched field that will be stretched.
        dipoleTilt : float
            The dipole tilt angle.
        deltaPhi : float
            Determines the amount of shift of the center of the FAC region
            to the nightside.
        """
        self.unstretchedField = unstretchedField
        self.deltaPhi = deltaPhi
        self.dipoleTilt = dipoleTilt
        self.fFunction = Ffunction(deltaPhi, dipoleTilt)

    def evaluate(self, location, buffer):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        buffer : VectorIJK
            Buffer to hold the result.

        Returns
        -------
        buffer : VectorIJK
            Field evaluated at location.
        """
        x = location.i
        y = location.j
        z = location.k

        # Convert to spherical and cylindrical.
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
        # respect to phi, rho, and y.
        fValues = self.fFunction.evaluate(CylindricalVector(rho, phi, y))

        # The derivatives.
        dF_dPhi = fValues.dF_dPhi
        dF_dRho = fValues.dF_dRho
        dF_dy = fValues.dF_dy
        sinF = sin(fValues.f)
        cosF = cos(fValues.f)
        xStar = rho*cosF
        yStar = y
        zStar = -rho*sinF

        unstretchedVector = self.unstretchedField.evaluate(
            VectorIJK(xStar, yStar, zStar)
        )

        # Tsy 2002-1 eqn 22, B* the original undeformed field evaluated with
        # the deformed coordinates.
        bRhoStar = (
            unstretchedVector.i*cosF - unstretchedVector.k*sinF
        )
        bPhiStar = (
            -unstretchedVector.i*sinF - unstretchedVector.k*cosF
        )

        # Tsy 2002-1 eqn 23, B' apply the transformation matrix.
        bRho = bRhoStar*dF_dPhi
        bPhi = bPhiStar - rho*(unstretchedVector.j*dF_dy +
                               bRhoStar*dF_dRho)
        by = unstretchedVector.j*dF_dPhi

        # Tsy 2002-1 eqn 24, and now convert B' from cylindrial to Cartesian.
        bx = bRho*cosPhi - bPhi*sinPhi
        bz = -bRho*sinPhi - bPhi*cosPhi

        buffer[:] = [bx, by, bz]
        return buffer

    def evaluate2(self, location, buffer):
        """An alternative evaluation of the field.

        An alternative evaluation of the field.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        buffer : VectorIJK
            Buffer to hold the result.

        Returns
        -------
        buffer : VectorIJK
            Field evaluated at location.
        """
        x = location.i
        y = location.j
        z = location.k

        # Convert to spherical and cylindrical.
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
        # term applied to b?!).
        # The constant has been scaled by the constant rho02 / (rho02 + 1).
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

        # "F" in literature.
        phiStretched = phi - sinPhiCoef*sinPhi - psiTerm

        # Compute derivatives of F with respect to phi, rho, and y.
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

        unstretchedVector = (
            self.unstretchedField.evaluate(VectorIJK(xStar, yStar, zStar))
        )

        # Tsy 2002-1 eqn 22, B* the original undeformed field evaluated with
        # the deformed coordinates.
        bRhoStar = (
            unstretchedVector.i*cosF - unstretchedVector.k*sinF
        )
        bPhiStar = (
            -unstretchedVector.i*sinF - unstretchedVector.k*cosF
        )

        # Tsy 2002-1 eqn 23, B' apply the transformation matrix.
        bRho = bRhoStar*dF_dPhi
        bPhi = bPhiStar - rho*(unstretchedVector.j*dF_dy +
                               bRhoStar*dF_dRho)
        by = unstretchedVector.j*dF_dPhi

        # Tsy 2002-1 eqn 24, and now convert B' from cylindrial to Cartesian.
        bx = bRho*cosPhi - bPhi*sinPhi
        bz = -bRho*sinPhi - bPhi*cosPhi

        return buffer.setTo(bx, by, bz)
