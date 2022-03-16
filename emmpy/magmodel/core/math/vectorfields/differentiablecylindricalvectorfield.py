"""A differentiable vector field in cylindrical coordinates.

A differentiable vector field in cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class Results:
    """The spatial derivatives of a cylindrical VectorField.

    The spatial derivatives of a cylindrical VectorField.

    Attributes
    ----------
    f : CylindricalVector
        Location to evaluate derivatives.
    dFrDr, dFrDp, dFrDz : float
        Derivatives of radial component wrt radius, angle, height.
    dFpDr, dFpDp, dFpDz : float
        Derivatives of angular component wrt radius, angle, height.
    dFzDr, dFzDp, dFzDz : float
        Derivatives of height component wrt radius, angle, height.
    """

    def __init__(self, f, dFrDr, dFrDp, dFrDz, dFpDr, dFpDp, dFpDz, dFzDr,
                 dFzDp, dFzDz):
        """Initialize a new DifferentiableCylindricalVectorField object.

        Initialize a new DifferentiableCylindricalVectorField object.

        Parameters
        ----------
        f : CylindricalVector
            Location to evaluate derivatives.
        dFrDr, dFrDp, dFrDz : float
            Derivatives of radial component wrt radius, angle, height.
        dFpDr, dFpDp, dFpDz : float
            Derivatives of angular component wrt radius, angle, height.
        dFzDr, dFzDp, dFzDz : float
            Derivatives of height component wrt radius, angle, height.
        """
        self.f = f
        self.dFrDr = dFrDr
        self.dFrDp = dFrDp
        self.dFrDz = dFrDz
        self.dFpDr = dFpDr
        self.dFpDp = dFpDp
        self.dFpDz = dFpDz
        self.dFzDr = dFzDr
        self.dFzDp = dFzDp
        self.dFzDz = dFzDz
