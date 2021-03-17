import unittest

from emmpy.utilities.isragged import isRagged


class TestBuilder(unittest.TestCase):

    def test_isRagged(self):
        self.assertTrue(isRagged([[0,], [1, 2]]))
        self.assertFalse(isRagged([[0, 1], [2, 3]]))


if __name__ == '__main__':
    unittest.main()
