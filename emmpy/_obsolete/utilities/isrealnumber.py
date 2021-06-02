"""emmpy.utilities.isrealnumber"""


def isRealNumber(x):
    """If the argument is a real number (int or float), return True. If not,
    return False."""
    if isinstance(x, int) or isinstance(x, float):
        return True
    return False
