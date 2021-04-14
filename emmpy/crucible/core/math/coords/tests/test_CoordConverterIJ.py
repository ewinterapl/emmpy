import unittest

from emmpy.crucible.core.math.coords.coordconverterij import (
    CoordConverterIJ
)


class TestBuilderIJ(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            CoordConverterIJ()

    def test_toCoordinate(self):
        with self.assertRaises(Exception):
            CoordConverterIJ.toCoordinate(None, None)

    def test_toCartesian(self):
        with self.assertRaises(Exception):
            CoordConverterIJ.toCartesian(None, None)


if __name__ == '__main__':
    unittest.main()
