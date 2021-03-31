import unittest

from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        cvfv = CartesianVectorFieldValue([0, 0, 0], [0, 0, 0])
        self.assertIsNotNone(cvfv)

if __name__ == '__main__':
    unittest.main()
