"""A differentiable vector field in spherical coordinates."""


from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


class Results:
    """The 9 spatial derivatives of a VectorField in spherical coordinates.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephes
    """

    def __init__(self, f, dFrDr, dFrDt, dFrDp, dFtDr, dFtDt, dFtDp, dFpDr,
                 dFpDt, dFpDp):
        """Build a new object.

        param SphericalVector f
        param double dFrDr
        param double dFrDt
        param double dFrDp
        param double dFtDr
        param double dFtDt
        param double dFtDp
        pram double dFpDr
        param double dFpDt
        param double dFpDp
        """
        # SphericalVector f
        self.f = f
        # double dFrDr
        self.dFrDr = dFrDr
        # double dFrDt
        self.dFrDt = dFrDt
        # double dFrDp
        self.dFrDp = dFrDp
        # double dFtDr
        self.dFtDr = dFtDr
        # double dFtDt
        self.dFtDt = dFtDt
        # double dFtDp
        self.dFtDp = dFtDp
        # double dFpDr
        self.dFpDr = dFpDr
        # double dFpDt
        self.dFpDt = dFpDt
        # double dFpDp
        self.dFpDp = dFpDp

    def getF(self):
        """Return the field value.

        return SphericalVector
        """
        return self.f

    def getdFrDr(self):
        """Return dFr/dr."""
        return self.dFrDr

    def getdFrDt(self):
        """Return dFr/dt."""
        return self.dFrDt

    def getdFrDp(self):
        """Return dFr/dp."""
        return self.dFrDp

    def getdFtDr(self):
        """Return dFt/dr."""
        return self.dFtDr

    def getdFtDt(self):
        """Return dFt/dt."""
        return self.dFtDt

    def getdFtDp(self):
        """Return dFt/dp."""
        return self.dFtDp

    def getdFpDr(self):
        """Return dFp/dr."""
        return self.dFpDr

    def getdFpDt(self):
        """Return dFp/dt."""
        return self.dFpDt

    def getdFpDp(self):
        """Return dFp/dp."""
        return self.dFpDp

    def toString(self):
        """Convert the object to a string."""
        return (
            "Results [f=%s, dFrDr=%s, dFrDt=%s, dFrDp=%s, dFtDr=%s, dFtDt=%s, "
            "dFtDp=%s, dFpDr=%s, dFpDt=%s, dFpDp=%s]" %
            (self.f, self.dFrDr, self.dFrDt, self.dFrDp, self.dFtDr,
             self.dFtDt, self.dFtDp, self.dFpDr, self.dFpDt, self.dFpDp)
        )


class DifferentiableSphericalVectorField(SphericalVectorField):
    """A differentiable vector field in spherical coordinates.

    Represents the 9 spatial derivatives of a VectorField in spherical
    coordinates.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephens
    """

    def __init__(self):
        """Build a new object.

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def differentiate(self, location):
        """Evaluate the field and the derivatives at the given position.

        INTERFACE - DO NOT INVOKE

        param location SphericalVector, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9 spatial derivatives
        """
        raise Exception
