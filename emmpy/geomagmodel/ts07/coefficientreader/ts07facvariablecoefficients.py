"""Time-dependent coeffidients for TS07 field-aligned currents."""


class Ts07FacVariableCoefficients:
    """Time-dependent coeffidients for TS07 field-aligned currents."""

    def __init__(
        self, region1KappaScaling, region2KappaScaling, facConfigurations
    ):
        """Build a new object."""
        self.region1KappaScaling = region1KappaScaling
        self.region2KappaScaling = region2KappaScaling
        self.facConfigurations = facConfigurations

    def getRegion1KappaScaling(self):
        """Return the kappa scaling factor for region 1."""
        return self.region1KappaScaling

    def getRegion2KappaScaling(self):
        """Return the kappa scaling factor for region 2."""
        return self.region2KappaScaling

    def getFacConfigurations(self):
        """Return the field-aligned current configurations."""
        return self.facConfigurations

    # def getLienarCoefficients(self):
    #     """we must construct a new one every time so that it doesn't change"""
    #     linearCoeefs = [None]*len(self.facConfigurations)
    #     for i in range(len(linearCoeefs)):
    #         linearCoeefs[i] = self.facConfigurations[i].getAmplitudeScaling()
    #     return linearCoeefs
