"""malformedrotationexception.py
"""


class MalformedRotationException(Exception):
    """Simple exception that indicates the specification of a rotation matrix
    is invalid.

    @author F.S.Turner
    """

    # Default serialization ID.
    serialVersionUID = 1

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 1:
            Exception(self, args[0])
        elif len(args) == 2:
            Exception(self, args[0], args[1])
        else:
            raise Exception
