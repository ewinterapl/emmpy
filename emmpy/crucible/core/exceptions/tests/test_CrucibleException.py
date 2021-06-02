import unittest

from emmpy.crucible.core.exceptions.crucibleexception import CrucibleException


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        CrucibleException()


if __name__ == '__main__':
    unittest.main()
