import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facregion import (
    FacRegion
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        fr = FacRegion(FacRegion.REGION_1)
        self.assertIsNotNone(fr)
        self.assertEqual(fr.number, FacRegion.REGION_1)


if __name__ == '__main__':
    unittest.main()
