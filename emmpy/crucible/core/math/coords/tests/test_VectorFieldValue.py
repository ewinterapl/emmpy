import unittest

from emmpy.crucible.core.math.coords.vectorfieldvalue import VectorFieldValue


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            VectorFieldValue()

    def test_getPosition(self):
        with self.assertRaises(Exception):
            VectorFieldValue.getPosition(None)

    def test_getValue(self):
        with self.assertRaises(Exception):
            VectorFieldValue.getValue(None)


if __name__ == '__main__':
    unittest.main()
