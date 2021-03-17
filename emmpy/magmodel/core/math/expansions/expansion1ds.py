"""emmpy.magmodel.core.math.expansionsexpansion1ds"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D
from emmpy.magmodel.core.math.expansions.listexpansion1d import ListExpansion1D


class Expansion1Ds:
    """Expansion1Ds"""

    @staticmethod
    def createFromList(aList, firstRadialExpansionNumber):
        """createFromList

        @param list
        @param firstRadialExpansionNumber
        @return
        @author stephgk1
        """
        return ListExpansion1D(aList, firstRadialExpansionNumber)

    @staticmethod
    def createFromArray(array, firstRadialExpansionNumber):
        """createFromArray

        @param array
        @param firstRadialExpansionNumber
        @return
        """
        return ArrayExpansion1D(array, firstRadialExpansionNumber)

    # NOT SURE HOW TO HANDLE THIS EMBEDDED CLASS YET. IT DOES NOT SEEM
    # TO BE USED ANYWHERE.

#   public static class Vectors {

#     /**
#      * 
#      * @param firstRadialExpansionNumber
#      * @param lastRadialExpansionNumber
#      * @param constant
#      * @return
#      */
#     public static Expansion1D<UnwritableVectorIJK> createConstant(
#         final int firstRadialExpansionNumber, final int lastRadialExpansionNumber,
#         final UnwritableVectorIJK constant) {

#       final UnwritableVectorIJK constantCopy = UnwritableVectorIJK.copyOf(constant);

#       return new Expansion1D<UnwritableVectorIJK>() {

#         @Override
#         public int getUpperBoundIndex() {
#           return lastRadialExpansionNumber;
#         }

#         @Override
#         public int getLowerBoundIndex() {
#           return firstRadialExpansionNumber;
#         }

#         @Override
#         public UnwritableVectorIJK getExpansion(@SuppressWarnings("unused") int radialExpansion) {
#           return constantCopy;
#         }
#       };
#     }

#     /**
#      * 
#      * @param a
#      * @param b
#      * @return
#      */
#     public static Expansion1D<UnwritableVectorIJK> add(final Expansion1D<UnwritableVectorIJK> a,
#         final Expansion1D<UnwritableVectorIJK> b) {

#       checkArgument(a.getLowerBoundIndex() == b.getLowerBoundIndex());
#       checkArgument(a.getUpperBoundIndex() == b.getUpperBoundIndex());

#       final int firstExpansion = a.getLowerBoundIndex();
#       final int lastExpansion = a.getUpperBoundIndex();

#       final UnwritableVectorIJK[] array =
#           new UnwritableVectorIJK[lastExpansion - firstExpansion + 1];

#       return new Expansion1D<UnwritableVectorIJK>() {

#         @Override
#         public int getLowerBoundIndex() {
#           return firstExpansion;
#         }

#         @Override
#         public int getUpperBoundIndex() {
#           return lastExpansion;
#         }

#         @Override
#         public UnwritableVectorIJK getExpansion(int radialExpansion) {

#           UnwritableVectorIJK value = array[radialExpansion - firstExpansion];

#           if (value == null) {
#             value = VectorIJK.add(a.getExpansion(radialExpansion), b.getExpansion(radialExpansion));
#             array[radialExpansion - firstExpansion] = value;
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
#     public static Expansion1D<UnwritableVectorIJK> scale(final Expansion1D<UnwritableVectorIJK> a,
#         final double scaleFactor) {

#       return new Expansion1D<UnwritableVectorIJK>() {

#         @Override
#         public int getLowerBoundIndex() {
#           return a.getLowerBoundIndex();
#         }

#         @Override
#         public int getUpperBoundIndex() {
#           return a.getUpperBoundIndex();
#         }

#         @Override
#         public UnwritableVectorIJK getExpansion(int radialExpansion) {
#           return new UnwritableVectorIJK(scaleFactor, a.getExpansion(radialExpansion));
#         }
#       };
#     }

#     /**
#      * 
#      * @param a
#      * @param scaleFactors
#      * @return
#      */
#     public static Expansion1D<UnwritableVectorIJK> scale(final Expansion1D<UnwritableVectorIJK> a,
#         final CoefficientExpansion1D scaleFactors) {

#       checkArgument(a.getLowerBoundIndex() == scaleFactors.getLowerBoundIndex());
#       checkArgument(a.getUpperBoundIndex() == scaleFactors.getUpperBoundIndex());

#       return new Expansion1D<UnwritableVectorIJK>() {

#         @Override
#         public int getLowerBoundIndex() {
#           return a.getLowerBoundIndex();
#         }

#         @Override
#         public int getUpperBoundIndex() {
#           return a.getUpperBoundIndex();
#         }

#         @Override
#         public UnwritableVectorIJK getExpansion(int radialExpansion) {
#           double scaleFactor = scaleFactors.getCoefficient(radialExpansion);
#           return new UnwritableVectorIJK(scaleFactor, a.getExpansion(radialExpansion));
#         }
#       };
#     }

#     /**
#      * 
#      * @param a
#      * @return
#      */
#     public static UnwritableVectorIJK computeSum(final Expansion1D<UnwritableVectorIJK> a) {

#       double bx = 0.0;
#       double by = 0.0;
#       double bz = 0.0;

#       for (int rad = a.getLowerBoundIndex(); rad <= a.getUpperBoundIndex(); rad++) {
#         UnwritableVectorIJK vect = a.getExpansion(rad);
#         bx += vect.getI();
#         by += vect.getJ();
#         bz += vect.getK();
#       }
#       return new UnwritableVectorIJK(bx, by, bz);
#     }

#   }
