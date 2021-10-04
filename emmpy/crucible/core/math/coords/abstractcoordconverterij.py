"""Abstract base class for 2-D (i, j) coordinate converters.

This is the abstract base class for all 2-D (i, j) coordinate
converters.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.coordconverterij import CoordConverterIJ


class AbstractCoordConverterIJ(CoordConverterIJ):
    """Abstract base class for 2-D (i, j) coordinate converters.

    Attributes
    ----------
    jacobian : 2x2 array-like
        Jacobian matrix for coordinate conversion.
    """

    def __init__(self, jacobian):
        """Initialize a new AbstractCoordConverterIJ object.

        Initialize a new AbstractCoordConverterIJ object.

        Parameters
        ----------
        jacobian : 2x2 array-like of float
            Jacobian matrix for coordinate conversion.
        """
        self.jacobian = jacobian
