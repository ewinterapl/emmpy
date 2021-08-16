"""Test code for the abstractcoordconverterij module."""


import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverterij import (
    AbstractCoordConverterIJ
)


class TestBuilder(unittest.TestCase):
    """Test code for the abstractcoordconverterij module."""

    def test___init__(self):
        """Test the __init__ method."""
        jacobian = [[0, 1], [3, 4]]
        acc = AbstractCoordConverterIJ(jacobian)
        self.assertIsInstance(acc, AbstractCoordConverterIJ)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(acc.jacobian[row][col],
                                       jacobian[row][col])


if __name__ == '__main__':
    unittest.main()
