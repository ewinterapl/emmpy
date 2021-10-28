"""Store the static coefficients for the TS07D model.

Store the static coefficients for the TS07D model.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class ThinCurrentSheetShieldingCoefficients:
    """Store the static coefficients for the TS07D model.

    This class stores the static coefficients for the TS07D model. These
    are available on the model webpage at
    http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.

    To construct this class, use the TS07DStaticCoefficientsFactor class.

    Attributes
    ----------
    numRadialExpansions : int
        Number of radial expansions.
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    symmetricTailExpansion : CoefficientExpansion2D
        Coefficients for symmetric tail expansion.
    symmetricTailWaveExpansion : CoefficientExpansion1D
        Coefficients for symmetric tail wave expansion.
    oddTailExpansion : CoefficientExpansion2D
        Coefficients for odd tail expansion.
    oddTailWaveExpansion : CoefficientExpansion1D
        Coefficients for odd tail wave expansion.
    evenTailExpansion : CoefficientExpansion2D
        Coefficients for even tail expansion.
    evenTailWaveExpansion : CoefficientExpansion1D
        Coefficients for even tail wave expansion.
    """

    def __init__(
        self, numAzimuthalExpansions, numRadialExpansions,
        symmetricTailExpansion, symmetricTailWaveExpansion,
        oddTailExpansion, oddTailWaveExpansion,
        evenTailExpansion, evenTailWaveExpansion):
        """Initialize a new ThinCurrentSheetShieldingCoefficients object.

        Constructor is package private, should be constructed using the
        TS07DStaticCoefficientsFactory class.

        Parameters
        ----------
        numRadialExpansions : int
            Number of radial expansions.
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        symmetricTailExpansion : CoefficientExpansion2D
            Coefficients for symmetric tail expansion.
        symmetricTailWaveExpansion : CoefficientExpansion1D
            Coefficients for symmetric tail wave expansion.
        oddTailExpansion : CoefficientExpansion2D
            Coefficients for odd tail expansion.
        oddTailWaveExpansion : CoefficientExpansion1D
            Coefficients for odd tail wave expansion.
        evenTailExpansion : CoefficientExpansion2D
            Coefficients for even tail expansion.
        evenTailWaveExpansion : CoefficientExpansion1D
            Coefficients for even tail wave expansion.

        """
        self.numRadialExpansions = numRadialExpansions
        self.numAzimuthalExpansions = numAzimuthalExpansions
        self.symmetricTailExpansion = symmetricTailExpansion
        self.symmetricTailWaveExpansion = symmetricTailWaveExpansion
        self.oddTailExpansion = oddTailExpansion
        self.oddTailWaveExpansion = oddTailWaveExpansion
        self.evenTailExpansion = evenTailExpansion
        self.evenTailWaveExpansion = evenTailWaveExpansion
