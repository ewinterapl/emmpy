from math import sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
    computeDeterminant,
    computeNorm,
    checkRotation,
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class TestBuilder(unittest.TestCase):

    def test_absMaxComponent(self):
        with self.assertRaises(Exception):
            absMaxComponent()
        with self.assertRaises(Exception):
            absMaxComponent(1)
        self.assertEqual(absMaxComponent(0, 0), 0)
        self.assertEqual(absMaxComponent(1, -2), 2)
        self.assertEqual(absMaxComponent(2, -2), 2)
        self.assertEqual(absMaxComponent(0, 0, 0), 0)
        self.assertEqual(absMaxComponent(1, 2, -3), 3)
        with self.assertRaises(Exception):
            absMaxComponent(1, -2, 3, -4), 5

    def test_computeNorm(self):
        with self.assertRaises(Exception):
            computeNorm(0)
        with self.assertRaises(Exception):
            computeNorm(1)
        self.assertAlmostEqual(computeNorm(1, 1), sqrt(2))
        self.assertAlmostEqual(computeNorm(0, 0), 0)
        self.assertAlmostEqual(computeNorm(1, 1, 1), sqrt(3))
        self.assertAlmostEqual(computeNorm(0, 0, 0), 0)
        with self.assertRaises(Exception):
            computeNorm(1, 2, 3, 4)

    def test_checkRotation(self):
        checkRotation(1, 0, 0, 0, 1, 0, 0, 0, 1, 1e-6, 1e-6)
        with self.assertRaises(MalformedRotationException):
            checkRotation(1, 1, 0, 0, 1, 0, 0, 0, 1, 1e-6, 1e-6)

    def test_computeDeterminant(self):
        with self.assertRaises(Exception):
            computeDeterminant()
        with self.assertRaises(Exception):
            computeDeterminant(0)
        self.assertAlmostEqual(computeDeterminant(1, 2, 3, 4), -2)
        with self.assertRaises(Exception):
            computeDeterminant([0]*5)
        self.assertAlmostEqual(
            computeDeterminant(0, 0, 0, 0, 0, 0, 0, 0, 0), 0)
        self.assertAlmostEqual(
            computeDeterminant(1.1, 2.2, 3.3, 4.4, 5, 6.6, 7.7, 8.8, 9.9),
            7.26
        )
        with self.assertRaises(Exception):
            computeDeterminant([0]*10)


if __name__ == '__main__':
    unittest.main()
