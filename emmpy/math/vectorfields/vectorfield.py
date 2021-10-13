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
