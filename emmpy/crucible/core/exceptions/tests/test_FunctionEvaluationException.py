import unittest

from emmpy.crucible.core.exceptions.functionevaluationexpression import FunctionEvaluationException

class TestFunctionEvaluationException(unittest.TestCase):

    def test___init__(self):
        fee = FunctionEvaluationException()


if __name__ == '__main__':
    unittest.main()
