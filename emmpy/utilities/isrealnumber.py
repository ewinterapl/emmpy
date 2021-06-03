"""The isRealNumber() function detects real numbers."""


def isRealNumber(x):
    """If x is a real number, return True. If not, return False."""
    if isinstance(x, (float, int)):
        return True
    return False
