"""Trigonometric parity (sine and cosine).

Trigonometric parity (sine and cosine).

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)


class TrigParity(DifferentiableUnivariateFunction):
    """Trigonometric parity (sine and cosine).

    A representation of the odd and even parity that exists between the
    sine and cosine function. This type of parity often arises in Fourier
    series and boundary value problems. Solutions to boundary problems are
    often linear combinations of sines and cosines.

    EVEN: f(x) = cos(x), df/dx = -sin(x)
    ODD: f(x) = sin(x), df/dx = cos(x)

    Attributes
    ----------
    function : function
        A single-argument function returning float.
    """

    # The even trigonometric parity, the cosine function.
    EVEN = DifferentiableUnivariateFunction()
    EVEN.evaluate = cos
    EVEN.differentiate = lambda t: -sin(t)

    # The odd trigonometric parity, the sine function.
    ODD = DifferentiableUnivariateFunction()
    ODD.evaluate = sin
    ODD.differentiate = cos

    def __init__(self, function):
        """Initialize a new TrigParity object.
        
        Initialize a new TrigParity object.

        Parameters
        ----------
        function : function
            A single-argument function returning float.
        """
        self.function = function

    def evaluate(self, t):
        """Evaluate the function.
        
        Evaluate the function.
        
        Parameters
        ----------
        t : float
            Argument for function.
        
        Returns
        -------
        result : float
            Result of function(t).
        """
        return self.function.evaluate(t)

    def differentiate(self, t):
        """Evaluate the function derivative.
        
        Evaluate the function derivative.

        Parameters
        ----------
        t : float
            Argument for function.
        
        Returns
        -------
        result : float
            Result of derivative of function(t).
        """
        return self.function.differentiate(t)
