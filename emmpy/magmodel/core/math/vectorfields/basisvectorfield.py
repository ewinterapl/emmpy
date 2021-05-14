"""emmpy.magmodel.core.math.vectorfields.basisvectorfield

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class BasisVectorField(VectorField):
    """An interface that represents a VectorField that can decomposed into a
    linear expansion of vector fields.

    returns the results of the vector field expansion in an ImmutableList.

    The coefficients a_i are considered an implementation detail.

    author G.K.Stephens
    """

    def __init__(self):
        pass

    def evaluate(self, location, buffer):
        basisVectors = self.evaluateExpansion(location, buffer)
        fx = 0.0
        fy = 0.0
        fz = 0.0
        for basisVector in basisVectors:
            fx += basisVector.getI()
            fy += basisVector.getJ()
            fz += basisVector.getK()
        return buffer.setTo(fx, fy, fz)

    def evaluateExpansion(self, location):
        """Evaluate the field expansion at the given position, and returns an
        ImmutableList of the results of each individual field in the expansion

        param location VectorIJK, often location
        return the result of evaluating each of the Basis functions VectorField
        for the given location as an ImmutableList
        throws FunctionEvaluationException if the function cannot perform the
        evaluation
        """
        raise Exception

    # def getNumberOfBasisFunctions(self):
    #     """return the number of individual vector fields in the expansion"""
    #     raise Exception
