import unittest

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        CylindricalVector(1.1, 2.2, 3.3)


if __name__ == '__main__':
    unittest.main()
