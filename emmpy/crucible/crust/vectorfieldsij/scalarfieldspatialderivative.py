"""emmpy.crucible.crust.vectorfieldsij.scalarfieldspatialderivative"""


class ScalarFieldIJSpatialDerivative:
    """ScalarFieldIJSpatialDerivative"""

    def __init__(self, location):
        """Interface - do not instantiate."""
        raise Exception

    def differentiateFDi(self, location):
        # Interface - do not invoke.
        raise Exception

    def differentiateFDj(self, location):
        # Interface - do not invoke.
        raise Exception
