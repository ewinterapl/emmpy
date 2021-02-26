import unittest

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import DifferentiableScalarFieldIJ

class TestOptionalDouble(unittest.TestCase):

    def test___init__(self):
        DifferentiableScalarFieldIJ()
    

if __name__ == '__main__':
    unittest.main()
