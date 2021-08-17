"""Tests for the vectorfieldvalue module."""


import unittest

from emmpy.crucible.core.math.coords.vectorfieldvalue import VectorFieldValue
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            VectorFieldValue()

    def test_getPosition(self):
        """Test the getPosition method."""
        with self.assertRaises(AbstractMethodException):
            VectorFieldValue.getPosition(None)

    def test_getValue(self):
        """Test the getValue method."""
        with self.assertRaises(AbstractMethodException):
            VectorFieldValue.getValue(None)


if __name__ == '__main__':
    unittest.main()
