"""Tests for the unwritablerotation module."""


import unittest

from emmpy.crucible.core.rotations.unwritablerotation import (
    UnwritableRotation
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the unwritablerotation module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            UnwritableRotation()

    def test_getRotation(self):
        """Test the getRotation method."""
        with self.assertRaises(AbstractMethodException):
            UnwritableRotation.getRotation(None, None)


if __name__ == '__main__':
    unittest.main()
