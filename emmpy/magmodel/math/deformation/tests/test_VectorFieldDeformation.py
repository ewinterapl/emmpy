import unittest

from emmpy.magmodel.math.deformation.vectorfielddeformation import (
    VectorFieldDeformation
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            VectorFieldDeformation()

    def test_evaluate(self):
        # IMPLEMENT
        pass

    def test_computeMatrix(self):
        # IMPLEMENT
        pass


if __name__ == '__main__':
    unittest.main()
