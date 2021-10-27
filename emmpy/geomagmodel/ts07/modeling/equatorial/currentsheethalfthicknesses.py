"""Utility function to help construct different current sheet thicknesses.

Utility function to help construct different current sheet thicknesses.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


def createConstant(currentSheetHalfThickness):
    """Return a constant current sheet half thickness.

    Return a constant current sheet half thickness.

    Parameters
    ----------
    currentSheetHalfThickness : float
        The current sheet half thickness (in R_E).
    
    Returns
    -------
    dsfij : DifferentiableScalarFieldIJ
        The constant half thickness field.
    """
    dsfij = DifferentiableScalarFieldIJ()
    # These lambdas are not bound methods.
    dsfij.differentiateFDi = lambda location: 0
    dsfij.differentiateFDj = lambda location: 0
    dsfij.evaluate = lambda location: currentSheetHalfThickness
    return dsfij
