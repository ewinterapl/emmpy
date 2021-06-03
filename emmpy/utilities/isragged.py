"""The isRagged() function detects ragged lists."""


def isRagged(a):
    """If a is a ragged list, return True. If not,return False."""
    if len(a) == 1:
        return False
    n = len(a[0])
    for x in a[1:]:
        if len(x) != n:
            return True
    return False
