import unittest

from emmpy.java.lang.object import Object


class TestObject(unittest.TestCase):

    def test___init__(self):
        Object()


if __name__ == '__main__':
    unittest.main()
