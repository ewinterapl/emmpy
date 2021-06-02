import unittest

from emmpy.crucible.core.collections.abstractreadonlylist import (
    AbstractReadOnlyList
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        AbstractReadOnlyList()


if __name__ == '__main__':
    unittest.main()
