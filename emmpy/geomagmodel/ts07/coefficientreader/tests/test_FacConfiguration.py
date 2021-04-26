import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facconfiguration import (
    FacConfiguration
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            FacConfiguration()

    def test_createFromCoeffs(self):
        with self.assertRaises(Exception):
            FacConfiguration.createFromCoeffs(None, None)

    def test_getNumberOfFields(self):
        with self.assertRaises(Exception):
            FacConfiguration.getNumberOfFields(None)


if __name__ == '__main__':
    unittest.main()
