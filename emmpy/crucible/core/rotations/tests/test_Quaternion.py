import unittest

from emmpy.crucible.core.rotations.rotation import (
    Rotation
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Rotation()

    def test_setTo(self):
        with self.assertRaises(Exception):
            Rotation.setTo(None, None)


if __name__ == '__main__':
    unittest.main()
