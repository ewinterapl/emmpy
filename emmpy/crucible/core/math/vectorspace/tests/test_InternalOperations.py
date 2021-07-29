from math import sqrt
import unittest

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    absMaxComponent,
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

    def test_checkRotation(self):
        checkRotation(1, 0, 0, 0, 1, 0, 0, 0, 1, 1e-6, 1e-6)
        with self.assertRaises(MalformedRotationException):
            checkRotation(1, 1, 0, 0, 1, 0, 0, 0, 1, 1e-6, 1e-6)


if __name__ == '__main__':
    unittest.main()
