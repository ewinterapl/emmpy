"""emmpy.magmodel.core.math.expansions.coefficientexpansions"""


from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


class CoefficientExpansions:

    @staticmethod
    def createExpansionFromArray(*args):
        """Wraps an array and returns a view of the array as a
        {@link CoefficientExpansion1D}."""
        if len(args) == 2:
            # @param data the array that backs the {@link CoefficientExpansion1D}
            # @param firstExpansionNumber the first index to be used in the
            # expansion
            # @return a newly created {@link CoefficientExpansion1D} that is a view
            # of the input array
            (data, firstExpansionNumber) = args
            return ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        elif len(args) == 3:
            # @param data the 2D array that backs the
            # {@link CoefficientExpansion2D}
            # @param firstIexpansionNumber the first index to be used in the
            # first dimension of the expansion
            # @param firstJexpansionNumber the first index to be used in the
            # second dimensions of the expansion
            # @return a newly created {@link CoefficientExpansion2D} that is a
            # view of the input array
            (data, firstIexpansionNumber, firstJexpansionNumber) = args
            return ArrayCoefficientExpansion2D(data, firstIexpansionNumber,
                                               firstJexpansionNumber)

    # DON'T KNOW HOW TO HANDLE COMPUTED CLASSES USED BELOW.

    #   /**
    #    * Returns an inverted view of the supplied expansion coefficients.
    #    * <p>
    #    * p'<sub>i</sub>= 1/p<sub>i</sub>
    #    * 
    #    * @param p the set of coefficients p<sub>i</sub> to invert
    #    * @return the inverted set of coefficients p'<sub>i</sub>
    #    */
    #   public static CoefficientExpansion1D invert(final CoefficientExpansion1D p) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return p.getLowerBoundIndex();
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return p.getUpperBoundIndex();
    #       }

    #       @Override
    #       public double getCoefficient(int index) {
    #         return 1.0 / p.getCoefficient(index);
    #       }
    #     };

    #   }

    #   public static CoefficientExpansion1D negate(final CoefficientExpansion1D a) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return a.getLowerBoundIndex();
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return a.getUpperBoundIndex();
    #       }

    #       @Override
    #       public double getCoefficient(int index) {
    #         return -a.getCoefficient(index);
    #       }
    #     };

    #   }

    #   /**
    #    * 
    #    * @param firstRadialExpansionNumber
    #    * @param lastRadialExpansionNumber
    #    * @return
    #    */
    #   public static CoefficientExpansion1D createUnity(final int firstRadialExpansionNumber,
    #       final int lastRadialExpansionNumber) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return lastRadialExpansionNumber;
    #       }

    #       @Override
    #       public double getCoefficient(@SuppressWarnings("unused") int radialExpansion) {
    #         return 1.0;
    #       }
    #     };
    #   }

    #   /**
    #    * 
    #    * @param a
    #    * @param scaleFactor
    #    * @return
    #    */
    #   public static CoefficientExpansion1D scale(final CoefficientExpansion1D a,
    #       final double scaleFactor) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return a.getLowerBoundIndex();
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return a.getUpperBoundIndex();
    #       }

    #       @Override
    #       public double getCoefficient(int radialExpansion) {
    #         return scaleFactor * a.getCoefficient(radialExpansion);
    #       }
    #     };
    #   }

    #   /**
    #    * 
    #    * @param firstRadialExpansionNumber
    #    * @param lastRadialExpansionNumber
    #    * @param constant
    #    * @return
    #    */
    #   public static CoefficientExpansion1D createConstant(final int firstRadialExpansionNumber,
    #       final int lastRadialExpansionNumber, final double constant) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return lastRadialExpansionNumber;
    #       }

    #       @Override
    #       public double getCoefficient(@SuppressWarnings("unused") int radialExpansion) {
    #         return constant;
    #       }
    #     };
    #   }

    #   /**
    #    * 
    #    * @param a
    #    * @param b
    #    * @return
    #    */
    #   public static CoefficientExpansion1D add(final CoefficientExpansion1D a,
    #       final CoefficientExpansion1D b) {

    #     checkArgument(a.getLowerBoundIndex() == b.getLowerBoundIndex());
    #     checkArgument(a.getUpperBoundIndex() == b.getUpperBoundIndex());

    #     final int firstExpansion = a.getLowerBoundIndex();
    #     final int lastExpansion = a.getUpperBoundIndex();

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return firstExpansion;
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return lastExpansion;
    #       }

    #       @Override
    #       public double getCoefficient(int radialExpansion) {
    #         return a.getCoefficient(radialExpansion) + b.getCoefficient(radialExpansion);
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
    #   public static CoefficientExpansion2D createNullExpansion(int firstAzimuthalExpansionNumber,
    #       int firstRadialExpansionNumber, int lastRadialExpansionNumber) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return firstAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return firstAzimuthalExpansionNumber - 1;
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return lastRadialExpansionNumber;

    #       }

    #       @Override
    #       public double getCoefficient(@SuppressWarnings("unused") int iIndex,
    #           @SuppressWarnings("unused") int jIndex) {
    #         throw new UnsupportedOperationException();
    #       }
    #     };

    #   }

    #   /**
    #    * 
    #    * @param expansion
    #    * @return
    #    */
    #   public static CoefficientExpansion2D negate(final CoefficientExpansion2D expansion) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return expansion.getILowerBoundIndex();
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return expansion.getIUpperBoundIndex();
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return expansion.getJLowerBoundIndex();
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return expansion.getJUpperBoundIndex();
    #       }

    #       @Override
    #       public double getCoefficient(int iExpansion, int kExpansion) {
    #         return -expansion.getCoefficient(iExpansion, kExpansion);
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
    #   public static CoefficientExpansion2D createConstant(final int firstAzimuthalExpansionNumber,
    #       final int lastAzimuthalExpansionNumber, final int firstRadialExpansionNumber,
    #       final int lastRadialExpansionNumber, double constant) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return firstAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return lastAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return lastRadialExpansionNumber;
    #       }

    #       @Override
    #       public double getCoefficient(@SuppressWarnings("unused") int azimuthalExpansion,
    #           @SuppressWarnings("unused") int radialExpansion) {
    #         return constant;
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
    #   public static CoefficientExpansion2D createUnity(final int firstAzimuthalExpansionNumber,
    #       final int lastAzimuthalExpansionNumber, final int firstRadialExpansionNumber,
    #       final int lastRadialExpansionNumber) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return firstAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return lastAzimuthalExpansionNumber;
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return firstRadialExpansionNumber;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return lastRadialExpansionNumber;
    #       }

    #       @Override
    #       public double getCoefficient(@SuppressWarnings("unused") int azimuthalExpansion,
    #           @SuppressWarnings("unused") int radialExpansion) {
    #         return 1.0;
    #       }
    #     };
    #   }

    #   /**
    #    * 
    #    * @param a
    #    * @param scaleFactor
    #    * @return
    #    */
    #   public static CoefficientExpansion2D scale(final CoefficientExpansion2D a,
    #       final double scaleFactor) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return a.getILowerBoundIndex();
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return a.getIUpperBoundIndex();
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return a.getJLowerBoundIndex();
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return a.getJUpperBoundIndex();
    #       }

    #       @Override
    #       public double getCoefficient(int azimuthalExpansion, int radialExpansion) {
    #         return scaleFactor * a.getCoefficient(azimuthalExpansion, radialExpansion);
    #       }

    #     };

    #   }

    #   /**
    #    * 
    #    * @param a
    #    * @param b
    #    * @return
    #    */
    #   public static CoefficientExpansion2D add(final CoefficientExpansion2D a,
    #       final CoefficientExpansion2D b) {

    #     // check that all the indices are identical
    #     checkArgument(a.getILowerBoundIndex() == b.getILowerBoundIndex());
    #     checkArgument(a.getIUpperBoundIndex() == b.getIUpperBoundIndex());

    #     checkArgument(a.getJLowerBoundIndex() == b.getJLowerBoundIndex());
    #     checkArgument(a.getJUpperBoundIndex() == b.getJUpperBoundIndex());

    #     final int firstAzimuthalExpansion = a.getILowerBoundIndex();
    #     final int lastAzimuthalExpansion = a.getIUpperBoundIndex();

    #     final int firstRadialExpansion = a.getJLowerBoundIndex();
    #     final int lastRadialExpansion = a.getJUpperBoundIndex();

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return firstAzimuthalExpansion;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return lastAzimuthalExpansion;
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return firstRadialExpansion;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return lastRadialExpansion;
    #       }

    #       @Override
    #       public double getCoefficient(int azimuthalExpansion, int radialExpansion) {
    #         return a.getCoefficient(azimuthalExpansion, radialExpansion)
    #             + b.getCoefficient(azimuthalExpansion, radialExpansion);
    #       }

    #     };

    #   }

    #   // public static CoefficientExpansion2D addAll(final CoefficientExpansion2D... coeffs) {
    #   // return new CoefficientExpansion2D() {
    #   //
    #   // @Override
    #   // public int getJUpperBoundIndex() {
    #   // // TODO Auto-generated method stub
    #   // return 0;
    #   // }
    #   //
    #   // @Override
    #   // public int getJLowerBoundIndex() {
    #   // // TODO Auto-generated method stub
    #   // return 0;
    #   // }
    #   //
    #   // @Override
    #   // public int getIUpperBoundIndex() {
    #   // // TODO Auto-generated method stub
    #   // return 0;
    #   // }
    #   //
    #   // @Override
    #   // public int getILowerBoundIndex() {
    #   // // TODO Auto-generated method stub
    #   // return 0;
    #   // }
    #   //
    #   // @Override
    #   // public double getCoefficient(int iIndex, int jIndex) {
    #   // double sum = 0.0;
    #   // for (CoefficientExpansion2D c : coeffs) {
    #   // sum += c.getCoefficient(iIndex, jIndex);
    #   // }
    #   // return sum;
    #   // }
    #   // };
    #   // }

    #   /**
    #    * Converts the supplied 2D coefficient expansion by converting it to a 1D coefficient expansion.
    #    * The fast index is the second index.
    #    * 
    #    * @param data
    #    * @param lowerBoundIndex
    #    * @return
    #    */
    #   public static CoefficientExpansion1D convertTo1D(final CoefficientExpansion2D data,
    #       int lowerBoundIndex) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return lowerBoundIndex;
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return getLowerBoundIndex() + data.iSize() * data.jSize() - 1;
    #       }

    #       @Override
    #       public double getCoefficient(int index) {

    #         int shiftedIndex = index - lowerBoundIndex;

    #         int iIndex = data.getILowerBoundIndex() + shiftedIndex / data.jSize();
    #         int jIndex = data.getJLowerBoundIndex() + shiftedIndex % data.jSize();

    #         return data.getCoefficient(iIndex, jIndex);
    #       }
    #     };

    #   }

    #   /**
    #    * Converts the supplied 1D coefficient expansion by converting it to a 2D coefficient expansion.
    #    * The fast index is the second index.
    #    * <p>
    #    * This is not view friendly, as the size of the returned {@link CoefficientExpansion2D} is
    #    * determined at construction time (although the values are view friendly).
    #    * 
    #    * @param data
    #    * @param iLowerBoundIndex
    #    * @param jLowerBoundIndex
    #    * @return
    #    */
    #   public static CoefficientExpansion2D convertTo2D(final CoefficientExpansion1D data,
    #       int iLowerBoundIndex, int iUpperBoundIndex, int jLowerBoundIndex, int jUpperBoundIndex) {

    #     return new CoefficientExpansion2D() {

    #       @Override
    #       public int getILowerBoundIndex() {
    #         return iLowerBoundIndex;
    #       }

    #       @Override
    #       public int getIUpperBoundIndex() {
    #         return iUpperBoundIndex;
    #       }

    #       @Override
    #       public int getJLowerBoundIndex() {
    #         return jLowerBoundIndex;
    #       }

    #       @Override
    #       public int getJUpperBoundIndex() {
    #         return jUpperBoundIndex;
    #       }

    #       @Override
    #       public double getCoefficient(int iIndex, int jIndex) {

    #         int shiftedIndex = (iIndex - iLowerBoundIndex) * jSize() + (jIndex - jLowerBoundIndex);

    #         return data.getCoefficient(shiftedIndex + data.getLowerBoundIndex());
    #       }

    #     };

    #   }

    #   /**
    #    * Wraps two {@link CoefficientExpansion1D}s by concatenating them together.
    #    * 
    #    * @param a
    #    * @param b
    #    * @return
    #    */
    #   public static CoefficientExpansion1D concat(final CoefficientExpansion1D a,
    #       final CoefficientExpansion1D b) {

    #     return new CoefficientExpansion1D() {

    #       @Override
    #       public int getLowerBoundIndex() {
    #         return a.getLowerBoundIndex();
    #       }

    #       @Override
    #       public int getUpperBoundIndex() {
    #         return a.getLowerBoundIndex() + a.size() + b.size() - 1;
    #       }

    #       @Override
    #       public double getCoefficient(int index) {

    #         if (index > a.getUpperBoundIndex()) {

    #           int shiftedIndex = index - a.getUpperBoundIndex() + b.getLowerBoundIndex() - 1;

    #           return b.getCoefficient(shiftedIndex);
    #         }
    #         return a.getCoefficient(index);
    #       }
    #     };

    #   }

    # }
