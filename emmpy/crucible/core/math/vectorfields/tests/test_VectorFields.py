"""Tests for the vectorfields module."""


import unittest

from emmpy.crucible.core.math.vectorfields.vectorfields import (
    VectorFields
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfields module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            VectorFields()

    def test_add(self):
        """Test the add method."""
        pass

    def test_addAll(self):
        """Test the addAll method."""
        pass

    def test_negate(self):
        """Test the negate method."""
        pass

    def test_scale(self):
        """Test the scale method."""
        pass

    def test_scaleLocation(self):
        """Test the scaleLocation method."""
        pass


if __name__ == '__main__':
    unittest.main()
