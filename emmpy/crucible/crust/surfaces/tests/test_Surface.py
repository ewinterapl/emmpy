import unittest

from emmpy.crucible.crust.surfaces.surface import Surface


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Surface()


if __name__ == '__main__':
    unittest.main()
