import unittest

from emmpy.java.util.optionaldouble import OptionalDouble

class TestOptionalDouble(unittest.TestCase):

    def test___init__(self):
        OptionalDouble()

    def test_empty(self):
        OptionalDouble.empty()
    

if __name__ == '__main__':
    unittest.main()
