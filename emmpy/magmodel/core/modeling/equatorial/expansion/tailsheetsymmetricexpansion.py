"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetsymmetricexpansion"""


# import static com.google.common.base.Preconditions.checkNotNull;
# import static crucible.core.math.CrucibleMath.exp;
# import static crucible.core.math.CrucibleMath.sqrt;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJ;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class TailSheetSymmetricExpansion(VectorField):
    pass

    # /**
    #  * This is the symmetric (axissymmetric) part of the expansion of the solution of the magnetic field
    #  * from a thin current sheet along the z=0 plane, from Tsyganenko and Sitnov 2007, eq. 15.
    #  * <p>
    #  * <img src="./doc-files/ts07_eq_15.png" />
    #  * <p>
    #  * <pre>
    #  *      SUBROUTINE TAILSHT_S (M,X,Y,Z,BX,BY,BZ)
    #  *</pre>
    #  * 
    #  * @author G.K.Stephens
    #  *
    #  */
    # public class TailSheetSymmetricExpansion implements VectorField {

    #   private final double waveNumber;

    #   private final DifferentiableScalarFieldIJ currentSheetHalfThickness;

    #   private final BesselFunctionEvaluator bessel;

    #   /**
    #    * Constructor
    #    * 
    #    * @param waveNumber the wave number of this expansion
    #    * @param currentSheetHalfThickness a 2D scalar field representing the current sheet half
    #    *        thickness throughout the equatorial current system
    #    * @param bessel the Bessel function evaluator
    #    */
    #   public TailSheetSymmetricExpansion(double waveNumber,
    #       DifferentiableScalarFieldIJ currentSheetHalfThickness, BesselFunctionEvaluator bessel) {
    #     super();
    #     this.waveNumber = waveNumber;
    #     // this.currentSheetHalfThickness = checkNotNull(currentSheetHalfThickness);
    #     this.currentSheetHalfThickness = currentSheetHalfThickness;
    #     // this.bessel = checkNotNull(bessel);
    #     this.bessel = bessel;
    #   }

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

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

    #     // convert derivatives to polar
    #     double dThickdRho = (x * dThickdx + y * dThickdy) / rho;

    #     double cosPhi = x / rho;
    #     double sinPhi = y / rho;
    #     // introduce a finite thickness in z by replacing z with this value
    #     double zDist = sqrt(z * z + thick * thick);

    #     // kn is the wave number
    #     double kn = waveNumber;

    #     // evaluate the Bessel function
    #     double j0 = bessel.besselj0(kn * rho);
    #     double j1 = bessel.besselj1(kn * rho);

    #     double ex = exp(-kn * zDist);

    #     double bx = kn * z * j1 * cosPhi * ex / zDist;
    #     double by = kn * z * j1 * sinPhi * ex / zDist;
    #     double bz = kn * ex * (j0 - thick * dThickdRho * j1 / zDist);

    #     return buffer.setTo(bx, by, bz);
    #   }

    # }
