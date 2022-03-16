"""Tests for the t96magnetopause module."""


import unittest

from emmpy.geomagmodel.magnetopause.t96magnetopause import (
    T96Magnetopause
)


class TestBuilder(unittest.TestCase):
    """Tests for the t96magnetopause module."""

    def test___init__(self):
        """Test the __init__ method."""
        t96mp = T96Magnetopause(1, 1, 1, 1, 1)
        self.assertIsInstance(t96mp, T96Magnetopause)
        self.assertAlmostEqual(t96mp.scaledA0, 2.0)
        self.assertAlmostEqual(t96mp.sigma0, 1.0)
        self.assertAlmostEqual(t96mp.scaledX0, 2.0)
        self.assertAlmostEqual(t96mp.XM, 0.0)
        self.assertAlmostEqual(t96mp.semiMinorAxis, 0.0)


if __name__ == "__main__":
    unittest.main()
