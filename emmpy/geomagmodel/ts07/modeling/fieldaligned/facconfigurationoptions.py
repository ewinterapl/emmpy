"""Configuration options for field-aligned currents.

Configuration options for field-aligned currents.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class FacConfigurationOptions:
    """Configuration options for field-aligned currents.
    
    A set of configuration options that tells how to construct a magnetic
    vector field for a Field Aligned Current.

    Attributes
    ----------
    amplitudeScaling : float
        The linear coefficient that determines the strength of the field.
    region : FacRegion
        Region-1 or region-2.
    mode : int
        FAC mode in sin(K*phi).
    trigParity : TrigParity
        The parity even-cos(k*phi) or odd-sin(k*phi).
    theta0 : float
        The center polar angle of the FAC system.
    deltaTheta : float
        The half thickness angle of FAC system.
    smoothed : bool
        True to smooth along theta.
    shielded : bool
        The magnetopause shielding fields should be evaluated, normally
        you should shield the fields.
    """

    def __init__(
        self, amplitudeScaling, region, mode, trigParity, theta0, deltaTheta,
        smoothed, shielded
    ):
        """Initialize a new FacConfigurationOptions object.

        Initialize a new FacConfigurationOptions object.

        Parameters
        ----------
        amplitudeScaling : float
            The linear coefficient that determines the strength of the field.
        region : FacRegion
            Region-1 or region-2.
        mode : int
            FAC mode in sin(K*phi).
        trigParity : TrigParity
            The parity even-cos(k*phi) or odd-sin(k*phi).
        theta0 : float
            The center polar angle of the FAC system.
        deltaTheta : float
            The half thickness angle of FAC system.
        smoothed : bool
            True to smooth along theta.
        shielded : bool
            The magnetopause shielding fields should be evaluated, normally
            you should shield the fields.
        """
        self.amplitudeScaling = float(amplitudeScaling)
        self.region = region
        self.mode = mode
        self.trigParity = trigParity
        self.theta0 = theta0
        self.deltaTheta = float(deltaTheta)
        self.smoothed = smoothed
        self.shielded = shielded
