import unittest

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        avfv = AbstractVectorFieldValue([0], [0])
        self.assertIsNotNone(avfv)
        self.assertAlmostEqual(avfv.position, [0])
        self.assertAlmostEqual(avfv.value, [0])

    def test_getPosition(self):
        avfv = AbstractVectorFieldValue([0], [0])
        self.assertAlmostEqual(avfv.getPosition(), [0])

    def test_getValue(self):
        avfv = AbstractVectorFieldValue([0], [0])
        self.assertAlmostEqual(avfv.getValue(), [0])

    def test_toString(self):
        avfv = AbstractVectorFieldValue([0], [0])
        self.assertEqual(avfv.toString(), "[position=[0], value=[0]]")

    def test_hashCode(self):
        uvijk0 = UnwritableVectorIJK(0, 0, 0)
        uvijk1 = UnwritableVectorIJK(1, 1, 1)
        avfv = AbstractVectorFieldValue(uvijk0, uvijk1)
        self.assertEqual(avfv.hashCode(), 1057896697761)

    def test_equals(self):
        uvijk0 = UnwritableVectorIJK(0, 0, 0)
        uvijk1 = UnwritableVectorIJK(1, 1, 1)
        uvijk2 = UnwritableVectorIJK(2, 2, 2)
        avfv1 = AbstractVectorFieldValue(uvijk0, uvijk1)
        avfv2 = AbstractVectorFieldValue(uvijk0, uvijk1)
        avfv3 = AbstractVectorFieldValue(uvijk0, uvijk2)
        self.assertTrue(avfv1.equals(avfv1))
        self.assertFalse(avfv1.equals(None))
        self.assertFalse(avfv1.equals([]))
        self.assertFalse(avfv1.equals(avfv3))
        avfv1.position = None
        self.assertFalse(avfv1.equals(avfv2))
        avfv1 = AbstractVectorFieldValue(uvijk0, uvijk1)
        self.assertFalse(avfv1.equals(avfv3))
        avfv1.value = None
        self.assertFalse(avfv1.equals(avfv2))
        avfv1 = AbstractVectorFieldValue(uvijk0, uvijk1)
        self.assertTrue(avfv1.equals(avfv2))


if __name__ == '__main__':
    unittest.main()
