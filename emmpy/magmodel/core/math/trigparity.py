"""Trigonometric parity (sine and cosine).

Trigonometric parity (sine and cosine).

A representation of the odd and even parity that exists between the
sine and cosine function. This type of parity often arises in Fourier
series and boundary value problems. Solutions to boundary problems are
often linear combinations of sines and cosines.

EVEN: f(x) = cos(x), df/dx = -sin(x)
ODD: f(x) = sin(x), df/dx = cos(x)

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

from emmpy.crucible.core.math.functions.differentiableunivariatefunction import (
    DifferentiableUnivariateFunction
)


# The even trigonometric parity, the cosine function.
EVEN = DifferentiableUnivariateFunction()
EVEN.evaluate = cos
EVEN.differentiate = lambda t: -sin(t)

# The odd trigonometric parity, the sine function.
ODD = DifferentiableUnivariateFunction()
ODD.evaluate = sin
ODD.differentiate = cos
