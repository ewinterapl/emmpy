"""emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D
from emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative import (
    ScalarFieldIJSpatialDerivative
)


class DifferentiableScalarFieldIJ(
      ScalarField2D, ScalarFieldIJSpatialDerivative):
    """Represents the Cartesian spatial derivatives of a ScalarField.

    # There are three such derivatives.

    # author G.K.Stephens
    # """

    def __init__(self):
        """Do-nothing constructor to avoid Exception in inherited ScalarField2D
        constructor"""
        pass
