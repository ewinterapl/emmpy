import unittest

from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)


class TestUnsupportedOperationException(unittest.TestCase):

    def test___init__(self):
        UnsupportedOperationException()


if __name__ == '__main__':
    unittest.main()
