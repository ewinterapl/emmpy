"""The value and derivatives of a 2-D scalar field.

This class defines a differentiable scalar field in 2 dimensions.
"""


class DifferentiableScalarFieldIJ:
    """The value and derivatives of a 2-D scalar field.

    This class defines a differentiable scalar field in 2 dimensions.

    Attributes
    ----------
    evaluate: function(Vector2D)->float
        Function to evaluate the scalar field at the specified position.

    differentiateFDi: function(Vector2D)->float
        Function to evaluate the first derivative with respect to the first
        coordinate of the scalar field at the specified position.

    differentiateFDi: function(Vector2D)->float
        Function to evaluate the first derivative with respect to the
        second coordinate of the scalar field at the specified position.
    """

    def __init__(self, evaluateFunction, iDerivativeFunction,
                 jDerivativeFunction):
        """Initialize a new DifferentiableScalarFieldIJ object.

        Initialize a new DifferentiableScalarFieldIJ object by setting the
        functions to use for evaluation and differentiation.

        Parameters
        ----------
        evaluateFunction: function(Vector2D)->float
            Function to evaluate the scalar field at the specified position.

        iDerivativeFunction: function(Vector2D)->float
            Function to evaluate the first derivative with respect to the first
            coordinate of the scalar field at the specified position.

        jDerivativeFunction: function(Vector2D)->float
            Function to evaluate the first derivative with respect to the
            second coordinate of the scalar field at the specified position.

        Returns
        -------
        None
        """
        self.evaluate = evaluateFunction
        self.differentiateFDi = iDerivativeFunction
        self.differentiateFDj = jDerivativeFunction

    @staticmethod
    def createConstant(constant):
        """Create a constant differentiable scalar field.

        Return a constant differentiable scalar field. The derivatives of the
        constant field are always 0.

        Parameters
        ----------
        constant : float
            The constant field value.
        
        Returns
        -------
        dsfij : DifferentiableScalarFieldIJ
            The constant differentiable 2-D scalar field.
        """
        evaluateFunction = lambda location: constant
        iDerivativeFunction = lambda location: 0
        jDerivativeFunction = lambda location: 0
        dsfij = DifferentiableScalarFieldIJ(
            evaluateFunction, iDerivativeFunction, jDerivativeFunction
        )
        return dsfij
