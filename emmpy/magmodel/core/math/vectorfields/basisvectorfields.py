"""Utility functions for basis vector fields."""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class BasisVectorFields:
    """Utility functions for basis vector fields.

    A class containing utility methods for manipulating BasisVectorField
    objects.

    author G.K.Stephens
    """

    @staticmethod
    def asBasisField(field):
        """Create a BasisVectorField view of a vector field."""
        bvf = BasisVectorField()

        def my_evaluateExpansion(location):
            return [field.evaluate(location)]
        bvf.evaluateExpansion = my_evaluateExpansion
        bvf.getNumberOfBasisFunctions = lambda: 1
        return bvf

    @staticmethod
    def scaleLocation(field, scaleFactor):
        """Create a vector field with a scaled location.

        param BasisVectorField field a vector field
        param float scaleFactor a value to scale the location vector
        return BasisVectorField a newly created vector field that scales the
        input location vector (location*scaleFactor)
        """
        bvf = BasisVectorField()
        bvf.evaluate = (
            lambda location, buffer:
            field.evaluate(VectorIJK(scaleFactor, location), buffer)
        )
        bvf.evaluateExpansion = (
            lambda location:
            field.evaluateExpansion(VectorIJK(scaleFactor, location))
        )
        bvf.getNumberOfBasisFunctions = (
            lambda: field.getNumberOfBasisFunctions()
        )
        return bvf

    # @staticmethod
    # def concat(a, b):
    #     """Concatenates two BasisVectorFields into a single BasisVectorField.

    #     Note, this is different from add(BasisVectorField, BasisVectorField)

    #     @param a a BasisVectorField
    #     @param b another BasisVectorField
    #     @return a newly constructed BasisVectorField
    #     """
    #     bvf = BasisVectorField()
    #     bvf.evaluateExpansion = (
    #         lambda my_self, location:
    #         [a.evaluateExpansion(), b.evaluateExpansion()]
    #     )
    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: a.getNumberOfBasisFunctions() +
    #         b.getNumberOfBasisFunctions()
    #     )
    #     bvf.toString = lambda my_self: a.toString() + " + " + b.toString()
    #     return bvf

    @staticmethod
    def concatAll(fields):
        """Concatenate multiple BasisVectorFields.

        Note, this is different from add(BasisVectorField, BasisVectorField)

        param a a BasisVectorField
        param b another BasisVectorField
        return a newly constructed BasisVectorField
        """
        bvf = BasisVectorField()

        def my_evaluateExpansion(location):
            result = []
            for field in fields:
                # field is:
                # emmpy.magmodel.core.math.vectorfields.basisvectorfield.BasisVectorField
                # But evaluate() is a lambda from WHERE?
                e = field.evaluateExpansion(location)
                result.extend(e)
            return result
        bvf.evaluateExpansion = my_evaluateExpansion
        bvf.getNumberOfBasisFunctions = (
            lambda my_self: sum([field.getNumberOfBasisFunctions()
                                for field in fields])
        )

        def my_toString():
            s = ""
            for field in fields:
                s += field.toString()
                s += " "
            return s
        bvf.toString = my_toString
        return bvf

    # @staticmethod
    # def add(a, b):
    #     """Adds two BasisVectorFields into a single BasisVectorField

    #     Note, this is different from concat(BasisVectorField, BasisVectorField)

    #     @param a a BasisVectorField
    #     @param b another BasisVectorField
    #     @return a newly constructed BasisVectorField
    #     """
    #     Preconditions.checkArgument(
    #         a.getNumberOfBasisFunctions() == b.getNumberOfBasisFunctions(),
    #         "Both basis vector fields must have the same number of basis"
    #         " functions, field a had %s while field b had %s " %
    #         (a.getNumberOfBasisFunctions(), b.getNumberOfBasisFunctions())
    #     )
    #     bvf = BasisVectorField()

    #     def my_evaluateExpansion(my_self, location):
    #         aResults = a.evaluateExpansion(location)
    #         bResults = b.evaluateExpansion(location)
    #         results = [
    #             UnwritableVectorIJK.copyOf(VectorIJK.add(aResults.get(i),
    #                                                      bResults.get(i)))
    #             for i in range(my_self.getNumberOfBasisFunctions())
    #         ]
    #         return results
    #     bvf.evaluateExpansion = my_evaluateExpansion

    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: a.getNumberOfBasisFunctions()
    #     )
    #     return bvf

    # @staticmethod
    # def expandCoefficients(field, coeffs, moreCoeffs):
    #     """Expands the supplied BasisVectorField via:

    #     Note: no checking is performed to ensure consistency

    #     @param field a {@link BasisVectorField}
    #     """
    #     bvf = BasisVectorField()
    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self:
    #         field.getNumberOfBasisFunctions()*(1 + len(moreCoeffs))
    #     )

    #     def my_evaluateExpansion(my_self, location):
    #         # evaluate the supplied basis function expansion
    #         expansions = field.evaluateExpansion(location)
    #         scaledExpansions = []
    #         # get the lower bound index for the coefficients, we have to
    #         # assume that this is the same for all the other sets of
    #         # coefficients
    #         expansionIndex = coeffs.getLowerBoundIndex()
    #         # Now, loop through the coefficients
    #         for expansion in expansions:
    #             scaledExpansions.append(
    #                 expansion.createScaled(
    #                     coeffs.getCoefficient(expansionIndex)
    #                 )
    #             )
    #             for c in moreCoeffs:
    #                 scaledExpansions.append(
    #                     expansion.createScaled(
    #                         c.getCoefficient(expansionIndex)
    #                     )
    #                 )
    #             expansionIndex += 1
    #         return scaledExpansions
    #     bvf.evaluateExpansion = my_evaluateExpansion
    #     return bvf

    @staticmethod
    def expandCoefficients2(field, coeffs, moreCoeffs):
        """Expand the supplied BasisVectorField.

        Note: no checking is performed to ensure consistency

        param BasisVectorField field
        param CoefficientExpansion1D coeffs
        param [CoefficientExpansion1D] moreCoeffs
        return BasisVectorField
        """
        bvf = BasisVectorField()
        bvf.getNumberOfBasisFunctions = (
            lambda my_self:
            field.getNumberOfBasisFunctions()*(1 + len(moreCoeffs))
        )

        def my_evaluateExpansion(location):
            # evaluate the supplied basis function expansion
            # list of UnwritableVectorIJK
            expansions = field.evaluateExpansion(location)
            # list of UnwritableVectorIJK
            scaledExpansions = []
            # get the lower bound index for the coefficients, we have to assume
            # that this is the same for all the other sets of coefficients
            expansionIndex = coeffs.getLowerBoundIndex()
            # Now, loop through the coefficients
            for expansion in expansions:
                scaledExpansions.append(
                    expansion.createScaled(
                        coeffs.getCoefficient(expansionIndex)
                    )
                )
                expansionIndex += 1
            for c in moreCoeffs:
                expansionIndex = coeffs.getLowerBoundIndex()
                for expansion in expansions:
                    scaledExpansions.append(
                        expansion.createScaled(
                            c.getCoefficient(expansionIndex)
                        )
                    )
                    expansionIndex += 1
            return scaledExpansions
        bvf.evaluateExpansion = my_evaluateExpansion

        return bvf

    @staticmethod
    def rotate(field, matrix):
        """Rotate the field."""
        bvf = BasisVectorField()

        # def my_evaluate(location, buffer):
        def my_evaluate(*myargs):
            if len(myargs) == 1:
                (location,) = myargs
                buffer = VectorIJK()
            elif len(myargs) == 2:
                (location, buffer) = myargs
            else:
                raise Exception
            # rotate the location
            rotated = matrix.mxv(location)
            # evaluate using the rotated vector
            field.evaluate(rotated, buffer)
            # rotate the field value back
            return matrix.mtxv(buffer, buffer)
        bvf.evaluate = my_evaluate
        bvf.getNumberOfBasisFunctions = (
            lambda: field.getNumberOfBasisFunctions()
        )

        def my_evaluateExpansion(location):
            # rotate the location
            rotated = matrix.mxv(location)
            # evaluate using the rotated vector
            expansions = field.evaluateExpansion(rotated)
            # rotate the field value back
            rotatedExpansions = []
            for expansion in expansions:
                rotatedExpansions.append(matrix.mtxv(expansion))
            return rotatedExpansions
        bvf.evaluateExpansion = my_evaluateExpansion

        return bvf

    @staticmethod
    def filter(field, retainIfTrue, fillValue):
        """Create a new basis vector field by filtering.

        If true, the value of the supplied field is returned, if false, the
        supplied fill value is returned.

        @param field a basis vector field to be filtered
        @param retainIfTrue a Predicate to be used as a filter when false is
        returned
        @param fillValue the value to return if the filter returns false
        @return a newly created basis vector field that is a filtered view of
        the supplied field
        """
        raise Exception
    #     bvf = BasisVectorField()

    #     def my_evaluateExpansion(my_self, location):
    #         # if true return the supplied field expansion
    #         retain = retainIfTrue(location)
    #         if retain:
    #             return field.evaluateExpansion(location)
    #         # if false, construct a new list and fill it will the fill value,
    #         # and return it
    #         fillExpansion = []
    #         for i in range(my_self.getNumberOfBasisFunctions()):
    #             fillExpansion.append(fillValue)
    #         return fillExpansion
    #     bvf.evaluateExpansion = my_evaluateExpansion

    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: field.getNumberOfBasisFunctions()
    #     )

    #     return bvf
