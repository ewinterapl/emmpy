"""Tests for the emmpyexception module.

author Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.exceptions.emmpyexception import (
    EmmpyException
)


class TestBuilder(unittest.TestCase):
    """Build and run tests for the emmpyexception module."""

    def test___init__(self):
        """Test the __init__() function."""
        default_message = EmmpyException._default_message
        message = 'Uh-oh!'
        # Test simple object creation, with and without messages.
        e = EmmpyException()
        self.assertIsNotNone(e)
        self.assertEqual(e.message, default_message)
        e = EmmpyException(message)
        self.assertIsNotNone(e)
        self.assertEqual(e.message, message)
        # Now try raising and catching the exceptions.
        try:
            raise EmmpyException
        except EmmpyException as e:
            self.assertEqual(e.message, default_message)
        try:
            raise EmmpyException(message)
        except EmmpyException as e:
            self.assertEqual(e.message, message)


if __name__ == '__main__':
    unittest.main()
