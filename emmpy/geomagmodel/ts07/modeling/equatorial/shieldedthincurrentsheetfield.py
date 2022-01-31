"""A shielded this current sheet field.

A shielded this current sheet field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.geomagmodel.ts07.modeling.equatorial.thinasymmetriccurrentsheetbasisvectorshieldingfield import (
    ThinAsymmetricCurrentSheetBasisVectorShieldingField
)
from emmpy.magmodel.core.math.expansions.arrayexpansion1d import ArrayExpansion1D
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
)
from emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield import (
    ThinAsymmetricCurrentSheetBasisVectorField
)


class ShieldedThinCurrentSheetField(BasisVectorField):
    """A shielded this current sheet field.

    A shielded this current sheet field.

    Attributes
    ----------
    thinCurrentSheet : ThinAsymmetricCurrentSheetBasisVectorField
        thinCurrentSheet
    thinCurrentSheetShield : ThinAsymmetricCurrentSheetBasisVectorShieldingField
        thinCurrentSheetShield
    includeShield : bool
        True to include the shielding field, else False.
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, thinCurrentSheet, thinCurrentSheetShield,
        includeShield):
        """Initialize a new ShieldedThinCurrentSheetField object.

        Initialize a new ShieldedThinCurrentSheetField object.

        Parameters
        ----------
        thinCurrentSheet : ThinAsymmetricCurrentSheetBasisVectorField
            thinCurrentSheet
        thinCurrentSheetShield : ThinAsymmetricCurrentSheetBasisVectorShieldingField
            thinCurrentSheetShield
        includeShield : bool
            True to include the shielding field, else False.
        """
        self.thinCurrentSheet = thinCurrentSheet
        self.thinCurrentSheetShield = thinCurrentSheetShield
        self.includeShield = includeShield
        self.numAzimuthalExpansions = thinCurrentSheet.numAzimuthalExpansions
        self.numRadialExpansions = thinCurrentSheet.numRadialExpansions

    @staticmethod
    def createUnity(currentSheetHalfThickness, tailLength,
                    staticCoefficients, includeShield):
        """The createUnity method.

        The createUnity method.

        Parameters
        ----------
        currentSheetHalfThickness : DifferentiableScalarFieldIJ
            currentSheetHalfThickness
        tailLength : float
            Tail length,
        staticCoefficients : ThinCurrentSheetShieldingCoefficients
            Static coefficients.
        includeShield : bool
            True to include the shield.
        
        Returns
        -------
        result : ShieldedThinCurrentSheetField
            The shielded field.
        """
        thinCurrentSheet = (
            ThinAsymmetricCurrentSheetBasisVectorField.createUnity(
                tailLength, currentSheetHalfThickness,
                staticCoefficients.numAzimuthalExpansions,
                staticCoefficients.numRadialExpansions)
        )
        thinCurrentSheetShield = ThinAsymmetricCurrentSheetBasisVectorShieldingField(
            staticCoefficients)
        return ShieldedThinCurrentSheetField(
            thinCurrentSheet, thinCurrentSheetShield, includeShield)

    def evaluateExpansions(self, position):
        """Evaluate the expansions at the given position.

        Evaluate the expansions at the given position.

        Parameters
        ----------
        position : VectoriJK
            Position to evaluate the expansions.
        
        Returns
        -------
        result : TailSheetExpansions
            The expansions evaluated at the location.
        """
        equatorialExpansions = (
            self.thinCurrentSheet.evaluateExpansions(position)
        )

        # Calculate the field expansions.
        tailSheetSymmetricValues = equatorialExpansions.tailSheetSymmetricValues
        tailSheetOddValues = equatorialExpansions.tailSheetOddValues
        tailSheetEvenValues = equatorialExpansions.tailSheetEvenValues

        # This is the most expensive lines of the module, If you don't need the
        # shielding, it should NOT be computed. These three lines account for
        # for over 90% of the model evaluation.
        if self.includeShield:
            shield = self.thinCurrentSheetShield.evaluateExpansions(position)
            tailSheetSymmetricShieldValues = shield.tailSheetSymmetricValues
            tailSheetOddShieldValues = shield.tailSheetOddValues
            tailSheetEvenShieldValues = shield.tailSheetEvenValues
            tailSheetSymmetricValues = (
                ArrayExpansion1D.add(tailSheetSymmetricValues,
                                     tailSheetSymmetricShieldValues)
            )
            tailSheetOddValues = Expansion2Ds.Vectors.add(
                tailSheetOddValues, tailSheetOddShieldValues
            )
            tailSheetEvenValues = Expansion2Ds.Vectors.add(
                tailSheetEvenValues, tailSheetEvenShieldValues
            )

        return TailSheetExpansions(tailSheetSymmetricValues, tailSheetOddValues,
                                   tailSheetEvenValues)

    def evaluateExpansion(self, location):
        """Evaluate the expansion at the given location.

        Evaluate the expansion at the given location.

        Parameters
        ----------
        location : VectorIJK
            Location to evaluate the expansion.
        
        Returns
        -------
        result : list of VectorIJK
            Expansion evaluated at location.
        """
        return self.evaluateExpansions(location).getExpansionsAsList()
