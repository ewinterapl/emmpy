"""emmpy.magmodel.core.math.vectorfields.differentiablecylindricalvectorfield"""


# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.vectorfields.VectorField;

from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class Results:
    """Represents the 9 spatial derivatives of a VectorField in cylindrical
    coordinates.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephes
    """

    # private final CylindricalVector f;
    # private final double dFrDr;
    # private final double dFrDp;
    # private final double dFrDz;
    # private final double dFpDr;
    # private final double dFpDp;
    # private final double dFpDz;
    # private final double dFzDr;
    # private final double dFzDp;
    # private final double dFzDz;

    def __init__(self, f, dFrDr, dFrDp, dFrDz, dFpDr, dFpDp, dFpDz, dFzDr,
                 dFzDp, dFzDz):
        """Constructor

        param CylindricalVector f
        param double dFrDr
        param double dFrDp
        param double dFrDz
        param double dFpDr
        param double dFpDp
        param double dFpDz
        param double dFzDr
        param double dFzDp
        param double dFzDz
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
        """return the value of the CylindricalVectorField evaluated at the
        supplied location

        return CylindricalVector f
        """
        return self.f

    def getdFrDr(self):
        """return the partial derivative of the radial component of the field
        with respect to the radius evaluated at the supplied location as a
        double"""
        return self.dFrDr

    def getdFrDp(self):
        """return the partial derivative of the radial component of the field
        with respect to the longitude evaluated at the supplied location as a
        double"""
        return self.dFrDp

    def getdFrDz(self):
        """return the partial derivative of the radial component of the field
        with respect to the height evaluated at the supplied location as a
        double"""
        return self.dFrDz

    def getdFpDr(self):
        """return the partial derivative of the longitude component of the
        field with respect to the radius evaluated at the supplied location
        as a double"""
        return self.dFpDr

    def getdFpDp(self):
        """return the partial derivative of the longitude component of the
        field with respect to the longitude evaluated at the supplied location
        as a double
        """
        return self.dFpDp

    def getdFpDz(self):
        """return the partial derivative of the longitude component of the
        field with respect to the height evaluated at the supplied location
        as a double"""
        return self.dFpDz

    def getdFzDr(self):
        """return the partial derivative of the height component of the field
        with respect to the radius evaluated at the supplied location as a
        double"""
        return self.dFzDr

    def getdFzDp(self):
        """return the partial derivative of the height component of the field
        with respect to the longitude evaluated at the supplied location as a
        double"""
        return self.dFzDp

    def getdFzDz(self):
        """return the partial derivative of the height component of the field
        with respect to the height evaluated at the supplied location as a
        double"""
        return self.dFzDz


class DifferentiableCylindricalVectorField(CylindricalVectorField):
    """Represents the 9 spatial derivatives of a VectorField in cylindrical
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
        in cylindrical coordinates

        INTERFACE - DO NOT INVOKE

        param location CylindricalVector, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9 spatial derivatives
        """
        raise Exception

