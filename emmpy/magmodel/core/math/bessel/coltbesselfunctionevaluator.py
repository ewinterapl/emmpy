"""emmpy.magmodel.core.math.bessel.coltbesselfunctionevaluator"""

# package magmodel.core.math.bessel;

# import static crucible.core.math.CrucibleMath.abs;

class ColtBesselFunctionEvaluator:
    pass

# /**
#  * An implementation of a {@link BesselFunctionEvaluator} using the Colt library.
#  * 
#  * @author G.K.Stephens
#  *
#  */
# public class ColtBesselFunctionEvaluator implements BesselFunctionEvaluator {

#   @Override
#   public double besselj0(double x) {
#     return ColtBessel.j0(x);
#   }

#   @Override
#   public double besselj1(double x) {
#     return ColtBessel.j1(x);
#   }

#   @Override
#   public double besseljn(int n, double x) {
#     /*
#      * TODO Ugh, when x is small but non-zero, the Colt evaluator will often return NaNs. This is a
#      * bug in their algorithm, that looks like the recursive algorithm gets so small that it is
#      * smaller than the smallest double. Tsyganenko's code has the same problem, so Sasha fixed it
#      * with the following change. This is a hack though, the algorithm should be fixed.
#      */
#     if (abs(n) > 1 && abs(x) < 1.0E-12) {
#       return 0.0;
#     }
#     return ColtBessel.jn(n, x);
#   }

#   @Override
#   public double[] besselj0jn(int n, double x) {

#     double[] bessels = new double[n + 1];

#     for (int nn = 0; nn <= n; nn++) {
#       bessels[nn] = besseljn(nn, x);
#     }

#     return bessels;
#   }

# }
