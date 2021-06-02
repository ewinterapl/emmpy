import unittest

from emmpy.java.util.nosuchelementexception import NoSuchElementException

class TestNoSuchElementException(unittest.TestCase):

    def test___init__(self):
        NoSuchElementException()
    

if __name__ == '__main__':
    unittest.main()
