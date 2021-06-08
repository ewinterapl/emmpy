"""Codes for regions for field-aligned currents."""


class FacRegion:
    """Codes for regions for field-aligned currents.

    An enumeration for the two field-aligned current (FAC) configurations,
    region-1 and region-2.

    author G.K.Stephens
    """

    REGION_1 = 1
    REGION_2 = 2

    def __init__(self, number):
        """Build a new object."""
        self.number = number

    def getAsInt(self):
        """Return the region as an integer.

        @return an int associated with the FAC configuration
        (1 = region-1, 2 = region-2)
        """
        return self.number
