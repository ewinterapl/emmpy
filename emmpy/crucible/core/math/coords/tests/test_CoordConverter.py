"""Test code for the coordconverter module."""


import unittest

from emmpy.crucible.core.math.coords.coordconverter import CoordConverter
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Test code for the coordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverter()

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverter.toCoordinate(None, None)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverter.toCartesian(None, None)


if __name__ == '__main__':
    unittest.main()
