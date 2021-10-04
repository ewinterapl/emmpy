"""Test code for the bugexception module."""


import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException


class TestBuilder(unittest.TestCase):
    """Build and run tests for the bugexception module."""

    def test___init__(self):
        """Test the __init__ method."""
        e = BugException()
        self.assertIsNotNone(e)


if __name__ == '__main__':
    unittest.main()
