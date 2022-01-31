import unittest

from emmpy.magmodel.core.math.expansions.arrayexpansion2d import (
    ArrayExpansion2D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayExpansion2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertAlmostEqual(e, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])


if __name__ == '__main__':
    unittest.main()
