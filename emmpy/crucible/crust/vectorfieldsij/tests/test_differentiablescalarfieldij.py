"""Tests for the differentiablescalarfieldij module."""


import unittest

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


class TestBuilder(unittest.TestCase):
    """Tests for the differentiablescalarfieldij module."""

    def test___init__(self):
        """Test the __init__ method."""
        dsfij = DifferentiableScalarFieldIJ()
        self.assertIsInstance(dsfij, DifferentiableScalarFieldIJ)


if __name__ == '__main__':
    unittest.main()
