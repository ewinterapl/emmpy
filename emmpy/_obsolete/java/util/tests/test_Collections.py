import unittest

from emmpy.java.util.collections import Collections

class TestCollections(unittest.TestCase):

    def test_binarySearch(self):
        # List must be sorted.
        a = [0, 2, 4.6, 5.4, 7]
        # Check key as each element.
        for (i, x) in enumerate(a):
            self.assertEqual(Collections.binarySearch(a, x), i)
        # Check key before array start.
        self.assertEqual(Collections.binarySearch(a, -0.5), -1)
        # Check key after array end.
        self.assertEqual(Collections.binarySearch(a, 10), -6)
        # Check key between each element.
        for (i, x) in enumerate(a):
            self.assertEqual(Collections.binarySearch(a, x + 0.5), -i - 2)

if __name__ == '__main__':
    unittest.main()
