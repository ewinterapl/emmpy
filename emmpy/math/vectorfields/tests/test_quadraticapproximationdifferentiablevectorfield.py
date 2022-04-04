"""Tests for the quadraticapproximationdifferentiablevectorfield module."""


from re import X
import unittest

from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.quadraticapproximationdifferentiablevectorfield import (
    QuadraticApproximationDifferentiableVectorField
)
from emmpy.math.vectorfields.vectorfield import VectorField


# Test data

# Location for differentiation.
location = VectorIJK(1.0, 2.0, 3.0)

# Coordinate increments for finite difference differentiation.
deltaI = 0.1
deltaJ = 0.2
deltaK = 0.3

# Vector field to differentiate.
ax = 1.1
ay = 2.2
az = 3.3
def my_evaluate(location):
    vx = ax*location.i
    vy = ay*location.j**2
    vz = az*location.k**3
    v = VectorIJK(vx, vy, vz)
    return v
vf = VectorField()
vf.evaluate = my_evaluate

# Correct vector value
v_ref = VectorIJK(ax*location.i, ay*location.j**2, az*location.k**3)

# Correct finite-difference derivative values
dvx_dx_ref = ax
dvy_dx_ref = 0
dvz_dx_ref = 0
dvx_dy_ref = 0
dvy_dy_ref = 8.8
dvz_dy_ref = 0
dvx_dz_ref = 0
dvy_dz_ref = 0
dvz_dz_ref = 89.397


class TestBuilder(unittest.TestCase):
    """Tests for the quadraticapproximationdifferentiablevectorfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        self.assertIsInstance(qadvf, QuadraticApproximationDifferentiableVectorField)

    def test_differentiateFiDi(self):
        """Test the differentiateFiDi method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvx_dx = qadvf.differentiateFiDi(location)
        self.assertAlmostEqual(dvx_dx, dvx_dx_ref)

    def test_differentiateFjDi(self):
        """Test the differentiateFjDi method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvy_dx = qadvf.differentiateFjDi(location)
        self.assertAlmostEqual(dvy_dx, dvy_dx_ref)

    def test_differentiateFkDi(self):
        """Test the differentiateFkDi method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvz_dx = qadvf.differentiateFkDi(location)
        self.assertAlmostEqual(dvz_dx, dvz_dx_ref)

    def test_differentiateFiDj(self):
        """Test the differentiateFiDj method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvx_dy = qadvf.differentiateFiDj(location)
        self.assertAlmostEqual(dvx_dy, dvx_dy_ref)

    def test_differentiateFjDj(self):
        """Test the differentiateFjDj method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvy_dy = qadvf.differentiateFjDj(location)
        self.assertAlmostEqual(dvy_dy, dvy_dy_ref)

    def test_differentiateFkDj(self):
        """Test the differentiateFkDj method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvz_dy = qadvf.differentiateFkDj(location)
        self.assertAlmostEqual(dvz_dy, dvz_dy_ref)

    def test_differentiateFiDk(self):
        """Test the differentiateFiDk method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvx_dz = qadvf.differentiateFiDk(location)
        self.assertAlmostEqual(dvx_dz, dvx_dz_ref)

    def test_differentiateFjDk(self):
        """Test the differentiateFjDk method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvy_dz = qadvf.differentiateFjDk(location)
        self.assertAlmostEqual(dvy_dz, dvy_dz_ref)

    def test_differentiateFkDk(self):
        """Test the differentiateFkDk method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        dvz_dz = qadvf.differentiateFkDk(location)
        self.assertAlmostEqual(dvz_dz, dvz_dz_ref)

    def test_evaluate(self):
        """Test the evaluate method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        v = qadvf.evaluate(location)
        self.assertAlmostEqual(v.i, v_ref.i)
        self.assertAlmostEqual(v.j, v_ref.j)
        self.assertAlmostEqual(v.k, v_ref.k)

    def test_differentiate(self):
        """Test the differentiate method."""
        qadvf = QuadraticApproximationDifferentiableVectorField(
            vf, deltaI, deltaJ, deltaK
        )
        results = qadvf.differentiate(location)
        self.assertAlmostEqual(results.f.i, v_ref.i)
        self.assertAlmostEqual(results.f.j, v_ref.j)
        self.assertAlmostEqual(results.f.k, v_ref.k)
        self.assertAlmostEqual(results.dFxDx, dvx_dx_ref)
        self.assertAlmostEqual(results.dFyDx, dvy_dx_ref)
        self.assertAlmostEqual(results.dFzDx, dvz_dx_ref)
        self.assertAlmostEqual(results.dFxDy, dvx_dy_ref)
        self.assertAlmostEqual(results.dFyDy, dvy_dy_ref)
        self.assertAlmostEqual(results.dFzDy, dvz_dy_ref)
        self.assertAlmostEqual(results.dFxDz, dvx_dz_ref)
        self.assertAlmostEqual(results.dFyDz, dvy_dz_ref)
        self.assertAlmostEqual(results.dFzDz, dvz_dz_ref)


if __name__ == "__main__":
    unittest.main()
