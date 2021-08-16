"""emmpy.geomagmodel.ts07.modeling.equatorial.thinasymmetriccurrentsheetbasisvectorshieldingfield"""


# import com.google.common.collect.ImmutableList;
# import crucible.core.math.vectorspace.VectorIJK;
# import geomagmodel.ts07.coefficientreader.ThinCurrentSheetShieldingCoefficients;
# import magmodel.core.math.bessel.BesselFunctionEvaluator;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.cylindricalharmonicfield import (
    CylindricalHarmonicField
)
from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions import (
    TailSheetExpansions
)
from emmpy.utilities.nones import nones


class ThinAsymmetricCurrentSheetBasisVectorShieldingField(BasisVectorField):

    def __init__(self, coeffs, bessel):
        """Constructor

        param ThinCurrentSheetShieldingCoefficients coeffs
        param BesselFunctionEvaluator bessel
        """
        # ThinCurrentSheetShieldingCoefficients coeffs
        self.coeffs = coeffs
        # BesselFunctionEvaluator bessel
        self.bessel = bessel
        # int numAzimuthalExpansions
        self.numAzimuthalExpansions = coeffs.getNumAzimuthalExpansions()
        # int numRadialExpansions
        self.numRadialExpansions = coeffs.getNumRadialExpansions()

    def evaluateExpansion(self, location):
        """evaluateExpansion

        param UnwritableVectorIJK location
        return ImmutableList<UnwritableVectorIJK>
        """
        return self.evaluateExpansions(location).getExpansionsAsList()

    def evaluateExpansions(self, location):
        """evaluateExpansions

        param UnwritableVectorIJK location
        return TailSheetExpansions
        """
        # [UnwritableVectorIJK] symmetricExpansions
        symmetricExpansions = nones((self.numRadialExpansions,))
        # [[UnwritableVectorIJK]] oddExpansions, evenExpansions
        oddExpansions = nones((self.numAzimuthalExpansions,
                               self.numRadialExpansions))
        evenExpansions = nones((self.numAzimuthalExpansions,
                                self.numRadialExpansions))
        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):
            # CoefficientExpansion2D tailExpansion
            tailExpansion = (
                self.coeffs.getSymmetricTailExpansion().getExpansion(n)
            )
            # CoefficientExpansion1D waveNumberExpansion
            waveNumberExpansion = (
                self.coeffs.getSymmetricTailWaveExpansion().getExpansion(n)
            )
            buffer = VectorIJK()
            chf = CylindricalHarmonicField(tailExpansion, waveNumberExpansion,
                                           self.bessel, TrigParity.ODD)
            chf.evaluate(location, buffer)
            symmetricExpansions[n - 1] = VectorIJK(
                buffer.i, buffer.j, buffer.k
            )

        # n is the radial expansion number
        # m is the azimuthal expansion number
        # float negateConst
        negateConst = 1.0
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                # CoefficientExpansion2D tailExpansion
                tailExpansion = (
                    self.coeffs.getOddTailExpansion().getExpansion(m, n)
                )
                # CoefficientExpansion1D waveNumberExpansion
                waveNumberExpansion = (
                    self.coeffs.getOddTailWaveExpansion().getExpansion(m, n)
                )
                buffer = VectorIJK()
                chf = CylindricalHarmonicField(
                    tailExpansion, waveNumberExpansion, self.bessel,
                    TrigParity.ODD
                )
                chf.evaluate(location, buffer)
                # buffer.scale(negateConst)
                buffer *= negateConst
                oddExpansions[m - 1][n - 1] = (
                    VectorIJK(buffer.i, buffer.j, buffer.k))

        # n is the radial expansion number
        # m is the azimuthal expansion number
        # float negateConst
        negateConst = -1.0
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                # CoefficientExpansion2D tailExpansion
                tailExpansion = (
                    self.coeffs.getEvenTailExpansion().getExpansion(m, n)
                )
                # CoefficientExpansion1D waveNumberExpansion
                waveNumberExpansion = (
                    self.coeffs.getEvenTailWaveExpansion().getExpansion(m, n)
                )
                buffer = VectorIJK()
                chf = CylindricalHarmonicField(
                    tailExpansion, waveNumberExpansion, self.bessel,
                    TrigParity.EVEN
                )
                chf.evaluate(location, buffer)
                # buffer.scale(negateConst)
                buffer *= negateConst
                evenExpansions[m - 1][n - 1] = (
                    VectorIJK(buffer.i, buffer.j, buffer.k))

        return TailSheetExpansions(Expansion1Ds.createFromArray(symmetricExpansions, 1),
            Expansion2Ds.createFromArray(oddExpansions, 1, 1),
            Expansion2Ds.createFromArray(evenExpansions, 1, 1))

    def getNumberOfBasisFunctions(self):
        """return int"""
        return (
            self.numRadialExpansions +
            2*self.numRadialExpansions*self.numAzimuthalExpansions
        )
