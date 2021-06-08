"""Store the static coefficients for the TS07D model."""


class ThinCurrentSheetShieldingCoefficients:
    """Store the static coefficients for the TS07D model.

    This class stores the static coefficients for the TS07D model. These
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
        """Build a new object.

        Constructor is package private, should be constructed using the
        TS07DStaticCoefficientsFactory class.
        """
        self.numRadialExpansions = numRadialExpansions
        self.numAzimuthalExpansions = numAzimuthalExpansions
        self.symmetricTailExpansion = symmetricTailExpansion
        self.symmetricTailWaveExpansion = symmetricTailWaveExpansion
        self.oddTailExpansion = oddTailExpansion
        self.oddTailWaveExpansion = oddTailWaveExpansion
        self.evenTailExpansion = evenTailExpansion
        self.evenTailWaveExpansion = evenTailWaveExpansion

    def getSymmetricTailExpansion(self):
        """Return the symmetric tail expansion."""
        return self.symmetricTailExpansion

    def getSymmetricTailWaveExpansion(self):
        """Return the symmetric tail wave expansion."""
        return self.symmetricTailWaveExpansion

    def getOddTailExpansion(self):
        """Return the odd tail expansion."""
        return self.oddTailExpansion

    def getOddTailWaveExpansion(self):
        """Return the odd tail wve expansion."""
        return self.oddTailWaveExpansion

    def getEvenTailExpansion(self):
        """Return the even tail expansion."""
        return self.evenTailExpansion

    def getEvenTailWaveExpansion(self):
        """Return the even tail wave expansion."""
        return self.evenTailWaveExpansion

    def getNumRadialExpansions(self):
        """Return the number of radial expanions."""
        return self.numRadialExpansions

    def getNumAzimuthalExpansions(self):
        """Return the number of azimuthal expansions."""
        return self.numAzimuthalExpansions
