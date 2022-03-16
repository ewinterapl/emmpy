"""A container class for the output of the magnetopause methods.

A container class for the output of the magnetopause methods mirroring the
output of the magnetopause subroutines in the Geopack FORTRAN code
(T96_MGNP_08 and SHUETAL_MGNP_08). This contains a boolean indicating if the
query point is inside or outside the magnetopause along with a point located
on the magnetopause boundary that is approximately the closest point located
on the magnetopause to the query point.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class MagnetopauseOutput:
    """A container class for the output of the magnetopause methods.

    Attributes
    ----------
    None
    """

    def __init__(self, magnetopauseLocation, distanceToMagnetopause,
                 withinMagnetosphere):
        """Initialize a new MagnetopauseOutput object.

        Initialize a new MagnetopauseOutput object.

        Parameters
        ----------
        magnetopauseLocation : VectorIJK
            A point located on the magnetopause boundary that is approximately
            the closest point on the magnetopause to the query point.
        distanceToMagnetopause : float
            The distance between the query point and the point located on the
            magnetopause boundary that is approximately the closest point to
            it.
        withinMagnetosphere : bool
            True if the query point is within the magnetopause (inside the
            magnetosphere), False if it is outside the magnetopaause (outside
            the magnetosphere).

        Returns
        -------
        None
        """
        self.magnetopauseLocation = magnetopauseLocation
        self.distanceToMagnetopause = distanceToMagnetopause
        self.withinMagnetosphere = withinMagnetosphere
