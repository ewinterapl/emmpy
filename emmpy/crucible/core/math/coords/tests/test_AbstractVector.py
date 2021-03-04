# import unittest

# from emmpy.crucible.core.math.coords.abstractvector import (
#     AbstractVector
# )


# class TestAbstractVector(unittest.TestCase):

#     def test___init__(self):
#         AbstractVector(0, 0, 0)

#     def test_getI(self):
#         av = AbstractVector(0.1, 1.2, 2.3)
#         self.assertAlmostEqual(av.getI(), 0.1)

#     def test_getJ(self):
#         av = AbstractVector(0.1, 1.2, 2.3)
#         self.assertAlmostEqual(av.getJ(), 1.2)

#     def test_getK(self):
#         av = AbstractVector(0.1, 1.2, 2.3)
#         self.assertAlmostEqual(av.getK(), 2.3)

#     def test_getVectorIJK(self):
#         av = AbstractVector(0.1, 1.2, 2.3)
#         vijk = av.getVectorIJK()
#         self.assertAlmostEqual(vijk.getI(), 0.1)
#         self.assertAlmostEqual(vijk.getJ(), 1.2)
#         self.assertAlmostEqual(vijk.getK(), 2.3)

#     def test_hashCode(self):
#         av = AbstractVector(0.1, 1.2, 2.3)

# if __name__ == '__main__':
#     unittest.main()