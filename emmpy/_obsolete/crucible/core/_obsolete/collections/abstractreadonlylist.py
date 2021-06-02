from emmpy.crucible.core.collections.abstractsequentialreadonlylist import (
    AbstractSequentialReadOnlyList
)
from emmpy.java.util.randomaccess import RandomAccess


class AbstractReadOnlyList(AbstractSequentialReadOnlyList, RandomAccess):
    pass
