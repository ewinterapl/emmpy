import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        BugException()


if __name__ == '__main__':
    unittest.main()
