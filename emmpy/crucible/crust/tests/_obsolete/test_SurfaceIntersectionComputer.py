import unittest

from emmpy.crucible.crust.surfaces.surfaceintersectioncomputer import (
    SurfaceIntersectionComputer
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            SurfaceIntersectionComputer()

    def test_intersects(self):
        with self.assertRaises(Exception):
            SurfaceIntersectionComputer.intersects(None, None, None)

    def test_compute(self):
        with self.assertRaises(Exception):
            SurfaceIntersectionComputer.compute(None, None, None, None)


if __name__ == '__main__':
    unittest.main()
