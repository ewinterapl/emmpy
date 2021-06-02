import unittest

from emmpy.crucible.crust.surfaces.surfacenormalcomputer import (
    SurfaceNormalComputer
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            SurfaceNormalComputer()

    def test_computeOutwardNormal(self):
        with self.assertRaises(Exception):
            SurfaceNormalComputer.computeOutwardNormal(None, None)


if __name__ == '__main__':
    unittest.main()
