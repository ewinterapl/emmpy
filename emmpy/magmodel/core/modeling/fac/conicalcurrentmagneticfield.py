"""emmpy.magmodel.core.modeling.fac.conicalcurrentmagneticfield"""


# import static crucible.core.math.CrucibleMath.sin;
# import crucible.core.math.coords.SphericalVector;
# import crucible.core.math.functions.DifferentiableUnivariateFunction;
# import magmodel.core.math.TrigParity;

from emmpy.magmodel.core.modeling.fac.tfunction import TFunction
from emmpy.magmodel.core.math.vectorfields.sphericalvectorfield import (
    SphericalVectorField
)


class ConicalCurrentMagneticField(SphericalVectorField):
    """Represents the magnetic field of an azimuthal harmonic of a finite
    thickness conical current sheet
    
    As described in "Methods for quantitative modeling of the magnetic field
    from Birkeland currents" by N. A. Tsyganenko. See eq. (16). The cone's axis
    is the +Z axis.

    The magnetic field is the curl of the following vector potential:
    see http://www.sciencedirect.com/science/article/pii/003206339190058I
    (Tsyganenko, 1990)

           SUBROUTINE ONE_CONE(A,X,Y,Z,BX,BY,BZ)
    c
    c  RETURNS FIELD COMPONENTS FOR A DEFORMED CONICAL CURRENT SYSTEM, FITTED TO A BIOSAVART FIELD
    c    BY SIM_14.FOR.  HERE ONLY THE NORTHERN CONE IS TAKEN INTO ACCOUNT.

    author G.K.Stephens
    """

    def __init__(self, tFunction, mode, trigParity):
        """Constructor

        param TFunction tFunction
        param int mode
        param TrigParity trigParity
        """
    #   ConicalCurrentMagneticField(TFunction tFunction, int mode, TrigParity trigParity) {
    #     super();
    #   private final DifferentiableUnivariateFunction tFunction;
    #     this.tFunction = tFunction;
    #     this.mode = mode;
    #   private final TrigParity trigParity;
    #     this.trigParity = trigParity;
    #   }

    #   /**
    #    * Creates a {@link ConicalCurrentMagneticField} where the current sheet is centered at theta0 and
    #    * has a half thickness of deltaTheta. The theta co-latitude dependence (theta) is determined by
    #    * the {@link TFunction}.
    #    * 
    #    * @param theta0 a polar angle (colatitude) that is the center of the conical current sheet
    #    * @param deltaTheta the half thickness of the conical current sheet
    #    * @param mode the mode of the harmonic (m)
    #    * @param trigParity the parity of the harmonic (EVEN for cosine and ODD for sine)
    #    * @return a newly constructed {@link ConicalCurrentMagneticField}
    #    */
    #   public static ConicalCurrentMagneticField create(double theta0, double deltaTheta, int mode,
    #       TrigParity trigParity) {
    #     return new ConicalCurrentMagneticField(TFunction.createFromDelta(theta0, deltaTheta, mode),
    #         mode, trigParity);
    #   }

    #   /**
    #    * Evaluates the field at the given position in the spherical coordinate system
    #    * 
    #    * @param location the location to evaluate the field
    #    * @return the result of the evaluation
    #    */
    #   @Override
    #   public SphericalVector evaluate(SphericalVector location) {
    #     /*
    #      * This is the curl of equation 16
    #      */
    #     double r = location.getRadius();
    #     double phi = location.getLongitude();
    #     double theta = location.getColatitude();
    #     double t = tFunction.evaluate(theta);
    #     double dt_dTheta = tFunction.differentiate(theta);
    #     // even or odd
    #     double sinMphi = trigParity.evaluate(mode * phi);
    #     double cosMphi = trigParity.differentiate(mode * phi);
    #     double br = 0.0;
    #     double bTheta = mode * t * cosMphi / (r * sin(theta));
    #     double bPhi = -dt_dTheta * sinMphi / r;
    #     return new SphericalVector(br, bTheta, bPhi);
    #   }
    # }
