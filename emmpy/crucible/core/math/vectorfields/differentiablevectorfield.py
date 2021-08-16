"""A spatially differentiable vector field in a 3-D Cartesian space.

This class represents a spatially differentiable vector field in a
3-D Cartesian space. The required methods are for the various components
of the derivatives of the vector field components.

N.B. This class was created from a Java interface, and therefore most of
these methods will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class DifferentiableVectorField(VectorField):
    """A spatially differentiable vector field in a 3-D Cartesian space.

    This class represents a spatially differentiable vector field in a 3-D
    Cartesian space. The required methods are for the various components
    of the derivatives of the vector field components.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new DifferentiableVectorField object.
        
        Initialize a new DifferentiableVectorField object.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFiDi(self, location):
        """Compute dFi/dxi.
        
        Compute the derivative of the first vector component with respect
        to the first Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFjDi(self, location):
        """Compute dFj/dxi.
        
        Compute the derivative of the second vector component with respect
        to the first Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFkDi(self, location):
        """Compute dFk/dxi.
        
        Compute the derivative of the third vector component with respect
        to the first Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFiDj(self, location):
        """Compute dFi/dxj.
        
        Compute the derivative of the first vector component with respect
        to the second Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFjDj(self, location):
        """Compute dFj/dxj.
        
        Compute the derivative of the second vector component with respect
        to the second Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFkDj(self, location):
        """Compute dFk/dxj.
        
        Compute the derivative of the third vector component with respect
        to the second Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFiDk(self, location):
        """Compute dFi/dxk.
        
        Compute the derivative of the first vector component with respect
        to the third Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFjDk(self, location):
        """Compute dFj/dxk.
        
        Compute the derivative of the second vector component with respect
        to the third Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiateFkDk(self, location):
        """Compute dFk/dxk.
        
        Compute the derivative of the third vector component with respect
        to the third Cartesian coordinate.

        Parameters
        ---------
        location : Vector3D
            Location for the differentiation.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def differentiate(self, location):
        """Compute the field and derivatives at a location.

        Evaluate the field and the spatial derivatives at the given
        position in Cartesian coordinates

        Parameters
        ----------
        location : VectorIJK

        Returns
        -------
        results : Results
            Object containing the vector value of the function and the 9
            spatial derivatives of the vector components.
        
        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException


class Results:
    """Value and spatial derivatives of a 3-D Cartesian vector field.

    Attributes
    ----------
    f : VectorIJK
        Value of vector field at a specific location.
    dFxDx, dFxDy, dFxDz : float
        Gradient components of x-component of f
    dFyDx, dFyDy, dFyDz : float
        Gradient components of y-component of f
    dFzDx, dFzDy, dFzDz : float
        Gradient components of z-component of f
    """

    def __init__(self, f, dFxDx, dFxDy, dFxDz, dFyDx, dFyDy, dFyDz, dFzDx,
                 dFzDy, dFzDz):
        """Initialize a new Results object.

        Initialize a new Results object.

        Attributes
        ----------
        f : VectorIJK
            Value of vector field at a specific location.
        dFxDx, dFxDy, dFxDz : float
            Gradient components of x-component of f
        dFyDx, dFyDy, dFyDz : float
            Gradient components of y-component of f
        dFzDx, dFzDy, dFzDz : float
            Gradient components of z-component of f
        """
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
        """Return the vector field value.
        
        Return the vector field value.

        Parameters
        ----------
        None

        Returns
        -------
        self.f : VectorIJK
            Value of vector field.
        """
        return self.f

    def getdFxDx(self):
        """Return dFx/dx.
        
        Return the x-derivative of the x-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFxDx : float
            x-derivative of the x-component of the vector field value.
        """
        return self.dFxDx

    def getdFxDy(self):
        """Return dFx/dy.
        
        Return the y-derivative of the x-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFxDy : float
            y-derivative of the x-component of the vector field value.
        """
        return self.dFxDy

    def getdFxDz(self):
        """Return dFx/dz.
        
        Return the z-derivative of the x-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFxDz : float
            z-derivative of the x-component of the vector field value.
        """
        return self.dFxDz

    def getdFyDx(self):
        """Return dFy/dx.
        
        Return the x-derivative of the y-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFyDx : float
            x-derivative of the y-component of the vector field value.
        """
        return self.dFyDx

    def getdFyDy(self):
        """Return dFy/dy.
        
        Return the y-derivative of the y-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFyDy : float
            y-derivative of the y-component of the vector field value.
        """
        return self.dFyDy

    def getdFyDz(self):
        """Return dFy/dz.
        
        Return the z-derivative of the y-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFyDz : float
            z-derivative of the y-component of the vector field value.
        """
        return self.dFyDz

    def getdFzDx(self):
        """Return dFz/dx.
        
        Return the x-derivative of the z-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFzDx : float
            x-derivative of the z-component of the vector field value.
        """
        return self.dFzDx

    def getdFzDy(self):
        """Return dFz/dy.
        
        Return the y-derivative of the z-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFzDy : float
            y-derivative of the z-component of the vector field value.
        """
        return self.dFzDy

    def getdFzDz(self):
        """Return dFz/dz.
        
        Return the z-derivative of the z-component of the vector field
        value.

        Parameters
        ----------
        None

        Returns
        -------
        self.dFzDz : float
            z-derivative of the z-component of the vector field value.
        """
        return self.dFzDz
