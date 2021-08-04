"""Tests for the malformedrotationexception module."""


import unittest

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class TestBuilder(unittest.TestCase):
    """Tests for the malformedrotationexception module."""

    def test___init__(self):
        """Test the __init__ method."""
        MalformedRotationException()


if __name__ == '__main__':
    unittest.main()
