import unittest

from emmpy.geomagmodel.ts07.modeling.fieldaligned.ffunction import Ffunction


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        ff = Ffunction(0, 0)
        self.assertAlmostEqual(ff.deltaPhi, 0)
        self.assertAlmostEqual(ff.dipoleTilt, 0)

    def test_evaluate(self):
        pass


if __name__ == '__main__':
    unittest.main()
