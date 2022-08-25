"""Thin asymmetric current sheet basis vector shielding field.

Thin asymmetric current sheet basis vector shielding field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.math.cylindricalharmonicfield import (
    CylindricalHarmonicField
)
from emmpy.magmodel.math.expansions.arrayexpansion1d import ArrayExpansion1D
from emmpy.magmodel.math.expansions.arrayexpansion2d import ArrayExpansion2D
from emmpy.magmodel.math.trigparity import EVEN, ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class ThinAsymmetricCurrentSheetBasisVectorShieldingField(BasisVectorField):
    """Thin asymmetric current sheet basis vector shielding field.

    Thin asymmetric current sheet basis vector shielding field.

    Attributes
    ----------
    coeffs : ThinCurrentSheetShieldingCoefficients
        Shielding coefficients.
    numAzimuthalExpansions : int
        Number of azimuthal expansions
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, coeffs):
        """Initialize a new object.

        Initialize a new object.

        Parameters
        ----------
        coeffs : ThinCurrentSheetShieldingCoefficients
            Shielding coefficients.
        """
        self.coeffs = coeffs
        self.numAzimuthalExpansions = coeffs.numAzimuthalExpansions
        self.numRadialExpansions = coeffs.numRadialExpansions

    def evaluateExpansion(self, location):
        """Evaluate the expansion at a location.

        Evaluate the expansion at a location.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        
        Returns
        -------
        result : list of VectorIJK
            Expansion evaluated at location.
        """
        return self.evaluateExpansions(location).getExpansionsAsList()

    def evaluateExpansions(self, location):
        """Evaluate the expansions at a location.

        Evaluate the expansions at a location.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        
        Returns
        -------
        result : TailSheetExpansions
            Expansions evaluated at location.
        """
        symmetricExpansions = nones((self.numRadialExpansions,))
        oddExpansions = nones((self.numAzimuthalExpansions,
                               self.numRadialExpansions))
        evenExpansions = nones((self.numAzimuthalExpansions,
                                self.numRadialExpansions))
        # n is the radial expansion number.
        for n in range(self.numRadialExpansions):
            tailExpansion = (
                self.coeffs.symmetricTailExpansion[n]
            )
            waveNumberExpansion = (
                self.coeffs.symmetricTailWaveExpansion[n]
            )
            buffer = VectorIJK()
            chf = CylindricalHarmonicField(tailExpansion, waveNumberExpansion,
                                           ODD)
            chf.evaluate(location, buffer)
            symmetricExpansions[n] = VectorIJK(
                buffer.i, buffer.j, buffer.k
            )

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        negateConst = 1.0
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                tailExpansion = (
                    self.coeffs.oddTailExpansion[m][n]
                )
                waveNumberExpansion = (
                    self.coeffs.oddTailWaveExpansion[m][n]
                )
                buffer = VectorIJK()
                chf = CylindricalHarmonicField(
                    tailExpansion, waveNumberExpansion, ODD)
                chf.evaluate(location, buffer)
                buffer *= negateConst
                oddExpansions[m][n] = (
                    VectorIJK(buffer.i, buffer.j, buffer.k))

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        negateConst = -1.0
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                tailExpansion = (
                    self.coeffs.evenTailExpansion[m][n]
                )
                waveNumberExpansion = (
                    self.coeffs.evenTailWaveExpansion[m][n]
                )
                buffer = VectorIJK()
                chf = CylindricalHarmonicField(
                    tailExpansion, waveNumberExpansion, EVEN)
                chf.evaluate(location, buffer)
                buffer *= negateConst
                evenExpansions[m][n] = (
                    VectorIJK(buffer.i, buffer.j, buffer.k))

        return TailSheetExpansions(ArrayExpansion1D(symmetricExpansions),
            ArrayExpansion2D(oddExpansions),
            ArrayExpansion2D(evenExpansions))

    def getNumberOfBasisFunctions(self):
        """Return the number of basis functions.

        Return the number of basis functions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            The number of basis functions.
        """
        return (
            self.numRadialExpansions +
            2*self.numRadialExpansions*self.numAzimuthalExpansions
        )
