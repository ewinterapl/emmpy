"""Author : vandejd1 Created : Mar 16, 2010

Copyright (C) 2010 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved

    @author vandejd1
"""


# NOTE: Since this class was originally a Java interface, all methods will
# raise exceptions.


from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)


class Reference:
    """This interface describes a singlton container."""

    def __init__(self):
        raise CrucibleRuntimeException

    def get(self) -> object:
        raise CrucibleRuntimeException

    def set(self, obj: object) -> None:
        raise CrucibleRuntimeException
