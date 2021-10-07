"""Test code for the abstractvectorfieldvalue module."""


import unittest

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Test code for the abstractvectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        position = VectorIJK(1, 2, 3)
        value = VectorIJK(4, 5, 6)
        avfv = AbstractVectorFieldValue(position, value)
        self.assertIsInstance(avfv, AbstractVectorFieldValue)
        for i in range(3):
            self.assertAlmostEqual(avfv.position[i], position[i])
            self.assertAlmostEqual(avfv.value[i], value[i])


if __name__ == '__main__':
    unittest.main()
