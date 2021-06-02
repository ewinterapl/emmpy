import unittest

from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D


class TestBuilder(unittest.TestCase):

    def test_size(self):
        pass

    def test_getLowerBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion1D.getLowerBoundIndex(None)

    def test_getUpperBoundIndex(self):
        with self.assertRaises(Exception):
            Expansion1D.getUpperBoundIndex(None)

    def test_getExpansion(self):
        with self.assertRaises(Exception):
            Expansion1D.getExpansion(None, 0)


if __name__ == '__main__':
    unittest.main()
