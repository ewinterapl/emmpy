"""Tests for the vectorfield module."""


import unittest

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            vf = VectorField()

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            VectorField.evaluate(None, None)


if __name__ == '__main__':
    unittest.main()
