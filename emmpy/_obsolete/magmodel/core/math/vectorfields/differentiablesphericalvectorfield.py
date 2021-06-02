"""emmp.magmodel.core.math.vectorfields.differentiablesphericalvectorfield"""


from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


class Results:
    """Represents the 9 spatial derivatives of a VectorField in spherical
    coordinates.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephes
    """

    def __init__(self, f, dFrDr, dFrDt, dFrDp, dFtDr, dFtDt, dFtDp, dFpDr,
                 dFpDt, dFpDp):
        """Constructor

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
        """return the value of the SphericalVectorField evaluated at the
        supplied location

        return SphericalVector
        """
        return self.f

    def getdFrDr(self):
        """return the partial derivative of the radial component of the field
        with respect to the radius evaluated at the supplied location

        return double
        """
        return self.dFrDr

    def getdFrDt(self):
        """return the partial derivative of the radial component of the field
        with respect to the co-latitude evaluated at the supplied location

        return double
        """
        return self.dFrDt

    def getdFrDp(self):
        """return the partial derivative of the radial component of the field
        with respect to the longitude evaluated at the supplied location

        return double
        """
        return self.dFrDp

    def getdFtDr(self):
        """return the partial derivative of the co-latitude component of the
        field with respect to the radius evaluated at the supplied location

        return double
        """
        return self.dFtDr

    def getdFtDt(self):
        """return the partial derivative of the co-latitude component of the
        field with respect to the co-latitude evaluated at the supplied
        location

        return double
        """
        return self.dFtDt

    def getdFtDp(self):
        """return the partial derivative of the co-latitude component of the
        field with respect to the longitude evaluated at the supplied location

        return double
        """
        return self.dFtDp

    def getdFpDr(self):
        """return the partial derivative of the longitude component of the
        field with respect to the radius evaluated at the supplied location

        return double
        """
        return self.dFpDr

    def getdFpDt(self):
        """return the partial derivative of the longitude component of the
        field with respect to the co-latitude evaluated at the supplied
        location

        return double
        """
        return self.dFpDt

    def getdFpDp(self):
        """return the partial derivative of the longitude component of the
        field with respect to the longitude evaluated at the supplied location

        return double
        """
        return self.dFpDp

    def toString(self):
      return (
          "Results [f=%s, dFrDr=%s, dFrDt=%s, dFrDp=%s, dFtDr=%s, dFtDt=%s, "
          "dFtDp=%s, dFpDr=%s, dFpDt=%s, dFpDp=%s]" %
          (self.f, self.dFrDr, self.dFrDt, self.dFrDp, self.dFtDr, self.dFtDt,
           self.dFtDp, self.dFpDr, self.dFpDt, self.dFpDp)
      )


class DifferentiableSphericalVectorField(SphericalVectorField):
    """Represents the 9 spatial derivatives of a VectorField in spherical
    coordinates.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephens
    """

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def differentiate(self, location):
        """Evaluate the field and the spatial derivatives at the given position
        in spherical coordinates

        INTERFACE - DO NOT INVOKE

        param location SphericalVector, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9 spatial derivatives
        """
        raise Exception

