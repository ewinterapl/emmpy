import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)


class TestAbstractCoordConverter(unittest.TestCase):

    def test___init__(self):
        AbstractCoordConverter()


if __name__ == '__main__':
    unittest.main()
