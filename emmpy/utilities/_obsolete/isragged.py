"""isRagged.py
"""


def isRagged(a: list) -> bool:
    """If the argument is a ragged array, return True. If not,return False."""
    n = len(a[0])
    for x in a[1:]:
        if len(x) != n:
            return True
    return False
