"""emmpy.magmodel.core.math.vectorfields.basisvectorfields"""


# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
#     UnwritableVectorIJK
# )
# from emmpy.crucible.core.math.vectorspace.vectorijk import (
#     VectorIJK
# )
# from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
#     BasisVectorField
# )


class BasisVectorFields:
    """A class containing utility methods for manipulating BasisVectorField
    objects.

    author G.K.Stephens
    """
    pass

    # @staticmethod
    # def asBasisField(field):
    #     bvf = BasisVectorField()
    #     bvf.evaluateExpansion = (
    #         lambda location, buffer: field.evaluate(location)
    #     )
    #     bvf.getNumberOfBasisFunctions = lambda my_self: 1
    #     return bvf

    # @staticmethod
    # def scaleLocation(field, scaleFactor):
    #     """Creates a vector field by scaling the input location vector of the
    #     supplied vector field.

    #     @param field a vector field
    #     @param scaleFactor a value to scale the location vector
    #     @return a newly created vector field that scales the input location
    #     vector (location*scaleFactor )
    #     """
    #     bvf = BasisVectorField()
    #     bvf.evaluate = (
    #         lambda my_self, location, buffer:
    #         field.evaluate(UnwritableVectorIJK(scaleFactor, location), buffer)
    #     )
    #     bvf.evaluateExpansion = (
    #         lambda my_self, location:
    #         field.evaluateExpansion(UnwritableVectorIJK(scaleFactor, location))
    #     )
    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: field.getNumberOfBasisFunctions()
    #     )
    #     return bvf

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

    # @staticmethod
    # def concatAll(fields):
    #     """Concatenates multiple BasisVectorFields into a single
    #     BasisVectorField

    #     Note, this is different from add(BasisVectorField, BasisVectorField)

    #     @param a a BasisVectorField
    #     @param b another BasisVectorField
    #     @return a newly constructed BasisVectorField
    #     """
    #     bvf = BasisVectorField()

    #     def my_evaluateExpansion(location):
    #         result = []
    #         for field in fields:
    #             result.extend(field.evaluateExpansion(location))
    #         return result
    #     bvf.evaluateExpansion = my_evaluateExpansion
    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: sum([field.getNumberOfBasisFunctions()
    #                             for field in fields])
    #     )

    #     def my_toString(my_self):
    #         s = ""
    #         for field in fields:
    #             s += field.toString()
    #             s += " "
    #         return s
    #     bvf.toString = my_toString
    #     return bvf

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

    # @staticmethod
    # def expandCoefficients2(field, coeffs, moreCoeffs):
    #     """Expands the supplied BasisVectorField

    #     Note: no checking is performed to ensure consistency

    #     @param field a {@link BasisVectorField}
    #     @param coeffs
    #     @param moreCoeffs
    #     @return
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
    #         # get the lower bound index for the coefficients, we have to assume
    #         # that this is the same for all the other sets of coefficients
    #         expansionIndex = coeffs.getLowerBoundIndex()
    #         # Now, loop through the coefficients
    #         for expansion in expansions:
    #             scaledExpansions.append(
    #                 expansion.createScaled(
    #                     coeffs.getCoefficient(expansionIndex)
    #                 )
    #             )
    #             expansionIndex += 1
    #         for c in moreCoeffs:
    #             expansionIndex = coeffs.getLowerBoundIndex()
    #             for expansion in expansions:
    #                 scaledExpansions.append(
    #                     expansion.createScaled(
    #                         c.getCoefficient(expansionIndex)
    #                     )
    #                 )
    #                 expansionIndex += 1
    #         return scaledExpansions.build()
    #     bvf.evaluateExpansion = my_evaluateExpansion

    #     return bvf

    # @staticmethod
    # def rotate(field, matrix):
    #     """Rotates"""
    #     bvf = BasisVectorField()

    #     def my_evaluate(my_self, location, buffer):
    #         # rotate the location
    #         rotated = matrix.mxv(location)
    #         # evaluate using the rotated vector
    #         field.evaluate(rotated, buffer)
    #         # rotate the field value back
    #         return matrix.mtxv(buffer, buffer)
    #     bvf.evaluate = my_evaluate

    #     bvf.getNumberOfBasisFunctions = (
    #         lambda my_self: field.getNumberOfBasisFunctions()
    #     )

    #     def my_evaluateExpansion(my_self, location):
    #         # rotate the location
    #         rotated = matrix.mxv(location)
    #         # evaluate using the rotated vector
    #         expansions = field.evaluateExpansion(rotated)
    #         # rotate the field value back
    #         rotatedExpansions = []
    #         for expansion in expansions:
    #             rotatedExpansions.append(matrix.mtxv(expansion))
    #         return rotatedExpansions
    #     bvf.evaluateExpansion = my_evaluateExpansion

    #     return bvf

    # @staticmethod
    # def filter(field, retainIfTrue, fillValue):
    #     """Creates a new basis vector field by filtering the supplied basis
    #     vector field using the supplied Predicate.

    #     If true, the value of the supplied field is returned, if false, the
    #     supplied fill value is returned.

    #     @param field a basis vector field to be filtered
    #     @param retainIfTrue a Predicate to be used as a filter when false is
    #     returned
    #     @param fillValue the value to return if the filter returns false
    #     @return a newly created basis vector field that is a filtered view of
    #     the supplied field
    #     """
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
