"""emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses"""


class CurrentSheetHalfThicknesses:
    pass

    # import crucible.core.math.vectorspace.UnwritableVectorIJ;
    # import crucible.crust.vectorfieldsij.DifferentiableScalarFieldIJ;

    # /**
    #  * Utility class to help construct different current sheet thicknesses.
    #  * 
    #  * @author G.K.Stephens
    #  *
    #  */
    # public class CurrentSheetHalfThicknesses {

    #   /**
    #    * no need to construct
    #    */
    #   private CurrentSheetHalfThicknesses() {}

    #   /**
    #    * Returns a constant current sheet half thickness
    #    * 
    #    * @param currentSheetHalfThickness the current sheet half thickness (in <i>R<sub>E</sub></i>)
    #    * @return a newly created {@link DifferentiableScalarFieldIJ} representing the current sheet
    #    *         thickness
    #    */
    #   public static DifferentiableScalarFieldIJ createConstant(final double currentSheetHalfThickness) {

    #     return new DifferentiableScalarFieldIJ() {

    #       @Override
    #       public double differentiateFDj(@SuppressWarnings("unused") UnwritableVectorIJ location) {
    #         return 0;
    #       }

    #       @Override
    #       public double differentiateFDi(@SuppressWarnings("unused") UnwritableVectorIJ location) {
    #         return 0;
    #       }

    #       @Override
    #       public double evaluate(@SuppressWarnings("unused") UnwritableVectorIJ location) {
    #         return currentSheetHalfThickness;
    #       }
    #     };
    #   }

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
