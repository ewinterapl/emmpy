import unittest

from emmpy.crucible.core.exceptions.exceptionfactory import ExceptionFactory

class TestExceptionFactory(unittest.TestCase):

    def test___init__(self):
        ef = ExceptionFactory(Exception())


if __name__ == '__main__':
    unittest.main()
