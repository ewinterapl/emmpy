import unittest

from emmpy.crucible.core.exceptions.runtimeexception import RuntimeException

class TestRuntimeException(unittest.TestCase):

    def test___init__(self):
        re = RuntimeException()


if __name__ == '__main__':
    unittest.main()
