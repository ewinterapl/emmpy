import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        AbstractCoordConverter([])
        with self.assertRaises(Exception):
            AbstractCoordConverter(None)


if __name__ == '__main__':
    unittest.main()
