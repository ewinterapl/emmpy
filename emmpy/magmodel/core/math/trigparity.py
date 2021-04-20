"""emmpy.magmodel.core.math.trigparity"""

# import static crucible.core.math.CrucibleMath.cos;
# import static crucible.core.math.CrucibleMath.sin;
# import crucible.core.math.functions.DifferentiableUnivariateFunction;


# public enum TrigParity implements DifferentiableUnivariateFunction {
class TrigParity(DifferentiableUnivariateFunction):
    """A representation of the odd and even parity that exists between the sine
    and cosine function. This type of parity often arises in Fourier series and
    boundary value problems. Solutions to boundary problems are often linear
    combinations of sines and cosines.

    EVEN: f(x) = cos(x), df/dx = -sin(x)
    ODD: f(x) = sin(x), df/dx = cos(x)

    @author G.K.Stephens
    """

    def __init__(self):
        """Constructor"""
        pass

    #   /**
    #    * the even trigonometric parity, the cosine function
    #    */
    #   // EVEN(DifferentiableUnivariateFunctions.cosine()),
    #   EVEN(new DifferentiableUnivariateFunction() {
    #     @Override
    #     public double evaluate(double t) {
    #       return cos(t);
    #     }

    #     @Override
    #     public double differentiate(double t) {
    #       return -sin(t);
    #     }
    #   }),

    #   /**
    #    * the odd trigonometric parity, the sine function
    #    */
    #   // ODD(DifferentiableUnivariateFunctions.sine());
    #   ODD(new DifferentiableUnivariateFunction() {
    #     @Override
    #     public double evaluate(double t) {
    #       return sin(t);
    #     }

    #     @Override
    #     public double differentiate(double t) {
    #       return cos(t);
    #     }
    #   });

    #   private final DifferentiableUnivariateFunction function;

    #   private TrigParity(DifferentiableUnivariateFunction function) {
    #     this.function = function;
    #   }

    #   @Override
    #   public double evaluate(double t) {
    #     return function.evaluate(t);
    #   }

    #   @Override
    #   public double differentiate(double t) {
    #     return function.differentiate(t);
    #   }

    # }
