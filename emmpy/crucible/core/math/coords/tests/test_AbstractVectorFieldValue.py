import unittest

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
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


if __name__ == '__main__':
    unittest.main()
