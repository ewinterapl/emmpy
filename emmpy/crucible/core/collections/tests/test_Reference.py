import unittest

from emmpy.crucible.core.collections.reference import Reference
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(CrucibleRuntimeException):
            Reference()

    def test_get(self):
        with self.assertRaises(CrucibleRuntimeException):
            Reference.get(None)

    def test_set(self):
        with self.assertRaises(CrucibleRuntimeException):
            Reference.set(None, None)


if __name__ == '__main__':
    unittest.main()
