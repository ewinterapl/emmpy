"""Tests for the rotation module."""


import unittest

from emmpy.math.rotations.rotation import Rotation
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the rotation module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            Rotation()

    def test_setTo(self):
        """Test the setTo method."""
        with self.assertRaises(AbstractMethodException):
            Rotation.setTo(None, None)


if __name__ == '__main__':
    unittest.main()
