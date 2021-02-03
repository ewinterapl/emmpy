# package crucible.core.math;

# import com.google.common.annotations.VisibleForTesting;

# import net.jafama.FastMath;

# /**
#  * This defines the standard set of Math methods to be used throughout the Crucible library. This
#  * class was created because there are 3rd party implementations of standard math methods that are
#  * much faster compared to the standard JDK (java.lang.Math) methods.
#  * <p>
#  * As of now, the implementation that we have chosen in
#  * <a href="https://github.com/jeffhain/jafama">JAFAMA</a>
#  * <p>
#  * I took the method comments from {@link FastMath}.
#  * 
#  * @author G.K.Stephens
#  *
#  */

import math

class CrucibleMath():

    #   /*
    #    * Switches to the JDK (java.lang.Math) instead. As this should be only be set to true once, and
    #    * because making this lockable would have performance implications, I choose to make this
    #    * volatile instead of using AtomicBoolean.
    #    */
    USE_JDK_MATH = False

    #   /**
    #    * Constructor should be private
    #    */
    def __init__(self):
        raise Exception

    #   /**
    #    * Calling this method uses the standard JDK (java.lang.Math) methods instead of the preferred
    #    * Crucible math methods. This is intended to be called once at the beginning of the application.
    #    * Therefore, and because of performance considerations, this has not been implemented in a thread
    #    * safe way. To encourage safe use with this method, no method has been provided to switch back.
    #    */
    @classmethod
    def useJdkMath(cls):
        cls.USE_JDK_MATH = True

    #   /**
    #    * This shouldn't be called, it is only here for unit testing.
    #    */
    #   @VisibleForTesting
    @classmethod
    def useFastMath(cls):
        cls.USE_JDK_MATH = False

    #   /**
    #    * The {@code double} value that is closer than any other to <i>e</i>, the base of the natural
    #    * logarithms.
    #    */
    E = math.e

    #   /**
    #    * The {@code double} value that is closer than any other to <i>pi</i>, the ratio of the
    #    * circumference of a circle to its diameter.
    #    */
    PI = math.pi

    #   /**
    #    * @param angle Angle in radians.
    #    * @return Angle sine.
    #    */
    @classmethod
    def sin(cls, a):
        if cls.USE_JDK_MATH:
            return math.sin(a)
        return math.sin(a)

    #   /**
    #    * @param angle Angle in radians.
    #    * @return Angle cosine.
    #    */
    @classmethod
    def cos(cls, a):
        if cls.USE_JDK_MATH:
            return math.cos(a)
        return math.cos(a)

    #   /**
    #    * Can have very bad relative error near +-PI/2, but of the same magnitude than the relative delta
    #    * between StrictMath.tan(PI/2) and StrictMath.tan(nextDown(PI/2)).
    #    * 
    #    * @param angle Angle in radians.
    #    * @return Angle tangent.
    #    */
    @classmethod
    def tan(cls, a):
        if cls.USE_JDK_MATH:
            return math.tan(a)
        return math.tan(a)

    #   /**
    #    * @param value Value in [-1,1].
    #    * @return Value arcsine, in radians, in [-PI/2,PI/2].
    #    */
    @classmethod
    def asin(cls, a):
        if cls.USE_JDK_MATH:
            return math.asin(a)
        return math.asin(a)

    #   /**
    #    * @param value Value in [-1,1].
    #    * @return Value arccosine, in radians, in [0,PI].
    #    */
    @classmethod
    def acos(cls, a):
        if cls.USE_JDK_MATH:
            return math.acos(a)
        return math.acos(a)

    #   /**
    #    * @param value A double value.
    #    * @return Value arctangent, in radians, in [-PI/2,PI/2].
    #    */
    @classmethod
    def atan(cls, a):
        if cls.USE_JDK_MATH:
            return math.atan(a)
        return math.atan(a)

    #   /**
    #    * Gives same result as Math.toRadians for some particular values like 90.0, 180.0 or 360.0, but
    #    * is faster (no division).
    #    * 
    #    * @param angdeg Angle value in degrees.
    #    * @return Angle value in radians.
    #    */
    @classmethod
    def toRadians(cls, angdeg):
        if cls.USE_JDK_MATH:
            return math.radians(angdeg)
        return math.radians(angdeg)

    #   /**
    #    * Gives same result as Math.toDegrees for some particular values like Math.PI/2, Math.PI or
    #    * 2*Math.PI, but is faster (no division).
    #    * 
    #    * @param angrad Angle value in radians.
    #    * @return Angle value in degrees.
    #    */
    @classmethod
    def toDegrees(cls, angrad):
        if cls.USE_JDK_MATH:
            return math.degrees(angrad)
        return math.degrees(angrad)

    #   /**
    #    * @param value A double value.
    #    * @return e^value.
    #    */
    @classmethod
    def exp(cls, a):
        if cls.USE_JDK_MATH:
            return math.exp(a)
        return math.exp(a)

    #   /**
    #    * @param value A double value.
    #    * @return Value logarithm (base e).
    #    */
    @classmethod
    def log(cls, a):
        if cls.USE_JDK_MATH:
            return math.log(a)
        return math.log(a)

    #   /**
    #    * @param value A double value.
    #    * @return Value logarithm (base 10).
    #    */
    @classmethod
    def log10(cls, a):
        if cls.USE_JDK_MATH:
            return math.log10(a)
        return math.log10(a)

    #   /**
    #    * @param value A double value.
    #    * @return Value square root.
    #    */
    @classmethod
    def sqrt(cls, a):
        if cls.USE_JDK_MATH:
            return math.sqrt(a)
        return math.sqrt(a)

    #   /**
    #    * @param value A double value.
    #    * @return Value cubic root.
    #    */
    @classmethod
    def cbrt(cls, a):
        if cls.USE_JDK_MATH:
            return a**(1.0/3.0)
        return a**(1.0/3.0)

    @classmethod
    def IEEEremainder(cls, f1, f2):
        if cls.USE_JDK_MATH:
            # return Math.IEEEremainder(f1, f2);
            raise Exception
        # return FastMath.IEEEremainder(f1, f2);
        raise Exception

    #   /**
    #    * @param value A double value.
    #    * @return Ceiling of value.
    #    */
    @classmethod
    def ceil(cls, a):
        if cls.USE_JDK_MATH:
            return math.ceil(a)
        return math.ceil(a)

    #   /**
    #    * @param value A double value.
    #    * @return Floor of value.
    #    */
    @classmethod
    def floor(cls, a):
        if cls.USE_JDK_MATH:
            return math.floor(a)
        return math.floor(a)

    #   /**
    #    * For special values for which multiple conventions could be adopted, behaves like
    #    * Math.atan2(double,double).
    #    * 
    #    * @param y Coordinate on y axis.
    #    * @param x Coordinate on x axis.
    #    * @return Angle from x axis positive side to (x,y) position, in radians, in [-PI,PI]. Angle
    #    *         measure is positive when going from x axis to y axis (positive sides).
    #    */
    @classmethod
    def atan2(cls, y, x):
        if cls.USE_JDK_MATH:
            return math.atan2(y, x)
        return math.atan2(y, x)

    #   /**
    #    * 1e-13ish accuracy or better on whole double range.
    #    * 
    #    * @param value A double value.
    #    * @param power A power.
    #    * @return value^power.
    #    */
    @classmethod
    def pow(cls, a, b):
        if cls.USE_JDK_MATH:
            return math.pow(a, b)
        return math.pow(a, b)

    #   /**
    #    * Might have different semantics than Math.round(double), see bugs 6430675 and 8010430.
    #    * 
    #    * @param value A double value.
    #    * @return Value rounded to nearest long, choosing superior long in case two are equally close
    #    *         (i.e. rounding-up).
    #    */
    @classmethod
    def round(cls, a):
        if cls.USE_JDK_MATH:
            return round(a)
        return int(round(a))

    #   /**
    #    * @param value An int value.
    #    * @return The absolute value, except if value is Integer.MIN_VALUE, for which it returns
    #    *         Integer.MIN_VALUE.
    #    */
    @classmethod
    def abs(cls, a):
        if cls.USE_JDK_MATH:
            return abs(a)
        return abs(a)

    #   /**
    #    * Returns the absolute value of a {@code double} value. If the argument is not negative, the
    #    * argument is returned. If the argument is negative, the negation of the argument is returned.
    #    * Special cases:
    #    * <ul>
    #    * <li>If the argument is positive zero or negative zero, the result is positive zero.
    #    * <li>If the argument is infinite, the result is positive infinity.
    #    * <li>If the argument is NaN, the result is NaN.
    #    * </ul>
    #    * In other words, the result is the same as the value of the expression:
    #    * <p>
    #    * {@code Double.longBitsToDouble((Double.doubleToLongBits(a)<<1)>>>1)}
    #    *
    #    * @param a the argument whose absolute value is to be determined
    #    * @return the absolute value of the argument.
    #    */
    #   public static double abs(double a) {
    #     if (USE_JDK_MATH) {
    #       return Math.abs(a);
    #     }
    #     return FastMath.abs(a);
    #   }

    #   /**
    #    * Returns the greater of two {@code int} values. That is, the result is the argument closer to
    #    * the value of {@link Integer#MAX_VALUE}. If the arguments have the same value, the result is
    #    * that same value.
    #    *
    #    * @param a an argument.
    #    * @param b another argument.
    #    * @return the larger of {@code a} and {@code b}.
    #    */
    @classmethod
    def max(cls, a, b):
        if cls.USE_JDK_MATH:
            return max(a, b)
        return max(a, b)

    #   /**
    #    * Returns the greater of two {@code double} values. That is, the result is the argument closer to
    #    * positive infinity. If the arguments have the same value, the result is that same value. If
    #    * either value is NaN, then the result is NaN. Unlike the numerical comparison operators, this
    #    * method considers negative zero to be strictly smaller than positive zero. If one argument is
    #    * positive zero and the other negative zero, the result is positive zero.
    #    *
    #    * @param a an argument.
    #    * @param b another argument.
    #    * @return the larger of {@code a} and {@code b}.
    #    */
    #   public static double max(double a, double b) {
    #     if (USE_JDK_MATH) {
    #       return Math.max(a, b);
    #     }
    #     return FastMath.max(a, b);
    #   }

    #   /**
    #    * Returns the smaller of two {@code int} values. That is, the result the argument closer to the
    #    * value of {@link Integer#MIN_VALUE}. If the arguments have the same value, the result is that
    #    * same value.
    #    *
    #    * @param a an argument.
    #    * @param b another argument.
    #    * @return the smaller of {@code a} and {@code b}.
    #    */
    @classmethod
    def min(cls, a, b):
        if cls.USE_JDK_MATH:
            return min(a, b)
        return min(a, b)

    #   /**
    #    * Returns the smaller of two {@code double} values. That is, the result is the value closer to
    #    * negative infinity. If the arguments have the same value, the result is that same value. If
    #    * either value is NaN, then the result is NaN. Unlike the numerical comparison operators, this
    #    * method considers negative zero to be strictly smaller than positive zero. If one argument is
    #    * positive zero and the other is negative zero, the result is negative zero.
    #    *
    #    * @param a an argument.
    #    * @param b another argument.
    #    * @return the smaller of {@code a} and {@code b}.
    #    */
    #   public static double min(double a, double b) {
    #     if (USE_JDK_MATH) {
    #       return Math.min(a, b);
    #     }
    #     return FastMath.min(a, b);
    #   }

    #   /**
    #    * The ULP (Unit in the Last Place) is the distance to the next value larger in magnitude.
    #    *
    #    * @param value A double value.
    #    * @return The size of an ulp of the specified value, or Double.MIN_VALUE if it is +-0.0, or
    #    *         +Infinity if it is +-Infinity, or NaN if it is NaN.
    #    */
    @classmethod
    def ulp(cls, d):
        if cls.USE_JDK_MATH:
            # Implemented in Python 3.9
            # return math.ulp(d)
            raise Exception
        # return math.ulp(d)
        raise Exception

    #   /**
    #    * @param value A double value.
    #    * @return -1.0 if the specified value is < 0, 1.0 if it is > 0, and the value itself if it is NaN
    #    *         or +-0.0.
    #    */
    @classmethod
    def signum(cls, d):
        # if cls.USE_JDK_MATH:
        #     return math.sign(d)
        # return math.sign(d)
        if d < 0:
            return -1.0
        elif d > 0:
            return 1.0
        else:
            return 0

    #   /**
    #    * Some properties of sinh(x) = (exp(x)-exp(-x))/2: <pre>
    #    * 1) defined on ]-Infinity,+Infinity[
    #    * 2) result in ]-Infinity,+Infinity[
    #    * 3) sinh(x) = -sinh(-x) (implies sinh(0) = 0)
    #    * 4) sinh(epsilon) ~= epsilon
    #    * 5) lim(sinh(x),x->+Infinity) = +Infinity
    #    *    (y increasing exponentially faster than x)
    #    * 6) reaches +Infinity (double overflow) for x >= 710.475860073944,
    #    *    i.e. a bit further than exp(x)
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic sine.
    #    */
    @classmethod
    def sinh(cls, x):
        if cls.USE_JDK_MATH:
            return math.sinh(x)
        return math.sinh(x)

    #   /**
    #    * Some properties of cosh(x) = (exp(x)+exp(-x))/2: <pre>
    #    * 1) defined on ]-Infinity,+Infinity[
    #    * 2) result in [1,+Infinity[
    #    * 3) cosh(0) = 1
    #    * 4) cosh(x) = cosh(-x)
    #    * 5) lim(cosh(x),x->+Infinity) = +Infinity
    #    *    (y increasing exponentially faster than x)
    #    * 6) reaches +Infinity (double overflow) for x >= 710.475860073944,
    #    *    i.e. a bit further than exp(x)
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic cosine.
    #    */
    @classmethod
    def cosh(cls, x):
        if cls.USE_JDK_MATH:
            return math.cosh(x)
        return math.cosh(x)

    #   /**
    #    * Some properties of tanh(x) = sinh(x)/cosh(x) = (exp(2*x)-1)/(exp(2*x)+1): <pre>
    #    * 1) defined on ]-Infinity,+Infinity[
    #    * 2) result in ]-1,1[
    #    * 3) tanh(x) = -tanh(-x) (implies tanh(0) = 0)
    #    * 4) tanh(epsilon) ~= epsilon
    #    * 5) lim(tanh(x),x->+Infinity) = 1
    #    * 6) reaches 1 (double loss of precision) for x = 19.061547465398498
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic tangent.
    #    */
    @classmethod
    def tanh(cls, x):
        if cls.USE_JDK_MATH:
            return math.tanh(x)
        return math.tanh(x)

    #   /**
    #    * Some properties of acosh(x) = log(x + sqrt(x^2 - 1)): <pre>
    #    * 1) defined on [1,+Infinity[
    #    * 2) result in ]0,+Infinity[ (by convention, since cosh(x) = cosh(-x))
    #    * 3) acosh(1) = 0
    #    * 4) acosh(1+epsilon) ~= log(1 + sqrt(2*epsilon)) ~= sqrt(2*epsilon)
    #    * 5) lim(acosh(x),x->+Infinity) = +Infinity
    #    *    (y increasing logarithmically slower than x)
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic arccosine.
    #    */
    @classmethod
    def acosh(cls, x):
        return math.acosh(x)

    #   /**
    #    * Some properties of asinh(x) = log(x + sqrt(x^2 + 1)): <pre>
    #    * 1) defined on ]-Infinity,+Infinity[
    #    * 2) result in ]-Infinity,+Infinity[
    #    * 3) asinh(x) = -asinh(-x) (implies asinh(0) = 0)
    #    * 4) asinh(epsilon) ~= epsilon
    #    * 5) lim(asinh(x),x->+Infinity) = +Infinity
    #    *    (y increasing logarithmically slower than x)
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic arcsine.
    #    */
    @classmethod
    def asinh(cls, x):
        return math.asinh(x)

    #   /**
    #    * Some properties of atanh(x) = log((1+x)/(1-x))/2: <pre>
    #    * 1) defined on ]-1,1[
    #    * 2) result in ]-Infinity,+Infinity[
    #    * 3) atanh(-1) = -Infinity (by continuity)
    #    * 4) atanh(1) = +Infinity (by continuity)
    #    * 5) atanh(epsilon) ~= epsilon
    #    * 6) lim(atanh(x),x->1) = +Infinity
    #    * </pre>
    #    * 
    #    * @param x A double value.
    #    * @return Value hyperbolic arctangent.
    #    */
    @classmethod
    def atanh(cls, x):
        return math.atanh(x)

    #   /**
    #    * @return sqrt(x^2+y^2) without intermediate overflow or underflow.
    #    */
    @classmethod
    def hypot(cls, x, y):
        if cls.USE_JDK_MATH:
            return math.hypot(x, y)
        return math.hypot(x, y)

    #   /**
    #    * @param x A double value.
    #    * @return The double mathematical integer closest to the specified value,
    #    *         choosing even one if two are equally close, or respectively
    #    *         NaN, +-Infinity or +-0.0 if the value is any of these.
    #    */
    @classmethod
    def rint(cls, x):
        if cls.USE_JDK_MATH:
            return round(x + (x % 2 - 1 if (x % 1 == 0.5) else 0))
        return round(x + (x % 2 - 1 if (x % 1 == 0.5) else 0))
