import unittest

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class TestAbstractVectorFieldValue(unittest.TestCase):

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
        # FIX THIS TEST.
        avfv = AbstractVectorFieldValue([0], [0])
        self.assertEqual(avfv.hashCode, 0)

    def test_equals(self):
        avfv1 = AbstractVectorFieldValue([0], [0])
        avfv2 = AbstractVectorFieldValue([0], [0])
        avfv3 = AbstractVectorFieldValue([1], [0])
        self.assertTrue(avfv1.equals(avfv2))

if __name__ == '__main__':
    unittest.main()
