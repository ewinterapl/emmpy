"""An interface for a differentiable 2-D vector field.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D
from emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative import (
    ScalarFieldIJSpatialDerivative
)


class DifferentiableScalarFieldIJ(
      ScalarField2D, ScalarFieldIJSpatialDerivative):
    """An interface for a differentiable 2-D vector field.

    Represents the Cartesian spatial derivatives of a 2-D scalar field.

    There are two such derivatives.
    """

    def __init__(self):
        """Build a DifferentiableScalarFieldIJ object.

        INTERFACE - BUT MAY BE INSTANTIATED.

        This constructor does a pass instead of raise an Exception since this
        class is instantiated in some other classes, such as
        CurrentSheetHalfThicknesses.
        """
