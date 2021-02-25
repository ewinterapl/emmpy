"""Author : vandejd1 Created : Mar 16, 2010

Copyright (C) 2010 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved

@author vandejd1
"""


# NOTE: This class may have no useful function in the Python version of the
# emmpy code.


from emmpy.crucible.core.collections.reference import Reference


class BasicReference(Reference):
    """This class lets you pass around a singlton container."""

    def __init__(self, obj: object):
        self.__object = obj

    def get(self) -> object:
        return self.__object

    def set(self, obj: object) -> object:
        self.__object = obj
