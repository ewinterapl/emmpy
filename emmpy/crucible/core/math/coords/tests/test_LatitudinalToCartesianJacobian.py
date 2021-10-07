"""Tests for the latitudinaltocartesianjacobian module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.latitudinaltocartesianjacobian import (
    LatitudinalToCartesianJacobian
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.latitudinalvector import LatitudinalVector


# Test grids.
n = 25
rs = np.linspace(0, 10, n)
lats = np.linspace(-pi/2, pi/2, n)
lons = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the latitudinaltocartesianjacobian module."""

    def test___init__(self):
        """Test the __init__ method."""
        l2cj = LatitudinalToCartesianJacobian()
        self.assertIsInstance(l2cj, LatitudinalToCartesianJacobian)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        l2cj = LatitudinalToCartesianJacobian()
        for r in rs:
            for lat in lats:
                for lon in lons:
                    latitudinal = LatitudinalVector(r, lat, lon)
                    buffer = MatrixIJK()
                    jac = l2cj.getTransformation(latitudinal, buffer)
                    self.assertIs(jac, buffer)
                    cos_lat = cos(lat)
                    sin_lat = sin(lat)
                    cos_lon = cos(lon)
                    sin_lon = sin(lon)
                    jac_ref = np.array(
                        [[cos_lat*cos_lon, -r*cos_lon*sin_lat,
                          -r*sin_lon*cos_lat],
                         [sin_lon*cos_lat, -r*sin_lon*sin_lat,
                          r*cos_lon*cos_lat],
                         [sin_lat, r*cos_lat, 0]])
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        l2cj = LatitudinalToCartesianJacobian()
        for r in rs:
            for lat in lats:
                for lon in lons:
                    latitudinal = LatitudinalVector(r, lat, lon)
                    buffer = MatrixIJK()
                    if r == 0:
                        # Raises uncatchable exception?
                        continue
                    jac = l2cj.getInverseTransformation(latitudinal, buffer)
                    self.assertIs(jac, buffer)
                    cos_lat = cos(lat)
                    sin_lat = sin(lat)
                    cos_lon = cos(lon)
                    sin_lon = sin(lon)
                    jac_ref = np.array(
                        [[cos_lat*cos_lon, -r*cos_lon*sin_lat,
                          -r*sin_lon*cos_lat],
                         [sin_lon*cos_lat, -r*sin_lon*sin_lat,
                          r*cos_lon*cos_lat],
                         [sin_lat, r*cos_lat, 0]])
                    jac_ref = np.linalg.inv(jac_ref)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        l2cj = LatitudinalToCartesianJacobian()
        v1_lat = LatitudinalVector(1, 1, 1)
        v2_cart = VectorIJK(1, 1, 1)
        for r in rs:
            if r == 0:
                continue
            for lat in lats:
                for lon in lons:
                    # Assemble the location for the transformation.
                    latitudinal = LatitudinalVector(r, lat, lon)
                    jac = MatrixIJK()
                    # Multiply a latitudinal velocity vector by the
                    # Jacobian to get a Cartesian velocity vector.
                    l2cj.getTransformation(latitudinal, jac)
                    v1_cart = l2cj.mxv(jac, v1_lat)
                    v1_cart_ref = jac.dot(v1_lat)
                    for i in range(3):
                        self.assertAlmostEqual(v1_cart[i], v1_cart_ref[i])
                    # Multiply a Cartesian velocity vector by the inverse
                    # Jacobian to get a latitudinal velocity vector.
                    l2cj.getInverseTransformation(latitudinal, jac)
                    v2_lat = l2cj.mxv(jac, v2_cart)
                    v2_lat_ref = jac.dot(v2_cart)
                    for i in range(3):
                        self.assertAlmostEqual(v2_lat[i], v2_lat_ref[i])


if __name__ == '__main__':
    unittest.main()
