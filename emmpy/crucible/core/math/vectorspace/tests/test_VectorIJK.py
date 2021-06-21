"""Tests for VectorIJK."""

from math import pi, sqrt
import unittest

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Build and run the tests."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v1 = VectorIJK()
        self.assertIsInstance(v1, VectorIJK)
        self.assertAlmostEqual(v1.i, 0)
        self.assertAlmostEqual(v1.j, 0)
        self.assertAlmostEqual(v1.k, 0)

    def test_createUnitized(self):
        """Test the createUnitized method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v1 = VectorIJK(i, j, k)
        v2 = v1.createUnitized()
        self.assertIsNot(v2, v1)
        self.assertIsInstance(v2, VectorIJK)
        self.assertAlmostEqual(v2.i, i/length)
        self.assertAlmostEqual(v2.j, j/length)
        self.assertAlmostEqual(v2.k, k/length)

    def test_createNegated(self):
        """Test the createNegated method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK(i, j, k)
        v2 = v1.createNegated()
        self.assertIsNot(v2, v1)
        self.assertAlmostEqual(v2.i, -i)
        self.assertAlmostEqual(v2.j, -j)
        self.assertAlmostEqual(v2.k, -k)

    def test_createScaled(self):
        """Test the createScaled method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        _scale = -2.2
        v1 = VectorIJK(i, j, k)
        v2 = v1.scale(_scale)
        self.assertAlmostEqual(v2.i, i*_scale)
        self.assertAlmostEqual(v2.j, j*_scale)
        self.assertAlmostEqual(v2.k, k*_scale)

    def test_unitize(self):
        """Test the unitize method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v1 = VectorIJK(i, j, k)
        v2 = v1.unitize()
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v1.i, i/length)
        self.assertAlmostEqual(v1.j, j/length)
        self.assertAlmostEqual(v1.k, k/length)
        v1 = VectorIJK(0, 0, 0)
        with self.assertRaises(BugException):
            v1.unitize()

    def test_negate(self):
        """Test the negate method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK(i, j, k)
        v2 = v1.negate()
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, -i)
        self.assertAlmostEqual(v2.j, -j)
        self.assertAlmostEqual(v2.k, -k)

    def test_scale(self):
        """Test the scale method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        _scale = -2.2
        v1 = VectorIJK(i, j, k)
        v2 = v1.scale(_scale)
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v1.i, i*_scale)
        self.assertAlmostEqual(v1.j, j*_scale)
        self.assertAlmostEqual(v1.k, k*_scale)

    def test_clear(self):
        """Test the clear method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK(i, j, k)
        v2 = v1.clear()
        self.assertIs(v2, v1)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 0)
        self.assertAlmostEqual(v2.k, 0)

    def test_setI(self):
        """Test the setI method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        value = 4.4
        v1 = VectorIJK(i, j, k)
        v1.setI(value)
        self.assertAlmostEqual(v1.i, value)

    def test_setJ(self):
        """Test the setJ method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        value = 4.4
        v1 = VectorIJK(i, j, k)
        v1.setJ(value)
        self.assertAlmostEqual(v1.j, value)

    def test_setK(self):
        """Test the setK method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        value = 4.4
        v1 = VectorIJK(i, j, k)
        v1.setK(value)
        self.assertAlmostEqual(v1.k, value)

    def test_set(self):
        """Test the set method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        value = 4.4
        v1 = VectorIJK(i, j, k)
        for index in range(3):
            v1.set(index, value)
            self.assertAlmostEqual(v1[index], value)
        with self.assertRaises(IndexError):
            v1.set(3, value)

    def test_setTo(self):
        """Test the setTo method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK()
        v2 = VectorIJK(i, j, k)
        # 1-argument forms
        # Copy from vector
        v3 = v1.setTo(v2)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, v2.i)
        self.assertAlmostEqual(v3.j, v2.j)
        self.assertAlmostEqual(v3.k, v2.k)
        # Copy from list
        v1 = VectorIJK()
        v3 = v1.setTo([i, j, k])
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # Copy from tuple
        v1 = VectorIJK()
        v3 = v1.setTo((i, j, k))
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # 2-argument forms
        # Scale another vector
        scale = -2.2
        v1 = VectorIJK()
        v2 = VectorIJK([i, j, k])
        v3 = v1.setTo(scale, v2)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, scale*i)
        self.assertAlmostEqual(v3.j, scale*j)
        self.assertAlmostEqual(v3.k, scale*k)
        # List and offset
        v1 = VectorIJK()
        data = [0, i, j, k]
        v3 = v1.setTo(1, data)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # Tuple and offset
        v1 = VectorIJK()
        data = (0, i, j, k)
        v3 = v1.setTo(1, data)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # 3-argument forms
        v1 = VectorIJK()
        v3 = v1.setTo(i, j, k)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, i)
        self.assertAlmostEqual(v3.j, j)
        self.assertAlmostEqual(v3.k, k)
        # Invalid forms
        with self.assertRaises(ValueError):
            v2.setTo()
        with self.assertRaises(ValueError):
            v2.setTo(None)
        with self.assertRaises(ValueError):
            v2.setTo(None, None)
        with self.assertRaises(ValueError):
            v2.setTo(None, None, None, None)

    def test_setToUnitized(self):
        """Test the setToUnitized method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        length = sqrt(i**2 + j**2 + k**2)
        v1 = VectorIJK()
        v2 = VectorIJK(i, j, k)
        v3 = v1.setToUnitized(v2)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, v2.i/length)
        self.assertAlmostEqual(v3.j, v2.j/length)
        self.assertAlmostEqual(v3.k, v2.k/length)

    def setToNegated(self):
        """Test the setToNegated method."""
        (i, j, k) = (1.1, 2.2, 3.3)
        v1 = VectorIJK()
        v2 = VectorIJK(i, j, k)
        v3 = v1.setToNegated(v2)
        self.assertIs(v3, v1)
        self.assertAlmostEqual(v3.i, -v2.i)
        self.assertAlmostEqual(v3.j, -v2.j)
        self.assertAlmostEqual(v3.k, -v2.k)

    def test_rotate(self):
        """Test the rotate method."""
        v1 = VectorIJK(1, 0, 0)
        z_axis = VectorIJK(0, 0, 1)
        angle = pi/2
        v2 = VectorIJK.rotate(v1, z_axis, angle)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)
        v = VectorIJK()
        v2 = VectorIJK.rotate(v1, z_axis, angle, v)
        self.assertIs(v2, v)
        self.assertAlmostEqual(v2.i, 0)
        self.assertAlmostEqual(v2.j, 1)
        self.assertAlmostEqual(v2.k, 0)
        # Invalid forms.
        with self.assertRaises(ValueError):
            VectorIJK.rotate()
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None)
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None, None)
        with self.assertRaises(ValueError):
            VectorIJK.rotate(None, None, None, None, None)

    def test_planeProject(self):
        """Test the planeProject method."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        v3 = VectorIJK.planeProject(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 1)
        self.assertAlmostEqual(v3.k, 1)
        v = VectorIJK()
        v3 = VectorIJK.planeProject(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 1)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.planeProject()

    def test_project(self):
        """Test the project method."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 0, 0)
        # Create the rotated vector.
        v3 = VectorIJK.project(v1, v2)
        self.assertAlmostEqual(v3.i, 1)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 0)
        # Allocate the buffer, then rotate the vector.
        v4 = VectorIJK()
        v5 = VectorIJK.project(v1, v2, v4)
        self.assertIs(v5, v4)
        self.assertAlmostEqual(v5.i, 1)
        self.assertAlmostEqual(v5.j, 0)
        self.assertAlmostEqual(v5.k, 0)
        # Invalid cases.
        with self.assertRaises(Exception):
            VectorIJK.project()
        with self.assertRaises(Exception):
            VectorIJK.project(None)
        with self.assertRaises(Exception):
            VectorIJK.project(None, None, None, None)

    def test_combine(self):
        """Test the combine method."""
        v = VectorIJK()
        v0 = VectorIJK(0, 0, 0)
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(2, 3, 4)
        v3 = VectorIJK(3, 4, 5)
        v4 = VectorIJK(4, 5, 6)
        v5 = VectorIJK(5, 6, 7)
        v6 = VectorIJK(6, 7, 8)
        v7 = VectorIJK(7, 8, 9)
        # 2 vectors
        vc = VectorIJK.combine(1, v0, 2, v1)
        self.assertAlmostEqual(vc.i, 2)
        self.assertAlmostEqual(vc.j, 4)
        self.assertAlmostEqual(vc.k, 6)
        vc = VectorIJK.combine(1, v0, 2, v1, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 2)
        self.assertAlmostEqual(vc.j, 4)
        self.assertAlmostEqual(vc.k, 6)
        # 3 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2)
        self.assertAlmostEqual(vc.i, 8)
        self.assertAlmostEqual(vc.j, 13)
        self.assertAlmostEqual(vc.k, 18)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 8)
        self.assertAlmostEqual(vc.j, 13)
        self.assertAlmostEqual(vc.k, 18)
        # 4 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3)
        self.assertAlmostEqual(vc.i, 20)
        self.assertAlmostEqual(vc.j, 29)
        self.assertAlmostEqual(vc.k, 38)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 20)
        self.assertAlmostEqual(vc.j, 29)
        self.assertAlmostEqual(vc.k, 38)
        # 5 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4)
        self.assertAlmostEqual(vc.i, 40)
        self.assertAlmostEqual(vc.j, 54)
        self.assertAlmostEqual(vc.k, 68)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 40)
        self.assertAlmostEqual(vc.j, 54)
        self.assertAlmostEqual(vc.k, 68)
        # 6 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5)
        self.assertAlmostEqual(vc.i, 70)
        self.assertAlmostEqual(vc.j, 90)
        self.assertAlmostEqual(vc.k, 110)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 70)
        self.assertAlmostEqual(vc.j, 90)
        self.assertAlmostEqual(vc.k, 110)
        # 7 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6)
        self.assertAlmostEqual(vc.i, 112)
        self.assertAlmostEqual(vc.j, 139)
        self.assertAlmostEqual(vc.k, 166)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 112)
        self.assertAlmostEqual(vc.j, 139)
        self.assertAlmostEqual(vc.k, 166)
        # 8 vectors
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, 8, v7)
        self.assertAlmostEqual(vc.i, 168)
        self.assertAlmostEqual(vc.j, 203)
        self.assertAlmostEqual(vc.k, 238)
        vc = VectorIJK.combine(1, v0, 2, v1, 3, v2, 4, v3, 5, v4, 6, v5,
                               7, v6, 8, v7, v)
        self.assertIs(vc, v)
        self.assertAlmostEqual(vc.i, 168)
        self.assertAlmostEqual(vc.j, 203)
        self.assertAlmostEqual(vc.k, 238)
        # Invalid forms
        with self.assertRaises(ValueError):
            VectorIJK.combine()

    def test_uCross(self):
        """Test the uCross method."""
        v = VectorIJK()
        v1 = VectorIJK(2, 0, 0)
        v2 = VectorIJK(0, 3, 0)
        v3 = VectorIJK.uCross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.uCross(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.uCross()

    def test_cross(self):
        """Test the cross method."""
        v = VectorIJK()
        v1 = VectorIJK(1, 0, 0)
        v2 = VectorIJK(0, 1, 0)
        v3 = VectorIJK.cross(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        v3 = VectorIJK.cross(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        with self.assertRaises(Exception):
            VectorIJK.cross()

    def test_pointwiseMultiply(self):
        """Test the pointwiseMultiply method."""
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(4, 5, 6)
        v3 = VectorIJK.pointwiseMultiply(v1, v2)
        self.assertAlmostEqual(v3.i, 4)
        self.assertAlmostEqual(v3.j, 10)
        self.assertAlmostEqual(v3.k, 18)
        v3 = VectorIJK.pointwiseMultiply(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, 4)
        self.assertAlmostEqual(v3.j, 10)
        self.assertAlmostEqual(v3.k, 18)
        with self.assertRaises(Exception):
            VectorIJK.pointwiseMultiply()

    def test_subtract(self):
        """Test the subtract method."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        buffer = VectorIJK()
        # Check without buffer.
        v3 = VectorIJK.subtract(v1, v2)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        # Check with buffer.
        v3 = VectorIJK.subtract(v1, v2, buffer)
        self.assertIs(v3, buffer)
        self.assertAlmostEqual(v3.i, 0)
        self.assertAlmostEqual(v3.j, 0)
        self.assertAlmostEqual(v3.k, 1)
        # Invalid cases.
        with self.assertRaises(Exception):
            VectorIJK.subtract()
        with self.assertRaises(Exception):
            VectorIJK.subtract(None)
        with self.assertRaises(Exception):
            VectorIJK.subtract(None, None, None, None)

    def test_add(self):
        """Test the add method."""
        v1 = VectorIJK(1, 1, 1)
        v2 = VectorIJK(1, 1, 0)
        buffer = VectorIJK()
        # Check without buffer.
        v3 = VectorIJK.add(v1, v2)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        # Check with buffer.
        v3 = VectorIJK.add(v1, v2, buffer)
        self.assertIs(v3, buffer)
        self.assertAlmostEqual(v3.i, 2)
        self.assertAlmostEqual(v3.j, 2)
        self.assertAlmostEqual(v3.k, 1)
        # Invalid cases.
        with self.assertRaises(Exception):
            VectorIJK.add()
        with self.assertRaises(Exception):
            VectorIJK.subtract(None)
        with self.assertRaises(Exception):
            VectorIJK.subtract(None, None, None, None)

    def test_addAll(self):
        """Test the addAll method."""
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK(5, 6, 7)
        v4 = VectorIJK.addAll([v1, v2, v3])
        self.assertAlmostEqual(v4.i, 9)
        self.assertAlmostEqual(v4.j, 12)
        self.assertAlmostEqual(v4.k, 15)
        v4 = VectorIJK.addAll([v1, v2, v3], v)
        self.assertIs(v4, v)
        self.assertAlmostEqual(v4.i, 9)
        self.assertAlmostEqual(v4.j, 12)
        self.assertAlmostEqual(v4.k, 15)
        with self.assertRaises(Exception):
            VectorIJK.addAll()

    def test_addRSS(self):
        """Test the addRSS method."""
        v = VectorIJK()
        v1 = VectorIJK(1, 2, 3)
        v2 = VectorIJK(3, 4, 5)
        v3 = VectorIJK.addRSS(v1, v2)
        self.assertAlmostEqual(v3.i, sqrt(10))
        self.assertAlmostEqual(v3.j, sqrt(20))
        self.assertAlmostEqual(v3.k, sqrt(34))
        v3 = VectorIJK.addRSS(v1, v2, v)
        self.assertIs(v3, v)
        self.assertAlmostEqual(v3.i, sqrt(10))
        self.assertAlmostEqual(v3.j, sqrt(20))
        self.assertAlmostEqual(v3.k, sqrt(34))
        with self.assertRaises(Exception):
            VectorIJK.addRSS()


if __name__ == '__main__':
    unittest.main()
