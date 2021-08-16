"""Tests for the abstractmethodexception module.

author Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class TestBuilder(unittest.TestCase):
    """Build and run tests for the abstractmethodexception module."""

    def test___init__(self):
        """Test the __init__ function."""
        default_message = AbstractMethodException._default_message
        message = 'Uh-oh!'
        # Test simple object creation, with and without messages.
        e = AbstractMethodException()
        self.assertIsNotNone(e)
        self.assertEqual(e.message, default_message)
        e = AbstractMethodException(message)
        self.assertIsNotNone(e)
        self.assertEqual(e.message, message)
        # Now try raising and catching the exceptions.
        try:
            raise AbstractMethodException
        except AbstractMethodException as e:
            self.assertEqual(e.message, default_message)
        try:
            raise AbstractMethodException(message)
        except AbstractMethodException as e:
            self.assertEqual(e.message, message)


if __name__ == '__main__':
    unittest.main()
