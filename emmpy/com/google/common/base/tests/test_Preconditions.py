import unittest

from emmpy.com.google.common.base.preconditions import Preconditions


class TestPreconditions(unittest.TestCase):

    def test_checkArgument(self):
        self.assertIsNone(Preconditions.checkArgument(True))
        with self.assertRaises(Exception):
            Preconditions.checkArgument(False)
        with self.assertRaises(Exception) as cm:
            Preconditions.checkArgument(False, 'This is false.')
            self.assertEqual(cm.exception.__str__(), 'This is false.')
        with self.assertRaises(Exception) as cm:
            Preconditions.checkArgument(False, '%s %s false.', 'This', 'is')
            self.assertEqual(cm.exception.__str__(), 'This is false.')

    def test_checkElementIndex(self):
        x = [1, 2, 3]
        for i in range(len(x)):
            self.assertEqual(Preconditions.checkElementIndex(i, len(x)), i)
        with self.assertRaises(Exception):
            Preconditions.checkElementIndex(-1, len(x), len(x))
        with self.assertRaises(Exception):
            Preconditions.checkElementIndex(len(x), len(x), len(x))

    def test_checkNotNull(self):
        self.assertEqual(Preconditions.checkNotNull(1), 1)
        with self.assertRaises(Exception):
            Preconditions.checkNotNull(None)
        with self.assertRaises(Exception) as cm:
            Preconditions.checkNotNull(None, 'This is None.')
            self.assertEqual(cm.exception.__str__(), 'This is None.')
        with self.assertRaises(Exception) as cm:
            Preconditions.checkNotNull(None, '%s %s None.', 'This', 'is')
            self.assertEqual(cm.exception.__str__(), 'This is None.')


if __name__ == '__main__':
    unittest.main()
