import unittest

from emmpy.java.lang.indexoutofboundsexception import IndexOutOfBoundsException


class TestIndexOutOfBoundsException(unittest.TestCase):

    def test___init__(self):
        IndexOutOfBoundsException()


if __name__ == '__main__':
    unittest.main()
