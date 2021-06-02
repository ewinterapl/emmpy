import unittest

from emmpy.magmodel.core.time.utcnumerator import UTCNumerator


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            UTCNumerator()

    def test_numerate(self):
        with self.assertRaises(Exception):
            UTCNumerator.numerate(None, None)

    def test_calendarize(self):
        with self.assertRaises(Exception):
            UTCNumerator.calendarize(None, None)


if __name__ == '__main__':
    unittest.main()
