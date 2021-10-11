"""Exception for detecting a point on an axis.

This exception should be raised when a point on an axis is detected
during a coordinate transformation.

Authors
-------
The Crucible Developers
Eric Winter (eric.winter@jhuapl.edu)
"""


class PointOnAxisException(Exception):
    """Exception for detecting a point on an axis.

    This exception should be raised when a point on an axis is detected
    during a coordinate transformation.

    Attributes
    ----------
    None
    """

    def __init__(self, *args):
        """Initialize a new PointOnAxisException.

        Initialize a new PointOnAxisException.

        Parameters
        ----------
        args[0] : str or object, optional
            Message or cause of exception.
        args[1] : object, optional
            Cause of exception.
        """
        if len(args) == 0:
            pass
        elif len(args) == 1:
            # args[0] can be message or cause
            Exception.__init__(self, args[0])
        elif len(args) == 2:
            (message, cause) = args
            Exception.__init__(self, message, cause)
