import unittest

from emmpy.crucible.core.exceptions.runtimeinterruptedexception import RuntimeInterruptedException

class TestRuntimeInterruptedException(unittest.TestCase):

    def test___init__(self):
        rie = RuntimeInterruptedException()


if __name__ == '__main__':
    unittest.main()
