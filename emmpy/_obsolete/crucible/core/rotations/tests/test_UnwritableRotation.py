import unittest

from emmpy.crucible.core.rotations.unwritablerotation import (
    UnwritableRotation
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            UnwritableRotation()

    def test_getRotation(self):
        with self.assertRaises(Exception):
            UnwritableRotation.getRotation(None, None)


if __name__ == '__main__':
    unittest.main()
