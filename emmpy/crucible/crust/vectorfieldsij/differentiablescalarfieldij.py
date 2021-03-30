"""emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij"""

from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D
from emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative import (
    ScalarFieldIJSpatialDerivative
)


class DifferentiableScalarFieldIJ(ScalarField2D, ScalarFieldIJSpatialDerivative):
    """Represents the Cartesian spatial derivatives of a ScalarField.

    There are three such derivatives.

    author G.K.Stephens
    """

    def __init__(self):
        """Interface - do not instantiate."""
        raise Exception
