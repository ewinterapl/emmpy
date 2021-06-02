import unittest

from emmpy.java.lang.illegalargumentexception import IllegalArgumentException


class TestIllegalArgumentException(unittest.TestCase):

    def test___init__(self):
        IllegalArgumentException()


if __name__ == '__main__':
    unittest.main()
