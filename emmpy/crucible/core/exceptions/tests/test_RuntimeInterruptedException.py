import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.exceptions.runtimeinterruptedexception import (
    RuntimeInterruptedException
)


class TestRuntimeInterruptedException(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(CrucibleRuntimeException):
            RuntimeInterruptedException()


if __name__ == '__main__':
    unittest.main()
