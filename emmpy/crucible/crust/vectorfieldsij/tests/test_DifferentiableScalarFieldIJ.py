import unittest

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            DifferentiableScalarFieldIJ()


if __name__ == '__main__':
    unittest.main()
