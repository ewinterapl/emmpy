import unittest

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)
from emmpy.magmodel.core.math.trigparity import TrigParity


# Helper functions
def f(x):
    return x + 1


def df_dx(x):
    return 1


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        duf = DifferentiableUnivariateFunction()
        duf.evaluate = f
        duf.differentiate = df_dx
        tp = TrigParity(duf)
        self.assertIsNotNone(tp)
        self.assertIs(tp.function, duf)

    def test_evaluate(self):
        duf = DifferentiableUnivariateFunction()
        duf.evaluate = f
        duf.differentiate = df_dx
        tp = TrigParity(duf)
        self.assertAlmostEqual(tp.evaluate(0), f(0))
        self.assertAlmostEqual(tp.differentiate(0), df_dx(0))


if __name__ == '__main__':
    unittest.main()
