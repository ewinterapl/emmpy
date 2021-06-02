"""emmpy.geomagmodel.ts07.modeling.fieldaligned.birkelanddeformation"""


from math import cos, sin, sqrt

from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.magmodel.core.math.vectorfields.differentiablesphericalvectorfield import (
    Results, DifferentiableSphericalVectorField
)


class BirkelandDeformationFunction(DifferentiableSphericalVectorField):
    """Represents the analytical deformation of spherical coordinates to model
    the shape of Birkeland current sheets as described in Tsyganenko 2002
    "A model of the near magnetosphere with a dawn-dusk asymmetry
    1. Mathematical structure" by N. A. Tsyganenko. See eq. (18 and 19).

    author G.K.Stephens
    """

    # Used for numerical differentiation
    delta = 1E-6

    def __init__(self, a, b, c, d):
        """Construct deformed field by providing the coefficients a, b, c,
        and d.

        param a an array of doubles containing the radial deformation constants
        param b an array of doubles containing the radial deformation constants
        param c an array of doubles containing the co-latitudinal deformation constants
        param d an array of doubles containing the co-latitudinal deformation constants
        """
        # make defensive copy
        self.a = a[:]
        self.b = b[:]
        self.c = c[:]
        self.d = d[:]

    def evaluate(self, location):
        """evaluate

        param SphericalVector location
        return SphericalVector
        """
        # float r, theta, phi
        r = location.getRadius()
        theta = location.getColatitude()
        phi = location.getLongitude()

        # Deform the coordinate system
        # float rDef, thetaDef
        rDef = self.rDeform(r, theta)
        thetaDef = self.thetaDeform(r, theta)

        return SphericalVector(rDef, thetaDef, phi)

    def differentiate(self, location):
        """differentiate

        param SphericalVector location
        return Results
        """

        # float r, theta, phi
        r = location.getRadius()
        theta = location.getColatitude()
        phi = location.getLongitude()

        # Deform the coordinate system
        # float rDef, thetaDef
        rDef = self.rDeform(r, theta)
        thetaDef = self.thetaDeform(r, theta)
        # SphericalVector locDef
        locDef = SphericalVector(rDef, thetaDef, phi)

        # Numerically approximate derivatives for deformation
        # SphericalVector locPr, locMr
        locPr = self.evaluate(
            SphericalVector(r + BirkelandDeformationFunction.delta, theta,
                            phi)
        )
        locMr = self.evaluate(
            SphericalVector(r - BirkelandDeformationFunction.delta, theta,
                            phi)
        )

        # SphericalVector locPt, locMt
        locPt = self.evaluate(
            SphericalVector(r, theta + BirkelandDeformationFunction.delta,
            phi)
        )
        locMt = self.evaluate(
            SphericalVector(r, theta - BirkelandDeformationFunction.delta,
            phi)
        )

        # double drDef_dr, drDef_dtheta, dthetaDef_dr, dthetaDef_dTheta,
        # dphiDef_dPhi
        drDef_dr = (
            (locPr.getRadius() - locMr.getRadius()) /
            (2*BirkelandDeformationFunction.delta)
        )
        drDef_dtheta = (
            (locPt.getRadius() - locMt.getRadius()) /
            (2*BirkelandDeformationFunction.delta)
        )
        dthetaDef_dr = (
            (locPr.getColatitude() - locMr.getColatitude()) /
            (2*BirkelandDeformationFunction.delta)
        )
        dthetaDef_dTheta = (
            (locPt.getColatitude() - locMt.getColatitude()) /
            (2*BirkelandDeformationFunction.delta)
        )
        dphiDef_dPhi = 1.0

        return Results(locDef, drDef_dr, drDef_dtheta, 0, dthetaDef_dr,
                       dthetaDef_dTheta, 0, 0, 0, dphiDef_dPhi)

    def rDeform(self, r, theta):
        """Deforms the radius to describe the field aligned current.

        See Tsy 2002-1 Eqn 18
        The b coefficients as given in table 2 were always squared, so they are
        squared here to save math. Note the difference.

        There are two differences between this calculation and the published
        equation. An email to Nikolai Tsyganenko confirmed that these are the
        proper versions (6/25/2011).

        param double r the undeformed radius
        param double theta the underformed polar angle (measured from the GSM Z axis)
        return (double) the deformed radius
        """
        # double r2
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

        See Tsy 2002-1 Eqn 19.
        The d coefficients as given in table 2 were always squared, so they
        are squared here to save math. Note the difference.

        param r the initial radius
        param theta the initial polar angle (measured from the GSM Z axis)
        return the deformed polar angle (theta)
        """
        # double r2
        r2 = r*r
        return (
            theta + (self.c[0] + self.c[1]/r + self.c[2]/r2 +
                     self.c[3]*r/sqrt(r2 + self.d[0]*self.d[0]))*sin(theta) +
            (self.c[4] + self.c[5]*r/sqrt(r2 + self.d[1]*self.d[1]) +
             self.c[6]*r/(r2 + self.d[2]*self.d[2])) * sin(2 * theta) +
            (self.c[7] + self.c[8]/r + self.c[9]*r /
             (r2 + self.d[3]*self.d[3]))*sin(3*theta)
        )
