"""Abstract base class for 3-D coordinate converters.

This is the abstract base class for all coordinate converters.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.coordconverter import CoordConverter


class AbstractCoordConverter(CoordConverter):
    """Abstract base class for 3-D coordinate converters.

    Attributes
    ----------
    jacobian : 3x3 array-like of float
        Jacobian matrix for coordinate conversion.
    """

    def __init__(self, jacobian):
        """Initialize a new AbstractCoordConverter object.

        Initialize a new AbstractCoordConverter object.

        Parameters
        ----------
        jacobian : 3x3 array-like of float
            Jacobian matrix for coordinate conversion.
        """
        self.jacobian = jacobian
