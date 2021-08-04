"""Linear combination of perpendicular and parallel Cartesian harmonic fields."""


from emmpy.math.vectors.vector import Vector
from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import (J, VectorIJK)
from emmpy.crucible.core.rotations.axisandangle import AxisAndAngle

from emmpy.magmodel.core.math.alternatecartesianharmonicfield import (
    AlternateCartesianHarmonicField
)
from emmpy.magmodel.core.math.cartesianharmonicfield import (
    CartesianHarmonicField
)
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)


class PerpendicularAndParallelCartesianHarmonicField(BasisVectorField):
    """Linear combination of perpendicular and parallel Cartesian fields.

    Represents the linear combination of a perpendicular and parallel
    Cartesian harmonic vector field.

    This is often useful because a VectorField can be decomposed into the sum
    of a vertical and horizontal vector field.

    This formulation has shown to be effective for representing the
    magnetopause currents that can be used to contain the magnetic field within
    the magnetosphere: e.g. Tsyganenko 1998].

    author G.K.Stephens
    author Nicholas Sharp
    """

    def __init__(self, perpendicularField, parallelField):
        """Build a new object.

        param BasisVectorField perpendicularField
        param BasisVectorField parallelField
        """
        self.perpendicularField = perpendicularField
        self.parallelField = parallelField

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

    @staticmethod
    def createWithRotation(
        trigParityI, perpendicularTiltAngle, p, r, perpCoeffs,
        parallelTiltAngle, q, s, parrCoeffs
    ):
        """Create a field rotated about the y-axis.

        Described in detail in the appendix of Tsyganenko [1998].

        param TrigParity trigParityI the TrigParity associated with the Y terms
        (odd=sine, even=cosine)
        param double perpendicularTiltAngle the angle to rotate the
        perpendicular field about the y-axis
        param CoefficientExpansion1D p an expansion containing the nonlinear
        set of coefficients p_i
        param CoefficientExpansion1D r an expansion containing the nonlinear
        set of coefficients r_k
        param CoefficientExpansion2D perpCoeffs an expansion containing the
        linear scaling coefficients a_ik
        param double parallelTiltAngle the angle to rotate the parallel field
        about the y-axis
        param CoefficientExpansion1D q an expansion containing the nonlinear
        set of coefficients q_i
        param CoefficientExpansion1D s an expansion containing the nonlinear
        set of coefficients s_k
        param CoefficientExpansion2D parrCoeffs an expansion containing the
        linear scaling coefficients b_ik
        return a newly constructed
        PerpendicularAndParallelCartesianHarmonicField
        """
        # construct the unrotated fields
        # BasisVectorField perpField, paraField
        perpField = CartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, TrigParity.ODD)
        paraField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, TrigParity.EVEN)

        # the rotation matrices about Y axis
        # AxisAndAngle aaa1, aaa2
        # RotationMatrixIJK rmijk1, rmijk2
        # UnwritableRotationMatrixIJK perpendicularRotation, parallelRotation
        # (same objects as rmijk1, rmijk2)
        aaa1 = AxisAndAngle(J, -perpendicularTiltAngle)
        rmijk1 = RotationMatrixIJK()
        perpendicularRotation = aaa1.getRotation(rmijk1)
        aaa2 = AxisAndAngle(J, -parallelTiltAngle)
        rmijk2 = RotationMatrixIJK()
        parallelRotation = aaa2.getRotation(rmijk2)

        # now rotate the fields
        # BasisVectorField rotatedPerpField, rotatedParaField
        rotatedPerpField = BasisVectorFields.rotate(
            perpField, perpendicularRotation)
        rotatedParaField = BasisVectorFields.rotate(
            paraField, parallelRotation)

        papchf = PerpendicularAndParallelCartesianHarmonicField(
            rotatedPerpField, rotatedParaField)
        return papchf

    @staticmethod
    def createWithRotationAndAlternate(
        trigParityI, perpendicularTiltAngle, p,
        r, perpCoeffs, parallelTiltAngle, q, s, parrCoeffs
    ):
        """Create a field rotated by an arbitrary angle about the y-axis.

        Described in detail in the appendix of Tsyganenko [1998].

        param TrigParity trigParityI the TrigParity associated with the Y terms
        (odd=sine, even=cosine)
        param double perpendicularTiltAngle the angle to rotate the
        perpendicular field about the y-axis
        param CoefficientExpansion1D p an expansion containing the nonlinear
        set of coefficients p_i
        param CoefficientExpansion1D r an expansion containing the nonlinear
        set of coefficients r_k
        param CoefficientExpansion2D perpCoeffs an expansion containing the
        linear scaling coefficients a_ik
        param double parallelTiltAngle the angle to rotate the parallel field
        about the y-axis
        param CoefficientExpansion1D q an expansion containing the nonlinear
        set of coefficients q_i
        param CoefficientExpansion1D s an expansion containing the nonlinear
        set of coefficients s_k
        param CoefficientExpansion2D parrCoeffs an expansion containing the
        linear scaling coefficients b_ik
        return a newly constructed
        PerpendicularAndParallelCartesianHarmonicField
        """
        # construct the unrotated fields
        # BasisVectorField perpField, paraField
        perpField = AlternateCartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, TrigParity.ODD)
        paraField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, TrigParity.EVEN)

        # the rotation matrices about Y axis
        # AxisAndAngle aaa1, aaa2
        # RotationMatrixIJK rmijk1, rmijk2
        # UnwritableRotationMatrixIJK perpendicularRotation, parallelRotation
        # (same objects as rmijk1, rmijk2)
        aaa1 = AxisAndAngle(J, -perpendicularTiltAngle)
        rmijk1 = RotationMatrixIJK()
        perpendicularRotation = aaa1.getRotation(rmijk1)
        aaa2 = AxisAndAngle(J, -parallelTiltAngle)
        rmijk2 = RotationMatrixIJK()
        parallelRotation = aaa2.getRotation(rmijk2)

        # now rotate the fields
        # BasisVectorField rotatedPerpField, rotatedParaField
        rotatedPerpField = BasisVectorFields.rotate(
            perpField, perpendicularRotation)
        rotatedParaField = BasisVectorFields.rotate(
            paraField, parallelRotation)

        papchf = PerpendicularAndParallelCartesianHarmonicField(
            rotatedPerpField, rotatedParaField)
        return papchf

    def evaluate(self, location, buffer):
        """Evaluate the field.

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK buffer
        """
        # VectorIJK perpField, parField
        perpField = self.perpendicularField.evaluate(location)
        parField = self.parallelField.evaluate(location, buffer)
        vectorSum = VectorIJK()
        vectorSum[:] = perpField + parField
        buffer[:] = vectorSum
        return buffer

    def evaluateExpansion(self, location):
        """Evaluate the expansion."""
        perpFields = self.perpendicularField.evaluateExpansion(location)
        parFields = self.parallelField.evaluateExpansion(location)
        expansions = []
        for f in perpFields:
            expansions.append(f)
        for f in parFields:
            expansions.append(f)
        return expansions

    # def getNumberOfBasisFunctions(self):
    #     return (self.perpendicularField.getNumberOfBasisFunctions()
    #             + self.parallelField.getNumberOfBasisFunctions())

    # def getPerpendicularField(self):
    #     """return the perpendicular field"""
    #     return self.perpendicularField

    # def getParallelField(self):
    #     """return the parallel field"""
    #     return self.parallelField
