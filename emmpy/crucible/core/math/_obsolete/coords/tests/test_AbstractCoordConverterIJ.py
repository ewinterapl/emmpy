import unittest

from emmpy.crucible.core.math.coords.abstractcoordconverterij import (
    AbstractCoordConverterIJ
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        AbstractCoordConverterIJ([])
        with self.assertRaises(Exception):
            AbstractCoordConverterIJ(None)


if __name__ == '__main__':
    unittest.main()
