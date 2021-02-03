import unittest

from emmpy.com.google.common.base.preconditions import Preconditions

class TestPreconditions(unittest.TestCase):

    def test_checkElementIndex(self):
        Preconditions.checkElementIndex(0, 0, '')

if __name__ == '__main__':
    unittest.main()
