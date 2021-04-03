import unittest

from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.exceptions.functionevaluationexception import (
    FunctionEvaluationException
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = FunctionEvaluationException()
        self.assertEqual(
            e.__str__(),
            "The function is not able to evaluate at the supplied value"
        )
        e = FunctionEvaluationException(1)
        self.assertEqual(
            e.__str__(),
            "The function is not able to evaluate at the value 1"
        )
        e = FunctionEvaluationException(1, 2)
        self.assertEqual(
            e.__str__(),
            "The function is not able to evaluate at the value 1. 2"
        )
        with self.assertRaises(CrucibleRuntimeException):
            FunctionEvaluationException(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
