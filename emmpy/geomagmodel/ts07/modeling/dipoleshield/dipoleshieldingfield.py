"""emmpy.geomagmodel.ts07.modeling.dipoleshield.dipoleshieldingfield"""


from math import cos, sin

from emmpy.crucible.core.math.vectorfields.vectorfields import VectorFields
from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)
from emmpy.magmodel.core.math.perpendicularandparallelcartesianharmonicfield import (
    PerpendicularAndParallelCartesianHarmonicField
)
from emmpy.magmodel.core.math.trigparity import TrigParity


class DipoleShieldingField:
    """The shielding field for the Earth's dipole constructed from the
    combination of a parallel and a perpendicular 2x2x3 Cartesian Harmonic
    field.

    See Tsyganenko 2002, A model of the near magnetosphere with a dawn-dusk
    asymmetry 1. Mathematical structure Eq. 29 - 32.

    see Tsyganenko 1995, section 2.3:
    http://onlinelibrary.wiley.com/doi/10.1029/94JA03193/abstract
    Tsyganenko 1998, appendix:
    http://onlinelibrary.wiley.com/doi/10.1029/98JA02292/abstract
    Tsyganenko 2002, section 2.4.1
    http://onlinelibrary.wiley.com/doi/10.1029/2001JA000219/abstract

    SUBROUTINE  SHLCAR3X3(X,Y,Z,PS,BX,BY,BZ)
    C   THIS S/R RETURNS THE SHIELDING FIELD FOR THE EARTH'S DIPOLE,
    C   REPRESENTED BY  2x3x3=18 "CARTESIAN" HARMONICS, tilted with respect
    C   to the z=0 plane (see NB#4, p.74-74)
    C
    C - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    C  The 36 coefficients enter in pairs in the amplitudes of the "cartesian"
    c    harmonics (A(1)-A(36).
    c  The 14 nonlinear parameters (A(37)-A(50) are the scales Pi,Ri,Qi,and Si
    C   entering the arguments of exponents, sines, and cosines in each of the
    C   18 "Cartesian" harmonics  PLUS TWO TILT ANGLES FOR THE CARTESIAN
    C       HARMONICS (ONE FOR THE PSI=0 MODE AND ANOTHER FOR THE PSI=90 MODE)

    author Nicholas Sharp
    author G.K.Stephens
    """

    kappaPerp = .8385953499E-01  # Previously T1
    kappaParallel = .3477844929  # Previously T2

    # These coefficients were determined in Tsyganenko 2002-1 referenced above.
    p = CoefficientExpansions.createExpansionFromArray(
        [9.620648151, 6.082014949, 27.75216226], 1)
    r = CoefficientExpansions.createExpansionFromArray(
        [12.44199571, 5.122226936, 6.982039615], 1)
    q = CoefficientExpansions.createExpansionFromArray(
        [20.12149582, 6.150973118, 4.663639687], 1)
    s = CoefficientExpansions.createExpansionFromArray(
        [15.73319647, 2.303504968, 5.840511214], 1)
    a = CoefficientExpansions.createExpansionFromArray(
        [[-901.2327248, 817.6208321, -83.73539535],
         [336.8781402, -311.2947120, 31.94469304],
         [125.8739681, -235.4720434, 21.86305585]],
        1, 1)
    b = CoefficientExpansions.createExpansionFromArray(
        [[895.8011176, -845.5880889, 86.58542841],
         [-329.3619944, 308.6011161, -31.30824526],
         [-372.3384278, 286.7594095, -27.42344605]],
        1, 1)
    c = CoefficientExpansions.createExpansionFromArray(
        [[-150.4874688, 1.395023949, -56.85224007],
         [-43.48705106, 1.073551279, 12.21404266],
         [5.799964188, -1.044652977, 3.536082962]],
        1, 1)
    d = CoefficientExpansions.createExpansionFromArray(
        [[2.669338538, -.5540427503, 3.681827033],
         [5.103131905, -.6673083508, 4.177465543],
         [-.3977802319, .5703560010, -3.222069852]],
        1, 1)

    @staticmethod
    def create(dipoleTiltAngle, dynamicPressure):
        """Creates a new dipole shielding field.

        Note: this is a point of inconsistency with the Fortran code, in the
        Fortran this calculation is done in single precision. When the field
        values are very large, this can result in tenths of differences between
        the Java and the Fortran version of the model
        """
        pDynScale = pow(dynamicPressure/2, 0.155)
        perpCoeffs = CoefficientExpansions.add(
            DipoleShieldingField.a,
            CoefficientExpansions.scale(DipoleShieldingField.b,
                                        cos(dipoleTiltAngle)))
        parrCoeffs = CoefficientExpansions.add(
            CoefficientExpansions.scale(DipoleShieldingField.c,
                                        sin(dipoleTiltAngle)),
            CoefficientExpansions.scale(DipoleShieldingField.d,
                                        sin(2*dipoleTiltAngle)))
        ppchf = (
            PerpendicularAndParallelCartesianHarmonicField.
            createWithRotationAndAlternate(
                TrigParity.EVEN,
                dipoleTiltAngle*DipoleShieldingField.kappaPerp,
                CoefficientExpansions.invert(DipoleShieldingField.p),
                CoefficientExpansions.invert(DipoleShieldingField.r),
                perpCoeffs, dipoleTiltAngle*DipoleShieldingField.kappaParallel,
                CoefficientExpansions.invert(DipoleShieldingField.q),
                CoefficientExpansions.invert(DipoleShieldingField.s),
                parrCoeffs)
        )
        ppchf = (
            PerpendicularAndParallelCartesianHarmonicField.
            createWithRotationAndAlternate(
                TrigParity.EVEN,
                dipoleTiltAngle*DipoleShieldingField.kappaPerp,
                CoefficientExpansions.invert(DipoleShieldingField.p),
                CoefficientExpansions.invert(DipoleShieldingField.r),
                perpCoeffs,
                dipoleTiltAngle*DipoleShieldingField.kappaParallel,
                CoefficientExpansions.invert(DipoleShieldingField.q),
                CoefficientExpansions.invert(DipoleShieldingField.s),
                parrCoeffs)
        )
        pDynScale3 = pDynScale*pDynScale*pDynScale
        dipoleShieldingField = (VectorFields.scale(
            VectorFields.scaleLocation(ppchf, pDynScale), pDynScale3))

        return dipoleShieldingField

    @staticmethod
    def createScaled(dipoleTiltAngle, dynamicPressure, scaleFactor):
        """Creates a new dipole shielding field where the output vector is
        scaled by the supplied value."""
        return VectorFields.scale(
            DipoleShieldingField.create(dipoleTiltAngle, dynamicPressure),
            scaleFactor)
