import unittest

from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        MalformedRotationException()


if __name__ == '__main__':
    unittest.main()
