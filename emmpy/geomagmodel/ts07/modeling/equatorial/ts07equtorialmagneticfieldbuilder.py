"""Build an equatorial magnetic field for the TS07 model.

From the original Java code:

--------------------------------------------------------------------------
package geomagmodel.ts07.modeling.equatorial;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static crucible.core.math.CrucibleMath.pow;

import java.util.OptionalDouble;

import crucible.core.designpatterns.Builder;
import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
import geomagmodel.t01.deformation.PositionBender;
import geomagmodel.t01.deformation.TwistWarpFfunction;
import geomagmodel.ta15.modeling.deformation.DeformationI;
import geomagmodel.ta15.modeling.deformation.DeformationII;
import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
import geomagmodel.ts07.coefficientreader.Ts07EquatorialLinearCoefficients;
import geomagmodel.ts07.coefficientreader.Ts07EquatorialVariableCoefficients;
import magmodel.core.math.bessel.AlbertBesselFunctionEvaluator;
import magmodel.core.math.bessel.BesselFunctionEvaluator;
import magmodel.core.math.bessel.ColtBesselFunctionEvaluator;
import magmodel.core.math.expansions.CoefficientExpansion1D;
import magmodel.core.math.vectorfields.BasisVectorField;
import magmodel.core.math.vectorfields.BasisVectorFields;

/**
 * A {@link Builder} for constructing the TS07D empirical magnetic field model and derivatives of
 * the model.
 * 
 * @author Nicholas Sharp
 * @author G.K.Stephens
 *
 */
--------------------------------------------------------------------------

Classes
-------
Ts07EquatorialMagneticFieldBuilder
    Python version of the Ts07EquatorialMagneticFieldBuilder Java class
"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.designpatterns.builder import Builder


class Ts07EquatorialMagneticFieldBuilder(Builder):

    """Ts07EquatorialMagneticFieldBuilder

    Python version of the Ts07EquatorialMagneticFieldBuilder Java class
    
    Based on the original Java class:
    geomagmodel.ts07.modeling.equatorial.Ts07EquatorialMagneticFieldBuilder
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
                 shieldingCoeffs):
        """Initialize a new Ts07EquatorialMagneticFieldBuilder object.

        DESCRIBE

        Parameters
        ----------
        self : Ts07EquatorialMagneticFieldBuilder
            New object to initialize.
        dipoleTiltAngle : float
            DESCRIBE
        dynamicPressure : float
            DESCRIBE
        coeffs : Ts07EquatorialVariableCoefficients
            DESCRIBE
        tailLength : float
            DESCRIBE
        shieldingCoeffs : ThinCurrentSheetShieldingCoefficients
            DESCRIBE
        
        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            New object after initialization.
        """
        self.__dipoleTiltAngle = dipoleTiltAngle
        self.__dynamicPressure = dynamicPressure
        self.__coeffs = Preconditions.checkNotNull(coeffs)
        self.__tailLength = tailLength
        self.__shieldingCoeffs = Preconditions.checkNotNull(shieldingCoeffs)
        # Optional settings
        self.__bessel = None
        self.__includeShield = True
        self.__withTA15deformation = None

    def withAlbertBessel(self):
        """From the original Java code:

        ----------------------------
        /**
        * Use Jay Albert's faster Bessel function evaluator.
        * <p>
        * By default, the Bessel function evaluator will be Tsyganenko's, if this is set, Jay Albert's
        * Bessel function evaluator will be used instead. Jay Albert's implementation is about 4 times
        * faster, although it gives slightly different, but negligible, differences.
        *
        * @return this builder object
        */
        ----------------------------

        Parameters
        ----------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        
        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        """
        self.__bessel = AlbertBesselFunctionEvaluator(14)
        return self

    def withTA15deformation(self, bzIMF):
        """From the original Java code:

        ----------------------------
        /**
        * Use the TA15 bending and warping deformation instead of the T01 bending and warping
        * deformation.
        * <p>
        * By default, the model uses the T01 bending and warping deformation.
        * 
        * @param bzIMF the z-component of the IMF (interplanetary magnetic field) averaged over the
        *        previous 30 minutes
        * @return this builder object
        */
        ----------------------------

        Parameters
        ----------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        bzIMF : float
            The z-component of the IMF (interplanetary magnetic field)
            averaged over the previous 30 minutes.
        
        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        """
        self.__withTA15deformation = bzIMF
        return self

    def withEquatorialShielding(self):
        """From the original Java code:

        ----------------------------
        /**
        * By default, the equatorial shielding fields are evaluated, so if you haven't previously turned
        * them off, you won't need to call this.
        *
        * @return this builder object
        */
        ----------------------------

        Parameters
        ----------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        
        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        """
        self.__includeShield = True
        return self

    def withoutEquatorialShielding(self):
        """From the original Java code:

        ----------------------------
        /**
        * By default, the equatorial shielding fields are evaluated. Evaluating the shielding of the
        * equatorial fields, is about 90% of the computation time required of the model. Since they are
        * not needed in all applications, like computing the current density inside the magnetopause, the
        * option to turn them off can significantly speed up the code.
        *
        * @return this builder object
        */
        ----------------------------

        Parameters
        ----------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        
        Returns
        -------
        self : Ts07EquatorialMagneticFieldBuilder
            This object.
        """
        self.__includeShield = False
        return self
