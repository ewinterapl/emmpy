"""Tests for the differentiablevectorfield module."""


import unittest

from emmpy.crucible.core.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Tests for the differentiablevectorfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableVectorField()

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

    def test_Results___init__(self):
        """Test the Results.__init__ method."""

    def test_Results_getF(self):
        """Test the Results.getF method."""

    def test_Results_getdFxDx(self):
        """Test the Results.getdFxDx method."""

    def test_Results_getdFxDy(self):
        """Test the Results.getdFxDy method."""

    def test_Results_getdFxDz(self):
        """Test the Results.getdFxDz method."""

    def test_Results_getdFyDx(self):
        """Test the Results.getdFyDx method."""

    def test_Results_getdFyDy(self):
        """Test the Results.getdFyDy method."""

    def test_Results_getdFyDz(self):
        """Test the Results.getdFyDz method."""

    def test_Results_getdFzDx(self):
        """Test the Results.getdFzDx method."""

    def test_Results_getdFzDy(self):
        """Test the Results.getdFzDy method."""

    def test_Results_getdFzDz(self):
        """Test the Results.getdFzDz method."""


if __name__ == '__main__':
    unittest.main()
