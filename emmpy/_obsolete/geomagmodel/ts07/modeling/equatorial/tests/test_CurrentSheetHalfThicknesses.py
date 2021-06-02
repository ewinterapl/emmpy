import unittest

from emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses import (
    CurrentSheetHalfThicknesses
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(CurrentSheetHalfThicknesses())

    def test_createConstant(self):
        dsfij = CurrentSheetHalfThicknesses.createConstant(1.9)
        self.assertAlmostEqual(dsfij.evaluate(None), 1.9)


if __name__ == '__main__':
    unittest.main()
