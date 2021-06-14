"""Tests for the abstractclassexception module.

author Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

from emmpy.exceptions.abstractclassexception import AbstractClassException


class TestBuilder(unittest.TestCase):
    """Build and run tests for the abstractclassexception module."""

    def test___init__(self):
        """Test the __init__ function."""
        default_message = AbstractClassException._default_message
        message = 'Uh-oh!'
        # Test simple object creation, with and without messages.
        e = AbstractClassException()
        self.assertIsNotNone(e)
        self.assertEqual(e.message, default_message)
        e = AbstractClassException(message)
        self.assertIsNotNone(e)
        self.assertEqual(e.message, message)
        # Now try raising and catching the exceptions.
        try:
            raise AbstractClassException
        except AbstractClassException as e:
            self.assertEqual(e.message, default_message)
        try:
            raise AbstractClassException(message)
        except AbstractClassException as e:
            self.assertEqual(e.message, message)


if __name__ == '__main__':
    unittest.main()
