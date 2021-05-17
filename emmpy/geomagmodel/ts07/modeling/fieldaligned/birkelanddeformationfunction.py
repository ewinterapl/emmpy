"""emmpy.geomagmodel.ts07.modeling.fieldaligned.birkelanddeformation"""


# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.sqrt;
# import java.util.Arrays;
# import crucible.core.math.coords.SphericalVector;

from emmpy.magmodel.core.math.vectorfields.differentiablesphericalvectorfield import (
    DifferentiableSphericalVectorField
)


class BirkelandDeformationFunction(DifferentiableSphericalVectorField):
    """Represents the analytical deformation of spherical coordinates to model
    the shape of Birkeland current sheets as described in Tsyganenko 2002
    "A model of the near magnetosphere with a dawn-dusk asymmetry
    1. Mathematical structure" by N. A. Tsyganenko. See eq. (18 and 19).

    author G.K.Stephens
    """
    pass
    # public class BirkelandDeformationFunction implements DifferentiableSphericalVectorField {

    #   // Used for numerical differentiation
    #   private final static double delta = 1E-6;

    #   private final double[] a;
    #   private final double[] b;
    #   private final double[] c;
    #   private final double[] d;

    #   /**
    #    * Construct deformed field:
    #    * <p>
    #    * <img src="./doc-files/t02_eq18_19.png"/>
    #    * <p>
    #    * by providing the coefficients a, b, c, and d.
    #    * 
    #    * @param a an array of doubles containing the radial deformation constants
    #    * @param b an array of doubles containing the radial deformation constants
    #    * @param c an array of doubles containing the co-latitudinal deformation constants
    #    * @param d an array of doubles containing the co-latitudinal deformation constants
    #    */
    #   public BirkelandDeformationFunction(double[] a, double[] b, double[] c, double[] d) {
    #     super();
    #     // make defensive copy
    #     this.a = Arrays.copyOf(a, a.length);
    #     this.b = Arrays.copyOf(b, b.length);
    #     this.c = Arrays.copyOf(c, c.length);
    #     this.d = Arrays.copyOf(d, d.length);
    #   }

    #   @Override
    #   public SphericalVector evaluate(SphericalVector location) {

    #     double r = location.getRadius();
    #     double theta = location.getColatitude();
    #     double phi = location.getLongitude();

    #     // Deform the coordinate system
    #     double rDef = rDeform(r, theta);
    #     double thetaDef = thetaDeform(r, theta);

    #     return new SphericalVector(rDef, thetaDef, phi);
    #   }

    #   @Override
    #   public Results differentiate(SphericalVector location) {

    #     double r = location.getRadius();
    #     double theta = location.getColatitude();
    #     double phi = location.getLongitude();

    #     // Deform the coordinate system
    #     double rDef = rDeform(r, theta);
    #     double thetaDef = thetaDeform(r, theta);

    #     SphericalVector locDef = new SphericalVector(rDef, thetaDef, phi);

    #     // Numerically approximate derivatives for deformation
    #     SphericalVector locPr = evaluate(new SphericalVector(r + delta, theta, phi));
    #     SphericalVector locMr = evaluate(new SphericalVector(r - delta, theta, phi));

    #     SphericalVector locPt = evaluate(new SphericalVector(r, theta + delta, phi));
    #     SphericalVector locMt = evaluate(new SphericalVector(r, theta - delta, phi));

    #     double drDef_dr = (locPr.getRadius() - locMr.getRadius()) / (2 * delta);
    #     double drDef_dtheta = (locPt.getRadius() - locMt.getRadius()) / (2 * delta);

    #     double dthetaDef_dr = (locPr.getColatitude() - locMr.getColatitude()) / (2 * delta);
    #     double dthetaDef_dTheta = (locPt.getColatitude() - locMt.getColatitude()) / (2 * delta);

    #     double dphiDef_dPhi = 1.0;

    #     return new DifferentiableSphericalVectorField.Results(locDef, drDef_dr, drDef_dtheta, 0,
    #         dthetaDef_dr, dthetaDef_dTheta, 0, 0, 0, dphiDef_dPhi);
    #   }

    #   /**
    #    * Deforms the radius to describe the field aligned current. See Tsy 2002-1 Eqn 18
    #    * 
    #    * The b coefficients as given in table 2 were always squared, so they are squared here to save
    #    * math. Note the difference.
    #    * 
    #    * There are two differences between this calculation and the published equation. An email to
    #    * Nikolai Tsyganenko confirmed that these are the proper versions (6/25/2011).
    #    * 
    #    * @param r the undeformed radius
    #    * @param theta the underformed polar angle (measured from the GSM Z axis)
    #    * @return the deformed radius
    #    */
    #   private double rDeform(double r, double theta) {

    #     double r2 = r * r;

    #     return r + a[0] / r + (a[1] * r / (sqrt(r2 + b[0] * b[0]))) + (a[2] * r / (r2 + b[1] * b[1]))

    #         + cos(theta)
    #             * (a[3] + a[4] / r + a[5] * r / sqrt(r2 + b[2] * b[2]) + a[6] * r / (r2 + b[3] * b[3]))

    #         + cos(2 * theta) * (a[7] * r / sqrt(r2 + b[4] * b[4])
    #             + a[8] * r / ((r2 + b[5] * b[5]) * (r2 + b[5] * b[5])));
    #   }

    #   /**
    #    * Deforms theta to describe the field aligned current. See Tsy 2002-1 Eqn 19.
    #    * 
    #    * The d coefficients as given in table 2 were always squared, so they are squared here to save
    #    * math. Note the difference.
    #    * 
    #    * @param r the initial radius
    #    * @param theta the initial polar angle (measured from the GSM Z axis)
    #    * @return the deformed polar angle (theta)
    #    */
    #   private double thetaDeform(double r, double theta) {

    #     double r2 = r * r;

    #     return theta + (c[0] + c[1] / r + c[2] / r2 + c[3] * r / sqrt(r2 + d[0] * d[0])) * sin(theta)
    #         + (c[4] + c[5] * r / sqrt(r2 + d[1] * d[1]) + c[6] * r / (r2 + d[2] * d[2]))
    #             * sin(2 * theta)
    #         + (c[7] + c[8] / r + c[9] * r / (r2 + d[3] * d[3])) * sin(3 * theta);
    #   }

    # }
