import unittest

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(DifferentiableScalarFieldIJ())


if __name__ == '__main__':
    unittest.main()
