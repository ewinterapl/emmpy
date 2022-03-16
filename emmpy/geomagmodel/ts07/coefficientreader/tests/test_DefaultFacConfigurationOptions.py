import unittest

from emmpy.geomagmodel.ts07.coefficientreader.defaultfacconfigurationoptions import (
    DefaultFacConfigurationOptions
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        dfco = DefaultFacConfigurationOptions(
            DefaultFacConfigurationOptions.TS07D
        )
        self.assertIsNotNone(dfco)
        self.assertEqual(
            dfco.numberOfFields, DefaultFacConfigurationOptions.TS07D
        )

    def test_createFromCoeffs(self):
        pass

    def test_getTs07(self):
        pass

    def test_get6Fac(self):
        pass

    def test_get12Fac(self):
        pass

    def test_get16Fac(self):
        pass


if __name__ == '__main__':
    unittest.main()
