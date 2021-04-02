import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverter import (
    AbstractCoordConverter
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        acc = AbstractCoordConverter([])


if __name__ == '__main__':
    unittest.main()
