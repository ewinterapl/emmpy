"""emmpy.magmodel.core.math.perpendicularandparallelcartesianharmonicfield"""


# from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
# from emmpy.crucible.core.rotations.axisandangle import AxisAndAngle
# from emmpy.magmodel.core.math.alternatecartesianharmonicfield import (
#     AlternateCartesianHarmonicField
# )
# from emmpy.magmodel.core.math.cartesianharmonicfield import (
#     CartesianHarmonicField
# )
# from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
# from emmpy.magmodel.core.math.vectorfields.basisvectorfields import (
#     BasisVectorFields
# )
# from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
#     RotationMatrixIJK
# )


class PerpendicularAndParallelCartesianHarmonicField(BasisVectorField):
    """Represents the linear combination of a perpendicular and parallel
    Cartesian harmonic vector field.

    This is often useful because a VectorField can be decomposed into the sum
    of a vertical and horizontal vector field.

    This formulation has shown to be effective for representing the
    magnetopause currents that can be used to contain the magnetic field within
    the magnetosphere: e.g. Tsyganenko 1998].

    author G.K.Stephens
    author Nicholas Sharp
    """
    pass

    # def __init__(self, perpendicularField, parallelField):
    #     """Constructor"""
    #     self.perpendicularField = perpendicularField
    #     self.parallelField = parallelField

    # @staticmethod
    # def create(trigParityI, p, r, perpCoeffs, q, s, parrCoeffs):
    #     """Creates a PerpendicularAndParallelCartesianHarmonicField

    #     param trigParityI the TrigParity associated with the Y terms
    #     (odd=sine, even=cosine)
    #     param p an expansion containing the nonlinear set of coefficients p_i
    #     param r an expansion containing the nonlinear set of coefficients r_k
    #     param perpCoeffs an expansion containing the linear scaling
    #     coefficients a_ik
    #     param q an expansion containing the nonlinear set of coefficients q_i
    #     param s an expansion containing the nonlinear set of coefficients s_k
    #     param parrCoeffs an expansion containing the linear scaling
    #     coefficients b_ik
    #     return a newly constructed
    #     PerpendicularAndParallelCartesianHarmonicField
    #     """
    #     perpendicularVectorField = CartesianHarmonicField(
    #         p, r, perpCoeffs, trigParityI, TrigParity.ODD)
    #     parallelDipoleShieldingField = CartesianHarmonicField(
    #         q, s, parrCoeffs, trigParityI, TrigParity.EVEN)
    #     return PerpendicularAndParallelCartesianHarmonicField(
    #         perpendicularVectorField, parallelDipoleShieldingField)

    # @staticmethod
    # def createWithRotation(trigParityI, perpendicularTiltAngle, p, r,
    #                        perpCoeffs, parallelTiltAngle, q, s, parrCoeffs):
    #     """Creates a PerpendicularAndParallelCartesianHarmonicField where each
    #     field is rotated by an arbitrary angle about the y-axis

    #     Described in detail in the appendix of Tsyganenko [1998].

    #     param trigParityI the TrigParity associated with the Y terms
    #     (odd=sine, even=cosine)
    #     param perpendicularTiltAngle the angle to rotate the perpendicular
    #     field about the y-axis
    #     param p an expansion containing the nonlinear set of coefficients p_i
    #     param r an expansion containing the nonlinear set of coefficients r_k
    #     param perpCoeffs an expansion containing the linear scaling
    #     coefficients a_ik
    #     param parallelTiltAngle the angle to rotate the parallel field about
    #     the y-axis
    #     param q an expansion containing the nonlinear set of coefficients q_i
    #     param s an expansion containing the nonlinear set of coefficients s_k
    #     param parrCoeffs an expansion containing the linear scaling
    #     coefficients b_ik
    #     return a newly constructed
    #     PerpendicularAndParallelCartesianHarmonicField
    #     """
    #     # construct the unrotated fields
    #     perpField = CartesianHarmonicField(
    #         p, r, perpCoeffs, trigParityI, TrigParity.ODD)
    #     paraField = CartesianHarmonicField(
    #         q, s, parrCoeffs, trigParityI, TrigParity.EVEN)

    #     # the rotation matrices about Y axis
    #     perpendicularRotation = AxisAndAngle(
    #         VectorIJK.J,
    #         -perpendicularTiltAngle).getRotation(RotationMatrixIJK())
    #     parallelRotation = AxisAndAngle(
    #         VectorIJK.J,
    #         -parallelTiltAngle).getRotation(RotationMatrixIJK())

    #     # now rotate the fields
    #     rotatedPerpField = BasisVectorFields.rotate(perpField,
    #                                                 perpendicularRotation)
    #     rotatedParaField = BasisVectorFields.rotate(paraField,
    #                                                 parallelRotation)

    #     return PerpendicularAndParallelCartesianHarmonicField(
    #         rotatedPerpField, rotatedParaField)

    @staticmethod
    def createWithRotationAndAlternate(
        trigParityI, perpendicularTiltAngle, p,
        r, perpCoeffs, parallelTiltAngle, q, s, parrCoeffs):
        """Creates a PerpendicularAndParallelCartesianHarmonicField where each
        field is rotated by an arbitrary angle about the y-axis

        Described in detail in the appendix of Tsyganenko [1998].

        param trigParityI the {@link TrigParity} associated with the Y terms
        (odd=sine, even=cosine)
        param perpendicularTiltAngle the angle to rotate the perpendicular
        field about the y-axis
        param p an expansion containing the nonlinear set of coefficients p_i
        param r an expansion containing the nonlinear set of coefficients r_k
        param perpCoeffs an expansion containing the linear scaling
        coefficients a_ik
        param parallelTiltAngle the angle to rotate the parallel field about
        the y-axis
        param q an expansion containing the nonlinear set of coefficients q)i
        param s an expansion containing the nonlinear set of coefficients s_k
        param parrCoeffs an expansion containing the linear scaling
        coefficients b_ik
        return a newly constructed
        PerpendicularAndParallelCartesianHarmonicField
        """
        pass
    #     # construct the unrotated fields
    #     perpField = AlternateCartesianHarmonicField(
    #         p, r, perpCoeffs, trigParityI, TrigParity.ODD)
    #     paraField = CartesianHarmonicField(
    #         q, s, parrCoeffs, trigParityI, TrigParity.EVEN)

    #     # the rotation matrices about Y axis
    #     perpendicularRotation = AxisAndAngle(
    #         VectorIJK.J,
    #         -perpendicularTiltAngle).getRotation(RotationMatrixIJK())
    #     parallelRotation = AxisAndAngle(
    #         VectorIJK.J,
    #         -parallelTiltAngle).getRotation(RotationMatrixIJK())

    #     # now rotate the fields
    #     rotatedPerpField = BasisVectorFields.rotate(
    #         perpField, perpendicularRotation)
    #     rotatedParaField = BasisVectorFields.rotate(
    #         paraField, parallelRotation)

    #     return PerpendicularAndParallelCartesianHarmonicField(
    #         rotatedPerpField, rotatedParaField)

    # def evaluate(self, location, buffer):
    #     perpField = self.perpendicularField.evaluate(location)
    #     parField = self.parallelField.evaluate(location, buffer)
    #     VectorIJK.add(perpField, parField, buffer)
    #     return buffer

    # def evaluateExpansion(self, location):
    #     perpFields = self.perpendicularField.evaluateExpansion(location)
    #     parFields = self.parallelField.evaluateExpansion(location)
    #     expansions = []
    #     for f in perpFields:
    #         expansions.append(f)
    #     for f in parFields:
    #         expansions.append(f)
    #     return expansions

    # def getNumberOfBasisFunctions(self):
    #     return (self.perpendicularField.getNumberOfBasisFunctions()
    #             + self.parallelField.getNumberOfBasisFunctions())

    # def getPerpendicularField(self):
    #     """return the perpendicular field"""
    #     return self.perpendicularField

    # def getParallelField(self):
    #     """return the parallel field"""
    #     return self.parallelField
