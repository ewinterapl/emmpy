import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import CrucibleRuntimeException

class TestCrucibleRuntimeException(unittest.TestCase):

    def test___init__(self):
        cre = CrucibleRuntimeException()


if __name__ == '__main__':
    unittest.main()
