from math import sqrt
import unittest

# import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    InternalOperations
)


class TestInternalOperations(unittest.TestCase):

    def test_absMaxComponent(self):
        self.assertEqual(InternalOperations.absMaxComponent(1, 2, -3), 3)

    def test_computeNorm(self):
        self.assertAlmostEqual(InternalOperations.computeNorm(1, 1, 1),
                               sqrt(3))

    def test_checkRotation(self):
        InternalOperations.checkRotation(1, 0, 0, 0, 1, 0, 0, 0, 1, 1e-6, 1e-6)

    def test_computeDeterminant(self):
        self.assertAlmostEqual(
            InternalOperations.computeDeterminant(0, 0, 0, 0, 0, 0, 0, 0, 0),
            0
        )


if __name__ == '__main__':
    unittest.main()
