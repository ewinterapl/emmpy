import math
import unittest

from emmpy.crucible.core.units.fundamentalphysicalconstants import FundamentalPhysicalConstants

class TestFundamentalPhysicalConstants(unittest.TestCase):

    def test_HALFPI(self):
        self.assertEqual(FundamentalPhysicalConstants.HALFPI, math.pi/2)

if __name__ == '__main__':
    unittest.main()
