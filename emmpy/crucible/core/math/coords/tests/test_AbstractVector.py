import unittest

from emmpy.crucible.core.math.coords.abstractvector import (
    AbstractVector
)


class TestAbstractVector(unittest.TestCase):

    def test___init__(self):
        AbstractVector()


if __name__ == '__main__':
    unittest.main()
