"""A differentiable vector field in spherical coordinates.

A differentiable vector field in spherical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
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

    def getF(self):
        """Return the field value.

        Return the field value.

        Parameters
        ----------
        None

        Returns
        -------
        result : SphericalVector
            Value of the field.
        """
        return self.f

    def getdFrDr(self):
        """Return dFr/dr.
        
        Return dFr/dr.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of r-component wrt r.
        """
        return self.dFrDr

    def getdFrDt(self):
        """Return dFr/dt.
        
        Return dFr/dt.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of r-component wrt theta.
        """
        return self.dFrDt

    def getdFrDp(self):
        """Return dFr/dp.
        
        Return dFr/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of r-component wrt phi.
        """
        return self.dFrDp

    def getdFtDr(self):
        """Return dFt/dr.
        
        Return dFt/dr.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of theta-component wrt r.
        """
        return self.dFtDr

    def getdFtDt(self):
        """Return dFt/dt.
        
        Return dFt/dt.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of theta-component wrt theta.
        """
        return self.dFtDt

    def getdFtDp(self):
        """Return dFt/dp.
        
        Return dFt/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of theta-component wrt phi.
        """
        return self.dFtDp

    def getdFpDr(self):
        """Return dFp/dr.
        
        Return dFp/dr.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of phi-component wrt r.
        """
        return self.dFpDr

    def getdFpDt(self):
        """Return dFp/dt.
        
        Return dFp/dt.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of phi-component wrt theta.
        """
        return self.dFpDt

    def getdFpDp(self):
        """Return dFp/dp.
        
        Return dFp/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Derivative of phi-component wrt phi.
        """
        return self.dFpDp


class DifferentiableSphericalVectorField(SphericalVectorField):
    """A differentiable vector field in spherical coordinates.

    Represents the 9 spatial derivatives of a VectorField in spherical
    coordinates.
    """
