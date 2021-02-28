import unittest

from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)


class TestCartesianVectorFieldValue(unittest.TestCase):

    def test___init__(self):
        CartesianVectorFieldValue()


if __name__ == '__main__':
    unittest.main()
