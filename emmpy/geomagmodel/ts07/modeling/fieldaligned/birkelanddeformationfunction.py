"""Deformation to model a Birkeland current sheet.

Deformation to model a Birkeland current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin, sqrt

from emmpy.magmodel.math.vectorfields.differentiablesphericalvectorfield import (
    Results
)
from emmpy.math.coordinates.sphericalvector import SphericalVector


class BirkelandDeformationFunction:
    """Deformation to model a Birkeland current sheet.

    Represents the analytical deformation of spherical coordinates to
    model the shape of Birkeland current sheets as described in
    Tsyganenko 2002 "A model of the near magnetosphere with a dawn-dusk
    asymmetry 1. Mathematical structure" by N. A. Tsyganenko.
    See eq. (18 and 19).

    Attributes
    ----------
    a : array-like of float
        Radial deformation constants.
    b : array-like of float
        Radial deformation constants.
    c : array-like of float
        Co-latitudinal deformation constants.
    d : array-like of float
        Co-latitudinal deformation constants.
    """

    # Used for numerical differentiation.
    delta = 1E-6

    def __init__(self, a, b, c, d):
        """Initialize a new BirkelandDeformationFunction object.

        Initialize a new BirkelandDeformationFunction object.

        Parameters
        ----------
        a : array-like of float
            Radial deformation constants.
        b : array-like of float
            Radial deformation constants.
        c : array-like of float
            Co-latitudinal deformation constants.
        d : array-like of float
            Co-latitudinal deformation constants.
        """
        # Make A defensive copy.
        self.a = a[:]
        self.b = b[:]
        self.c = c[:]
        self.d = d[:]

    def evaluate(self, location):
        """Evaluate the deformation.

        Evaluate the deformation.

        Parameters
        ----------
        location : SphericalVector
            Location for evaluation.
        
        Returns
        -------
        result : SphericalVector
            Value of deformation function at location.
        """
        r = location.r
        theta = location.theta
        phi = location.phi

        # Deform the coordinate system.
        rDef = self.rDeform(r, theta)
        thetaDef = self.thetaDeform(r, theta)

        return SphericalVector(rDef, thetaDef, phi)

    def differentiate(self, location):
        """Differentiate the deformation function.

        Differentiate the deformation function.

        Parameters
        ----------
        location : SphericalVector
            Location for differentiation.

        Returns
        -------
        result : differentiablesphericalvectorfield.Results
            Result of differentiation at location.
        """
        r = location.r
        theta = location.theta
        phi = location.phi

        # Deform the coordinate system.
        rDef = self.rDeform(r, theta)
        thetaDef = self.thetaDeform(r, theta)
        locDef = SphericalVector(rDef, thetaDef, phi)

        # Numerically approximate derivatives for deformation.
        locPr = self.evaluate(
            SphericalVector(r + BirkelandDeformationFunction.delta, theta,
                            phi)
        )
        locMr = self.evaluate(
            SphericalVector(r - BirkelandDeformationFunction.delta, theta,
                            phi)
        )

        locPt = self.evaluate(
            SphericalVector(r, theta + BirkelandDeformationFunction.delta,
            phi)
        )
        locMt = self.evaluate(
            SphericalVector(r, theta - BirkelandDeformationFunction.delta,
            phi)
        )

        drDef_dr = (
            (locPr.r - locMr.r) /
            (2*BirkelandDeformationFunction.delta)
        )
        drDef_dtheta = (
            (locPt.r - locMt.r) /
            (2*BirkelandDeformationFunction.delta)
        )
        dthetaDef_dr = (
            (locPr.theta - locMr.theta) /
            (2*BirkelandDeformationFunction.delta)
        )
        dthetaDef_dTheta = (
            (locPt.theta - locMt.theta) /
            (2*BirkelandDeformationFunction.delta)
        )
        dphiDef_dPhi = 1.0

        return Results(locDef, drDef_dr, drDef_dtheta, 0, dthetaDef_dr,
                       dthetaDef_dTheta, 0, 0, 0, dphiDef_dPhi)

    def rDeform(self, r, theta):
        """Deform the radius to describe the field aligned current.

        Deform the radius to describe the field aligned current.

        See Tsy 2002-1 Eqn 18. The b coefficients as given in table 2
        were always squared, so they are squared here to save math. Note
        the difference.

        There are two differences between this calculation and the
        published equation. An email to Nikolai Tsyganenko confirmed that
        these are the proper versions (6/25/2011).

        Parameters
        ----------
        r : float
            The undeformed radius.
        theta : float
            The undeformed polar angle (measured from the GSM Z axis).
        
        Returns
        -------
        result: float
            The deformed radius.
        """
        r2 = r*r
        return (
            r + self.a[0]/r + (self.a[1]*r /(sqrt(r2 + self.b[0]*self.b[0]))) +
            (self.a[2]*r/(r2 + self.b[1]*self.b[1])) +
            cos(theta)*(self.a[3] + self.a[4]/r + self.a[5]*r /
                        sqrt(r2 + self.b[2]*self.b[2]) +
                        self.a[6]*r/(r2 + self.b[3]*self.b[3])) +
            cos(2*theta)*(self.a[7]*r/sqrt(r2 + self.b[4]*self.b[4]) +
                          self.a[8]*r/((r2 + self.b[5]*self.b[5]) *
                                       (r2 + self.b[5]*self.b[5])))
        )

    def thetaDeform(self, r, theta):
        """Deforms theta to describe the field aligned current.

        See Tsy 2002-1 Eqn 19. The d coefficients as given in table 2 were
        always squared, so they are squared here to save math. Note the
        difference.

        Parameters
        ----------
        r : float
            The initial radius.
        theta : float
            The initial polar angle (measured from the GSM Z axis).
        
        Returns
        -------
        result : float
            The deformed polar angle (theta).
        """
        r2 = r*r
        return (
            theta + (self.c[0] + self.c[1]/r + self.c[2]/r2 +
                     self.c[3]*r/sqrt(r2 + self.d[0]*self.d[0]))*sin(theta) +
            (self.c[4] + self.c[5]*r/sqrt(r2 + self.d[1]*self.d[1]) +
             self.c[6]*r/(r2 + self.d[2]*self.d[2])) * sin(2 * theta) +
            (self.c[7] + self.c[8]/r + self.c[9]*r /
             (r2 + self.d[3]*self.d[3]))*sin(3*theta)
        )
