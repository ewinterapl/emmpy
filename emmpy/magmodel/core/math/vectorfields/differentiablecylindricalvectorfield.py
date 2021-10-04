"""A differentiable vector field in cylindrical coordinates.

A differentiable vector field in cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


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

    def getF(self):
        """Return the field location.

        Return the field location.

        Parameters
        ----------
        None

        Returns
        -------
        result : CylindricalVector
            Location in cylindrical field.
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
            r-derivative of r-component of field.
        """
        return self.dFrDr

    def getdFrDp(self):
        """Return dFr/p.
        
        Return dFr/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Angle-derivative of r-component of field.
        """
        return self.dFrDp

    def getdFrDz(self):
        """Return dFr/dz.
        
        Return dFr/dz.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            z-derivative of r-component of field.
        """
        return self.dFrDz

    def getdFpDr(self):
        """Return dFp/dr.
        
        Return dFp/dr.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            r-derivative of angle component of field.
        """
        return self.dFpDr

    def getdFpDp(self):
        """Return dFp/dp.
        
        Return dFp/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Angle-derivative of angle component of field.
        """
        return self.dFpDp

    def getdFpDz(self):
        """Return dFp/dz.
        
        Return dFp/dz.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            z-derivative of angle component of field.
        """
        return self.dFpDz

    def getdFzDr(self):
        """Return dFz/dr.
        
        Return dFz/dr.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            r-derivative of z-component of field.
        """
        return self.dFzDr

    def getdFzDp(self):
        """Return dFz/dp.
        
        Return dFz/dp.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            Angle derivative of z-component of field.
        """
        return self.dFzDp

    def getdFzDz(self):
        """Return dFz/dz.
        
        Return dFz/dz.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            z-derivative of z-component of field.
        """
        return self.dFzDz


class DifferentiableCylindricalVectorField(CylindricalVectorField):
    """A differentiable vector field in cylindrical coordinates.

    Represents the 9 spatial derivatives of a VectorField in cylindrical
    coordinates.
    """
