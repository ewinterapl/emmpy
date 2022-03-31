"""Tests for the earthcurrentdensityfield module."""


import unittest

from emmpy.geomagmodel.earthcurrentdensityfield import (
    EarthCurrentDensityField
)


class TestBuilder(unittest.TestCase):
    """Tests for the earthcurrentdensityfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        ecdf = EarthCurrentDensityField(None, None)
        self.assertIsInstance(ecdf, EarthCurrentDensityField)
        self.assertIsNone(ecdf.jField)


if __name__ == "__main__":
    unittest.main()
