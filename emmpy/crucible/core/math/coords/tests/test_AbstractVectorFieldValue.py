import unittest

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class TestAbstractVectorFieldValue(unittest.TestCase):

    def test___init__(self):
        AbstractVectorFieldValue()


if __name__ == '__main__':
    unittest.main()
