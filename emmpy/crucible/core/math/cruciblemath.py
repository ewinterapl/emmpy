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


def cbrt(a: float) -> float:
    """Compute the cube root of a value.

    @param value A double value
    @return Value cubic root
    """
    return a**(1/3)


def IEEEremainder(f1: float, f2: float) -> float:
    """Compute IEEE remainder from 2 values.

    NOT CURRENTLY IMPLEMENTED.
    """
    # return FastMath.IEEEremainder(f1, f2);
    raise Exception


def ulp(d: float) -> float:
    """The ULP (Unit in the Last Place) is the distance to the next value
    larger in magnitude.

    NOT CURRENTLY IMPLEMENTED

    @param value A double value
    @return The size of an ulp of the specified value, or Double.MIN_VALUE
    if it is +-0.0, or +Infinity if it is +-Infinity, or NaN if it is NaN.
    """
    # Implemented in Python 3.9
    # return math.ulp(d)
    raise Exception


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


def rint(x: float) -> float:
    """Round value to the nearest integer, as a float.

    @param x A double value
    @return The double mathematical integer closest to the specified value,
    choosing even one if two are equally close, or respectively NaN,
    +-Infinity or +-0.0 if the value is any of these.
    """
    return round(x + (x % 2 - 1 if (x % 1 == 0.5) else 0))
