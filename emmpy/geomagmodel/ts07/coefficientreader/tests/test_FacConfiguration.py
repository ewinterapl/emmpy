"""Tests for the facconfiguration module."""


import unittest

from emmpy.geomagmodel.ts07.coefficientreader.facconfiguration import (
    FacConfiguration
)


class TestBuilder(unittest.TestCase):
    """Tests for the facconfiguration module."""

    def test_createFromCoeffs(self):
        """Test the createFromCoeffs method."""
        with self.assertRaises(Exception):
            FacConfiguration.createFromCoeffs(None, None)


if __name__ == "__main__":
    unittest.main()
