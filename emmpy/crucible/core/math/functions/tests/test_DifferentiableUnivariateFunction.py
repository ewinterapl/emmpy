import unittest

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(DifferentiableUnivariateFunction)

    def test_differentiate(self):
        with self.assertRaises(Exception):
            DifferentiableUnivariateFunction.differentiate(None, 0)


if __name__ == '__main__':
    unittest.main()
