"""Tests for the differentiablescalarfieldij module."""


import unittest

from emmpy.math.vectorfields.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)
from emmpy.math.vectors.vector2d import Vector2D


# Test data
(x, y) = (1.1, 2.2)

class TestBuilder(unittest.TestCase):
    """Tests for the differentiablescalarfieldij module."""

    def test___init__(self):
        """Test the __init__ method."""
        location = Vector2D(x, y)
        evaluateFunction = lambda location: location[0]**2 + location[1]**3
        iDerivativeFunction = lambda location: 2*location[0]
        jDerivativeFunction = lambda location: 3*location[1]**2
        dsfij = DifferentiableScalarFieldIJ(
            evaluateFunction, iDerivativeFunction, jDerivativeFunction
        )
        self.assertIsInstance(dsfij, DifferentiableScalarFieldIJ)
        self.assertAlmostEqual(
            dsfij.evaluate(location), evaluateFunction(location)
        )
        self.assertAlmostEqual(
            dsfij.differentiateFDi(location), iDerivativeFunction(location)
        )
        self.assertAlmostEqual(
            dsfij.differentiateFDj(location), jDerivativeFunction(location)
        )

    def test_createConstant(self):
        """Test the createConstant function."""
        a = 1.9
        location = Vector2D(x, y)
        dsfij = DifferentiableScalarFieldIJ.createConstant(a)
        self.assertIsInstance(dsfij, DifferentiableScalarFieldIJ)
        self.assertAlmostEqual(dsfij.evaluate(location), a)
        self.assertAlmostEqual(dsfij.differentiateFDi(location), 0)
        self.assertAlmostEqual(dsfij.differentiateFDj(location), 0)


if __name__ == "__main__":
    unittest.main()
