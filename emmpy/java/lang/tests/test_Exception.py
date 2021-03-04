import unittest

from emmpy.java.lang.exception import Exception


class TestException(unittest.TestCase):

    def test___init__(self):
        Exception()


if __name__ == '__main__':
    unittest.main()
