import unittest

from emmpy.magmodel.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayExpansion1D([0, 1, 2])
        self.assertAlmostEqual(e, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
