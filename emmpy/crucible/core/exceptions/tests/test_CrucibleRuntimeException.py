"""Test code for crucibleruntimeexception module."""


import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class TestBuilder(unittest.TestCase):
    """Build and run tests for crucibleruntimeexception module."""

    def test___init__(self):
        """Test the __init__ function."""
        CrucibleRuntimeException()


if __name__ == '__main__':
    unittest.main()
