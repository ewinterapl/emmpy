import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.exceptions.exceptionfactory import ExceptionFactory


class TestExceptionFactory(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(CrucibleRuntimeException):
            ExceptionFactory()


if __name__ == '__main__':
    unittest.main()
