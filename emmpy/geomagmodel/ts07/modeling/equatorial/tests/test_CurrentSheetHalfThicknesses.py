"""Tests for the currentsheethalfthicknesses module."""


import unittest

from emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses import (
    createConstant
)


class TestBuilder(unittest.TestCase):
    """Tests for the currentsheethalfthicknesses module."""

    def test_createConstant(self):
        dsfij = createConstant(1.9)
        self.assertAlmostEqual(dsfij.evaluate(None), 1.9)


if __name__ == '__main__':
    unittest.main()
