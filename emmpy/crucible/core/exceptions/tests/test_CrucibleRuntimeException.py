import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        CrucibleRuntimeException()


if __name__ == '__main__':
    unittest.main()
