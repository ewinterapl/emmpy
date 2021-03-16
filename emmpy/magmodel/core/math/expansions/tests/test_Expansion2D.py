import unittest

from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D


class TestBuilder(unittest.TestCase):

    def test_iSize(self):
        pass

    def test_jSize(self):
        pass

    def test_getILowerBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion2D.getILowerBoundIndex(None)

    def test_getIUpperBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion2D.getIUpperBoundIndex(None)

    def test_getJLowerBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion2D.getJLowerBoundIndex(None)

    def test_getJUpperBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion2D.getJUpperBoundIndex(None)

    def test_getExpansion(self):
        with self.assertRaises(Exception):
            Expansion2D.getExpansion(None, 0, 0)


if __name__ == '__main__':
    unittest.main()
