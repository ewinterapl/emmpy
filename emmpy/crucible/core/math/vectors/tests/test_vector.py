"""Tests for the vector module."""

import unittest

from emmpy.crucible.core.math.vectors.vector import Vector
from emmpy.exceptions.abstractclassexception import AbstractClassException


class TestBuilder(unittest.TestCase):
    """Tests for the vector module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractClassException):
            Vector()


if __name__ == '__main__':
    unittest.main()
