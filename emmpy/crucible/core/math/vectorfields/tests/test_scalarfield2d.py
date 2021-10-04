"""Tests for the scalarfield2d module."""


import unittest

from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the scalarfield2d module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            ScalarField2D()

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            ScalarField2D.evaluate(None, None)


if __name__ == '__main__':
    unittest.main()
