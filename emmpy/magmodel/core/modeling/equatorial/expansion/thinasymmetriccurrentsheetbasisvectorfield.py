"""emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield"""


# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;
# import static magmodel.core.math.expansions.Expansion1Ds.createFromArray;
# import static magmodel.core.math.expansions.Expansion2Ds.createFromArray;
# import static magmodel.core.math.expansions.Expansion2Ds.createNull;
# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.vectorfields.BasisVectorField;

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)


class ThinAsymmetricCurrentSheetBasisVectorField(BasisVectorField):
    """This module described the tail fields as stated in Tsyganenko and Sitnov
    2007

    "Magnetospheric configurations from a high-resolution data-based magnetic
    fields model", eq. 14.

    This is equivalent to the FORTRAN subroutine:
    SUBROUTINE UNWARPED (X,Y,Z,BXS,BYS,BZS,BXO,BYO,BZO,BXE,BYE,BZE)

    @author G.K.Stephens
    """

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs, bessel):
        """Constructor

        @param tailLength
        @param currentSheetHalfThickness
        @param bessel
        """
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        self.numRadialExpansions = coeffs.getNumRadialExpansions()
        self.tailLength = tailLength
        self.currentSheetHalfThickness = currentSheetHalfThickness
        self.bessel = bessel

    @staticmethod
    def createUnity(
        tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
        numRadialExpansions, bessel
    ):
        """Creates a ThinAsymmetricCurrentSheetBasisVectorField where all
        the coefficients have been set to 1.

        @param tailLength
        @param currentSheetHalfThickness
        @param numAzimuthalExpansions
        @param numRadialExpansions
        param bessel
        return
        """
        #   public static ThinAsymmetricCurrentSheetBasisVectorField createUnity(double tailLength,
        #       final DifferentiableScalarFieldIJ currentSheetHalfThickness, int numAzimuthalExpansions,
        #       int numRadialExpansions, BesselFunctionEvaluator bessel) {
        coeffs = TailSheetCoefficients.createUnity(
            numAzimuthalExpansions, numRadialExpansions
        )

        return ThinAsymmetricCurrentSheetBasisVectorField(
            tailLength, currentSheetHalfThickness, coeffs, bessel)

    def evaluate(self, location):
        buffer = VectorIJK()
        #public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
        return buffer.setTo(self.evaluateExpansions(location).sum())

    #   @Override
    #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {
    #     return evaluateExpansions(location).getExpansionsAsList();
    #   }

    def evaluateExpansions(self, location):
        """This guy recalculates everything

        @param positionVector
        @param dipoleTilt
        @param dynamicPressure
        @param includeShield
        """
        symmetricExpansions = [UnwritableVectorIJK() for i in range(numRadialExpansions)]
        oddExpansions = (
            [[UnwritableVectorIJK() for j in numRadialExpansions]
             for i in numAzimuthalExpansions]
        )
        evenExpansions = (
            [[UnwritableVectorIJK() for j in numRadialExpansions]
             for i in numAzimuthalExpansions]
        )

        # n is the radial expansion number
        # for (int n = 1; n <= numRadialExpansions; n++) {
        for n in range(1, self.numRadialExpansions + 1):
            #   // Calculate the wave number (kn = n/rho0)
            #   double kn = n / tailLength;
            # Calculate the wave number (kn = n/rho0)
            kn = n/self.tailLength

            # VectorField symBasisFunction =
            #     new TailSheetSymmetricExpansion(kn, currentSheetHalfThickness, bessel);
            symBasisFunction = TailSheetSymmetricExpansion(
                kn, self.currentSheetHalfThickness, bessel
            )

            #   double a = coeffs.getTailSheetSymmetricValues().getCoefficient(n);
            a = self.coeffs.getTailSheetSymmetricValues().getCoefficient(n)

            #   symmetricExpansions[n - 1] = symBasisFunction.evaluate(location).scale(a);
            symmetricExpansions[n - 1] = symBasisFunction.evaluate(location).scale(a)

            #   // m is the azimuthal expansion number
            #   for (int m = 1; m <= numAzimuthalExpansions; m++) {
            # m is the azimuthal expansion number
            for m in range(1, numAzimuthalExpansions + 1):
                aOdd = self.coeffs.getTailSheetOddValues().getCoefficient(m, n)
                oddBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, TrigParity.ODD, currentSheetHalfThickness, bessel
                )
            #     oddExpansions[m - 1][n - 1] = oddBasisFunction.evaluate(location).scale(aOdd);
            #     double aEven = coeffs.getTailSheetEvenValues().getCoefficient(m, n);
            #     VectorField evenBasisFunction = new TailSheetAsymmetricExpansion(kn, m, TrigParity.EVEN,
            #         currentSheetHalfThickness, bessel);
            #     evenExpansions[m - 1][n - 1] = evenBasisFunction.evaluate(location).scale(aEven);

            #   }

            # }

        #     if (numAzimuthalExpansions == 0) {
        #       return new TailSheetExpansions(createFromArray(symmetricExpansions, 1),
        #           createNull(1, 1, numRadialExpansions), createNull(1, 1, numRadialExpansions));
        #     }

        #     return new TailSheetExpansions(createFromArray(symmetricExpansions, 1),
        #         createFromArray(oddExpansions, 1, 1), createFromArray(evenExpansions, 1, 1));
        #   }

    #   public int getNumAzimuthalExpansions() {
    #     return numAzimuthalExpansions;
    #   }

    #   public int getNumRadialExpansions() {
    #     return numRadialExpansions;
    #   }

    #   @Override
    #   public int getNumberOfBasisFunctions() {
    #     return numRadialExpansions + 2 * numRadialExpansions * numAzimuthalExpansions;
    #   }

    # }
