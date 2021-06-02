import unittest

from emmpy.crucible.core.math.statistics import Statistics


class TestStatistics(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Statistics()


if __name__ == '__main__':
    unittest.main()
