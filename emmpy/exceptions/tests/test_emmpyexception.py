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
        e = EmmpyException()
        self.assertIsNotNone(e)
        exception_str = 'Uh-oh!'
        try:
            raise EmmpyException(exception_str)
        except EmmpyException as e:
            self.assertEqual(e.__str__(), exception_str)


if __name__ == '__main__':
    unittest.main()
