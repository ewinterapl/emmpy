"""Test code for the crucibleexception module."""


import unittest

from emmpy.crucible.core.exceptions.crucibleexception import CrucibleException


class TestBuilder(unittest.TestCase):
    """Build and run tests for the crucibleexception module."""

    def test___init__(self):
        """Test the __init__ method."""
        e = CrucibleException()
        self.assertIsNotNone(e)


if __name__ == '__main__':
    unittest.main()
