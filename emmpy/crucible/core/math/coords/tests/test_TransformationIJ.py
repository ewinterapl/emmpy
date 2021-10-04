"""Tests for the transformationij module."""


import unittest

from emmpy.crucible.core.math.coords.transformationij import TransformationIJ
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the transformation module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            TransformationIJ()

    def test_getTransformation(self):
        """Test the getTransformation method."""
        with self.assertRaises(AbstractMethodException):
            TransformationIJ.getTransformation(None, None, None)

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        with self.assertRaises(AbstractMethodException):
            TransformationIJ.getInverseTransformation(None, None, None)

    def test_mxv(self):
        """Test the mxv method."""
        with self.assertRaises(AbstractMethodException):
            TransformationIJ.mxv(None, None, None)


if __name__ == '__main__':
    unittest.main()
