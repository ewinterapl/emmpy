"""Tests for the transformation module."""


import unittest

from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the transformation module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            Transformation()

    def test_getTransformation(self):
        """Test the getTransformation method."""
        with self.assertRaises(AbstractMethodException):
            Transformation.getTransformation(None, None, None)

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        with self.assertRaises(AbstractMethodException):
            Transformation.getInverseTransformation(None, None, None)

    def test_mxv(self):
        """Test the mxv method."""
        with self.assertRaises(AbstractMethodException):
            Transformation.mxv(None, None, None)


if __name__ == '__main__':
    unittest.main()
