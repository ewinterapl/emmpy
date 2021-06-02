import unittest

from emmpy.geomagmodel.t01.deformation.twistwarpffunction import (
    TwistWarpFfunction
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(TwistWarpFfunction(0.0, 0.0, 0.0))

    def test_deformField(self):
        pass


if __name__ == '__main__':
    unittest.main()
