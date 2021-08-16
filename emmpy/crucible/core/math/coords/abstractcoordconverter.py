"""Abstract base class for coordinate converters.

This is the abstract base class for all coordinate converters.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.coordconverter import CoordConverter


class AbstractCoordConverter(CoordConverter):
    """Abstract base class for coordinate converters.

    Attributes
    ----------
    jacobian : array-like
        Jacobian matrix for coordinate conversion.
    """

    def __init__(self, jacobian):
        """Initialize a new AbstractCoordConverter object.

        Initialize a new AbstractCoordConverter object.

        Parameters
        ----------
        jacobian : array-like
            Jacobian matrix for coordinate conversion.
        """
        self.jacobian = jacobian
