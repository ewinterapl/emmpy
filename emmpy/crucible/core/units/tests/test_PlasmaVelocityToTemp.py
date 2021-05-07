import unittest

from emmpy.crucible.core.units.plasmavelocitytotemp import PlasmaVelocityToTemp


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        pvtt = PlasmaVelocityToTemp(0)
        self.assertIsNotNone(pvtt)

    def test_getTempInKelvins(self):
        pvtt = PlasmaVelocityToTemp(1)
        self.assertAlmostEqual(pvtt.getTempInKelvins(0), 0)


if __name__ == '__main__':
    unittest.main()
