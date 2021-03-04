import unittest

from emmpy.java.lang.runtimeexception import RuntimeException


class TestRuntimeException(unittest.TestCase):

    def test___init__(self):
        RuntimeException()


if __name__ == '__main__':
    unittest.main()
