"""Test code for the differentiableunivariatefunction module."""


import unittest

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Test code for the differentiableunivariatefunction module."""

    def test___init__(self):
        """Test the __init__ method."""
        duf = DifferentiableUnivariateFunction()
        self.assertIsInstance(duf, DifferentiableUnivariateFunction)

    def test_differentiate(self):
        """Test the differentiate method."""
        with self.assertRaises(AbstractMethodException):
            DifferentiableUnivariateFunction.differentiate(None, 0)


if __name__ == '__main__':
    unittest.main()
