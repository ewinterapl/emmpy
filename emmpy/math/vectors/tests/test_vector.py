"""Tests for the vector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""

import unittest

import numpy as np

from emmpy.math.vectors.vector import Vector


class TestBuilder(unittest.TestCase):
    """Tests for the vector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # Constructor should not be invoked directly.
        # 1-arg form - number of elements
        # Use different sizes.
        for n in range(1, 11):
            # Positional form
            v = Vector.__new__(Vector, n)
            self.assertIsInstance(v, Vector)
            self.assertEqual(len(v), n)
            # Keyword form
            v = Vector(length=n)
            self.assertIsInstance(v, Vector)
            self.assertTrue(len(v), n)
        # Invalid forms.
        for n in (0, 2):
            with self.assertRaises(TypeError):
                args = (None,)*n
                v = Vector(*args)

    def test_unitize(self):
        """Test the unitize method."""
        datas = [[1.1], [1.1, 2.2], [1.1, 2.2, 3.3], [1.1, 2.2, 3.3, 4.4]]
        for data in datas:
            length = np.linalg.norm(data)
            v1 = Vector(length=len(data))
            v1[:] = data
            v2 = v1.unitize()
            self.assertIs(v2, v1)
            for col in range(len(data)):
                self.assertAlmostEqual(v2[col], data[col]/length)


if __name__ == '__main__':
    unittest.main()
