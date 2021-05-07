import unittest

from emmpy.crucible.core.units.relativisticenergyandmomentum import (
    RelativisticEnergyAndMomentum
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        ream = RelativisticEnergyAndMomentum()
        self.assertIsNotNone(ream)

    def test_convertKineticEnergyToMomentumSI(self):
        self.assertAlmostEqual(
            RelativisticEnergyAndMomentum.
            convertKineticEnergyToMomentumSI(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
