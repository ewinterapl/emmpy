"""emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients"""


class ThinCurrentSheetShieldingCoefficients:
    """This class stores the static coefficients for the TS07D model. These
    are available on the model webpage at
    http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.

    To construct this class, use the {@link TS07DStaticCoefficientsFactory}
    class.

    author Nicholas Sharp
    author G.K.Stephens
    """

    def __init__(
        self, numAzimuthalExpansions, numRadialExpansions,
        symmetricTailExpansion, symmetricTailWaveExpansion,
        oddTailExpansion, oddTailWaveExpansion,
        evenTailExpansion, evenTailWaveExpansion):
        """Constructor is package private, should be constructed using the
        TS07DStaticCoefficientsFactory class."""
        self.numRadialExpansions = numRadialExpansions
        self.numAzimuthalExpansions = numAzimuthalExpansions
        self.symmetricTailExpansion = symmetricTailExpansion
        self.symmetricTailWaveExpansion = symmetricTailWaveExpansion
        self.oddTailExpansion = oddTailExpansion
        self.oddTailWaveExpansion = oddTailWaveExpansion
        self.evenTailExpansion = evenTailExpansion
        self.evenTailWaveExpansion = evenTailWaveExpansion

    def getSymmetricTailExpansion(self):
        return self.symmetricTailExpansion

    def getSymmetricTailWaveExpansion(self):
        return self.symmetricTailWaveExpansion

    def getOddTailExpansion(self):
        return self.oddTailExpansion

    def getOddTailWaveExpansion(self):
        return self.oddTailWaveExpansion

    def getEvenTailExpansion(self):
        return self.evenTailExpansion

    def getEvenTailWaveExpansion(self):
        return self.evenTailWaveExpansion

    def getNumRadialExpansions(self):
        return self.numRadialExpansions

    def getNumAzimuthalExpansions(self):
        return self.numAzimuthalExpansions
