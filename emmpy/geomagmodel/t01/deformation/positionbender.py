"""emmpy.geomgmodel.t01.deformation.positionbender"""


# import static com.google.common.base.Preconditions.checkArgument;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.sqrt;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import magmodel.core.math.deformation.VectorFieldDeformation;
# import magmodel.core.math.vectorfields.BasisVectorField;

from math import sin

from emmpy.crucible.core.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField
)
from emmpy.magmodel.core.math.deformation.basisvectorfielddeformation import (
    BasisVectorFieldDeformation
)


class PositionBender(DifferentiableVectorField):
    """From Tsyganeneko's code, an implementation of Tsyganenko [1998]
    section 3, "deformation in the X-Z plane related to the dipole tilt"

    Computes:
    X* = Xcos&#936;*(r) - Zsin&#936;*(r)
    Y* = Y
    Z* = Xsin&#936;*(r) + Zcos&#936;*(r)
    where
    sin&#936;* = R<sub>H</sub>sin&#936;/(R<sub>H</sub><sup>3</sup>+r<sup>3</sup>)<sup>1/3</sup >
    R<sub>H</sub> =  R<sub>H0</sub> +  R<sub>H2</sub> Z<sup>2</sup>/r<sup>2</sup>
    This is similar to the FORTRAN subroutine: 
         SUBROUTINE DEFORMED (PS,X,Y,Z,BX,BY,BZ) 
    see ./doc-files/tsy1998Math.docx

    author G.K.Stephens
    """

    # private final double sinTilt;
    # private final double rh0;
    # // Can be changed to "0" to avoid problems with simplex iterating to
    # // non-real values.
    # private final double rh2 = -5.2;
    # private final double epsilon = 3;

    def __init__(self, dipoleTilt, hingeDistance):
        """Constructor

        param double dipoleTilt
        param double hingeDistance R_H0, must be greater than or equal to the
        value R_H2, which is 5.2
        """
        self.sinTilt = sin(dipoleTilt)
        self.rh0 = hingeDistance

    # /**
    # * 
    # * @param dipoleTilt
    # * @param hingeDistance
    # * @param undeformedField
    # * @return
    # */
    # public static VectorField deformField(double dipoleTilt, double hingeDistance,
    #     VectorField undeformedField) {
    #     // Construct the deformation
    #     PositionBender deformation = new PositionBender(dipoleTilt, hingeDistance);
    #     // Deform the field
    #     VectorFieldDeformation deformedField = new VectorFieldDeformation(undeformedField, deformation);
    #     return deformedField;
    # }

    @staticmethod
    def deformBasisField(dipoleTilt, hingeDistance, undeformedField):
        """deformBasisField

        param double dipoleTilt
        param double hingeDistance
        param BasisVectorField undeformedField
        return BasisVectorField
        """

        # Construct the deformation
        deformation = PositionBender(dipoleTilt, hingeDistance)

        # Deform the field
        deformedField = BasisVectorFieldDeformation(undeformedField,
                                                    deformation)

        return deformedField

    # /**
    # * Bend the position vector to account for the bending of the tail field in the X-Z GSM plane.
    # * 
    # * Derivation: Tsyganenko 2002-1 Eqn 13
    # * 
    # * @param position
    # * @param buffer
    # */
    # @Override
    # public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    #     double x = location.getI();
    #     double y = location.getJ();
    #     double z = location.getK();

    #     double r2 = x * x + y * y + z * z;
    #     double r = sqrt(r2);
    #     double z_r = z / r;

    #     /*
    #     * Allow the hinging distance to be a function of position, Tsy. 1998 eq. 12
    #     */
    #     double rh = rh0 + rh2 * z_r * z_r;

    #     // r/RH
    #     double r_rh = r / rh;

    #     /*
    #     * eq. 10 Tsy. 1998, Q(r) = [1+ (r/RH)^ep ]^(-1/ep)
    #     */
    #     double Q = 1 / pow(1 + pow(r_rh, epsilon), 1 / epsilon);

    #     /*
    #     * Now compute the cos and sin of the radial dependent tilt angle, this is Tsy. 1998 eq. 7
    #     */
    #     double sinTiltS = sinTilt * Q;
    #     double cosTiltS = sqrt(1 - sinTiltS * sinTiltS);

    #     /*
    #     * The point deformation from eq. 7 in Tsy. 1998
    #     */
    #     double xS = x * cosTiltS - z * sinTiltS;
    #     double yS = y;
    #     double zS = x * sinTiltS + z * cosTiltS;

    #     return buffer.setTo(xS, yS, zS);
    # }

    # @Override
    # public Results differentiate(UnwritableVectorIJK location) {

    #     double x = location.getI();
    #     double y = location.getJ();
    #     double z = location.getK();

    #     double r2 = x * x + y * y + z * z;
    #     double r = sqrt(r2);
    #     double z_r = z / r;

    #     /*
    #     * Allow the hinging distance to be a function of position, Tsy. 1998 eq. 12
    #     */
    #     double rh = rh0 + rh2 * z_r * z_r;

    #     // r/RH
    #     double r_rh = r / rh;

    #     /*
    #     * eq. 10 Tsy. 1998, Q(r) = [1+ (r/RH)^ep ]^(-1/ep)
    #     */
    #     double Q = 1 / pow(1 + pow(r_rh, epsilon), 1 / epsilon);

    #     /*
    #     * Now compute the cos and sin of the radial dependent tilt angle, this is Tsy. 1998 eq. 7
    #     */
    #     double sinTiltS = sinTilt * Q;
    #     double cosTiltS = sqrt(1 - sinTiltS * sinTiltS);

    #     /*
    #     * The point deformation from eq. 7 in Tsy. 1998
    #     */
    #     double xS = x * cosTiltS - z * sinTiltS;
    #     double yS = y;
    #     double zS = x * sinTiltS + z * cosTiltS;

    #     /*
    #     * The radial and height derivative of Rh
    #     */
    #     double dRhDr = -2. * rh2 * z_r * z_r / r;
    #     double dRhDz = 2. * rh2 * z_r / r;

    #     /*
    #     * Now compute the x,y,z derivatives of Q, apply the chain rule
    #     */
    #     // fr is the first term dQ/dr
    #     double fr = -pow(r_rh, epsilon - 1) * pow(Q, epsilon + 1) / rh;
    #     double dQdRh = -r_rh * fr;
    #     double dQdr = fr - fr * r_rh * dRhDr;
    #     double dQdx = dQdr * x / r;
    #     double dQdy = dQdr * y / r;
    #     double dQdz = dQdr * z / r + dQdRh * dRhDz;

    #     // store this ratio sinT/cosT*
    #     double sin_cos = sinTilt / cosTiltS;

    #     double dXsDx = cosTiltS - zS * dQdx * sin_cos;
    #     double dXsDy = -zS * dQdy * sin_cos;
    #     double dXsDz = -sinTiltS - zS * dQdz * sin_cos;

    #     double dYsDx = 0;
    #     double dYsDy = 1;
    #     double dYsDz = 0;

    #     double dZsDx = sinTiltS + xS * dQdx * sin_cos;
    #     double dZsDy = xS * dQdy * sin_cos;
    #     double dZsDz = cosTiltS + xS * dQdz * sin_cos;

    #     UnwritableVectorIJK f = new UnwritableVectorIJK(xS, yS, zS);

    #     Results results = new Results(f, dXsDx, dXsDy, dXsDz, dYsDx, dYsDy, dYsDz, dZsDx, dZsDy, dZsDz);

    #     return results;
    # }

    # @Override
    # public double differentiateFiDi(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFjDi(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFkDi(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFiDj(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFjDj(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFkDj(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFiDk(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFjDk(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # @Override
    # public double differentiateFkDk(@SuppressWarnings("unused") UnwritableVectorIJK location) {
    #     throw new UnsupportedOperationException();
    # }

    # }
