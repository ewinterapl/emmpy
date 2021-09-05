"""An interface for a differentiable 2-D scalar field.

This class defines the interface for a differentiable scalar field in 2
dimensions.

Note
----
This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorfields.scalarfield2d import ScalarField2D
from emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative import (
    ScalarFieldIJSpatialDerivative
)


class DifferentiableScalarFieldIJ(
      ScalarField2D, ScalarFieldIJSpatialDerivative):
    """An interface for a differentiable 2-D scalar field.

    Represents the Cartesian spatial derivatives of a 2-D scalar field.
    """

    def __init__(self):
        """Initialize a DifferentiableScalarFieldIJ object.

        Initialize a DifferentiableScalarFieldIJ object.

        This constructor does a pass instead of raise an Exception since this
        class is instantiated in some other classes, such as
        CurrentSheetHalfThicknesses.

        Parameters
        ----------
        None
        """
