"""emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses"""


from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)


class CurrentSheetHalfThicknesses:
    """Utility class to help construct different current sheet thicknesses.

    author G.K.Stephens
    """

    @staticmethod
    def createConstant(currentSheetHalfThickness):
        """Returns a constant current sheet half thickness

        param (float) currentSheetHalfThickness the current sheet half
        thickness (in R_E)
        return (DifferentiableScalarFieldIJ) a newly created
        DifferentiableScalarFieldIJ representing the current sheet thickness
        """
        dsfij = DifferentiableScalarFieldIJ()
        # These lambdas are not bound methods.
        # UnwritableVectorIJ location
        # These methods all return float.
        dsfij.differentiateFDi = lambda location: 0
        dsfij.differentiateFDj = lambda location: 0
        dsfij.evaluate = lambda location: currentSheetHalfThickness
        return dsfij

    #   /**
    #    * Returns the implementation of the current sheet half-thickness found in Tsyganenko and Sitnov
    #    * 2007, eq. 18
    #    * <p>
    #    * <img src="./doc-files/ts07_eq_18.png" />
    #    * <p>
    #    *
    #    * @param d0 the asymptotic half-thickness of the current sheet in the center of the distant tail
    #    * @param epsilon
    #    * @param alpha rate of current sheet expansion in the sunward direction
    #    * @param beta rate of current sheet expansion in the dawn-dusk direction
    #    *
    #    * @return a newly constructed {@link DifferentiableScalarFieldIJ} of the current sheet
    #    *         half-thickness
    #    */
    #   public static DifferentiableScalarFieldIJ createTs07VariableCurrentSheet(double d0,
    #       double epsilon, double alpha, double beta) {
    #     return new Ts07CurrentSheetHalfThickness(d0, epsilon, alpha, beta);
    #   }

    # }
