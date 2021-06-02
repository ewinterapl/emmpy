import unittest

from emmpy.crucible.core.exceptions.runtimeinterruptedexception import (
    RuntimeInterruptedException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        RuntimeInterruptedException()


if __name__ == '__main__':
    unittest.main()
