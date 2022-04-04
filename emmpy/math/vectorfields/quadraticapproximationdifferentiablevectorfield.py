"""A quadratic approximation of a differentiable vector field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# Import project modules.
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField, Results
)


class QuadraticApproximationDifferentiableVectorField(DifferentiableVectorField):
    """A quadratic approximation of a differentiable vector field.

    Attributes
    ----------
    field : VectorField
        Vector field to differentiate.
    deltaI, deltaJ, deltaK : float
        Differential distances along each dimension, for computing numerical
        derivatives.
    """

    def __init__(self, field, deltaI, deltaJ, deltaK):
        """Initialize a new object.

        Parameters
        ----------
        field : VectorField
            Vector field to differentiate.
        deltaI, deltaJ, deltaK : float
            Differential distances along each dimension, for computing
            numerical derivatives.

        Returns
        -------
        None
        """
        self.field = field
        self.deltaI = deltaI
        self.deltaJ = deltaJ
        self.deltaK = deltaK

    def differentiateFiDi(self, location):
        """Compute derivative of x-component of field wrt x.
        
        Compute derivative of x-component of field wrt x.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of x-component of field wrt x.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i + self.deltaI, j, k)
        sub = VectorIJK(i - self.deltaI, j, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaI*(v_add.i - v_sub.i)
        return d

    def differentiateFjDi(self, location):
        """Compute derivative of y-component of field wrt x.
        
        Compute derivative of y-component of field wrt x.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of y-component of field wrt x.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i + self.deltaI, j, k)
        sub = VectorIJK(i - self.deltaI, j, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaI*(v_add.j - v_sub.j)
        return d

    def differentiateFkDi(self, location):
        """Compute derivative of z-component of field wrt x.
        
        Compute derivative of z-component of field wrt x.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of z-component of field wrt x.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i + self.deltaI, j, k)
        sub = VectorIJK(i - self.deltaI, j, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaI*(v_add.k - v_sub.k)
        return d

    def differentiateFiDj(self, location):
        """Compute derivative of x-component of field wrt y.
        
        Compute derivative of x-component of field wrt y.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of x-component of field wrt y.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j + self.deltaJ, k)
        sub = VectorIJK(i, j - self.deltaJ, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaJ*(v_add.i - v_sub.i)
        return d

    def differentiateFjDj(self, location):
        """Compute derivative of y-component of field wrt y.
        
        Compute derivative of y-component of field wrt y.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of y-component of field wrt y.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j + self.deltaJ, k)
        sub = VectorIJK(i, j - self.deltaJ, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaJ*(v_add.j - v_sub.j)
        return d

    def differentiateFkDj(self, location):
        """Compute derivative of z-component of field wrt y.
        
        Compute derivative of z-component of field wrt y.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of z-component of field wrt y.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j + self.deltaJ, k)
        sub = VectorIJK(i, j - self.deltaJ, k)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaJ*(v_add.k - v_sub.k)
        return d

    def differentiateFiDk(self, location):
        """Compute derivative of x-component of field wrt z.
        
        Compute derivative of x-component of field wrt z.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of x-component of field wrt z.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j, k + self.deltaK)
        sub = VectorIJK(i, j, k - self.deltaK)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaK*(v_add.i - v_sub.i)
        return d

    def differentiateFjDk(self, location):
        """Compute derivative of y-component of field wrt z.
        
        Compute derivative of y-component of field wrt z.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of y-component of field wrt z.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j, k + self.deltaK)
        sub = VectorIJK(i, j, k - self.deltaK)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaK*(v_add.j - v_sub.j)
        return d

    def differentiateFkDk(self, location):
        """Compute derivative of z-component of field wrt z.
        
        Compute derivative of z-component of field wrt z.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate derivative.
        
        Returns
        -------
        d : float
            Derivative of z-component of field wrt z.
        """
        (i, j, k) = location[:]
        add = VectorIJK(i, j, k + self.deltaK)
        sub = VectorIJK(i, j, k - self.deltaK)
        v_add = self.field.evaluate(add)
        v_sub = self.field.evaluate(sub)
        d = 0.5/self.deltaK*(v_add.k - v_sub.k)
        return d

    def evaluate(self, location):
        """Compute the vector field value at location.
        
        Compute the vector field value at location.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate.
        
        Returns
        -------
        v : VectorIJK
            Vector field value at location.
        """
        v = self.field.evaluate(location)
        return v

    def differentiate(self, location):
        """Compute the field value and Jacobian at location.
        
        Compute the field value and Jacobian at location.
        
        Parameters
        ----------
        location : VectorIJK
            Location to compute Jacobian.
        
        Returns
        -------
        results : Results
            Field value and Jacobian at location.
        """
        (x, y, z) = location[...]

        f = self.field.evaluate(location)

        addX = VectorIJK(x + self.deltaI, y, z)
        subX = VectorIJK(x - self.deltaI, y, z)
        addY = VectorIJK(x, y + self.deltaJ, z)
        subY = VectorIJK(x, y - self.deltaJ, z)
        addZ = VectorIJK(x, y, z + self.deltaK)
        subZ = VectorIJK(x, y, z - self.deltaK)

        fieldAddX = self.field.evaluate(addX)
        fieldSubX = self.field.evaluate(subX)
        fieldAddY = self.field.evaluate(addY)
        fieldSubY = self.field.evaluate(subY)
        fieldAddZ = self.field.evaluate(addZ)
        fieldSubZ = self.field.evaluate(subZ)

        dFxDx = 0.5/self.deltaI*(fieldAddX.i - fieldSubX.i)
        dFyDx = 0.5/self.deltaI*(fieldAddX.j - fieldSubX.j)
        dFzDx = 0.5/self.deltaI*(fieldAddX.k - fieldSubX.k)
        dFxDy = 0.5/self.deltaJ*(fieldAddY.i - fieldSubY.i)
        dFyDy = 0.5/self.deltaJ*(fieldAddY.j - fieldSubY.j)
        dFzDy = 0.5/self.deltaJ*(fieldAddY.k - fieldSubY.k)
        dFxDz = 0.5/self.deltaK*(fieldAddZ.i - fieldSubZ.i)
        dFyDz = 0.5/self.deltaK*(fieldAddZ.j - fieldSubZ.j)
        dFzDz = 0.5/self.deltaK*(fieldAddZ.k - fieldSubZ.k)

        results = Results(f, dFxDx, dFxDy, dFxDz, dFyDx, dFyDy, dFyDz, dFzDx, dFzDy, dFzDz);
        return results
