import unittest

from emmpy.templates.scalarfield2d import ScalarField2D

class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            ScalarField2D()
    

if __name__ == '__main__':
    unittest.main()
