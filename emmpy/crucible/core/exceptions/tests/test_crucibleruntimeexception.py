"""Test code for the crucibleruntimeexception module."""


import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class TestBuilder(unittest.TestCase):
    """Build and run tests for the crucibleruntimeexception module."""

    def test___init__(self):
        """Test the __init__ method."""
        e = CrucibleRuntimeException()
        self.assertIsNotNone(e)


if __name__ == '__main__':
    unittest.main()
