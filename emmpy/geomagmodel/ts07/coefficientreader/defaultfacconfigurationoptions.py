"""Default configuration options for field-aligned currents.

Default configuration options for field-aligned currents.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.geomagmodel.ts07.coefficientreader.facregion import (
    REGION_1, REGION_2
)
from emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions import (
    FacConfigurationOptions
)
from emmpy.magmodel.math.trigparity import EVEN, ODD


class DefaultFacConfigurationOptions:
    """Default configuration options for field-aligned currents.

    Default configuration options for field-aligned currents.

    Attributes
    ----------
    numberOfFields : int
        Number of fields due to field-aligned currents.
    """

    TS07D = 4
    FAC6 = 6
    FAC12 = 12
    FAC16 = 16

    r1_m1_theta0 = 0.7113544659
    r1_m2_theta0 = 0.5567714182
    r2_m1_theta0 = 0.8867880020
    # r2_m2_theta0 = 0.7247997430
    r1_deltaTheta = 0.06
    r2_deltaTheta = 0.09
    shielded = True

    def __init__(self, numberOfFields):
        """Initialize a new DefaultFacConfigurationOptions object.

        Initialize a new DefaultFacConfigurationOptions object.

        Parameters
        ----------
        numberOfFields : int
            Number of fields due to field-aligned currents.
        """
        self.numberOfFields = numberOfFields

    def createFromCoeffs(self, coeffs):
        """Create the options from a set of coefficients.
        
        Create the options from a set of coefficients.
        
        Parameters
        ----------
        coeffs : array-like of float
            Coefficients to use for the field expansion.
        
        Returns
        -------
        result : DefaultFacConfigurationOptions
            FAC expansion built from coefficients.
        
        Raises
        ------
        TypeError
            If invalid parametersm are provided.
        """
        if self.numberOfFields == DefaultFacConfigurationOptions.TS07D:
            return DefaultFacConfigurationOptions.getTs07(coeffs)
        elif self.numberOfFields == DefaultFacConfigurationOptions.FAC6:
            raise TypeError
            # return DefaultFacConfigurationOptions.get6Fac(coeffs)
        elif self.numberOfFields == DefaultFacConfigurationOptions.FAC12:
            raise TypeError
            # return DefaultFacConfigurationOptions.get12Fac(coeffs)
        elif self.numberOfFields == DefaultFacConfigurationOptions.FAC16:
            raise TypeError
            # return DefaultFacConfigurationOptions.get16Fac(coeffs)
        else:
            raise TypeError

    @staticmethod
    def getTs07(coeffs):
        """Get the TS07 field-aligned currents.
        
        Get the TS07 field-aligned currents.

        Parameters
        ----------
        coeffs : array-like of float
            Array of coefficients.
        """
        smoothed = False
        count = 0

        # region 1
        region1Mode1Asym = FacConfigurationOptions(
            coeffs[count], REGION_1, 1, ODD,
            DefaultFacConfigurationOptions.r1_m1_theta0,
            DefaultFacConfigurationOptions.r1_deltaTheta,
            smoothed, DefaultFacConfigurationOptions.shielded
        )
        count += 1
        region1Mode2Asym = FacConfigurationOptions(
            coeffs[count], REGION_1, 2, ODD,
            DefaultFacConfigurationOptions.r1_m2_theta0,
            DefaultFacConfigurationOptions.r1_deltaTheta,
            smoothed, DefaultFacConfigurationOptions.shielded
        )
        count += 1

        # region 2
        region2Mode1Asym = FacConfigurationOptions(
            coeffs[count], REGION_2, 1, ODD,
            DefaultFacConfigurationOptions.r2_m1_theta0,
            DefaultFacConfigurationOptions.r2_deltaTheta,
            smoothed, DefaultFacConfigurationOptions.shielded
        )
        count += 1
        region2Mode1Sym = FacConfigurationOptions(
            coeffs[count], REGION_2, 1, EVEN,
            DefaultFacConfigurationOptions.r2_m1_theta0,
            DefaultFacConfigurationOptions.r2_deltaTheta,
            smoothed, DefaultFacConfigurationOptions.shielded
        )
        count += 1

        return (region1Mode1Asym, region1Mode2Asym, region2Mode1Asym,
                region2Mode1Sym)
