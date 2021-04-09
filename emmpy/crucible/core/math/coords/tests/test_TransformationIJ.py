import unittest

from emmpy.crucible.core.math.coords.transformationij import TransformationIJ


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            TransformationIJ()

    def test_getTransformation(self):
        with self.assertRaises(Exception):
            TransformationIJ.getTransformation(None, None, None)

    def test_getInverseTransformation(self):
        with self.assertRaises(Exception):
            TransformationIJ.getInverseTransformation(None, None, None)

    def test_mxv(self):
        with self.assertRaises(Exception):
            TransformationIJ.mxv(None, None, None)


if __name__ == '__main__':
    unittest.main()
