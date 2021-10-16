import unittest

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)


class TestBuilder(unittest.TestCase):

    def test_createExpansionFromArray(self):
        # 2 args - list + firstExpansionNumber
        e = CoefficientExpansions.createExpansionFromArray([0, 1, 2], 1)
        self.assertIsInstance(e, ArrayCoefficientExpansion1D)
        # 3 args - list + firstI,JexpansionNumber
        e = CoefficientExpansions.createExpansionFromArray(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
        self.assertIsInstance(e, ArrayCoefficientExpansion2D)
