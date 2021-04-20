"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetasymmetricexpansion"""


# import static com.google.common.base.Preconditions.checkNotNull;
# import static crucible.core.math.CrucibleMath.atan2;
# import static crucible.core.math.CrucibleMath.exp;
# import static crucible.core.math.CrucibleMath.sqrt;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJ;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField

class TailSheetAsymmetricExpansion(VectorField):
    """This is the odd and even type azimuthal symmetry part of the expansion
    of the solution of the magnetic field from a thin current sheet along the
    z=0 plane, from Tsyganenko and Sitnov 2007, eq. 16 and 17.

    The choice between odd or even is based on the provided TrigParity.

    SUBROUTINE TAILSHT_OE (M,X,Y,Z,BX,BY,BZ)

    @author G.K.Stephens
    """
    # public class TailSheetAsymmetricExpansion implements VectorField {

    #   private final double waveNumber;
    #   private final int azimuthalExpansionNumber;

    #   private final TrigParity trigParity;

    #   private final DifferentiableScalarFieldIJ currentSheetHalfThickness;

    #   private final BesselFunctionEvaluator bessel;

    #   /**
    #    * Constructor.
    #    * 
    #    * @param waveNumber the wave number of this expansion
    #    * @param azimuthalExpansionNumber the azimuthal expansion number
    #    * @param trigParity sine function is odd cosine is even
    #    * @param currentSheetHalfThickness a 2D scalar field representing the current sheet half
    #    *        thickness throughout the equatorial current system
    #    * @param bessel the Bessel function evaluator
    #    */
    #   public TailSheetAsymmetricExpansion(double waveNumber, int azimuthalExpansionNumber,
    #       TrigParity trigParity, DifferentiableScalarFieldIJ currentSheetHalfThickness,
    #       BesselFunctionEvaluator bessel) {
    #     super();
    #     this.waveNumber = waveNumber;
    #     this.azimuthalExpansionNumber = azimuthalExpansionNumber;
    #     // this.trigParity = checkNotNull(trigParity);
    #     this.trigParity = trigParity;
    #     // this.currentSheetHalfThickness = checkNotNull(currentSheetHalfThickness);
    #     this.currentSheetHalfThickness = currentSheetHalfThickness;
    #     // this.bessel = checkNotNull(bessel);
    #     this.bessel = bessel;
    #   }

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    #     int m = azimuthalExpansionNumber;

    #     double x = location.getI();
    #     double y = location.getJ();
    #     double z = location.getK();

    #     UnwritableVectorIJ locationIJ = new UnwritableVectorIJ(x, y);

    #     // get the current sheet half thickness
    #     double thick = currentSheetHalfThickness.evaluate(locationIJ);

    #     // now get the current sheet half thickness derivatives
    #     double dThickdx = currentSheetHalfThickness.differentiateFDi(locationIJ);
    #     double dThickdy = currentSheetHalfThickness.differentiateFDj(locationIJ);

    #     // convert to polar
    #     double rho = sqrt(x * x + y * y);

    #     // convert to polar
    #     double dThickdRho = (x * dThickdx + y * dThickdy) / rho;
    #     double dThickdPhi = -y * dThickdx + x * dThickdy;

    #     double cosPhi = x / rho;
    #     double sinPhi = y / rho;
    #     double phi = atan2(y, x);
    #     // introduce a finite thickness in z by replacing z with this value
    #     double zDist = sqrt(z * z + thick * thick);

    #     // sine if odd, -cosine if even
    #     double sinMPhi = trigParity.evaluate(m * phi);

    #     // cosine if odd, sine if even
    #     double cosMPhi = trigParity.differentiate(m * phi);

    #     double kn = waveNumber;

    #     double ex = exp(-kn * zDist);

    #     // calculate the bessel function
    #     double jK = bessel.besseljn(m, kn * rho);

    #     // calculate the derivative of the bessel function
    #     double jKDer = bessel.besseljn(m - 1, kn * rho) - m * jK / (kn * rho);

    #     /*
    #      * Eq. 16 and 17 from Tsyganenko and Sitnov 2007
    #      */
    #     double bRho = -(kn * z * jKDer * ex / zDist)
    #         * (cosMPhi - thick * (dThickdPhi * (kn + 1.0 / zDist) * sinMPhi) / (m * zDist));
    #     double bPhi = (kn * z * ex * sinMPhi / zDist) * (m * jK / (kn * rho)
    #         - rho * thick * dThickdRho * jKDer * (kn + 1.0 / zDist) / (m * zDist));
    #     double bZ = kn * jK * ex * (cosMPhi - kn * thick * dThickdPhi * sinMPhi / (m * zDist));

    #     // Convert from cylindrical coordinates to GSM
    #     buffer.setTo(bRho * cosPhi - bPhi * sinPhi, bRho * sinPhi + bPhi * cosPhi, bZ);

    #     /*
    #      * TODO for what ever reason, in the code the vectors are scaled by the azimuthal expansion
    #      * number divided by the wave number, this is not in the paper, this is okay, as this will just
    #      * rescale the scaling coeffs
    #      */
    #     return buffer.scale(-m / kn);
    #   }
    # }
