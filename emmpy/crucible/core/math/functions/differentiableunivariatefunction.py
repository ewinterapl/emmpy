"""Abstract base class for differentiable single-variable functions.

N.B. This class was created from a Java interface, and therefore most of
these methods will raise exceptions if invoked.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.functions.univariatefunction import (
    UnivariateFunction
)
from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class DifferentiableUnivariateFunction(UnivariateFunction):
    """Abstract base class for differentiable single-variable functions.

    N.B. This class was created from a Java interface, and therefore most
    of these methods will raise exceptions if invoked.
    """

    def __init__(self):
        """Initialize a new DifferentiableUnivariateFunction object.

        Initialize a new DifferentiableUnivariateFunction object.

        This method is a stub to prevent the AbstractMethodException from
        the inherited __init__.

        Parameters
        ----------
        None
        """

    def differentiate(self, t):
        """Evaluate the derivative at the specified value.

        Evaluate the derivative at the specified value.

        Parameters
        ----------
        t : float
            The value of interest.

        Returns
        -------
        result : float
            The value of the derivative at t.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
