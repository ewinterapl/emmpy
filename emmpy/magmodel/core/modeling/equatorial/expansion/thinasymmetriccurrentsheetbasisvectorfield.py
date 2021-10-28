"""Basis vector field for a thin asymmetric current sheet.

Basis vector field for a thin asymmetric current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.trigparity import EVEN, ODD
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetasymmetricexpansion import (
    TailSheetAsymmetricExpansion
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetsymmetricexpansion import (
    TailSheetSymmetricExpansion
)
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class ThinAsymmetricCurrentSheetBasisVectorField(BasisVectorField):
    """Basis vector field for a thin asymmetric current sheet.

    This module described the tail fields as stated in Tsyganenko and
    Sitnov 2007:

    "Magnetospheric configurations from a high-resolution data-based magnetic
    fields model", eq. 14.

    This is equivalent to the FORTRAN subroutine:
    SUBROUTINE UNWARPED (X,Y,Z,BXS,BYS,BZS,BXO,BYO,BZO,BXE,BYE,BZE)

    Attributes
    ----------
    tailLength : float
        Length of tail.
    currentSheetHalfThickness : DifferentiableScalarFieldIJ
        currentSheetHalfThickness
    coeffs : DifferentiableScalarFieldIJ
        Coefficients for expansion.
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, tailLength, currentSheetHalfThickness, coeffs):
        """Initialize a new ThinAsymmetricCurrentSheetBasisVectorField object.

        Initialize a new ThinAsymmetricCurrentSheetBasisVectorField object.

        Parameters
        ----------
        tailLength : float
            Length of tail.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            currentSheetHalfThickness
        coeffs : DifferentiableScalarFieldIJ
            Coefficients for expansion.
        """
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        self.numRadialExpansions = coeffs.numRadialExpansions
        self.tailLength = tailLength
        self.currentSheetHalfThickness = currentSheetHalfThickness

    @staticmethod
    def createUnity(
        tailLength, currentSheetHalfThickness, numAzimuthalExpansions,
        numRadialExpansions
    ):
        """Create a field where all coefficients are unity.

        Creates a ThinAsymmetricCurrentSheetBasisVectorField where all
        the coefficients have been set to 1.

        Parameters
        ----------
        tailLength : float
            Length of tail.
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            currentSheetHalfThickness
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            Number of radial expansions.
        
        Returns
        -------
        result : ThinAsymmetricCurrentSheetBasisVectorField
            Field with all coefficients set to unity.
        """
        coeffs = TailSheetCoefficients.createUnity(
            numAzimuthalExpansions, numRadialExpansions
        )
        return ThinAsymmetricCurrentSheetBasisVectorField(
            tailLength, currentSheetHalfThickness, coeffs)

    def evaluate(self, location):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        buffer : VectorIJK
            Vector result of evaluation at location.
        """
        buffer = VectorIJK()
        buffer[:] = self.evaluateExpansions(location).sum()
        return buffer

    def evaluateExpansion(self, location):
        """Evaluate the expansion.
        
        Evaluate the expansion.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        result : list of VectorIJK
            Components of expansion at location.
        """
        return self.evaluateExpansions(location).getExpansionsAsList()

    def evaluateExpansions(self, location):
        """Recalculate everything.
        
        Recalculate everything.

        Parameters
        ----------
        location : VectorIJK
            Cartesian location for evaluation.
        
        Returns
        -------
        result : TailSheetExpansions
            All expansion components at location.
        """
        # Preallocate the arrays of vectors for the expansions.
        symmetricExpansions = nones((self.numRadialExpansions,))
        oddExpansions = nones((self.numAzimuthalExpansions,
                               self.numRadialExpansions))
        evenExpansions = nones((self.numAzimuthalExpansions,
                                self.numRadialExpansions))
        # n is the radial expansion number.
        for n in range(1, self.numRadialExpansions + 1):

            # Calculate the wave number (kn = n/rho0).
            kn = n/self.tailLength

            symBasisFunction = TailSheetSymmetricExpansion(
                kn, self.currentSheetHalfThickness
            )
            a = self.coeffs.getTailSheetSymmetricValues()[n]
            symmetricExpansions[n - 1] = symBasisFunction.evaluate(CartesianVector(location))*a

            # m is the azimuthal expansion number.
            for m in range(1, self.numAzimuthalExpansions + 1):
                aOdd = self.coeffs.getTailSheetOddValues()[m, n]
                oddBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, ODD, self.currentSheetHalfThickness
                )
                oddExpansions[m - 1][n - 1] = (
                    oddBasisFunction.evaluate(CartesianVector(location))*aOdd)
                aEven = self.coeffs.getTailSheetEvenValues()[m, n]
                evenBasisFunction = TailSheetAsymmetricExpansion(
                    kn, m, EVEN, self.currentSheetHalfThickness
                )
                evenExpansions[m - 1][n - 1] = (
                    evenBasisFunction.evaluate(location)*aEven)

        if self.numAzimuthalExpansions == 0:
            return TailSheetExpansions(
                Expansion1Ds.createFromArray(symmetricExpansions, 1),
                Expansion2Ds.createNull(1, 1, self.numRadialExpansions),
                Expansion2Ds.createNull(1, 1, self.numRadialExpansions)
            )
        return TailSheetExpansions(
            Expansion1Ds.createFromArray(symmetricExpansions, 1),
            Expansion2Ds.createFromArray(oddExpansions, 1, 1),
            Expansion2Ds.createFromArray(evenExpansions, 1, 1)
        )

    def getNumAzimuthalExpansions(self):
        """Return the number of azimuthal expansions.
        
        Return the number of azimuthal expansions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Number of azimuthal expansions.
        """
        return self.numAzimuthalExpansions

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions.
        
        Return the number of basis functions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Total number of basis functions.
        """
        return (
            self.numRadialExpansions +
            2*self.numRadialExpansions*self.numAzimuthalExpansions
        )
