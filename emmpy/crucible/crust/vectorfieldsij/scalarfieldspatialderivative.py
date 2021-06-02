"""emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative"""


class ScalarFieldIJSpatialDerivative:
    """ScalarFieldIJSpatialDerivative"""

    def __init__(self, location):
        """INTERFACE - DO NOT INSTANTIATE.

        param (UnwritableVectorIJK) location
        """
        raise Exception

    def differentiateFDi(self, location):
        """INTERFACE - DO NOT INVOKE.

        param (UnwritableVectorIJK) location
        return (float)
        """
        raise Exception

    def differentiateFDj(self, location):
        """INTERFACE - DO NOT INVOKE.

        param (UnwritableVectorIJK) location
        return (float)
        """
        raise Exception
