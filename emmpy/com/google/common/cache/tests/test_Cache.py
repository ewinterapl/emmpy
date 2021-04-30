import unittest

from emmpy.com.google.common.cache.cache import Cache


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Cache()

    def test_getIfPresent(self):
        with self.assertRaises(Exception):
            Cache.getIfPresent(None, None)

    def test_get(self):
        with self.assertRaises(Exception):
            Cache.get(None, None)

    def test_getAllPresent(self):
        with self.assertRaises(Exception):
            Cache.getAllPresent(None)

    def test_put(self):
        with self.assertRaises(Exception):
            Cache.put(None, None, None)

    def test_putAll(self):
        with self.assertRaises(Exception):
            Cache.putAll(None, None)

    def test_invalidate(self):
        with self.assertRaises(Exception):
            Cache.invalidate(None, None)

    def test_invalidateAll(self):
        with self.assertRaises(Exception):
            Cache.invalidateAll(None)
        with self.assertRaises(Exception):
            Cache.invalidateAll(None, None)

    def test_size(self):
        with self.assertRaises(Exception):
            Cache.size(None)

    def test_stats(self):
        with self.assertRaises(Exception):
            Cache.stats(None)

    def test_asMap(self):
        with self.assertRaises(Exception):
            Cache.asMap(None)

    def test_cleanUp(self):
        with self.assertRaises(Exception):
            Cache.cleanUp(None)


if __name__ == '__main__':
    unittest.main()
