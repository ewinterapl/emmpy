"""Codes for regions for field-aligned currents.

Codes for regions for field-aligned currents.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class FacRegion:
    """Codes for regions for field-aligned currents.

    An enumeration for the two field-aligned current (FAC) configurations,
    region-1 and region-2.

    Attributes
    ----------
    number : int
        Code for the the FAC region.
    """

    REGION_1 = 1
    REGION_2 = 2

    def __init__(self, number):
        """Initialize a new FacRegion object.
        
        Initialize a new FacRegion object.

        Parameters
        ----------
        number : int
            Code for the the FAC region.
        """
        self.number = number

    def getAsInt(self):
        """Return the region as an integer.

        Return the region as an integer.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Code associated with the FAC configuration (1 = region-1,
            2 = region-2)
        """
        return self.number
