"""Tests for the scalarfieldijspatialderivative module."""


import unittest

from emmpy.crucible.crust.vectorfieldsij.scalarfieldijspatialderivative import (
    ScalarFieldIJSpatialDerivative
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the scalarfieldijspatialderivative module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            ScalarFieldIJSpatialDerivative(None)

    def test_differentiateFDi(self):
        """Test the differentiateFDi method."""
        with self.assertRaises(AbstractMethodException):
            ScalarFieldIJSpatialDerivative.differentiateFDi(None, None)

    def test_differentiateFDj(self):
        """Test the differentiateFDj method."""
        with self.assertRaises(AbstractMethodException):
            ScalarFieldIJSpatialDerivative.differentiateFDj(None, None)


if __name__ == '__main__':
    unittest.main()
