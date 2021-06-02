import unittest

from emmpy.crucible.core.designpatterns.writable import (
    ImplementationInterface, Writable
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Writable()

    def test_setTo(self):
        with self.assertRaises(Exception):
            Writable.setTo(None, None)

    def test_ImplementationInterface__init__(self):
        with self.assertRaises(Exception):
            ImplementationInterface()


if __name__ == '__main__':
    unittest.main()
