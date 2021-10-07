"""Tests for the coordconverters module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.coordinates.latitudinalvector import LatitudinalVector
from emmpy.math.coordinates.radecvector import RaDecVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)
radiuss = np.linspace(0, 10, n)
lats = np.linspace(-pi/2, pi/2, n)
lons = np.linspace(-pi, pi, n)
angles = np.linspace(0, 2*pi, n)
ras = np.linspace(0, 2*pi, n)
decs = np.linspace(-pi/2, pi/2, n)
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the coordconverters module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverters()

    def test_convertToCylindrical(self):
        """Test the convertToCylindrical method."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    rho = sqrt(x**2 + y**2)
                    phi = atan2(y, x)
                    if phi < 0:
                        phi += 2*pi
                    cyl = CoordConverters.convertToCylindrical(cartesian)
                    self.assertAlmostEqual(cyl.rho, rho)
                    self.assertAlmostEqual(cyl.phi, phi)
                    self.assertAlmostEqual(cyl.z, z)

    def test_convertToLatitudinal(self):
        """Test the convertToLatitudinal method."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    radius = sqrt(x**2 + y**2 + z**2)
                    lat = atan2(z, sqrt(x**2 + y**2))
                    lon = atan2(y, x)
                    latitudinal = CoordConverters.convertToLatitudinal(
                        cartesian)
                    self.assertAlmostEqual(latitudinal.r, radius)
                    self.assertAlmostEqual(latitudinal.lat, lat)
                    self.assertAlmostEqual(latitudinal.lon, lon)

    def test_convertToPolar(self):
        """Test the convertToPolar method."""
        for x in xs:
            for y in ys:
                cartesian = VectorIJ(x, y)
                radius = sqrt(x**2 + y**2)
                angle = atan2(y, x)
                cyl = CoordConverters.convertToPolar(cartesian)
                self.assertAlmostEqual(cyl.getRadius(), radius)
                self.assertAlmostEqual(cyl.getAngle(), angle)

    def test_convertToRaDec(self):
        """Test the convertToRaDec method."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    radius = sqrt(x**2 + y**2 + z**2)
                    rightAscension = atan2(y, x)
                    if rightAscension < 0:
                        rightAscension += 2*pi
                    declination = atan2(z, sqrt(x**2 + y**2))
                    radec = CoordConverters.convertToRaDec(cartesian)
                    self.assertAlmostEqual(radec.r, radius)
                    self.assertAlmostEqual(radec.ra, rightAscension)
                    self.assertAlmostEqual(radec.dec, declination)

    def test_convertToSpherical(self):
        """Test the convertToSpherical method."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    if x == y == z == 0:
                        theta = 0
                    else:
                        theta = pi/2 - atan2(z, sqrt(x**2 + y**2))
                    phi = atan2(y, x)
                    spherical = CoordConverters.convertToSpherical(cartesian)
                    self.assertAlmostEqual(spherical.r, r)
                    self.assertAlmostEqual(spherical.theta, theta)
                    self.assertAlmostEqual(spherical.phi, phi)

    def test_convert(self):
        """Test the convert method."""
        # Cylindrical to Cartesian
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    x = rho*cos(phi)
                    y = rho*sin(phi)
                    cylindrical = CylindricalVector(rho, phi, z)
                    cartesian = CoordConverters.convert(cylindrical)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)
        # Latitudinal to Cartesian
        for radius in radiuss:
            for lat in lats:
                for lon in lons:
                    x = radius*cos(lat)*cos(lon)
                    y = radius*cos(lat)*sin(lon)
                    z = radius*sin(lat)
                    latitudinal = LatitudinalVector(radius, lat, lon)
                    cartesian = CoordConverters.convert(latitudinal)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)
        # Polar to Cartesian
        for radius in radiuss:
            for angle in angles:
                x = radius*cos(angle)
                y = radius*sin(angle)
                polar = PolarVector(radius, angle)
                cartesian = CoordConverters.convert(polar)
                self.assertAlmostEqual(cartesian.i, x)
                self.assertAlmostEqual(cartesian.j, y)
        # RA/DEC to Cartesian
        # for radius in radiuss:
        #     for ra in ras:
        #         for dec in decs:
        #             x = radius*cos(dec)*cos(ra)
        #             y = radius*cos(dec)*sin(ra)
        #             z = radius*sin(dec)
        #             radec = RaDecVector(radius, ra, dec)
        #             cartesian = CoordConverters.convert(radec)
        #             self.assertAlmostEqual(cartesian.i, x)
        #             self.assertAlmostEqual(cartesian.j, y)
        #             self.assertAlmostEqual(cartesian.k, z)
        # Spherical to Cartesian
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    x = r*sin(theta)*cos(phi)
                    y = r*sin(theta)*sin(phi)
                    z = r*cos(theta)
                    radec = SphericalVector(r, theta, phi)
                    cartesian = CoordConverters.convert(radec)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)
        # Invalid args.
        with self.assertRaises(ValueError):
            CoordConverters.convert(None)


if __name__ == '__main__':
    unittest.main()
