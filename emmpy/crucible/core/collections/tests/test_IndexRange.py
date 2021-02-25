import unittest

from emmpy.crucible.core.collections.indexrange import IndexRange


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(IndexRange(0, 1))

    def test_getLowIndex(self):
        ir = IndexRange(0, 1)
        self.assertEqual(ir.getLowIndex(), 0)

    def test_getHighIndex(self):
        ir = IndexRange(0, 1)
        self.assertEqual(ir.getHighIndex(), 1)

    def test_getNumIndicesIncluded(self):
        ir = IndexRange(0, 1)
        self.assertEqual(ir.getNumIndicesIncluded(), 2)

    def test_contains(self):
        ir = IndexRange(0, 10)
        self.assertTrue(ir.contains(5))
        self.assertFalse(ir.contains(-5))

    def test_hashCode(self):
        ir = IndexRange(0, 1)
        self.assertEqual(ir.hashCode(), 992)

    def test_equals(self):
        ir1 = IndexRange(0, 1)
        ir2 = IndexRange(0, 1)
        ir3 = IndexRange(0, 2)
        ir4 = IndexRange(-1, 1)
        ir5 = IndexRange(-1, 2)
        self.assertTrue(ir1.equals(ir1))
        self.assertFalse(ir1.equals(None))
        self.assertFalse(ir1.equals(0))
        self.assertFalse(ir1.equals(ir3))
        self.assertFalse(ir1.equals(ir4))
        self.assertFalse(ir1.equals(ir5))
        self.assertTrue(ir1.equals(ir2))

    def test_toString(self):
        ir = IndexRange(0, 1)
        self.assertEqual(ir.toString(), "IndexRange [lowIndex=0, highIndex=1]")


if __name__ == '__main__':
    unittest.main()
