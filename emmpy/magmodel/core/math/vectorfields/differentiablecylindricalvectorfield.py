"""A differentiable vector field in cylindrical coordinates."""


# import crucible.core.math.coords.CylindricalVector;
# import crucible.core.math.vectorfields.VectorField;

from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class Results:
    """The 9 spatial derivatives of a VectorField in cylindrical coordinates.

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
        """Build a new object.

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
        """Return the field value at the supplied location.

        return CylindricalVector f
        """
        return self.f

    def getdFrDr(self):
        """Return dFr/dr."""
        return self.dFrDr

    def getdFrDp(self):
        """Return dFr/dp."""
        return self.dFrDp

    def getdFrDz(self):
        """Return dFr/dz."""
        return self.dFrDz

    def getdFpDr(self):
        """Return dFp/dr."""
        return self.dFpDr

    def getdFpDp(self):
        """Return dFp/dp."""
        return self.dFpDp

    def getdFpDz(self):
        """Return dFp/dz."""
        return self.dFpDz

    def getdFzDr(self):
        """Return dFz/dr."""
        return self.dFzDr

    def getdFzDp(self):
        """Return dFz/dp."""
        return self.dFzDp

    def getdFzDz(self):
        """Return dFz/dz."""
        return self.dFzDz


class DifferentiableCylindricalVectorField(CylindricalVectorField):
    """A differentiable vector field in cylindrical coordinates.

    Represents the 9 spatial derivatives of a VectorField in cylindrical
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
        """Evaluate the field and derivatives at the given position.

        INTERFACE - DO NOT INVOKE

        param location CylindricalVector, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9 spatial derivatives
        """
        raise Exception
