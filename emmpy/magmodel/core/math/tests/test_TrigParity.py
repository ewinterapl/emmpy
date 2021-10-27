"""Tests for the trigparity module."""


import unittest

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)
from emmpy.magmodel.core.math.trigparity import EVEN, ODD


# Helper functions
def f(x):
    return x + 1


def df_dx(x):
    return 1


class TestBuilder(unittest.TestCase):
    """Tests for the trigparity module."""


if __name__ == "__main__":
    unittest.main()
