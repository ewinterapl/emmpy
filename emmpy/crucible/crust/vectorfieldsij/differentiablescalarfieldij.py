"""An interface for a differentiable 2-D scalar field.

This class defines the interface for a differentiable scalar field in 2
dimensions.

Note
----
This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class DifferentiableScalarFieldIJ:
    """An interface for a differentiable 2-D scalar field.

    Represents the Cartesian spatial derivatives of a 2-D scalar field.
    """


def createConstant(constant):
    """Create a constant differentiable scalar field.

    Return a constant differentiable scalar field.

    Parameters
    ----------
    constant : float
        The constant field value.
    
    Returns
    -------
    dsfij : DifferentiableScalarFieldIJ
        The constant differentiable scalar field.
    """
    dsfij = DifferentiableScalarFieldIJ()
    dsfij.differentiateFDi = lambda location: 0
    dsfij.differentiateFDj = lambda location: 0
    dsfij.evaluate = lambda location: constant
    return dsfij
