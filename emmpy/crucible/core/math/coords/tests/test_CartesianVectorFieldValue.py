import unittest

from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        uvijk1 = VectorIJK(1, 1, 1)
        uvijk2 = VectorIJK(2, 2, 2)
        cvfv = CartesianVectorFieldValue(uvijk1, uvijk2)
        self.assertIsNotNone(cvfv)
        # self.assertTrue(cvfv.position.equals(uvijk1))
        # self.assertTrue(cvfv.value.equals(uvijk2))


if __name__ == '__main__':
    unittest.main()
