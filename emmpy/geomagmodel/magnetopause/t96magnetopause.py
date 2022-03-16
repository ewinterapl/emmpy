"""Compute the magnetopause according to the T96 model.

An implementation of the T96 magnetopause as described in Tsyganenko (1995)
[https://doi.org/10.1029/94JA03193]. The T96 magnetopause model was constructed
using an ellipsoid, described using the following equations (eq. (1) from
above):

    X = x0 - a(1 - s*t)
    Y = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * cos(phi)
    Z = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * sin(phi)

connected to a cylinder. See Fig. 2 from the above paper.

This model was later adapted by fitting its ellipsoidal part to the Shue et al
(1998) model [https://doi.org/10.1029/98JA01103], as described in
Tsyganenko (2002) [https://doi.org/10.1029/2001JA000219]. This magnetopause
boundary would become the basis for other the T01, TS05, and TS07D models.

Specifically, this class is equivalent the T96_MGNP_08 subroutine contained in
the Geopack code.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# Import standard modules.
from math import sqrt


# Program constants.

# Nominal pressure used to scale the magnetopause (nPa)
averagePressure = 2.0


class T96Magnetopause:
    """Compute the magnetopause according to the T96 model.

    Attributes
    ----------
    scaledA0 : float
        XXX
    sigma0 : float
        XXX
    scaledX0 : float
        XXX
    XM : float
        Center of the ellipsoid
    semiMinorAxis : float
        XXX
    """

    def __init__(self, dynamicPressure, a0, sigma0, x00, scalingPowerIndex):
        """Initialize a new T96Magnetopause object.

        Initialize a new T96Magnetopause object.

        Parameters
        ----------
        dynamicPressure : float
            Solar wind dynamic pressure (nPa)
        a0 : float
            XXX
        sigma0 : float
            XXX
        x00 : float
            XXX
        scalingPowerIndex : float
            Referred to as Kappa in the literature.

        Returns
        -------
        None
        """

        # Compute the ratio of the dynamic pressure to the average pressure.
        pdynRatio = dynamicPressure/averagePressure

        # Scale the magnetopause parameters.
        scalingFactor = pow(pdynRatio, scalingPowerIndex)
        self.scaledA0 = a0/scalingFactor
        self.sigma0 = sigma0
        self.scaledX0 = x00/scalingFactor
        self.XM = self.scaledX0 - self.scaledA0
        self.semiMinorAxis = self.scaledA0*sqrt((sigma0**2 - 1))


#   public static T96Magnetopause createGeopack(double dynamicPressure) {
#   public static T96Magnetopause createTS07(double dynamicPressure) {
#   public static Predicate<UnwritableVectorIJK> createBentTS07(double dynamicPressure,
#       double dipoleTiltAngle, double hingeDist, double warpParam, double twistFact) {
#   T96Magnetopause(double dynamicPressure, double a0, double sigma0, double x00,
#       double scalingPowerIndex) {
#   public MagnetopauseOutput evaluate(UnwritableVectorIJK positionGSM) {
#   public boolean apply(UnwritableVectorIJK positionGSM) {
#     return evaluate(positionGSM).isWithinMagnetosphere();
#   }


#   // the nominal pressure used to scale the magnetopause
#   private static double averagePressure = 2.0;

#   private final double scaledA0;
#   private final double sigma0;
#   private final double scaledX0;

#   // XM is the center of the ellipsoid
#   private final double XM;

#   private final double semiMinorAxis;

#   /**
#    * Constructs the T96 magnetopause model consistent with the T96_MGNP_08 subroutine from Geopack.
#    * Note, this does not apply the dipole tilt angle deformation effects.
#    * 
#    * @param dynamicPressure the solar wind dynamic pressure in nPa
#    * @return a newly constructed T96 magnetopause model
#    */
#   public static T96Magnetopause createGeopack(double dynamicPressure) {

#     // These values are very similar to those given in the T96 paper, x0 = 5.48 RE, a = 70.48 RE,
#     // and sigma0 = 1.078, see eq. (2)
#     double A0 = 70.0;
#     double sigma0 = 1.08;
#     double X00 = 5.48;

#     /*
#      * (THE POWER INDEX 0.14 IN THE SCALING FACTOR IS THE BEST-FIT VALUE OBTAINED FROM DATA AND USED
#      * IN THE T96_01 VERSION)
#      */
#     // the value used in the T96 model, see the second T96 paper, section 3.1
#     double scalingPowerIndex = 0.14;

#     return new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
#   }

#   /**
#    * Constructs the version of T96 magnetopause model used in the TS07D model. Note, this does not
#    * apply the dipole tilt angle deformation effects, which are included in
#    * {@link #createBentTS07(double, double, double, double, double)}.
#    * 
#    * @param dynamicPressure the solar wind dynamic pressure in nPa
#    * @return a newly constructed T96 magnetopause model as utilized in the TS07D model
#    */
#   public static T96Magnetopause createTS07(double dynamicPressure) {

#     /*
#      * these values originate in the T01 model source code, they are similar (although not quite the
#      * same) as those given in the first T01 paper (https://doi.org/2001JA000219) section 2.4: x0 =
#      * 3.486, sigma0 = 1.198, a = 35.13. According to the paper they were "... derived by fitting
#      * the surface (equation (26)) to an average boundary of Shue et al. [1998]". These values were
#      * also used in the TS05 model and the TS07 model.
#      */
#     double A0 = 34.586;
#     double sigma0 = 1.1960;
#     double X00 = 3.4397;

#     // the value used in the TS07D model, very similar to that used in the TS05 model (0.152759)
#     double scalingPowerIndex = 0.155;

#     return new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
#   }

#   /**
#    * Constructs the version of T96 magnetopause model used in the TS07D model which includes the
#    * dipole tilt angle deformation effects.
#    * 
#    * @param dynamicPressure the solar wind dynamic pressure in nPa
#    * @param dipoleTiltAngle the dipole tilt angle in radians
#    * @param hingeDist the hinging distance RH as defined in the TS07D model
#    * @param warpParam the warping parameter G as defined in the TS07D model
#    * @param twistFact the twisting parameter T as defined in the TS07D model
#    * 
#    * @return a newly constructed T96 magnetopause model as utilized in the TS07D model
#    */
#   public static Predicate<UnwritableVectorIJK> createBentTS07(double dynamicPressure,
#       double dipoleTiltAngle, double hingeDist, double warpParam, double twistFact) {

#     PositionBender bender = new PositionBender(dipoleTiltAngle, hingeDist);
#     TwistWarpFfunction warper = new TwistWarpFfunction(warpParam, twistFact, dipoleTiltAngle);

#     // the value from TS05 according to the Fortran source
#     double scalingPowerIndex = 0.155;

#     double pdynScaling = pow(dynamicPressure / averagePressure, scalingPowerIndex);

#     final T96Magnetopause unbent = createTS07(averagePressure);

#     return new Predicate<UnwritableVectorIJK>() {

#       @Override
#       public boolean apply(UnwritableVectorIJK location) {

#         UnwritableVectorIJK pdynScaledLocation = new UnwritableVectorIJK(pdynScaling, location);

#         UnwritableVectorIJK bentLocation = bender.evaluate(pdynScaledLocation);
#         UnwritableVectorIJK bentWarpedLocation = warper.evaluate(bentLocation);

#         return unbent.apply(bentWarpedLocation);
#       }
#     };
#   }

#   /**
#    * Constructor.
#    * 
#    * @param dynamicPressure the solar wind dynamic pressure in nPa
#    * @param a0
#    * @param sigma0
#    * @param x00
#    * @param scalingPowerIndex referred to Kappa in the literature
#    */
#   T96Magnetopause(double dynamicPressure, double a0, double sigma0, double x00,
#       double scalingPowerIndex) {

#     // RATIO OF PD TO THE AVERAGE PRESSURE, ASSUMED EQUAL TO 2 nPa:
#     double pdynRatio = dynamicPressure / averagePressure;

#     // the magnetopause is scaled by it's linear dimensions by X = (Pd/<Pd>)^(k)
#     double scalingFactor = pow(pdynRatio, scalingPowerIndex);

#     // VALUES OF THE MAGNETOPAUSE PARAMETERS, SCALED BY THE ACTUAL PRESSURE:
#     this.scaledA0 = a0 / scalingFactor;
#     this.sigma0 = sigma0;
#     this.scaledX0 = x00 / scalingFactor;

#     this.XM = scaledX0 - scaledA0;

#     this.semiMinorAxis = scaledA0 * sqrt((sigma0 * sigma0 - 1));

#   }

#   /**
#    * From Geopack:
#    * 
#    * <pre>
  
#   FOR ANY POINT OF SPACE WITH GIVEN COORDINATES (XGSW,YGSW,ZGSW), THIS SUBROUTINE DEFINES
#   THE POSITION OF A POINT (XMGNP,YMGNP,ZMGNP) AT THE T96 MODEL MAGNETOPAUSE WITH THE
#   SAME VALUE OF THE ELLIPSOIDAL TAU-COORDINATE, AND THE DISTANCE BETWEEN THEM.  THIS IS
#   NOT THE SHORTEST DISTANCE D_MIN TO THE BOUNDARY, BUT DIST ASYMPTOTICALLY TENDS TO D_MIN,
#   AS THE OBSERVATION POINT GETS CLOSER TO THE MAGNETOPAUSE.
  
#   INPUT: XN_PD - EITHER SOLAR WIND PROTON NUMBER DENSITY (PER C.C.) (IF VEL>0)
#                     OR THE SOLAR WIND RAM PRESSURE IN NANOPASCALS   (IF VEL<0)
#          VEL - EITHER SOLAR WIND VELOCITY (KM/SEC)
#                   OR ANY NEGATIVE NUMBER, WHICH INDICATES THAT XN_PD STANDS
#                      FOR THE SOLAR WIND PRESSURE, RATHER THAN FOR THE DENSITY
  
#          XGSW,YGSW,ZGSW - COORDINATES OF THE OBSERVATION POINT IN EARTH RADII
  
#   OUTPUT: XMGNP,YMGNP,ZMGNP - GSW POSITION OF THE BOUNDARY POINT, HAVING THE SAME
#           VALUE OF TAU-COORDINATE AS THE OBSERVATION POINT (XGSW,YGSW,ZGSW)
#           DIST -  THE DISTANCE BETWEEN THE TWO POINTS, IN RE,
#           ID -    POSITION FLAG; ID=+1 (-1) MEANS THAT THE POINT (XGSW,YGSW,ZGSW)
#           LIES INSIDE (OUTSIDE) THE MODEL MAGNETOPAUSE, RESPECTIVELY.
  
#   THE PRESSURE-DEPENDENT MAGNETOPAUSE IS THAT USED IN THE T96_01 MODEL
#   (TSYGANENKO, JGR, V.100, P.5599, 1995; ESA SP-389, P.181, OCT. 1996)
  
#    AUTHOR:  N.A. TSYGANENKO
#    DATE:    AUG.1, 1995, REVISED APRIL 3, 2003.
  
  
#   DEFINE SOLAR WIND DYNAMIC PRESSURE (NANOPASCALS, ASSUMING 4% OF ALPHA-PARTICLES),
#    IF NOT EXPLICITLY SPECIFIED IN THE INPUT:
#    * </pre>
#    * 
#    * @param positionGSM
#    * 
#    * @return
#    */
#   public MagnetopauseOutput evaluate(UnwritableVectorIJK positionGSM) {

#     double xGsw = positionGSM.getI();
#     double yGsw = positionGSM.getJ();
#     double zGsw = positionGSM.getK();

#     /**
#      * From Geopack:
#      * 
#      * <pre>
#     (XM IS THE X-COORDINATE OF THE "SEAM" BETWEEN THE ELLIPSOID AND THE CYLINDER)
    
#      (FOR DETAILS OF THE ELLIPSOIDAL COORDINATES, SEE THE PAPER:
#       N.A.TSYGANENKO, SOLUTION OF CHAPMAN-FERRARO PROBLEM FOR AN
#       ELLIPSOIDAL MAGNETOPAUSE, PLANET.SPACE SCI., V.37, P.1037, 1989).
#      * </pre>
#      */

#     double phiGsw = 0.0;
#     if (yGsw != 0.0 || zGsw != 0.0) {
#       phiGsw = atan2(yGsw, zGsw);
#     } else {
#       phiGsw = 0.0;
#     }

#     double rhoGsw = sqrt(yGsw * yGsw + zGsw * zGsw);

#     boolean withinMagnetosphere = false;
#     UnwritableVectorIJK magnetopauseLocation = null;

#     /*
#      * if X < XM, we are in the tailward of the ellipsoid center, so the magnetopause is defined
#      * using the cylinder
#      */
#     if (xGsw < XM) {

#       double xMgnp = xGsw;
#       double yMgnp = semiMinorAxis * sin(phiGsw);
#       double zMgnp = semiMinorAxis * cos(phiGsw);

#       // the magnetopause is outside of where we are, so we are in the magnetosphere
#       if (semiMinorAxis > rhoGsw) {
#         withinMagnetosphere = true;
#       }
#       if (semiMinorAxis <= rhoGsw) {
#         withinMagnetosphere = false;
#       }

#       magnetopauseLocation = new UnwritableVectorIJK(xMgnp, yMgnp, zMgnp);
#     }
#     /*
#      * Otherwise, we are in the ellipse region
#      */
#     else {

#       double XKSI = (xGsw - scaledX0) / scaledA0 + 1.0;
#       double XDZT = rhoGsw / scaledA0;
#       double sq1 = sqrt((1.0 + XKSI) * (1.0 + XKSI) + XDZT * XDZT);
#       double sq2 = sqrt((1.0 - XKSI) * (1.0 - XKSI) + XDZT * XDZT);

#       double sigma = 0.5 * (sq1 + sq2);
#       double tau = 0.5 * (sq1 - sq2);

#       // NOW CALCULATE (X,Y,Z) FOR THE CLOSEST POINT AT THE MAGNETOPAUSE

#       double xMgnp = scaledX0 - scaledA0 * (1. - sigma0 * tau);

#       double arg = (sigma0 * sigma0 - 1.) * (1. - tau * tau);
#       if (arg < 0.0) {
#         arg = 0.;
#       }

#       double rhoMagnetopause = scaledA0 * sqrt(arg);

#       double yMgnp = rhoMagnetopause * sin(phiGsw);
#       double zMgnp = rhoMagnetopause * cos(phiGsw);

#       if (sigma > sigma0) {
#         withinMagnetosphere = false; // ID=-1 MEANS THAT THE POINT LIES OUTSIDE
#       }

#       if (sigma <= sigma0) {
#         withinMagnetosphere = true; // ID=+1 MEANS THAT THE POINT LIES INSIDE THE MAGNETOSPHERE
#       }

#       magnetopauseLocation = new UnwritableVectorIJK(xMgnp, yMgnp, zMgnp);
#     }

#     /*
#      * NOW CALCULATE THE DISTANCE BETWEEN THE POINTS {XGSW,YGSW,ZGSW} AND {XMGNP,YMGNP,ZMGNP}: (IN
#      * GENERAL, THIS IS NOT THE SHORTEST DISTANCE D_MIN, BUT DIST ASYMPTOTICALLY TENDS TO D_MIN, AS
#      * WE ARE GETTING CLOSER TO THE MAGNETOPAUSE):
#      */
#     // compute the distance between the input position and the magnetopause
#     double distance = VectorIJK.subtract(positionGSM, magnetopauseLocation).getLength();

#     return new MagnetopauseOutput(magnetopauseLocation, distance, withinMagnetosphere);
#   }

#   /**
#    * @return true if the query point is within the magnetopause (inside the magnetosphere), false if
#    *         it is outside the magnetopaause (outside the magnetosphere)
#    */
#   @Override
#   public boolean apply(UnwritableVectorIJK positionGSM) {
#     return evaluate(positionGSM).isWithinMagnetosphere();
#   }

# }
