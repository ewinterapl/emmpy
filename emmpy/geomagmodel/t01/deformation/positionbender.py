"""Compute deformation in the X-Z plane related to the dipole tilt.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import sin, sqrt

import numpy as np

from emmpy.magmodel.math.deformation.basisvectorfielddeformation import (
    BasisVectorFieldDeformation
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField, Results
)


# WHAT ARE THESE CONSTANTS?
# Can be changed to "0" to avoid problems with simplex iterating to
# non-real values.
RH2 = -5.2
EPSILON = 3


class PositionBender(DifferentiableVectorField):
    """Compute deformation in the X-Z plane related to the dipole tilt.

    From Tsyganeneko's code, an implementation of Tsyganenko [1998]
    section 3, "deformation in the X-Z plane related to the dipole tilt"

    Computes:
    X* = X*cos(psi)*(r) - Z*sin(psi)*(r)
    Y* = Y
    Z* = Xsin(psi)*(r) + Zcos(psi)*(r)
    where
    sin(psi)* = R_H*sin(psi)/(R_H**3 + r**3)**(1/3)
    R_H =  R_H0 +  R_H2 Z**2/r**2
    This is similar to the FORTRAN subroutine:
         SUBROUTINE DEFORMED (PS,X,Y,Z,BX,BY,BZ)
    see ./doc-files/tsy1998Math.docx

    Attributes
    ----------
    sinTilt : float
        Sine of tilt angle.
    rh0 : float
        Hinge distance (units?)
    """

    def __init__(self, dipoleTilt, hingeDistance):
        """Initialize a new PositionBender object.

        Initialize a new PositionBender object.

        Parameters
        ----------
        dipoleTilt : float
            Dipole tilt angle (radians)
        hingeDistance : float
            Hinge distance; must be greater than or equal to R_H2.
        
        Returns
        -------
        None
        """
        self.sinTilt = sin(dipoleTilt)
        self.rh0 = hingeDistance

    def evaluate(self, location, buffer):
        """Bend the position vector.

        Bend the position vector to account for the bending of the tail field
        in the X-Z GSM plane.

        Derivation: Tsyganenko 2002-1 Eqn 13

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the field.
        buffer : VectorIJK
            Buffer to hold the evaluation result.

        Returns
        -------
        buffer : VectorIJK
            Bent evaluation at location.
        """
        (x, y, z) = location[...]
        r2 = x**2 + y**2 + z**2
        r = sqrt(r2)
        z_r = z/r

        # Allow the hinging distance to be a function of position
        # See Tsy. 1998 eq. 12.
        rh = self.rh0 + RH2*z_r**2
        r_rh = r/rh

        # Eq. 10 Tsy. 1998, Q(r) = [1+ (r/RH)^ep ]^(-1/ep)
        Q = 1/ pow(1 + pow(r_rh, EPSILON), 1/EPSILON)

        # Now compute the cosine and sine of the radial dependent tilt angle,
        # this is Tsy. 1998 eq. 7.
        sinTiltS = self.sinTilt*Q
        cosTiltS = sqrt(1 - sinTiltS**2)

        # The point deformation from eq. 7 in Tsy. 1998.
        xS = x*cosTiltS - z*sinTiltS
        yS = y
        zS = x*sinTiltS + z*cosTiltS

        buffer[...] = (xS, yS, zS)
        return buffer

    def differentiate(self, location):
        """Differentiate the field at the specified Cartesian location.

        Compute the gradient of the field at the specified Cartesian
        location.

        Parameters
        ----------
        location : Vector3D
            Cartesian location to compute differentiation.
        
        Returns
        -------
        results : Results
            Object containing gradient components.
        
        Notes
        -----
        A "S" suffix indicates starred quantities from the original paper.
        """
        # Fetch the Cartesian location components.
        x = location.i
        y = location.j
        z = location.k

        # Compute the radial distance, and normalize z to it.
        r = np.linalg.norm(location)
        z_r = z/r

        # Allow the hinging distance to be a function of position.
        # Tsy. 1998 eq. 12
        rh = self.rh0 + RH2*z_r**2
        r_rh = r/rh

        # eq. 10 Tsy. 1998, Q(r) = [1+ (r/rh)^ep]^(-1/ep)
        Q = 1/pow(1 + pow(r_rh, EPSILON), 1/EPSILON)

        # Now compute the cos and sin of the radially dependent tilt
        # angle. This is Tsy. 1998 eq. 7.
        sinTiltS = self.sinTilt*Q
        cosTiltS = sqrt(1 - sinTiltS**2)

        # The point deformation from eq. 7 in Tsy. 1998.
        xS = x*cosTiltS - z*sinTiltS
        yS = y
        zS = x*sinTiltS + z*cosTiltS

        # The radial and height derivative of rh.
        dRhDr = -2*RH2*z_r**2/r
        dRhDz = 2*RH2*z_r/r

        # Now compute the x,y,z derivatives of Q using the chain rule.
        # fr is the first term dQ/dr.
        fr = -pow(r_rh, EPSILON - 1)*pow(Q, EPSILON + 1)/rh
        dQdRh = -r_rh*fr
        dQdr = fr - fr*r_rh*dRhDr
        dQdx = dQdr*x/r
        dQdy = dQdr*y/r
        dQdz = dQdr*z/r + dQdRh*dRhDz

        # Store this ratio sinT/cosT*.
        sin_cos = self.sinTilt/cosTiltS

        # Compute the derivative components.
        dXsDx = cosTiltS - zS * dQdx*sin_cos
        dXsDy = -zS*dQdy*sin_cos
        dXsDz = -sinTiltS - zS*dQdz*sin_cos
        dYsDx = 0.0
        dYsDy = 1.0
        dYsDz = 0.0
        dZsDx = sinTiltS + xS*dQdx*sin_cos
        dZsDy = xS*dQdy*sin_cos
        dZsDz = cosTiltS + xS*dQdz*sin_cos

        # Make a Cartesian vector for the starred location.
        f = VectorIJK(xS, yS, zS)

        # Create and return the Results object.
        results = Results(f,
                          dXsDx, dXsDy, dXsDz,
                          dYsDx, dYsDy, dYsDz,
                          dZsDx, dZsDy, dZsDz)
        return results

    @staticmethod
    def deformBasisField(dipoleTilt, hingeDistance, undeformedField):
        """Deform a basis vector field.

        Deform a basis vector field.

        Parameters
        ----------
        dipoleTilt : float
            Dipole tilt angle (radians).
        hingeDistance : float
            ???
        undeformedField : BasisVectorField
            The basis vector field to deform.

        Returns
        -------
        deformedField : BasisVectorField
            The deformed basis vector field.
        """
        # Create a PositionBender to compute the deformation.
        deformation = PositionBender(dipoleTilt, hingeDistance)

        # Deform the field.
        deformedField = BasisVectorFieldDeformation(undeformedField,
                                                    deformation)

        # Return the deformed field.
        return deformedField
