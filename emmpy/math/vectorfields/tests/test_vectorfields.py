"""Tests for the vectorfields module."""


import unittest

from emmpy.math.vectorfields.vectorfields import (
    curl, scale
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField, Results
)
from emmpy.math.vectorfields.vectorfield import VectorField


# Create vector fields for testing.

# An identity mapping field.
vf1 = VectorField()
def my_eval1(location, buffer):
    buffer[:] = location
    return buffer
vf1.evaluate = my_eval1

# A unit field.
vf2 = VectorField()
def my_eval2(location, buffer):
    buffer[:] = 1
    return buffer
vf2.evaluate = my_eval2

# A shifted-by-2 location field.
vf3 = VectorField()
def my_eval3(location, buffer):
    buffer[:] = location + 2
    return buffer
vf3.evaluate = my_eval3


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfields module."""

    def test_scale(self):
        """Test the scale function."""
        scaleFactor = -1.1
        vf = scale(vf1, scaleFactor)
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        vs = location*scaleFactor
        buffer = VectorIJK()
        v = vf.evaluate(location, buffer)
        self.assertIs(v, buffer)
        for i in range(3):
            self.assertAlmostEqual(v[i], vs[i])

    def test_curl(self):
        """Test the curl function."""
        # Create a simple differentiable vector field:
        # (vx, vy, vz) = (x*y*z, x*y**2*z, x*y**2*z**3)
        dvf = DifferentiableVectorField()
        # loc = location VectorIJK

        def my_evaluate(loc):
            vx = loc.i*loc.j*loc.k
            vy = loc.i*loc.j**2*loc.k
            vz = loc.i*loc.j**2*loc.k**3
            v = VectorIJK(vx, vy, vz)
            return v
        dvf.evaluate = my_evaluate

        dvf.differentiateFiDi = lambda loc: loc.j*loc.k
        dvf.differentiateFiDj = lambda loc: loc.i*loc.k
        dvf.differentiateFiDk = lambda loc: loc.i*loc.j
        dvf.differentiateFjDi = lambda loc: loc.j**2*loc.k
        dvf.differentiateFjDj = lambda loc: 2*loc.i*loc.j*loc.k
        dvf.differentiateFjDk = lambda loc: loc.i*loc.j**2
        dvf.differentiateFkDi = lambda loc: loc.j**2*loc.k**3
        dvf.differentiateFkDj = lambda loc: 2*loc.i*loc.j*loc.k**3
        dvf.differentiateFkDk = lambda loc: 3*loc.i*loc.j**2*loc.k**2

        def my_differentiate(loc):
            v = dvf.evaluate(loc)
            dvx_dx = dvf.differentiateFiDi(loc)
            dvx_dy = dvf.differentiateFiDj(loc)
            dvx_dz = dvf.differentiateFiDk(loc)
            dvy_dx = dvf.differentiateFjDi(loc)
            dvy_dy = dvf.differentiateFjDj(loc)
            dvy_dz = dvf.differentiateFjDk(loc)
            dvz_dx = dvf.differentiateFkDi(loc)
            dvz_dy = dvf.differentiateFkDj(loc)
            dvz_dz = dvf.differentiateFkDk(loc)
            r = Results(
                v,
                dvx_dx, dvx_dy, dvx_dz,
                dvy_dx, dvy_dy, dvy_dz,
                dvz_dx, dvz_dy, dvz_dz
            )
            return r
        dvf.differentiate = my_differentiate
        dvf_curl = curl(dvf)
        loc = VectorIJK(1, 2, 3)
        loc_curl = dvf_curl.evaluate(loc)
        self.assertAlmostEqual(loc_curl[0], 104)
        self.assertAlmostEqual(loc_curl[1], -106)
        self.assertAlmostEqual(loc_curl[2], 9)
        loc = VectorIJK(1.1, 2.2, 3.3)
        loc_curl = dvf_curl.evaluate(loc)
        self.assertAlmostEqual(loc_curl[0], 168.611, delta=1e-4)
        self.assertAlmostEqual(loc_curl[1], -171.515, delta=1e-4)
        self.assertAlmostEqual(loc_curl[2], 12.342, delta=1e-4)


if __name__ == "__main__":
    unittest.main()
