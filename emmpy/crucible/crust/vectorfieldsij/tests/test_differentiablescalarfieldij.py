"""Tests for the differentiablescalarfieldij module."""


import unittest

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ, createConstant
)


class TestBuilder(unittest.TestCase):
    """Tests for the differentiablescalarfieldij module."""

    def test___init__(self):
        """Test the __init__ method."""
        dsfij = DifferentiableScalarFieldIJ()
        self.assertIsInstance(dsfij, DifferentiableScalarFieldIJ)

    def test_createConstant(self):
        a = 1.9
        dsfij = createConstant(a)
        self.assertAlmostEqual(dsfij.evaluate(None), a)
        self.assertEqual(dsfij.differentiateFDi(None), 0)
        self.assertEqual(dsfij.differentiateFDj(None), 0)


if __name__ == '__main__':
    unittest.main()
