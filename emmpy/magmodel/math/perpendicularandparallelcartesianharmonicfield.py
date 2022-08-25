"""Linear combination of perpendicular and parallel Cartesian harmonic fields.

Linear combination of perpendicular and parallel Cartesian harmonic fields.

Authors
-------
G.K. Stephens
Nicholas Sharp
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.math.rotations.axisandangle import AxisAndAngle

from emmpy.magmodel.math.alternatecartesianharmonicfield import (
    AlternateCartesianHarmonicField
)
from emmpy.magmodel.math.cartesianharmonicfield import (
    CartesianHarmonicField
)
from emmpy.magmodel.math.trigparity import EVEN, ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.math.vectorfields.basisvectorfields import (
    BasisVectorFields
)
from emmpy.math.coordinates.vectorijk import (
    VectorIJK, I, J, K
)
from emmpy.math.vectors.vector import Vector


class PerpendicularAndParallelCartesianHarmonicField(BasisVectorField):
    """Linear combination of perpendicular and parallel Cartesian fields.

    Represents the linear combination of a perpendicular and parallel
    Cartesian harmonic vector field.

    This is often useful because a VectorField can be decomposed into the sum
    of a vertical and horizontal vector field.

    This formulation has shown to be effective for representing the
    magnetopause currents that can be used to contain the magnetic field within
    the magnetosphere: e.g. Tsyganenko 1998].

    Attributes
    ----------
    perpendicularField : BasisVectorField
        The perpendicular field.
    parallelField : BasisVectorField
        The parallel field.
    """

    def __init__(self, perpendicularField, parallelField):
        """Initialize a new PerpendicularAndParallelCartesianHarmonicField object.

        Initialize a new PerpendicularAndParallelCartesianHarmonicField object.

        Parameters
        ----------
        perpendicularField : BasisVectorField
            The perpendicular field.
        parallelField : BasisVectorField
            The parallel field.
        """
        self.perpendicularField = perpendicularField
        self.parallelField = parallelField

    @staticmethod
    def createWithRotation(
        trigParityI, perpendicularTiltAngle, p, r, perpCoeffs,
        parallelTiltAngle, q, s, parrCoeffs
    ):
        """Create a field rotated about the y-axis.

        Described in detail in the appendix of Tsyganenko [1998].

        Parameters
        ----------
        trigParityI : TrigParity
            The TrigParity associated with the Y terms (odd=sine,
            even=cosine).
        perpendicularTiltAngle : float
            The angle (radians) to rotate the perpendicular field about
            the y-axis.
        p : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients p_i
        r : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients r_k.
        perpCoeffs : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients a_ik.
        parallelTiltAngle : float
            The angle (radians) to rotate the parallel field about the
            y-axis.
        q : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients q_i.
        s : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients s_k.
        parrCoeffs : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients b_ik.
        
        Returns
        -------
        papchf : PerpendicularAndParallelCartesianHarmonicField
            New field combining the input fields.
        """
        # Construct the unrotated fields.
        perpField = CartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, ODD)
        paraField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, EVEN)

        # The rotation matrices about Y axis.
        aaa1 = AxisAndAngle(J, -perpendicularTiltAngle)
        rmijk1 = RotationMatrixIJK()
        perpendicularRotation = aaa1.getRotation(rmijk1)
        aaa2 = AxisAndAngle(J, -parallelTiltAngle)
        rmijk2 = RotationMatrixIJK()
        parallelRotation = aaa2.getRotation(rmijk2)

        # Now rotate the fields.
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

        Parameters
        ----------
        trigParityI : TrigParity
            Parity associated with the Y terms (odd=sine, even=cosine).
        perpendicularTiltAngle : float
            The angle (radians) to rotate the perpendicular field about the
            y-axis.
        p : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients p_i.
        r : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients r_k.
        perpCoeffs : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients a_ik.
        parallelTiltAngle : float
            The angle to rotate the parallel field about the y-axis.
        q : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients q_i.
        s : CoefficientExpansion1D
            An expansion containing the nonlinear set of coefficients s_k.
        parrCoeffs : CoefficientExpansion2D
            An expansion containing the linear scaling coefficients b_ik.
        
        Returns
        -------
        papchf : PerpendicularAndParallelCartesianHarmonicField
            New harmonic field combining the inputs.
        """
        # Construct the unrotated fields.
        perpField = AlternateCartesianHarmonicField(
            p, r, perpCoeffs, trigParityI, ODD)
        paraField = CartesianHarmonicField(
            q, s, parrCoeffs, trigParityI, EVEN)

        # The rotation matrices about Y axis.
        aaa1 = AxisAndAngle(J, -perpendicularTiltAngle)
        rmijk1 = RotationMatrixIJK()
        perpendicularRotation = aaa1.getRotation(rmijk1)
        aaa2 = AxisAndAngle(J, -parallelTiltAngle)
        rmijk2 = RotationMatrixIJK()
        parallelRotation = aaa2.getRotation(rmijk2)

        # Now rotate the fields.
        rotatedPerpField = BasisVectorFields.rotate(
            perpField, perpendicularRotation)
        rotatedParaField = BasisVectorFields.rotate(
            paraField, parallelRotation)

        papchf = PerpendicularAndParallelCartesianHarmonicField(
            rotatedPerpField, rotatedParaField)
        return papchf

    def evaluate(self, location, buffer):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        buffer : VectorIJK
            Buffer to hold result.
        
        Returns
        -------
        buffer : VectorIJK
            Field evaluated at location.
        """
        perpField = self.perpendicularField.evaluate(location)
        parField = self.parallelField.evaluate(location, buffer)
        buffer[:] = perpField + parField
        return buffer

    def evaluateExpansion(self, location):
        """Evaluate the expansion.
        
        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        expansions : list of function
            Functions to represent the expansion components.
        """
        perpFields = self.perpendicularField.evaluateExpansion(location)
        parFields = self.parallelField.evaluateExpansion(location)
        expansions = []
        for f in perpFields:
            expansions.append(f)
        for f in parFields:
            expansions.append(f)
        return expansions
