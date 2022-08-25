"""Utility functions for basis vector fields.

Utility functions for basis vector fields.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class BasisVectorFields:
    """Utility functions for basis vector fields.

    A class containing utility methods for manipulating BasisVectorField
    objects.
    """

    @staticmethod
    def asBasisField(field):
        """Create a BasisVectorField view of a vector field.

        Create a BasisVectorField view of a vector field.

        Parameters
        ----------
        field : VectorField
            Vector field to convert to a basis vector field.
        
        Returns
        -------
        bvf : BasisVectorField
            Basis vector field version of input.
        """
        bvf = BasisVectorField()

        def my_evaluateExpansion(location):
            return [field.evaluate(location)]
        bvf.evaluateExpansion = my_evaluateExpansion
        bvf.getNumberOfBasisFunctions = lambda: 1
        return bvf

    @staticmethod
    def scaleLocation(field, scaleFactor):
        """Create a vector field with a scaled location.

        Create a vector field with a scaled location.

        Parameters
        ----------
        field : BasisVectorField
            Basis vector field to use for scaled inputs.
        scaleFactor : float
            Scale factor for input vectors.

        Returns
        -------
        bvf : BasisVectorField
            A wrapped basis vector field that scales input.
        """
        bvf = BasisVectorField()
        bvf.evaluate = (
            lambda location, buffer:
            field.evaluate(scaleFactor*VectorIJK(location), buffer)
        )
        bvf.evaluateExpansion = (
            lambda location:
            field.evaluateExpansion(scaleFactor*VectorIJK(location))
        )
        bvf.getNumberOfBasisFunctions = (
            lambda: field.getNumberOfBasisFunctions()
        )
        return bvf

    @staticmethod
    def concatAll(fields):
        """Concatenate multiple BasisVectorFields in a wrapper.

        Concatenate multiple BasisVectorFields in a wrapper.

        Note, this is different from add(BasisVectorField, BasisVectorField)

        Parameters
        ----------
        fields : list of BasisVectorField
            List of BasisVectorFields to concatenate.

        Returns
        -------
        bvf : BasisVectorField
            A wrapper which concatenates the supplied basis vector fields.
        """
        bvf = BasisVectorField()

        def my_evaluateExpansion(location):
            result = []
            for field in fields:
                e = field.evaluateExpansion(location)
                result.extend(e)
            return result
        bvf.evaluateExpansion = my_evaluateExpansion
        bvf.getNumberOfBasisFunctions = (
            lambda my_self: sum([field.getNumberOfBasisFunctions()
                                 for field in fields])
        )

        return bvf

    @staticmethod
    def expandCoefficients2(field, coeffs, moreCoeffs):
        """Expand the supplied BasisVectorField.

        Expand the supplied BasisVectorField.

        Note: no checking is performed to ensure consistency

        Parameters
        ----------
        field : BasisVectorField
            Basis vector field to evaluate.
        coeffs, moreCoeffs : CoefficientExpansion1D
            1st and 2nd sets of expansion coefficients.

        Returns
        -------
        bvf : BasisVectorField
            Expanded coefficients.
        """
        bvf = BasisVectorField()
        bvf.getNumberOfBasisFunctions = (
            lambda my_self:
            field.getNumberOfBasisFunctions()*(1 + len(moreCoeffs))
        )

        def my_evaluateExpansion(location):
            expansions = field.evaluateExpansion(location)
            scaledExpansions = []
            expansionIndex = 0
            for expansion in expansions:
                scaledExpansions.append(expansion*coeffs[expansionIndex])
                expansionIndex += 1
            for c in moreCoeffs:
                expansionIndex = 0
                for expansion in expansions:
                    scaledExpansions.append(expansion*c[expansionIndex])
                    expansionIndex += 1
            return scaledExpansions
        bvf.evaluateExpansion = my_evaluateExpansion

        return bvf

    @staticmethod
    def rotate(field, matrix):
        """Rotate the field.
        
        Rotate the field.
        
        Parameters
        ----------
        field : BasisVectorField
            Basis vector field to rotate.
        matrix : MatrixIJK
            Rotation matrix to apply to field.
        
        Returns
        -------
        bvf : BasisVectorField
            The rotated field.
        """
        bvf = BasisVectorField()

        def my_evaluate(*myargs):
            if len(myargs) == 1:
                (location,) = myargs
                buffer = VectorIJK()
            elif len(myargs) == 2:
                (location, buffer) = myargs
            else:
                raise Exception
            rotated = VectorIJK()
            rotated[:] = matrix.dot(location)
            field.evaluate(rotated, buffer)
            buffer[:] = matrix.T.dot(buffer)
            return buffer
        bvf.evaluate = my_evaluate
        bvf.getNumberOfBasisFunctions = (
            lambda: field.getNumberOfBasisFunctions()
        )

        def my_evaluateExpansion(location):
            rotated = matrix.mxv(location)
            expansions = field.evaluateExpansion(rotated)
            rotatedExpansions = []
            for expansion in expansions:
                rotatedExpansions.append(matrix.mtxv(expansion))
            return rotatedExpansions
        bvf.evaluateExpansion = my_evaluateExpansion

        return bvf
