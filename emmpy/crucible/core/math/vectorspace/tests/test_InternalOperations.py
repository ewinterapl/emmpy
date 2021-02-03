from math import sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.internaloperations import InternalOperations

class TestInternalOperations(unittest.TestCase):

    def test_absMaxComponent(self):
        self.assertEqual(InternalOperations.absMaxComponent(1, 2, 3), 3)

    def test_computeNorm(self):
        self.assertTrue(np.isclose(InternalOperations.computeNorm(1, 1, 1), sqrt(3)))

if __name__ == '__main__':
    unittest.main()
