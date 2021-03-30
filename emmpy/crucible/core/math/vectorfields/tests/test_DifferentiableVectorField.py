import unittest

from emmpy.crucible.core.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField()

    def test_differentiateFiDi(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFiDi(None, None)

    def test_differentiateFjDi(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFjDi(None, None)

    def test_differentiateFkDi(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFkDi(None, None)

    def test_differentiateFiDj(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFiDj(None, None)

    def test_differentiateFjDj(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFjDj(None, None)

    def test_differentiateFkDj(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFkDj(None, None)

    def test_differentiateFiDk(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFiDk(None, None)

    def test_differentiateFjDk(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFjDk(None, None)

    def test_differentiateFkDk(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiateFkDk(None, None)

    def test_differentiate(self):
        with self.assertRaises(Exception):
            DifferentiableVectorField.differentiate(None, None)


if __name__ == '__main__':
    unittest.main()
