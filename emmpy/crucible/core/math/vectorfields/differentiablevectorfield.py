"""emmpy.crucible.core.math.vectorfields.differentiablevectorfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class DifferentiableVectorField(VectorField):
    """Extends a VectorField by adding the 9 spatial derivatives of a in
    Cartesian coordinates.

    author G.K.Stephens
    """

    def __init__(self):
        """INTERFACE - DO NOT INSTANTIATE"""
        raise Exception

    def differentiateFiDi(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFjDi(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFkDi(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFiDj(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFjDj(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFkDj(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFiDk(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFjDk(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiateFkDk(self, location):
        """INTERFACE - DO NOT INVOKE"""
        raise Exception

    def differentiate(self, location):
        """INTERFACE - DO NOT INVOKE

        Evaluate the field and the spatial derivatives at the given position
        in Cartesian coordinates

        param location UnwritableVectorIJK, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9  spatial derivatives
        """
        raise Exception

    class Results:
        """Represents the 9 spatial derivatives of a VectorField in
        Cartesian coordinates.

        author G.K.Stephens
        """

        def __init__(self, f, dFxDx, dFxDy, dFxDz, dFyDx, dFyDy, dFyDz, dFzDx,
                     dFzDy, dFzDz):
            """Constructor"""
            self.f = f
            self.dFxDx = dFxDx
            self.dFxDy = dFxDy
            self.dFxDz = dFxDz
            self.dFyDx = dFyDx
            self.dFyDy = dFyDy
            self.dFyDz = dFyDz
            self.dFzDx = dFzDx
            self.dFzDy = dFzDy
            self.dFzDz = dFzDz

        def getF(self):
            """return the value of the UnwritableVectorIJK evaluated at the
            supplied location"""
            return self.f

        def getdFxDx(self):
            """return the partial derivative of the x-component of the field
            with respect to x evaluated at the supplied location"""
            return self.dFxDx

        def getdFxDy(self):
            """return the partial derivative of the x-component of the field
            with respect to y evaluated at the supplied location"""
            return self.dFxDy

        def getdFxDz(self):
            """return the partial derivative of the x-component of the field
            with respect to z evaluated at the supplied location"""
            return self.dFxDz

        def getdFyDx(self):
            """return the partial derivative of the y-component of the field
            with respect to x evaluated at the supplied location"""
            return self.dFyDx

        def getdFyDy(self):
            """return the partial derivative of the y-component of the field
            with respect to y evaluated at the supplied location"""
            return self.dFyDy

        def getdFyDz(self):
            """return the partial derivative of the y-component of the field
            with respect to z evaluated at the supplied location"""
            return self.dFyDz

        def getdFzDx(self):
            """return the partial derivative of the z-component of the field
            with respect to x evaluated at the supplied location"""
            return self.dFzDx

        def getdFzDy(self):
            """return the partial derivative of the z-component of the field
            with respect to y evaluated at the supplied location"""
            return self.dFzDy

        def getdFzDz(self):
            """return the partial derivative of the z-component of the field
            with respect to z evaluated at the supplied location"""
            return self.dFzDz
