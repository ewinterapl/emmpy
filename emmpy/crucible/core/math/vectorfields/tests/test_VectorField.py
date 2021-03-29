import unittest

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):

    # def test___init__(self):
    #     with self.assertRaises(Exception):
    #         VectorField()

    def test_evaluate(self):
        with self.assertRaises(Exception):
            VectorField().evaluate(VectorIJK())

if __name__ == '__main__':
    unittest.main()
