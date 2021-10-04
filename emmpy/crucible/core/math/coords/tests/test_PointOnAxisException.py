"""Tests for the pointonaxisexception module."""


import unittest

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)


class TestBuilder(unittest.TestCase):
    """Tests for the pointonaxisexception module."""

    def test___init__(self):
        """Test the __init__ method."""
        # 0-arg form
        e = PointOnAxisException()
        self.assertIsInstance(e, PointOnAxisException)
        # 1-arg form
        message_or_cause = "There is a problem."
        e = PointOnAxisException(message_or_cause)
        self.assertIsInstance(e, PointOnAxisException)
        self.assertEqual(e.args[0], message_or_cause)
        # 2-arg form
        message = "There is a problem."
        cause = object()
        e = PointOnAxisException(message, cause)
        self.assertIsInstance(e, PointOnAxisException)
        self.assertEqual(e.args[0], message)
        self.assertEqual(e.args[1], cause)
        # Now try raising and catching the exceptions.
        try:
            raise PointOnAxisException
        except PointOnAxisException as e:
            self.assertEqual(len(e.args), 0)
        try:
            raise PointOnAxisException(message)
        except PointOnAxisException as e:
            self.assertEqual(e.args[0], message)
        try:
            raise PointOnAxisException(message, cause)
        except PointOnAxisException as e:
            self.assertEqual(e.args[0], message)
            self.assertEqual(e.args[1], cause)


if __name__ == '__main__':
    unittest.main()
