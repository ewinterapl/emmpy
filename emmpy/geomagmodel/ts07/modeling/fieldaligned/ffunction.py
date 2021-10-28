"""Value and partial derivatives of the deformed coordinate F.

Value and partial derivatives of the deformed coordinate F.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import math

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.vectorijk import VectorIJK


class FDerivatives:
    """Partial derivatives of deformed coordinate F.

    A class that holds the deformed coordinate F (Tsyganenko 2002 eq. 21)
    and the partial derivatives of F with respect to the original
    undeformed coordinates phi, rho, and y.

    Attributes
    ----------
    f : float
        Value of F.
    dF_dPhi : float
        Partial of F wrt angle phi.
    dF_dRho : float
        Partial of F wrt radius rho.
    dF_dy : float
        Partial of F wrt y.
    """

    def __init__(self, f, dF_dPhi, dF_dRho, dF_dy):
        """Initialize a new FDerivatives object.

        Initialize a new FDerivatives object.

        Parameters
        ----------
        f : float
            Value of F.
        dF_dPhi : float
            Partial of F wrt angle phi.
        dF_dRho : float
            Partial of F wrt radius rho.
        dF_dy : float
            Partial of F wrt y.
        """
        self.f = f
        self.dF_dPhi = dF_dPhi
        self.dF_dRho = dF_dRho
        self.dF_dy = dF_dy


class Ffunction:
    """A stretch transformation for the magnetic field.

    From Tsyganenko 2002, A model of the near magnetosphere with a
    dawn-dusk asymmetry 1. Mathematical structure, eq. 21.
    
    Defines a stretch transformation that deforms the polar angle for the
    use in deforming the magnetic field of the field-aligned currents and
    the partial derivatives with respect to the original coordinates.

    The class FDerivatives holds references to the value F and the partial
    derivates of F with respect to the original coordinates.

    Attributes
    ----------
    deltaPhi : float
        deltaPhi
    dipoleTilt : float
        Dipole tilt angle.
    """

    rho02 = 49.0
    beta = 0.9
    hingeDistance = 10.0
    epsilon = 3.0
    bConst = .5  # These parameters adjust the deformation.

    def __init__(self, deltaPhi, dipoleTilt):
        """Initialize a new Ffunction object.
        
        Initialize a new Ffunction object.

        Parameters
        ----------
        deltaPhi : float
            deltaPhi
        dipoleTilt : float
            Dipole tilt angle.
        """
        self.deltaPhi = deltaPhi
        self.dipoleTilt = dipoleTilt

    def evaluate(self, location):
        """Evaluate the function at the given location.

        Evaluate the function at the given location.

        Parameters
        ----------
        location : CylindricalVector or VectorIJK
            Location for evaluation.
        
        Returns
        -------
        result : FDerivatives
            Result of the evaluation at location.
        
        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if isinstance(location, CylindricalVector):
            # Evaluates the stretch transformation of the polar angle,
            # F(rho, phi, y) where (rho, phi, y) are the original undistorted
            # coordinates (in modified cylindrical coordinates) and the partial
            # derivatives of F with respect to these original coordinates.
            y = location.z

            # Convert to spherical and cylindrical.
            rho = location.rho
            rho2 = rho*rho
            r = math.sqrt(rho2 + y*y)
            phi = location.phi
            sinPhi = math.sin(phi)
            cosPhi = math.cos(phi)

            # Implementation of Tsy 2002-1 eq. (21) (with some extra
            # normalization term applied to b?!).
            # The constant has been scaled by the constant rho02 / (rho02 + 1).
            sinPhiCoef = (
                self.deltaPhi + Ffunction.bConst*Ffunction.rho02 /
                (Ffunction.rho02 + 1)*(rho2 - 1)/(Ffunction.rho02 + rho2)
            )
            # The quantity (r-1)/rH.
            rRh = (r - 1)/Ffunction.hingeDistance

            # The quantity ((r-1)/rH)^eps.
            rRhEps = math.pow(rRh, Ffunction.epsilon)
            fm1 = rRhEps/rRh

            f = 1 + rRhEps

            # Tsy 1998 eq. 10, dipole tilt deformation function Q(r).
            qr = math.pow(f, (1/Ffunction.epsilon))
            dQr = qr*f  # results from the derivative of Q(r)

            psiTerm = Ffunction.beta*self.dipoleTilt/qr

            # "F" in literature.
            phiStretched = phi - sinPhiCoef*sinPhi - psiTerm

            # Compute derivatives of F with respect to phi, rho, and y.
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
        elif isinstance(location, VectorIJK):
            x = location.i
            y = location.j
            z = location.k

            # Convert to spherical and cylindrical.
            rho2 = x*x + z*z
            rho = math.sqrt(rho2)
            phi = 0.0
            if x == 0 and z == 0:
                phi = 0
            else:
                phi = math.atan2(-z, x)

            return self.evaluate(CylindricalVector(rho, phi, y)).getF()
        else:
            raise TypeError
