import unittest

from emmpy.com.google.common.collect.unmodifiableiterator import (
    UnmodifiableIterator
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        UnmodifiableIterator()

    def test_remove(self):
        with self.assertRaises(Exception):
            UnmodifiableIterator().remove()


if __name__ == '__main__':
    unittest.main()
