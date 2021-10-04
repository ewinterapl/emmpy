"""Check if an object is a real number.

The isRealNumber() function detects real numbers by checking if the object
is a float or int object.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


def isRealNumber(x):
    """Check if an object is a real number.

    If x is a real number (float or int), return True. If not, return
    False.

    Parameters
    ----------
    x : object
        The object to check for real number-ness.

    Returns
    -------
    result : bool
        True if x is a real number, otherwise False.
    """
    if isinstance(x, (float, int)):
        return True
    return False
