import unittest

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)


class TestPointOnAxisException(unittest.TestCase):

    def test___init__(self):
        PointOnAxisException()


if __name__ == '__main__':
    unittest.main()
