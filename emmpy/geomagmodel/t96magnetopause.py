"""emmpy.geomagmodel.t96magnetopause"""


# import static crucible.core.math.CrucibleMath.atan2;
# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.CrucibleMath.sin;
# import static crucible.core.math.CrucibleMath.sqrt;
# import com.google.common.base.Predicate;
# import crucible.core.math.vectorfields.VectorFields;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.crust.surfaces.Ellipsoid;
# import crucible.crust.surfaces.NoIntersectionException;
# import crucible.crust.surfaces.Surface;
# import crucible.crust.surfaces.Surfaces;
# import geomagmodel.t01.deformation.PositionBender;
# import geomagmodel.ta15.modeling.deformation.DeformationI;
# import magmodel.core.NewtonRaphsonInverseIJK;


class T96Magnetopause:
    """From Tsy. 1995

    X = x0 - a(1 - s*t)
    Y = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * cos(phi)
    Z = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * sin(phi)

    author stephgk1
    """
    pass

    # private static double averagePressure = 2.0;
    # private final double scaledA0;
    # private final double sigma0;
    # private final double scaledX0;
    # // XM is the center of the ellipsoid
    # private final double XM;
    # private final double semiMajorAxis;
    # private final double semiMinorAxis;
    # private final UnwritableVectorIJK ellipsoidCenter;
    # private final Surface ellipsoidalSurface;
    # private final Surface cylindricalSurface;

    #   public static T96Magnetopause createGeopack(double dynamicPressure) {
    #     double A0 = 70.;
    #     double sigma0 = 1.08;
    #     double X00 = 5.48;
    #     double scalingPowerIndex = 0.14;
    #     return new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
    #   }

    #   public static T96Magnetopause createTS07(double dynamicPressure) {
    #     // values listed in
    #     // not sure where these values came from, perhaps TS05?
    #     double A0 = 34.586;
    #     double sigma0 = 1.1960;
    #     double X00 = 3.4397;
    #     // the value from TS05 according to the Fortran source
    #     double scalingPowerIndex = 0.155;
    #     return new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
    #   }

    #   /**
    #    * Creates the bent version of the TS07 magnetopause.
    #    * 
    #    * @param dynamicPressure
    #    * @param dipoleTiltAngle
    #    * @param hingeDistance
    #    * @return
    #    */
    #   public static Predicate<UnwritableVectorIJK> createBentTS07(double dynamicPressure,
    #       double dipoleTiltAngle, double hingeDistance) {
    #     PositionBender bender = new PositionBender(-dipoleTiltAngle, hingeDistance);
    #     final NewtonRaphsonInverseIJK inverseBender =
    #         new NewtonRaphsonInverseIJK(VectorFields.quadraticApproximation(bender, .1, .1, .1));
    #     // values listed in
    #     // not sure where these values came from, perhaps TS05?
    #     double A0 = 34.586;
    #     double sigma0 = 1.1960;
    #     double X00 = 3.4397;
    #     // the value from TS05 according to the Fortran source
    #     double scalingPowerIndex = 0.155;
    #     final T96Magnetopause unbent =
    #         new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
    #     return new Predicate<UnwritableVectorIJK>() {
    #       @Override
    #       public boolean apply(UnwritableVectorIJK input) {
    #         return unbent.apply(inverseBender.evaluate(input));
    #       }
    #     };
    #   }

    #   /**
    #    * Creates the bent version of the TS07 magnetopause.
    #    * 
    #    * @param dynamicPressure
    #    * @param dipoleTiltAngle
    #    * @param hingeDistance
    #    * @return
    #    */
    #   public static Predicate<UnwritableVectorIJK> createBentTS07withTA15(double dynamicPressure,
    #       double dipoleTiltAngle, double hingeDistance, double bzIMF) {
    #     DeformationI bender = new DeformationI(-dipoleTiltAngle, hingeDistance, bzIMF);
    #     final NewtonRaphsonInverseIJK inverseBender =
    #         new NewtonRaphsonInverseIJK(VectorFields.quadraticApproximation(bender, .1, .1, .1));
    #     // values listed in
    #     // not sure where these values came from, perhaps TS05?
    #     double A0 = 34.586;
    #     double sigma0 = 1.1960;
    #     double X00 = 3.4397;
    #     // the value from TS05 according to the Fortran source
    #     double scalingPowerIndex = 0.155;
    #     final T96Magnetopause unbent =
    #         new T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex);
    #     return new Predicate<UnwritableVectorIJK>() {
    #       @Override
    #       public boolean apply(UnwritableVectorIJK input) {
    #         return unbent.apply(inverseBender.evaluate(input));
    #       }
    #     };
    #   }

    #   /**
    #    * 
    #    * @param dynamicPressure
    #    * @param a0
    #    * @param sigma0
    #    * @param x00
    #    * @param scalingPowerIndex referred to Kappa in the literature, the amount to scale the
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
    #     this.semiMajorAxis = -XM + scaledX0 - scaledA0 * (1.0 - sigma0);
    #     this.semiMinorAxis = scaledA0 * sqrt((sigma0 * sigma0 - 1));
    #     this.ellipsoidCenter = new UnwritableVectorIJK(XM, 0.0, 0.0);
    #     Ellipsoid ellipsoid =
    #         Surfaces.createEllipsoidalSurface(semiMajorAxis, semiMinorAxis, semiMinorAxis);
    #     this.ellipsoidalSurface = Surfaces.offset(ellipsoid, ellipsoidCenter.createNegated());
    #     this.cylindricalSurface = Surfaces.createCylinderAlongX(semiMinorAxis);
    #   }

    #   @Override
    #   public VectorIJK computeOutwardNormal(UnwritableVectorIJK surfacePoint, VectorIJK buffer) {
    #     if (surfacePoint.getI() >= XM) {
    #       return ellipsoidalSurface.computeOutwardNormal(surfacePoint, buffer);
    #     } else {
    #       return cylindricalSurface.computeOutwardNormal(surfacePoint, buffer);
    #     }
    #   }

    #   /**
    #    * From Geopack: <pre>
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
    #            * </pre>
    #    * 
    #    * @param positionGSM
    #    * 
    #    * @return
    #    */
    #   public MagnetopauseOutput evaluate(UnwritableVectorIJK positionGSM) {
    #     double xGsw = positionGSM.getI();
    #     double yGsw = positionGSM.getJ();
    #     double zGsw = positionGSM.getK();
    #     // SUBROUTINE T96_MGNP_08(XN_PD,VEL,XGSW,YGSW,ZGSW,XMGNP,YMGNP,ZMGNP,
    #     // * DIST,ID)
    #     /**
    #      * <pre>
    #     	 * 	    		C
    #     	 * 	    		C  FOR ANY POINT OF SPACE WITH GIVEN COORDINATES (XGSW,YGSW,ZGSW), THIS SUBROUTINE DEFINES
    #     	 * 	    		C  THE POSITION OF A POINT (XMGNP,YMGNP,ZMGNP) AT THE T96 MODEL MAGNETOPAUSE WITH THE
    #     	 * 	    		C  SAME VALUE OF THE ELLIPSOIDAL TAU-COORDINATE, AND THE DISTANCE BETWEEN THEM.  THIS IS
    #     	 * 	    		C  NOT THE SHORTEST DISTANCE D_MIN TO THE BOUNDARY, BUT DIST ASYMPTOTICALLY TENDS TO D_MIN,
    #     	 * 	    		C  AS THE OBSERVATION POINT GETS CLOSER TO THE MAGNETOPAUSE.
    #     	 * 	    		C
    #     	 * 	    		C  INPUT: XN_PD - EITHER SOLAR WIND PROTON NUMBER DENSITY (PER C.C.) (IF VEL>0)
    #     	 * 	    		C                    OR THE SOLAR WIND RAM PRESSURE IN NANOPASCALS   (IF VEL<0)
    #     	 * 	    		C         VEL - EITHER SOLAR WIND VELOCITY (KM/SEC)
    #     	 * 	    		C                  OR ANY NEGATIVE NUMBER, WHICH INDICATES THAT XN_PD STANDS
    #     	 * 	    		C                     FOR THE SOLAR WIND PRESSURE, RATHER THAN FOR THE DENSITY
    #     	 * 	    		C
    #     	 * 	    		C         XGSW,YGSW,ZGSW - COORDINATES OF THE OBSERVATION POINT IN EARTH RADII
    #     	 * 	    		C
    #     	 * 	    		C  OUTPUT: XMGNP,YMGNP,ZMGNP - GSW POSITION OF THE BOUNDARY POINT, HAVING THE SAME
    #     	 * 	    		C          VALUE OF TAU-COORDINATE AS THE OBSERVATION POINT (XGSW,YGSW,ZGSW)
    #     	 * 	    		C          DIST -  THE DISTANCE BETWEEN THE TWO POINTS, IN RE,
    #     	 * 	    		C          ID -    POSITION FLAG; ID=+1 (-1) MEANS THAT THE POINT (XGSW,YGSW,ZGSW)
    #     	 * 	    		C          LIES INSIDE (OUTSIDE) THE MODEL MAGNETOPAUSE, RESPECTIVELY.
    #     	 * 	    		C
    #     	 * 	    		C  THE PRESSURE-DEPENDENT MAGNETOPAUSE IS THAT USED IN THE T96_01 MODEL
    #     	 * 	    		C  (TSYGANENKO, JGR, V.100, P.5599, 1995; ESA SP-389, P.181, OCT. 1996)
    #     	 * 	    		C
    #     	 * 	    		c   AUTHOR:  N.A. TSYGANENKO
    #     	 * 	    		C   DATE:    AUG.1, 1995, REVISED APRIL 3, 2003.
    #     	 * 	    		C
    #     	 * 	    		C
    #     	 * 	    		C  DEFINE SOLAR WIND DYNAMIC PRESSURE (NANOPASCALS, ASSUMING 4% OF ALPHA-PARTICLES),
    #     	 * 	    		C   IF NOT EXPLICITLY SPECIFIED IN THE INPUT:
    #     	 * </pre>
    #      */
    #     /**
    #      * <pre>
    #     	 * 	    		C  (XM IS THE X-COORDINATE OF THE "SEAM" BETWEEN THE ELLIPSOID AND THE CYLINDER)
    #     	 * 	    		C
    #     	 * 	    		C     (FOR DETAILS OF THE ELLIPSOIDAL COORDINATES, SEE THE PAPER:
    #     	 * 	    		C      N.A.TSYGANENKO, SOLUTION OF CHAPMAN-FERRARO PROBLEM FOR AN
    #     	 * 	    		C      ELLIPSOIDAL MAGNETOPAUSE, PLANET.SPACE SCI., V.37, P.1037, 1989).
    #     	 * </pre>
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
    #       double SQ1 = sqrt((1.0 + XKSI) * (1.0 + XKSI) + XDZT * XDZT);
    #       double SQ2 = sqrt((1.0 - XKSI) * (1.0 - XKSI) + XDZT * XDZT);
    #       double sigma = 0.5 * (SQ1 + SQ2);
    #       double tau = 0.5 * (SQ1 - SQ2);
    #       // NOW CALCULATE (X,Y,Z) FOR THE CLOSEST POINT AT THE MAGNETOPAUSE
    #       double xMgnp = scaledX0 - scaledA0 * (1. - sigma0 * tau);
    #       double ARG = (sigma0 * sigma0 - 1.) * (1. - tau * tau);
    #       if (ARG < 0.0) {
    #         ARG = 0.;
    #       }
    #       double rhoMagnetopause = scaledA0 * sqrt(ARG);
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
    #     // UnwritableVectorIJK bentMagnetopauseLocation =
    #     // bendingWarping.evaluate(magnetopauseLocation, new VectorIJK());
    #     /*
    #      * NOW CALCULATE THE DISTANCE BETWEEN THE POINTS {XGSW,YGSW,ZGSW} AND {XMGNP,YMGNP,ZMGNP}: (IN
    #      * GENERAL, THIS IS NOT THE SHORTEST DISTANCE D_MIN, BUT DIST ASYMPTOTICALLY TENDS TO D_MIN, AS
    #      * WE ARE GETTING CLOSER TO THE MAGNETOPAUSE):
    #      */
    #     // compute the distance between the input position and the magnetopause
    #     double distance = VectorIJK.subtract(positionGSM, magnetopauseLocation).getLength();
    #     return new MagnetopauseOutput(magnetopauseLocation, distance, withinMagnetosphere);
    #   }

    #   @Override
    #   public boolean intersects(@SuppressWarnings("unused") UnwritableVectorIJK source,
    #       @SuppressWarnings("unused") UnwritableVectorIJK ray) {
    #     throw new UnsupportedOperationException();
    #   }

    #   @Override
    #   public VectorIJK compute(UnwritableVectorIJK source, UnwritableVectorIJK ray, VectorIJK buffer) {
    #     // TODO FIX THIS IT IS BROKEN
    #     UnwritableVectorIJK c = cylindricalSurface.compute(source, ray, new VectorIJK());
    #     if (c.getI() <= XM) {
    #       return buffer.setTo(c);
    #     } else {
    #       UnwritableVectorIJK e = ellipsoidalSurface.compute(source, ray, new VectorIJK());
    #       if (e.getI() < XM) {
    #         throw new NoIntersectionException();
    #       }
    #       return buffer.setTo(e);
    #     }
    #   }

    #   @Override
    #   public boolean apply(UnwritableVectorIJK positionGSM) {
    #     return evaluate(positionGSM).isWithinMagnetosphere();
    #   }

    # }
