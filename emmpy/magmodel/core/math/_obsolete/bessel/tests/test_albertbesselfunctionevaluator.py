import unittest

from emmpy.magmodel.core.math.bessel.albertbesselfunctionevaluator import (
    AlbertBesselFunctionEvaluator
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        AlbertBesselFunctionEvaluator()


if __name__ == '__main__':
    unittest.main()
