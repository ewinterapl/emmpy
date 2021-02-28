"""Math routines for Crucible

This defines the standard set of Math methods to be used throughout the
Crucible library. This class was created because there are 3rd party
implementations of standard math methods that are much faster compared to the
standard JDK (java.lang.Math) methods.

As of now, the implementation that we have chosen in
https://github.com/jeffhain/jafama

I took the method comments from {@link FastMath}.

@author G.K.Stephens
"""


import math


class CrucibleMath():
    """CrucibleMath"""

    # Switches to the JDK (java.lang.Math) instead. As this should be only be
    # set to true once, and because making this lockable would have performance
    # implications, I choose to make this volatile instead of using
    # AtomicBoolean.
    USE_JDK_MATH = False

    def __init__(self):
        """Constructor

        This class must not be instantiated.
        """
        raise Exception

    @staticmethod
    def useJdkMath() -> None:
        """Specify use of JDK math routines

        Calling this method uses the standard JDK (java.lang.Math) methods
        instead of the preferred Crucible math methods. This is intended to
        be called once at the beginning of the application. Therefore, and
        because of performance considerations, this has not been implemented
        in a thread safe way. To encourage safe use with this method, no
        method has been provided to switch back."""
        CrucibleMath.USE_JDK_MATH = True

    @staticmethod
    def useFastMath() -> None:
        """This shouldn't be called, it is only here for unit testing."""
        CrucibleMath.USE_JDK_MATH = False

    # The value that is closer than any other to e, the base of the natural
    # logarithms.
    E = math.e

    # The value that is closer than any other to pi, the ratio of the
    # circumference of a circle to its diameter.
    PI = math.pi

    @staticmethod
    def sin(a: float) -> float:
        """Compute the sine of an angle.

        @param angle Angle in radians.
        @return Angle sine
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.sin(a)
        return math.sin(a)

    @staticmethod
    def cos(a: float) -> float:
        """Compute the cosine of an angle.

        @param angle Angle in radians.
        @return Angle cosine
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.cos(a)
        return math.cos(a)

    @staticmethod
    def tan(a: float) -> float:
        """Compute the tangent of an angle.

        Can have very bad relative error near +-PI/2, but of the same magnitude
        than the relative delta between StrictMath.tan(PI/2) and
        StrictMath.tan(nextDown(PI/2)).

        @param angle Angle in radians.
        @return Angle tangent
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.tan(a)
        return math.tan(a)

    @staticmethod
    def asin(a: float) -> float:
        """Compute the arcsine of a value.

        @param value Value in [-1,1].
        @return Value arcsine, in radians, in [-PI/2,PI/2]
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.asin(a)
        return math.asin(a)

    @staticmethod
    def acos(a: float) -> float:
        """Compute the arccosine of a value.

        @param value Value in [-1,1].
        @return Value arccosine, in radians, in [0,PI]
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.acos(a)
        return math.acos(a)

    @staticmethod
    def atan(a: float) -> float:
        """Compute the arctangent of a value.

        @param value A double value.
        @return Value arctangent, in radians, in [-PI/2,PI/2]
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.atan(a)
        return math.atan(a)

    @staticmethod
    def toRadians(angdeg: float) -> float:
        """Convert an angle from degrees to radians.

        Gives same result as Math.toRadians for some particular values like
        90.0, 180.0 or 360.0, but is faster (no division).

        @param angdeg Angle value in degrees
        @return Angle value in radians
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.radians(angdeg)
        return math.radians(angdeg)

    @staticmethod
    def toDegrees(angrad: float) -> float:
        """Convert an angle from radians to degrees.

        Gives same result as Math.toDegrees for some particular values like
        Math.PI/2, Math.PI or 2*Math.PI, but is faster (no division).

        @param angrad Angle value in radians
        @return Angle value in degrees
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.degrees(angrad)
        return math.degrees(angrad)

    @staticmethod
    def exp(a: float) -> float:
        """Compute e raised to the specified power.

        @param value A double value
        @return e^value
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.exp(a)
        return math.exp(a)

    @staticmethod
    def log(a: float) -> float:
        """Compute the natural (base e) logarithm of a value.

        @param value A double value
        @return Value logarithm (base e)
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.log(a)
        return math.log(a)

    @staticmethod
    def log10(a: float) -> float:
        """Compute the base-10 logarithm of a value.

        @param value A double value
        @return Value logarithm (base 10)
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.log10(a)
        return math.log10(a)

    @staticmethod
    def sqrt(a: float) -> float:
        """Compute the square root of a value.

        @param value A double value
        @return Value square root
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.sqrt(a)
        return math.sqrt(a)

    @staticmethod
    def cbrt(a: float) -> float:
        """Compute the cube root of a value.

        @param value A double value
        @return Value cubic root
        """
        if CrucibleMath.USE_JDK_MATH:
            return a**(1.0/3.0)
        return a**(1.0/3.0)

    @staticmethod
    def IEEEremainder(f1: float, f2: float) -> float:
        """Compute IEEE remainder from 2 values.

        NOT CURRENTLY IMPLEMENTED.
        """
        if CrucibleMath.USE_JDK_MATH:
            # return Math.IEEEremainder(f1, f2);
            raise Exception
        # return FastMath.IEEEremainder(f1, f2);
        raise Exception

    @staticmethod
    def ceil(a: float) -> int:
        """Compute the ceiling of a value

        @param value A double value
        @return Ceiling of value
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.ceil(a)
        return math.ceil(a)

    @staticmethod
    def floor(a: float) -> int:
        """Compute the floor of a value

        @param value A double value
        @return Floor of value
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.floor(a)
        return math.floor(a)

    @staticmethod
    def atan2(y: float, x: float) -> float:
        """Compute the arctangent from 2 values

        For special values for which multiple conventions could be adopted,
        behaves like Math.atan2(double,double).

        @param y Coordinate on y axis
        @param x Coordinate on x axis
        @return Angle from x axis positive side to (x,y) position, in radians,
        in [-PI,PI]. Angle measure is positive when going from x axis to y
        axis (positive sides).
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.atan2(y, x)
        return math.atan2(y, x)

    @staticmethod
    def pow(a: float, b: float) -> float:
        """Compute a raised to the power b.

        1e-13ish accuracy or better on whole double range.

        @param value A double value
        @param power A power
        @return value^power
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.pow(a, b)
        return math.pow(a, b)

    @staticmethod
    def round(a: float) -> int:
        """Round a value to the nearest integer

        Might have different semantics than Math.round(double), see bugs
        6430675 and 8010430.

        @param value A double value
        @return Value rounded to nearest long, choosing superior long in case
        two are equally close (i.e. rounding-up)
        """
        if CrucibleMath.USE_JDK_MATH:
            return round(a)
        return int(round(a))

    @staticmethod
    def abs(a):
        """Compute the absolute value of a number.

        @param value A numeric value
        @return The absolute value
        """
        if CrucibleMath.USE_JDK_MATH:
            return abs(a)
        return abs(a)

    @staticmethod
    def max(a, b):
        """Determine the greater of 2 numeric values.

        Returns the greater of two numeric values. If the arguments have the
        same value, the result is that same value.

        @param a an argument
        @param b another argument
        @return the larger of {@code a} and {@code b}
        """
        if CrucibleMath.USE_JDK_MATH:
            return max(a, b)
        return max(a, b)

    @staticmethod
    def min(a, b):
        """Determine the lesser of 2 numeric values.

        Returns the smaller of two numeric values. If the arguments have the
        same value, the result is that same value.

        @param a an argument
        @param b another argument
        @return the smaller of {@code a} and {@code b}
        """
        if CrucibleMath.USE_JDK_MATH:
            return min(a, b)
        return min(a, b)

    @staticmethod
    def ulp(d: float) -> float:
        """The ULP (Unit in the Last Place) is the distance to the next value
        larger in magnitude.

        NOT CURRENTLY IMPLEMENTED

        @param value A double value
        @return The size of an ulp of the specified value, or Double.MIN_VALUE
        if it is +-0.0, or +Infinity if it is +-Infinity, or NaN if it is NaN.
        """
        if CrucibleMath.USE_JDK_MATH:
            # Implemented in Python 3.9
            # return math.ulp(d)
            raise Exception
        # return math.ulp(d)
        raise Exception

    @staticmethod
    def signum(d: float) -> float:
        """Return a numeric sign for the value.

        @param value A double value
        @return -1.0 if the specified value is < 0, 1.0 if it is > 0, and the
        value itself if it is NaN or +-0.0.
        """
        if d < 0:
            return -1.0
        elif d > 0:
            return 1.0
        else:
            return 0.0

    @staticmethod
    def sinh(x: float) -> float:
        """Compute the hyperbolic sine of a value.

        Some properties of sinh(x) = (exp(x)-exp(-x))/2:
        1) defined on ]-Infinity,+Infinity[
        2) result in ]-Infinity,+Infinity[
        3) sinh(x) = -sinh(-x) (implies sinh(0) = 0)
        4) sinh(epsilon) ~= epsilon
        5) lim(sinh(x),x->+Infinity) = +Infinity
           (y increasing exponentially faster than x)
        6) reaches +Infinity (double overflow) for x >= 710.475860073944,
           i.e. a bit further than exp(x)

        @param x A double value
        @return Value hyperbolic sine
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.sinh(x)
        return math.sinh(x)

    @staticmethod
    def cosh(x: float) -> float:
        """Compute the hyperbolic cosine of a value.

        Some properties of cosh(x) = (exp(x)+exp(-x))/2:
        1) defined on ]-Infinity,+Infinity[
        2) result in [1,+Infinity[
        3) cosh(0) = 1
        4) cosh(x) = cosh(-x)
        5) lim(cosh(x),x->+Infinity) = +Infinity
           (y increasing exponentially faster than x)
        6) reaches +Infinity (double overflow) for x >= 710.475860073944,
           i.e. a bit further than exp(x)

        @param x A double value
        @return Value hyperbolic cosine
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.cosh(x)
        return math.cosh(x)

    @staticmethod
    def tanh(x: float) -> float:
        """Compute the hyperbolic tangent of a value.

        Some properties of
        tanh(x) = sinh(x)/cosh(x) = (exp(2*x)-1)/(exp(2*x)+1):
        1) defined on ]-Infinity,+Infinity[
        2) result in ]-1,1[
        3) tanh(x) = -tanh(-x) (implies tanh(0) = 0)
        4) tanh(epsilon) ~= epsilon
        5) lim(tanh(x),x->+Infinity) = 1
        6) reaches 1 (double loss of precision) for x = 19.061547465398498

        @param x A double value
        @return Value hyperbolic tangent
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.tanh(x)
        return math.tanh(x)

    @staticmethod
    def acosh(x: float) -> float:
        """Compute the inverse hyperbolic cosine of a value.

        Some properties of acosh(x) = log(x + sqrt(x^2 - 1)):
        1) defined on [1,+Infinity[
        2) result in ]0,+Infinity[ (by convention, since cosh(x) = cosh(-x))
        3) acosh(1) = 0
        4) acosh(1+epsilon) ~= log(1 + sqrt(2*epsilon)) ~= sqrt(2*epsilon)
        5) lim(acosh(x),x->+Infinity) = +Infinity
           (y increasing logarithmically slower than x)

        @param x A double value
        @return Value hyperbolic arccosine
        """
        return math.acosh(x)

    @staticmethod
    def asinh(x: float) -> float:
        """Compute the inverse hyperbolic sine of a value.

        Some properties of asinh(x) = log(x + sqrt(x^2 + 1)):
        1) defined on ]-Infinity,+Infinity[
        2) result in ]-Infinity,+Infinity[
        3) asinh(x) = -asinh(-x) (implies asinh(0) = 0)
        4) asinh(epsilon) ~= epsilon
        5) lim(asinh(x),x->+Infinity) = +Infinity
           (y increasing logarithmically slower than x)

        @param x A double value
        @return Value hyperbolic arcsine
        """
        return math.asinh(x)

    @staticmethod
    def atanh(x: float) -> float:
        """Compute the inverse hyperbolic tangent of a value.

        Some properties of atanh(x) = log((1+x)/(1-x))/2:
        1) defined on ]-1,1[
        2) result in ]-Infinity,+Infinity[
        3) atanh(-1) = -Infinity (by continuity)
        4) atanh(1) = +Infinity (by continuity)
        5) atanh(epsilon) ~= epsilon
        6) lim(atanh(x),x->1) = +Infinity

        @param x A double value
        @return Value hyperbolic arctangent
        """
        return math.atanh(x)

    @staticmethod
    def hypot(x: float, y: float) -> float:
        """Compute the hypotenuse from 2 sides.

        @return sqrt(x^2+y^2) without intermediate overflow or underflow
        """
        if CrucibleMath.USE_JDK_MATH:
            return math.hypot(x, y)
        return math.hypot(x, y)

    @staticmethod
    def rint(x: float) -> float:
        """Round value to the nearest integer, as a float.

        @param x A double value
        @return The double mathematical integer closest to the specified value,
        choosing even one if two are equally close, or respectively NaN,
        +-Infinity or +-0.0 if the value is any of these.
        """
        if CrucibleMath.USE_JDK_MATH:
            return round(x + (x % 2 - 1 if (x % 1 == 0.5) else 0))
        return round(x + (x % 2 - 1 if (x % 1 == 0.5) else 0))
