import unittest

from emmpy.geomagmodel.t01.deformation.twistwarpfunction import (
    TwistWarpFfunction
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(TwistWarpFfunction())


if __name__ == '__main__':
    unittest.main()
