"""Tests for the magnetopauseoutput module."""


import unittest

from emmpy.geomagmodel.magnetopause.magnetopauseoutput import (
    MagnetopauseOutput
)


class TestBuilder(unittest.TestCase):
    """Tests for the magnetopauseoutput module."""

    def test___init__(self):
        """Test the __init__ method."""
        mo = MagnetopauseOutput()
        self.assertIsInstance(mo, MagnetopauseOutput)


if __name__ == "__main__":
    unittest.main()
