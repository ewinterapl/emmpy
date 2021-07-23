"""A rotation matrix without consistency checks."""


from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)


class PrivilegedRotationMatrixIJK(RotationMatrixIJK):
    """A rotation matrix without consistency checks.

    This extension of RotationMatrixIJK exists to allow code in this package
    that is constructing rotation matrices that are valid to bypass the
    checking inherent in the
    RotationMatrixIJK.setTo(double, double, double, double, double, double,
                            double, double, double)
    method family.

    The basic pattern to utilize this class is, replace this code:

    RotationMatrixIJK buffer;
    buffer.setTo(...);

    with:

    RotationMatrixIJK buffer;
    PrivilegedRotationMatrixIJK assigner = new PrivilegedRotationMatrixIJK();
    assigner.setToWithoutCheck(...);
    buffer.setTo(assigner);

    This will by-pass the check that the final setTo methods on
    RotationMatrixIJK are performing, so it should only be used when the values
    being assigned are clearly a rotation as determined by the normal setTo
    method.

    In performance testing on my mac laptop, I determined that this was as fast
    as disabling the check in the setTo() methods, and over 13 times faster
    than performing the check needlessly.

    author F.S.Turner
    """

    def __init__(self):
        """Build a new object."""

    def setToWithoutCheck(self, *args):
        """Set the matrix without checks."""
        if len(args) == 1:
            # RotationMatrixIJK#setTo(double[][])
            (data,) = args
            self.setToWithoutCheck(
                data[0][0], data[1][0], data[2][0],
                data[0][1], data[1][1], data[2][1],
                data[0][2], data[1][2], data[2][2])
            return self
        elif len(args) == 3:
            # see RotationMatrixIJK#setTo(UnwritableVectorIJK,
            # UnwritableVectorIJK, UnwritableVectorIJK)
            (ithColumn, jthColumn, kthColumn) = args
            return self.setToWithoutCheck(
                ithColumn.i, ithColumn.j, ithColumn.k,
                jthColumn.i, jthColumn.j, jthColumn.k,
                kthColumn.i, kthColumn.j, kthColumn.k)
        elif len(args) == 6:
            # see RotationMatrixIJK.setTo(double, UnwritableVectorIJK,
            # double, UnwritableVectorIJK, double, UnwritableVectorIJK)
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            return self.setToWithoutCheck(
                scaleI*ithColumn.getI(), scaleI*ithColumn.getJ(),
                scaleI*ithColumn.getK(),
                scaleJ*jthColumn.getI(), scaleJ*jthColumn.getJ(),
                scaleJ*jthColumn.getK(), scaleK*kthColumn.getI(),
                scaleK*kthColumn.getJ(), scaleK*kthColumn.getK())
        elif len(args) == 9:
            # see RotationMatrixIJK#setTo(double, double, double, double,
            # double, double, double, double, double)
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            self.ii = ii
            self.ji = ji
            self.ki = ki
            self.ij = ij
            self.jj = jj
            self.kj = kj
            self.ik = ik
            self.jk = jk
            self.kk = kk
            return self
        else:
            raise Exception
