import unittest

from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.math.expansions.listexpansion1d import ListExpansion1D


class TestBuilder(unittest.TestCase):

    def test__createFromList(self):
        e = Expansion1Ds.createFromList([0, 1, 2], 1)
        self.assertIsInstance(e, ListExpansion1D)

    def test__createFromArray(self):
        e = Expansion1Ds.createFromArray([0, 1, 2], 1)
        self.assertIsInstance(e, ArrayExpansion1D)


if __name__ == '__main__':
    unittest.main()
