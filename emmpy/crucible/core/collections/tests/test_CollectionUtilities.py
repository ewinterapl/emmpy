import unittest

from emmpy.crucible.core.collections.collectionutilities import (
    CollectionUtilities
)


class TestBuilder(unittest.TestCase):

    def test_lastLessThanOrEqualTo(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Check key values in list.
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 0), 0)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 2), 3)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 4), 5)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 7), 7)
        # Check key sorting before list start.
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, -1), -1)
        # Check keys sorting between each element.
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 0.5), 0)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 2.5), 3)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 4.5), 5)
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 5.5), 6)
        # Check key sorting after list end.
        self.assertEqual(CollectionUtilities.lastLessThanOrEqualTo(a, 10), 7)

    def test_lastLessThan(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Check key values in list.
        self.assertEqual(CollectionUtilities.lastLessThan(a, 0), -1)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 2), 0)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 4), 3)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 5), 5)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 7), 6)
        # Check key before first value.
        self.assertEqual(CollectionUtilities.lastLessThan(a, -1), -1)
        # Check key values between list values.
        self.assertEqual(CollectionUtilities.lastLessThan(a, 1), 0)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 2.5), 3)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 4.5), 5)
        self.assertEqual(CollectionUtilities.lastLessThan(a, 5.5), 6)
        # Check key after kast value,
        self.assertEqual(CollectionUtilities.lastLessThan(a, 8), 7)

    def test_firstGreaterThanOrEqualTo(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Check key values in list.
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 0),
                         0)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 2),
                         1)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 4),
                         4)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 5),
                         6)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 7),
                         7)
        # Check key before first value.
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, -1),
                         0)
        # Check key values between list values.
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 1.5),
                         1)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 3),
                         4)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 4.5),
                         6)
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 6),
                         7)
        # Check key after kast value,
        self.assertEqual(CollectionUtilities.firstGreaterThanOrEqualTo(a, 8),
                         8)

    def test_firstGreaterThan(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Check key less than 1st element.
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, -1), 0)
        # Check interior elements.
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, 1), 1)
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, 2.5), 4)
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, 4.5), 6)
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, 6), 7)
        # Check key greater than last element.
        self.assertEqual(CollectionUtilities.firstGreaterThan(a, 10), 8)

    def test_locateFirstElementEqualTo(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Verify exception when key not found.
        with self.assertRaises(ValueError):
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, -1, a)
        # First element
        self.assertEqual(CollectionUtilities.locateFirstElementEqualTo(0, a[0],
                                                                       a), 0)
        # Interior elements
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, 0, a), 0)
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, 2, a), 1)
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, 4, a), 4)
        with self.assertRaises(ValueError):
            CollectionUtilities.locateFirstElementEqualTo(3, 4, a)
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, 5, a), 6)
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, 7, a), 7)
        # Last element
        self.assertEqual(
            CollectionUtilities.locateFirstElementEqualTo(len(a) - 1, a[-1],
                                                          a), len(a) - 1)

    def test_locateLastElementEqualTo(self):
        # List must be sorted.
        a = [0, 2, 2, 2, 4, 4, 5, 7]
        # Verify exception when key not found.
        with self.assertRaises(ValueError):
            CollectionUtilities.locateLastElementEqualTo(0, -1, a)
        # First element
        self.assertEqual(CollectionUtilities.locateLastElementEqualTo(0, 0,
                                                                      a), 0)
        with self.assertRaises(ValueError):
            CollectionUtilities.locateLastElementEqualTo(1, 0, a)
        # Interior elements
        self.assertEqual(
            CollectionUtilities.locateLastElementEqualTo(0, 2, a), 3)
        with self.assertRaises(ValueError):
            CollectionUtilities.locateLastElementEqualTo(4, 2, a)
        self.assertEqual(
            CollectionUtilities.locateLastElementEqualTo(0, 4, a), 5)
        self.assertEqual(
            CollectionUtilities.locateLastElementEqualTo(0, 5, a), 6)
        # Last element
        self.assertEqual(
            CollectionUtilities.locateLastElementEqualTo(0, 7, a), 7)

    def test_convertIndexForLessThan(self):
        self.assertEqual(CollectionUtilities.convertIndexForLessThan(0, None),
                         -2)
        self.assertEqual(CollectionUtilities.convertIndexForLessThan(-1, None),
                         -1)
        self.assertEqual(CollectionUtilities.convertIndexForLessThan(-2, None),
                         0)

    def test_addAll(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        self.assertEqual(CollectionUtilities.addAll(b, a), [1, 2, 3, 4, 5, 6])

    def test_convertToListOfSuperclass(self):
        a = [1, 2, 3]
        self.assertEqual(CollectionUtilities.convertToListOfSuperclass(a), a)


if __name__ == '__main__':
    unittest.main()
