import unittest

from emmpy.crucible.core.math.functions.univariatefunction import (
    UnivariateFunction
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            UnivariateFunction()

    def test_evaluate(self):
        with self.assertRaises(Exception):
            UnivariateFunction.evaluate(None, 0)


if __name__ == '__main__':
    unittest.main()
