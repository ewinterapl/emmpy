import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.exceptions.functionevaluationexception import (
    FunctionEvaluationException
)


class TestFunctionEvaluationException(unittest.TestCase):

    def test___init__(self):
        FunctionEvaluationException()
        with self.assertRaises(CrucibleRuntimeException):
            FunctionEvaluationException(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
