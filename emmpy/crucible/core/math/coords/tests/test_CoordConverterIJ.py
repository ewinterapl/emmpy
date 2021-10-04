"""Test code for the coordconverterij module."""


import unittest

from emmpy.crucible.core.math.coords.coordconverterij import CoordConverterIJ
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilderIJ(unittest.TestCase):
    """Test code for the coordconverterij module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverterIJ()

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverterIJ.toCoordinate(None, None)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        with self.assertRaises(AbstractMethodException):
            CoordConverterIJ.toCartesian(None, None)


if __name__ == '__main__':
    unittest.main()
