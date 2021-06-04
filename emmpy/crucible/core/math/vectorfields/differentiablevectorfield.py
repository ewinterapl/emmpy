"""A differentiable 3-D vector field.

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class Results:
    """Value and derivatives of a differentiable 3-D vector field.

    author G.K.Stephens
    """

    def __init__(self, f, dFxDx, dFxDy, dFxDz, dFyDx, dFyDy, dFyDz, dFzDx,
                 dFzDy, dFzDz):
        """Build a new object."""
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
        """Return the field value at a location."""
        return self.f

    def getdFxDx(self):
        """Return dFx/dx at the supplied location."""
        return self.dFxDx

    def getdFxDy(self):
        """Return dFx/dy at the supplied location."""
        return self.dFxDy

    def getdFxDz(self):
        """Return dFx/dz at the supplied location."""
        return self.dFxDz

    def getdFyDx(self):
        """Return dFy/dx at the supplied location."""
        return self.dFyDx

    def getdFyDy(self):
        """Return dFy/dy at the supplied location."""
        return self.dFyDy

    def getdFyDz(self):
        """Return dFy/dz at the supplied location."""
        return self.dFyDz

    def getdFzDx(self):
        """Return dFz/dx at the supplied location."""
        return self.dFzDx

    def getdFzDy(self):
        """Return dFz/dy at the supplied location."""
        return self.dFzDy

    def getdFzDz(self):
        """Return dFz/dz at the supplied location."""
        return self.dFzDz


class DifferentiableVectorField(VectorField):
    """A differentiable 3-D vector field.

    author G.K.Stephens
    """

    def __init__(self):
        """Build a new object."""
        raise Exception

    def differentiateFiDi(self, location):
        """Compute dFi/dxi."""
        raise Exception

    def differentiateFjDi(self, location):
        """Compute dFj/dxi."""
        raise Exception

    def differentiateFkDi(self, location):
        """Compute dFk/dxi."""
        raise Exception

    def differentiateFiDj(self, location):
        """Compute dFi/dxj."""
        raise Exception

    def differentiateFjDj(self, location):
        """Compute dFj/dxj."""
        raise Exception

    def differentiateFkDj(self, location):
        """Compute dFk/dxj."""
        raise Exception

    def differentiateFiDk(self, location):
        """Compute dFi/dxk."""
        raise Exception

    def differentiateFjDk(self, location):
        """Compute dFj/dxk."""
        raise Exception

    def differentiateFkDk(self, location):
        """Compute dFk/dxk."""
        raise Exception

    def differentiate(self, location):
        """Compute the field and derivatives at a location.

        Evaluate the field and the spatial derivatives at the given position
        in Cartesian coordinates

        param location UnwritableVectorIJK, often location
        return the Results of the evaluation, which holds the value of the
        function and the 9  spatial derivatives
        """
        raise Exception
