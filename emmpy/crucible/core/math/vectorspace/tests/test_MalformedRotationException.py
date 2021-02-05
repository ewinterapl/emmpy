import unittest


from emmpy.crucible.core.math.vectorspace.malformedrotationexception import MalformedRotationException

class TestMalformedRotationException(unittest.TestCase):

    def test___init__(self):
        mre = MalformedRotationException

if __name__ == '__main__':
    unittest.main()
