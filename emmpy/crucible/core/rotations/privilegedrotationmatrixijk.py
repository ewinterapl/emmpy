"""A rotation matrix without consistency checks.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)


class PrivilegedRotationMatrixIJK(RotationMatrixIJK):
    """A rotation matrix without consistency checks.

    This extension of RotationMatrixIJK exists to allow code in this
    package that is constructing rotation matrices that are valid to
    bypass the checking inherent in the RotationMatrixIJK.setTo() method
    family.

    The basic pattern to utilize this class is, replace this code:

    RotationMatrixIJK buffer;
    buffer.setTo(...);

    with:

    RotationMatrixIJK buffer;
    PrivilegedRotationMatrixIJK assigner = new PrivilegedRotationMatrixIJK();
    assigner.setToWithoutCheck(...);
    buffer.setTo(assigner);

    This will by-pass the check that the final setTo methods on
    RotationMatrixIJK are performing, so it should only be used when the
    values being assigned are clearly a rotation as determined by the
    normal setTo method.

    In performance testing on my mac laptop, I determined that this was as
    fast as disabling the check in the setTo() methods, and over 13 times
    faster than performing the check needlessly.
    """

    def setToWithoutCheck(self, *args):
        """Set the matrix without checks.

        Set the matrix elements without checks for a valid rotation.

        Parameters
        ----------
        data : 3x3 array-like of float
            Values to copy to this object.
        """
        if len(args) == 1:
            # Copy from an existing array.
            (a,) = args
            data = np.array(a)
        elif len(args) == 3:
            # Set with 3 column vectors.
            (ithColumn, jthColumn, kthColumn) = args
            data = np.vstack([np.array(ithColumn),
                              np.array(jthColumn),
                              np.array(kthColumn)]).T
        elif len(args) == 6:
            # 3 column vectors and scale factors.
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK, kthColumn) = args
            data = np.vstack([np.array(ithColumn)*scaleI,
                              np.array(jthColumn)*scaleJ,
                              np.array(kthColumn)*scaleK]).T
        elif len(args) == 9:
            # Set elements in column-major order.
            data = np.array(args).reshape((3, 3)).T
        else:
            raise TypeError
        self[:, :] = data
        return self
