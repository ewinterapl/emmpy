"""Interface for a 1-D expansion.

Interface for a 1-D expansion.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class Expansion1D:
    """Interface for a 1-D expansion.

    An interface representing an arbitrary series expansion, that starts
    at a lower bound index (L) and ends at an upper bound index (U), where
    T is any Object.

    This is similar to an array or List of T, but with a non-zero starting
    index. If the object is a Double, the interface CoefficientExpansion1D
    can be used instead to avoid autoboxing.
    """
