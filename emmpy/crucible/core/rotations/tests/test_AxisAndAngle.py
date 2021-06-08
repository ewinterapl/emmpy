import unittest

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.rotations.axisandangle import AxisAndAngle


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        aaa = AxisAndAngle()
        self.assertIsNotNone(aaa)
        # self.assertTrue(aaa.axis.equals(VectorIJK.K))
        self.assertAlmostEqual(aaa.angle, 0.0)

    def test_getAxis(self):
        pass

    def test_getAngle(self):
        pass

    def test_setAxis(self):
        pass

    def test_setAngle(self):
        pass

    def test_setTo(self):
        pass

    def test_getRotation(self):
        pass

    def test_hashCode(self):
        pass

    def test_toString(self):
        pass


if __name__ == '__main__':
    unittest.main()
