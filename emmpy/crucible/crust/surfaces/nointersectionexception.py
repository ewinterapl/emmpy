"""emmpy.crucible.crust.surfaces.nointersectionexception"""


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class NoIntersectionException(CrucibleRuntimeException):
    """Exception indicating that an intersection computation has failed.

    In general methods that compute surface intersections, have companion
    methods that return a boolean entitled intersects which test for
    intersection.

    author F.S.Turner
    """

    # Default serial version UID.
    serialVersionUID = 1

    def __init__(self, *args):
        """Constructor"""
        CrucibleRuntimeException.__init__(self, *args)
