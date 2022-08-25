"""A differentiable vector field in spherical coordinates.

A differentiable vector field in spherical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


class Results:
    """The spatial derivatives of a VectorField in spherical coordinates.

    The spatial derivatives of a VectorField in spherical coordinates.

    Attributes
    ----------
    f : SphericalVector
        Location for computing derivatives.
    dFrDr, dFrDt, dFrDp : float
        Derivatives of radial component wrt r, theta, phi.
    dFtDr, dFtDt, dFtDp : float
        Derivatives of theta component wrt r, theta, phi.
    dFpDr, dFpDt, dFpDp : float
        Derivatives of phi component wrt r, theta, phi.
    """

    def __init__(self, f, dFrDr, dFrDt, dFrDp, dFtDr, dFtDt, dFtDp, dFpDr,
                 dFpDt, dFpDp):
        """Initialize a new Results object.

        Initialize a new Results object.

        Parameters
        ----------
        f : SphericalVector
            Location for computing derivatives.
        dFrDr, dFrDt, dFrDp : float
            Derivatives of radial component wrt r, theta, phi.
        dFtDr, dFtDt, dFtDp : float
            Derivatives of theta component wrt r, theta, phi.
        dFpDr, dFpDt, dFpDp : float
            Derivatives of phi component wrt r, theta, phi.
        """
        self.f = f
        self.dFrDr = dFrDr
        self.dFrDt = dFrDt
        self.dFrDp = dFrDp
        self.dFtDr = dFtDr
        self.dFtDt = dFtDt
        self.dFtDp = dFtDp
        self.dFpDr = dFpDr
        self.dFpDt = dFpDt
        self.dFpDp = dFpDp
