"""emmpy.geomagmodel.ts07.coefficientreader.facregion"""

class FacRegion:
    """An enumeration for the two field-aligned current (FAC) configurations,
    region-1 and region-2.

    @author G.K.Stephens
    """

    REGION_1 = 1
    REGION_2 = 2

    def __init__(self, number):
        """Constructor"""
        self.number = number

    def getAsInt(self):
        """@return an int associated with the FAC configuration 
        (1 = region-1, 2 = region-2)
        """
        return self.number
