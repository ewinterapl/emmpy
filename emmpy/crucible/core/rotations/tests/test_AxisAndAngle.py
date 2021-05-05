import unittest

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.rotations.axisandangle import AxisAndAngle


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        aaa = AxisAndAngle()
        self.assertIsNotNone(aaa)
        self.assertTrue(aaa.axis.equals(VectorIJK.K))
        # self.assertAlmostEqual(aaa.angle, 0.0)


if __name__ == '__main__':
    unittest.main()
