import unittest

from emmpy.crucible.core.math.coords.coordconverter import CoordConverter


class TestCoordConverter(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            CoordConverter()

    def test_toCoordinate(self):
        with self.assertRaises(Exception):
            CoordConverter.toCoordinate(None, None)

    def test_toCartesian(self):
        with self.assertRaises(Exception):
            CoordConverter.toCartesian(None, None)


if __name__ == '__main__':
    unittest.main()
