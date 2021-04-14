import unittest

from emmpy.magmodel.core.math.coords.cylindricalcoordsxaligned import (
    CylindricalCoordsXAligned
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        ccxa = CylindricalCoordsXAligned()
        self.assertIsNotNone(ccxa)

    def test_convert(self):
        ccxa = CylindricalCoordsXAligned()
        cartesian = UnwritableVectorIJK(1, 2, 3)
        cylindrical = ccxa.convert(cartesian)
        self.assertIsNotNone(cylindrical)
        self.assertAlmostEqual(cylindrical.getI(), 3.6055512754639896)
        self.assertAlmostEqual(cylindrical.getJ(), 0.982793723247329)
        self.assertAlmostEqual(cylindrical.getK(), 1)
        cartesian = ccxa.convert(cylindrical)
        self.assertIsNotNone(cartesian)
        self.assertAlmostEqual(cartesian.getI(), 1)
        self.assertAlmostEqual(cartesian.getJ(), 2)
        self.assertAlmostEqual(cartesian.getK(), 3)
        with self.assertRaises(Exception):
            ccxa.convert([])

    def test_convertFieldValue(self):
        ccxa = CylindricalCoordsXAligned()
        cartesianPosition = UnwritableVectorIJK(1, 2, 3)
        cartesianValue = UnwritableVectorIJK(4, 5, 6)
        cylindricalValue = ccxa.convertFieldValue(
            cartesianPosition, cartesianValue
        )
        self.assertIsNotNone(cylindricalValue)
        self.assertAlmostEqual(cylindricalValue.getI(), 7.7658027471532085)
        self.assertAlmostEqual(cylindricalValue.getJ(), -0.832050294337844)
        self.assertAlmostEqual(cylindricalValue.getK(), 4)
        cylindricalPosition = ccxa.convert(cartesianPosition)
        cartesianValue = ccxa.convertFieldValue(
            cylindricalPosition, cylindricalValue
        )
        self.assertIsNotNone(cartesianValue)
        self.assertAlmostEqual(cartesianValue.getI(), 4)
        self.assertAlmostEqual(cartesianValue.getJ(), 5)
        self.assertAlmostEqual(cartesianValue.getK(), 6)
        with self.assertRaises(Exception):
            ccxa.convertFieldValue([])

    def test_convertBasisField(self):
        ccxa = CylindricalCoordsXAligned()
        cartesian = UnwritableVectorIJK(1, 2, 3)
        cylindrical = ccxa.convertBasisField(cartesian)
        # self.assertIsNotNone(cylindrical)
        # self.assertAlmostEqual(cylindrical.getI(), 0)
        # self.assertAlmostEqual(cylindrical.getJ(), 0)
        # self.assertAlmostEqual(cylindrical.getK(), 0)


if __name__ == '__main__':
    unittest.main()
