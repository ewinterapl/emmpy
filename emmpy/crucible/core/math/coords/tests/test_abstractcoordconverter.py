"""Test code for the abstractcoordconverter module."""


import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)


class TestBuilder(unittest.TestCase):
    """Test code for the abstractcoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        jacobian = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        acc = AbstractCoordConverter(jacobian)
        self.assertIsInstance(acc, AbstractCoordConverter)
        for row in range(3):
            for col in range(3):
                self.assertAlmostEqual(acc.jacobian[row][col],
                                       jacobian[row][col])


if __name__ == '__main__':
    unittest.main()
