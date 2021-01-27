import unittest

import emmpy.crucible.core.math.vectorspace.unwritablevectorijk

class TestUnwritableVectorIJK(unittest.TestCase):

    def test___init__(self):
        v = emmpy.crucible.core.math.vectorspace.unwritablevectorijk.UnwritableVectorIJK([1, 2, 3])
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        v = emmpy.crucible.core.math.vectorspace.unwritablevectorijk.UnwritableVectorIJK((1, 2, 3))
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        v2 = emmpy.crucible.core.math.vectorspace.unwritablevectorijk.UnwritableVectorIJK(v)
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        v = emmpy.crucible.core.math.vectorspace.unwritablevectorijk.UnwritableVectorIJK(1, 2, 3)
        self.assertEqual(v.i, 1.0)
        self.assertEqual(v.j, 2.0)
        self.assertEqual(v.k, 3.0)
        
if __name__ == '__main__':
    unittest.main()
