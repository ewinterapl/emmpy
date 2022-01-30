import unittest

from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D


class TestBuilder(unittest.TestCase):

    def test_iSize(self):
        pass

    def test_jSize(self):
        pass

    def test_getExpansion(self):
        with self.assertRaises(Exception):
            Expansion2D.getExpansion(None, 0, 0)


if __name__ == '__main__':
    unittest.main()
