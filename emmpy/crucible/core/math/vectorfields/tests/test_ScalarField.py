"""Tests for the scalarfield module."""


import unittest

from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the scalarfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            ScalarField()

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            ScalarField.evaluate(None, None)


if __name__ == '__main__':
    unittest.main()
