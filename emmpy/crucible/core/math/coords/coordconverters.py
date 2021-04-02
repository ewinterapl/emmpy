"""emmpy.crucible.core.math.coords.coordconverters"""

# import crucible.core.math.vectorspace.UnwritableVectorIJ;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJ;
# import crucible.core.math.vectorspace.VectorIJK;

class CoordConverters:
    """CoordConverters

    @author G.K.Stephens
    """
    # public class CoordConverters {

    #   private static final SphericalCoordConverter sphericalCoordConverter =
    #       new SphericalCoordConverter();
    #   private static final LatitudinalCoordConverter latitudinalCoordConverter =
    #       new LatitudinalCoordConverter();
    #   private static final RaDecCoordConverter raDecCoordConverter = new RaDecCoordConverter();
    #   private static final CylindricalCoordConverter cylindricalCoordConverter =
    #       new CylindricalCoordConverter();

    #   private CoordConverters() {}

    #   /**
    #    * Converts a Cartesian position to spherical position.
    #    * 
    #    * @param cartesian A {@link UnwritableVectorIJK} holding the Cartesian position.
    #    * @param sphericalBuffer A {@link SphericalVector} buffer holding the spherical position;
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static SphericalVector convertToSpherical(UnwritableVectorIJK cartesian) {
    #     return sphericalCoordConverter.toCoordinate(cartesian);
    #   }

    #   /**
    #    * Converts a spherical position to a Cartesian position.
    #    * 
    #    * @param spherical A {@link SphericalVector} holding the spherical position.
    #    * @param cartesianBuffer A {@link VectorIJK} buffer holding the Cartesian position.
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static UnwritableVectorIJK convert(SphericalVector spherical) {
    #     return sphericalCoordConverter.toCartesian(spherical);
    #   }

    #   /**
    #    * Converts from Cartesian coordinates to Latitudinal coordinates
    #    * 
    #    * @param cartesian
    #    * @param LatitudinalBuffer
    #    * @return
    #    */
    #   public static LatitudinalVector convertToLatitudinal(UnwritableVectorIJK cartesian) {
    #     return latitudinalCoordConverter.toCoordinate(cartesian);
    #   }

    #   /**
    #    * Converts from Latitudinal coordinates to Cartesian coordinates
    #    * 
    #    * @param Latitudinal
    #    * @param cartesianBuffer
    #    * @return
    #    */
    #   public static UnwritableVectorIJK convert(LatitudinalVector Latitudinal) {
    #     return latitudinalCoordConverter.toCartesian(Latitudinal);
    #   }

    #   /**
    #    * Converts from Cartesian coordinates to RaDec coordinates
    #    * 
    #    * @param cartesian
    #    * @param RaDecBuffer
    #    * @return
    #    */
    #   public static RaDecVector convertToRaDec(UnwritableVectorIJK cartesian) {
    #     return raDecCoordConverter.toCoordinate(cartesian);
    #   }

    #   /**
    #    * Converts from RaDec coordinates to Cartesian coordinates
    #    * 
    #    * @param RaDec
    #    * @param cartesianBuffer
    #    * @return
    #    */
    #   public static UnwritableVectorIJK convert(RaDecVector RaDec) {
    #     return raDecCoordConverter.toCartesian(RaDec);
    #   }

    #   //
    #   //
    #   // /**
    #   // * Converts from Cartesian states to RaDec states
    #   // *
    #   // * @param cartesian
    #   // * @param RaDecBuffer
    #   // * @return
    #   // */
    #   // public static RaDecState convert(UnwritableCartesianState cartesian,
    #   // RaDecState raDecBuffer) {
    #   // return raDecCoordConverter.toCoordinate(cartesian, raDecBuffer);
    #   // }
    #   //
    #   // /**
    #   // * Converts from RaDec states to Cartesian states
    #   // *
    #   // * @param RaDec
    #   // * @param cartesianBuffer
    #   // * @return
    #   // */
    #   // public static CartesianState convert(UnwritableRaDecState RaDec,
    #   // CartesianState cartesianBuffer) {
    #   // return raDecCoordConverter.toCartesian(RaDec, cartesianBuffer);
    #   // }

    #   /**
    #    * Converts a Cartesian position to cylindrical position.
    #    * 
    #    * @param cartesian A {@link UnwritableVectorIJK} holding the Cartesian position.
    #    * @param cylindricalBuffer A {@link CylindricalVector} buffer holding the cylindrical position;
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static CylindricalVector convertToCylindrical(UnwritableVectorIJK cartesian) {
    #     return cylindricalCoordConverter.toCoordinate(cartesian);
    #   }

    #   /**
    #    * Converts a cylindrical position to a Cartesian position.
    #    * 
    #    * @param cylindrical A {@link CylindricalVector} holding the cylindrical position.
    #    * @param cartesianBuffer A {@link VectorIJK} buffer holding the Cartesian position.
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static UnwritableVectorIJK convert(CylindricalVector cylindrical) {
    #     return cylindricalCoordConverter.toCartesian(cylindrical);
    #   }

    #   // the two dimensional guys
    #   private static PolarCoordConverter polarCoordConverter = new PolarCoordConverter();

    #   /**
    #    * Converts a Cartesian position to polar position.
    #    * 
    #    * @param cartesian A {@link UnwritableVectorIJ} holding the Cartesian position.
    #    * @param polarBuffer A {@link PolarVector} buffer holding the polar position;
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static PolarVector convertToPolar(UnwritableVectorIJ cartesian) {
    #     return polarCoordConverter.toCoordinate(cartesian);
    #   }

    #   /**
    #    * Converts a polar position to a Cartesian position.
    #    * 
    #    * @param polar A {@link PolarVector} holding the polar position.
    #    * @param cartesianBuffer A {@link VectorIJ} buffer holding the Cartesian position.
    #    * @return a reference to buffer for convenience.
    #    */
    #   public static UnwritableVectorIJ convert(PolarVector polar) {
    #     return polarCoordConverter.toCartesian(polar);
    #   }

    # }
