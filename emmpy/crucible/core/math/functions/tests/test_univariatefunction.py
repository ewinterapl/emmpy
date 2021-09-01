"""Test code for the univariatefunction module."""

import unittest

from emmpy.crucible.core.math.functions.univariatefunction import (
    UnivariateFunction
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Test code for the univariatefunction module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(AbstractMethodException):
            UnivariateFunction()

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            UnivariateFunction.evaluate(None, 0)


if __name__ == '__main__':
    unittest.main()
