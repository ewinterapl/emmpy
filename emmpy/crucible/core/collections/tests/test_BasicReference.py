import unittest

from emmpy.crucible.core.collections.basicreference import BasicReference


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        BasicReference(None)

    def test_get(self):
        self.assertEqual(BasicReference(1).get(), 1)

    def test_set(self):
        br = BasicReference(None)
        br.set(1)
        self.assertEqual(br.get(), 1)


if __name__ == '__main__':
    unittest.main()
