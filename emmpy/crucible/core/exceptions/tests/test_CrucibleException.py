"""Test code for crucibleexception module."""


import unittest

from emmpy.crucible.core.exceptions.crucibleexception import CrucibleException


class TestBuilder(unittest.TestCase):
    """Build and run tests for crucibleexception module."""

    def test___init__(self):
        """Test the __init__ function."""
        CrucibleException()


if __name__ == '__main__':
    unittest.main()
