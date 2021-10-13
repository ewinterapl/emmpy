"""Tests for the vectorfield module."""


import unittest

from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.vectorfields.vectorfield import VectorField


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfield module."""

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            VectorField.evaluate(None, None)


if __name__ == "__main__":
    unittest.main()
