"""Tests for the differentiablevectorfield module."""


import unittest

from emmpy.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the differentiablevectorfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        # with self.assertRaises(AbstractMethodException):
            # DifferentiableVectorField()

    def test_differentiateFiDi(self):
        """Test the differentiateFiDi method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFiDi(None, None)

    def test_differentiateFjDi(self):
        """Test the differentiateFjDi method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFjDi(None, None)

    def test_differentiateFkDi(self):
        """Test the differentiateFkDi method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFkDi(None, None)

    def test_differentiateFiDj(self):
        """Test the differentiateFiDj method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFiDj(None, None)

    def test_differentiateFjDj(self):
        """Test the differentiateFjDj method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFjDj(None, None)

    def test_differentiateFkDj(self):
        """Test the differentiateFkDj method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFkDj(None, None)

    def test_differentiateFiDk(self):
        """Test the differentiateFiDk method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFiDk(None, None)

    def test_differentiateFjDk(self):
        """Test the differentiateFjDk method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFjDk(None, None)

    def test_differentiateFkDk(self):
        """Test the differentiateFkDk method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiateFkDk(None, None)

    def test_differentiate(self):
        """Test the differentiate method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField.differentiate(None, None)


if __name__ == "__main__":
    unittest.main()
