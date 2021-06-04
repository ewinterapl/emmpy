"""Test code for bugexception module."""


import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException


class TestBuilder(unittest.TestCase):
    """Build and run tests for bugexception module."""

    def test___init__(self):
        """Test the __init__ function."""
        BugException()


if __name__ == '__main__':
    unittest.main()
