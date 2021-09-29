"""Time-dependent coeffidients for TS07 field-aligned currents.

Time-dependent coeffidients for TS07 field-aligned currents.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


class Ts07FacVariableCoefficients:
    """Time-dependent coeffidients for TS07 field-aligned currents.
    
    Time-dependent coeffidients for TS07 field-aligned currents.
    
    Attributes
    ----------
    region1KappaScaling : float
        Kappa scale factor for FAC region 1.
    region2KappaScaling : float
        Kappa scale factor for FAC region 2.
    facConfigurations : list of FacConfigurationOptions
        FAC configuration options.
    """

    def __init__(
        self, region1KappaScaling, region2KappaScaling, facConfigurations
    ):
        """Initialize a new Ts07FacVariableCoefficients object.

        Initialize a new Ts07FacVariableCoefficients object.

        Parameters
        ----------
        region1KappaScaling : float
            Kappa scale factor for FAC region 1.
        region2KappaScaling : float
            Kappa scale factor for FAC region 2.
        facConfigurations : list of FacConfigurationOptions
            FAC configuration options.
        """
        self.region1KappaScaling = region1KappaScaling
        self.region2KappaScaling = region2KappaScaling
        self.facConfigurations = facConfigurations

    def getRegion1KappaScaling(self):
        """Return the kappa scaling factor for region 1.
        
        Return the kappa scaling factor for region 1.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        result : float
            FAC region 1 kappa scaling factor.
        """
        return self.region1KappaScaling

    def getRegion2KappaScaling(self):
        """Return the kappa scaling factor for region 2.
        
        Return the kappa scaling factor for region 2.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        result : float
            FAC region 2 kappa scaling factor.
        """
        return self.region2KappaScaling

    def getFacConfigurations(self):
        """Return the field-aligned current configurations.
        
        Return the field-aligned current configurations.
        
        Parameters
        ----------
        None

        Returns
        -------
        result : list of FacConfigurationOptions
            FAC configuration options.
        """
        return self.facConfigurations
