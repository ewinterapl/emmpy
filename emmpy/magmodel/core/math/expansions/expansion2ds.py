"""emmpy.magmodel.core.math.expansions.expansion2ds"""


from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D

class Expansion2Ds:
    pass

    # NOT SURE HOW TO HANDLE THIS EMBEDDED CLASS YET.

    # import static com.google.common.base.Preconditions.checkArgument;

    # import crucible.core.math.vectorspace.UnwritableVectorIJK;
    # import crucible.core.math.vectorspace.VectorIJK;

    # public class Expansion2Ds {

    #   /**
    #    * 
    #    * @param data
    #    * @param firstAzimuthalExpansionNumber
    #    * @param firstRadialExpansionNumber
    #    * @return
    #    */
    #   public static <T> Expansion2D<T> createNull(int firstAzimuthalExpansionNumber,
    #       int firstRadialExpansionNumber, int lastRadialExpansionNumber) {

    #     return new Expansion2D<T>() {

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return lastRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return firstAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return firstAzimuthalExpansionNumber - 1;
    #       }

    #       @Override
    #       public T getExpansion(@SuppressWarnings("unused") int mIndex,
    #           @SuppressWarnings("unused") int nIndex) {
    #         throw new UnsupportedOperationException();
    #       }
    #     };

    #   }

    #   /**
    #    * 
    #    * @param data
    #    * @param firstAzimuthalExpansionNumber
    #    * @param firstRadialExpansionNumber
    #    * @return
    #    */
    #   public static <T> Expansion2D<T> createFromArray(T[][] data, int firstAzimuthalExpansionNumber,
    #       int firstRadialExpansionNumber) {
    #     return new ArrayExpansion2D<T>(data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber);
    #   }

    #   /**
    #    * 
    #    * @author stephgk1
    #    * 
    #    */
    #   public static class Vectors {

    #     /**
    #      * 
    #      * @param a
    #      * @param b
    #      * @return
    #      */
    #     public static Expansion2D<UnwritableVectorIJK> add(final Expansion2D<UnwritableVectorIJK> a,
    #         final Expansion2D<UnwritableVectorIJK> b) {

    #       checkArgument(a.getILowerBoundIndex() == b.getILowerBoundIndex());
    #       checkArgument(a.getIUpperBoundIndex() == b.getIUpperBoundIndex());

    #       checkArgument(a.getJLowerBoundIndex() == b.getJLowerBoundIndex());
    #       checkArgument(a.getJUpperBoundIndex() == b.getJUpperBoundIndex());

    #       final int firstAzimuthalExpansion = a.getILowerBoundIndex();
    #       final int lastAzimuthalExpansion = a.getIUpperBoundIndex();

    #       final int firstRadialExpansion = a.getJLowerBoundIndex();
    #       final int lastRadialExpansion = a.getJUpperBoundIndex();

    #       final UnwritableVectorIJK[][] array = new UnwritableVectorIJK[lastAzimuthalExpansion
    #           - firstAzimuthalExpansion + 1][lastRadialExpansion - firstRadialExpansion + 1];

    #       return new Expansion2D<UnwritableVectorIJK>() {


    #         @Override
    #         public int getILowerBoundIndex() {
    #           return firstAzimuthalExpansion;
    #         }

    #         @Override
    #         public int getIUpperBoundIndex() {
    #           return lastAzimuthalExpansion;
    #         }

    #         @Override
    #         public int getJLowerBoundIndex() {
    #           return firstRadialExpansion;
    #         }

    #         @Override
    #         public int getJUpperBoundIndex() {
    #           return lastRadialExpansion;
    #         }

    #         @Override
    #         public UnwritableVectorIJK getExpansion(int azimuthalExpansion, int radialExpansion) {

    #           UnwritableVectorIJK value =
    #               array[azimuthalExpansion - firstAzimuthalExpansion][radialExpansion
    #                   - firstRadialExpansion];

    #           if (value == null) {
    #             value = VectorIJK.add(a.getExpansion(azimuthalExpansion, radialExpansion),
    #                 b.getExpansion(azimuthalExpansion, radialExpansion));
    #             array[azimuthalExpansion - firstAzimuthalExpansion][radialExpansion
    #                 - firstRadialExpansion] = value;
    #             return value;
    #           }
    #           return value;
    #         }

    #       };

    #     }

    #     /**
    #      * 
    #      * @param a
    #      * @param scaleFactor
    #      * @return
    #      */
    #     public static Expansion2D<UnwritableVectorIJK> scale(final Expansion2D<UnwritableVectorIJK> a,
    #         final double scaleFactor) {

    #       return new Expansion2D<UnwritableVectorIJK>() {

    #         @Override
    #         public int getILowerBoundIndex() {
    #           return a.getILowerBoundIndex();
    #         }

    #         @Override
    #         public int getIUpperBoundIndex() {
    #           return a.getIUpperBoundIndex();
    #         }

    #         @Override
    #         public int getJLowerBoundIndex() {
    #           return a.getJLowerBoundIndex();
    #         }

    #         @Override
    #         public int getJUpperBoundIndex() {
    #           return a.getJUpperBoundIndex();
    #         }

    #         @Override
    #         public UnwritableVectorIJK getExpansion(int azimuthalExpansion, int radialExpansion) {
    #           return new UnwritableVectorIJK(scaleFactor,
    #               a.getExpansion(azimuthalExpansion, radialExpansion));
    #         }

    #       };
    #     }

    @staticmethod
    def scale(a, scaleFactors):
        """scale

        @param a
        @param scaleFactors
        @return
        """
    #     public static Expansion2D<UnwritableVectorIJK> scale(final Expansion2D<UnwritableVectorIJK> a,
    #         final CoefficientExpansion2D scaleFactors) {

    #       checkArgument(a.getJLowerBoundIndex() == scaleFactors.getJLowerBoundIndex());
    #       checkArgument(a.getJUpperBoundIndex() == scaleFactors.getJUpperBoundIndex());

    #       return new Expansion2D<UnwritableVectorIJK>() {

    #         @Override
    #         public int getILowerBoundIndex() {
    #           return a.getILowerBoundIndex();
    #         }

    #         @Override
    #         public int getIUpperBoundIndex() {
    #           return a.getIUpperBoundIndex();
    #         }

    #         @Override
    #         public int getJLowerBoundIndex() {
    #           return a.getJLowerBoundIndex();
    #         }

    #         @Override
    #         public int getJUpperBoundIndex() {
    #           return a.getJUpperBoundIndex();
    #         }

    #         @Override
    #         public UnwritableVectorIJK getExpansion(int azimuthalExpansion, int radialExpansion) {
    #           double scaleFactor = scaleFactors.getCoefficient(azimuthalExpansion, radialExpansion);
    #           return new UnwritableVectorIJK(scaleFactor,
    #               a.getExpansion(azimuthalExpansion, radialExpansion));
    #         }
    #       };
    #     }

    #     /**
    #      * 
    #      * @param a
    #      * @return
    #      */
    #     public static UnwritableVectorIJK computeSum(final Expansion2D<UnwritableVectorIJK> a) {

    #       double bx = 0.0;
    #       double by = 0.0;
    #       double bz = 0.0;
    #       for (int az = a.getILowerBoundIndex(); az <= a
    #           .getIUpperBoundIndex(); az++) {
    #         for (int rad = a.getJLowerBoundIndex(); rad <= a
    #             .getJUpperBoundIndex(); rad++) {
    #           UnwritableVectorIJK vect = a.getExpansion(az, rad);
    #           bx += vect.getI();
    #           by += vect.getJ();
    #           bz += vect.getK();
    #         }
    #       }
    #       return new UnwritableVectorIJK(bx, by, bz);
    #     }

    #   }


    # }
