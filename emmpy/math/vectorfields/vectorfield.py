"""A vector field in a space of arbitrary dimension.

This class represents a vector field in a space of arbitrary dimension.
A vector field is defined as a mapping from a vector position in the
field to a vector value in the field. The position and value vectors are
assumed to have the same dimensionality as the space.

Authors
-------
J. Vanderpool
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.vectorijk import VectorIJK


class VectorField:
    """A vector field in a space of arbitrary dimension.

    This class represents a vector field in a space of arbitrary dimension.
    A vector field is defined as a mapping from a vector position in the
    field to a vector value in the field. The position and value vectors are
    assumed to have the same dimensionality as the space.

    Attributes
    ----------
    None
    """

    def evaluate(self, position):
        """Evaluate the vector field at a position.

        This abstract method must be overridden in a subclass.

        Evaluate the vector field at the specified position in the vector
        space.

        Parameters
        ----------
        position : Vector
            The position for evaluation in the vector space.

        Returns
        -------
        value : Vector
            Value of vector field at the specified position.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException

def negate(vectorField):
    """Create the negation of a vector field.

    Create the negation of a vector field. The original field maintains
    its separate nature, and is only negated when this negated field is
    evaluated.

    This method works on any VectorField-based object in any coordinate
    system.

    Parameters
    ----------
    vectorField : VectorField
        The vector field to negate.
    
    Returns
    -------
    negation : VectorField
        A VectorField that computes the negation of the original field.
    """
    negation = VectorField()

    # This custom evaluate() method dynamically negates the original vector
    # field and stores the result in the buffer.
    def my_evaluate(location):
        buffer = VectorIJK()
        vectorField.evaluate(location, buffer)
        buffer[:] = -buffer
        return buffer

    negation.evaluate = my_evaluate
    return negation
