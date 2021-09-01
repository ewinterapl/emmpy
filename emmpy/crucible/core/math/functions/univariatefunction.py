"""Abstract base class for single-variable functions.

N.B. This class was created from a Java interface, and therefore most of
these methods will raise exceptions if invoked.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class UnivariateFunction:
    """Abstract base class for single-variable functions.

    N.B. This class was created from a Java interface, and therefore most
    of these methods will raise exceptions if invoked.
    """

    def __init__(self):
        """Initialize a new CoordConverter object.

        Initialize a new CoordConverter object.

        Parameters
        ----------
        None

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

    def evaluate(self, t):
        """Evaluate the function at the specified value.

        Evaluate the function at the specified value.

        Parameters
        ----------
        t : float
            The value of interest.

        Returns
        -------
        result : float
            The value of the function at t.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
