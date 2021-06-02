"""emmpy.magmodel.core.modeling.equatorial.currentsheethalfthicknesses"""


# import crucible.core.math.vectorspace.UnwritableVectorIJ;

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


class CurrentSheetHalfThicknesses:
    """Utility class to help construct different current sheet thicknesses.

    author G.K.Stephens
    """

    @staticmethod
    def createConstant(currentSheetHalfThickness):
        """Return a constant current sheet half thickness

        param (float) currentSheetHalfThickness
        return (DifferentiableScalarFieldIJ)
        """
        dsfij = DifferentiableScalarFieldIJ()
        # UnwritableVectorIJ location
        # Return (float)
        dsfij.differentiateFDi = lambda location: 0
        dsfij.differentiateFDj = lambda location: 0
        dsfij.evaluate = lambda location: currentSheetHalfThickness
        return dsfij
