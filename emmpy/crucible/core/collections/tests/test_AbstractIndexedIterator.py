import unittest

from emmpy.crucible.core.collections.abstractindexediterator import AbstractIndexedIterator

class TestBuilder(unittest.TestCase):

    def test___init__(self):
        AbstractIndexedIterator()

    def test_hasNext(self):
        aii = AbstractIndexedIterator()
        with self.assertRaises(Exception):
            aii.hasNext()

    def test_next(self):
        aii = AbstractIndexedIterator()
        with self.assertRaises(Exception):
            aii.next()

    def test_elements(self):
        with self.assertRaises(Exception):
            AbstractIndexedIterator().elements()

    def test_element(self):
        with self.assertRaises(Exception):
            AbstractIndexedIterator().element(0)
    

if __name__ == '__main__':
    unittest.main()
