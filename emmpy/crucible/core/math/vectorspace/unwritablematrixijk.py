"""An unwritable 3-D (3x3) matrix.

Authors
-------
F.S.Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


import numpy as np

from emmpy.crucible.core.math.tensors.matrix3d import Matrix3D
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    checkRotation
)
from emmpy.crucible.core.math.vectorspace.malformedrotationexception import (
    MalformedRotationException
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


# Map matrix component names to indices.
components = {'ii': (0, 0), 'ji': (1, 0), 'ki': (2, 0),
              'ij': (0, 1), 'jj': (1, 1), 'kj': (2, 1),
              'ik': (0, 2), 'jk': (1, 2), 'kk': (2, 2)}


class UnwritableMatrixIJK(Matrix3D):
    """An unwritable 3-D matrix.

    A 3-dimensional matrix designed to properly support several
    subclasses.

    Note: Subclass implementers, you should only use the protected fields
    in this class to store the contents of the matrix components,
    otherwise all of the methods here and in the operations class may
    break.

    The fields in this matrix are arranged in the following manner:

    | ii ij ik |
    | ji jj jk |
    | ki kj kk |

    The class prefers column ordering, so when working with vectors and
    this class they are to be considered "column" vectors.
    """

    # One of the two default tolerances that control how close to a rotation
    # a rotation matrix must be. This value determines how far off unity the
    # norm of the column vectors of a matrix must be.
    NORM_TOLERANCE = 1E-4

    # The other of the two default tolerances that control how close to a
    # rotation a rotation matrix must be. This value determines how far off
    # unity the determinant of the matrix must be.
    DETERMINANT_TOLERANCE = 1E-4

    def __new__(cls, *args):
        """Create a new UnwritableMatrixIJK object.

        Allocate a new UnwritableMatrixIJK object by allocating a new
        Matrix3D object on which the UnwritableMatrixIJK will expand.

        Parameters
        ----------
        data : 3x3 (or larger) list of list of float.
            Values to use to initialize the matrix.
        OR
        matrix : UnwritableMatrixIJK
            The matrix whose contents are to be copied.
        OR
        scale : float
            The scale factor to apply.
        matrix : UnwritableMatrix3D
            The matrix whose components are to be scaled and copied.
        OR
        ithColumn, jthColumn, kthColumn - UnwritableVectorIJK
            Vectors to use as the columns of the matrix.
        OR
        scaleI, scaleJ, scaleK : float
            Scale factors to apply to the first, second, third columns
            of the supplied matrix.
        matrix : UnwritableMatrixIJK
            The matrix whose columns are to be scaled.
        OR
        scaleI : float
            The scale factor to apply to the ith column.
        ithColumn : UnwritableVectorIJK
            The vector containing the ith column.
        scaleJ : float
            The scale factor to apply to the jth column.
        jthColumn : UnwritableVectorIJK
            The vector containing the jth column.
        scaleK : float
            The scale factor to apply to the kth column.
        kthColumn : float
            The vector containing the kth column.
        OR
        ii : float
            ith row, ith column element
        ji : float
            jth row, ith column element
        ki : float
            kth row, ith column element
        ij : float
            ith row, jth column element
        jj : float
            jth row, jth column element
        kj : float
            kth row, jth column element
        ik : float
            ith row, kth column element
        jk : float
            jth row, kth column element
        kk : float
            kth row, kth column element

        Returns
        -------
        m : UnwritableMatrixIJK
            The newly-created object.

        Raises
        ------
        ValueError
            If invalid arguments are provided.
        """
        # Create the empty 3x3 matrix for initialization.
        nones = [None]*9
        m = Matrix3D.__new__(cls, *nones)

        # Initialize based on the arguments.
        if len(args) == 0:
            pass
        elif len(args) == 1:
            if isinstance(args[0], list):
                # Construct a matrix from the upper 3x3 block of a 2D
                # array of floats.
                # The values from the data array are copied into the matrix as
                # follows:
                # | data[0][0] data[0][1] data[0][2] |
                # | data[1][0] data[1][1] data[1][2] |
                # | data[2][0] data[2][1] data[2][2] |
                (data,) = args
                m[:] = np.array(data)[:3, :3]
            elif isinstance(args[0], UnwritableMatrixIJK):
                # Copy constructor.
                (matrix,) = args
                m[:] = matrix
            else:
                raise ValueError('Bad arguments for method!')
        elif len(args) == 2:
            # Scaling constructor. Creates a new matrix by applying a
            # scalar multiple to the components of a pre-existing matrix.
            (scale, matrix) = args
            a = np.array(matrix)
            m[:] = scale*a
        elif len(args) == 3:
            # Column vector constructor, creates a new matrix by populating
            # the columns of the matrix with the supplied vectors.
            (ithColumn, jthColumn, kthColumn) = args
            m[:, 0] = ithColumn
            m[:, 1] = jthColumn
            m[:, 2] = kthColumn
        elif len(args) == 4:
            # Column scaling constructor, creates a new matrix by applying
            # scalar multiples to the columns of a pre-existing matrix.
            # and copied
            (scaleI, scaleJ, scaleK, matrix) = args
            m[:, 0] = scaleI*matrix[:, 0]
            m[:, 1] = scaleJ*matrix[:, 1]
            m[:, 2] = scaleK*matrix[:, 2]
        elif len(args) == 6:
            # Scaled column vector constructor, creates a new matrix by
            # populating the columns of the matrix with scaled versions of
            # the supplied vectors
            (scaleI, ithColumn, scaleJ, jthColumn, scaleK,
                kthColumn) = args
            m[:, 0] = scaleI*ithColumn
            m[:, 1] = scaleJ*jthColumn
            m[:, 2] = scaleK*kthColumn
        elif len(args) == 9:
            # Constructs a matrix from the nine basic components.
            (ii, ji, ki, ij, jj, kj, ik, jk, kk) = args
            data = np.array(
                [ii, ji, ki, ij, jj, kj, ik, jk, kk]).reshape((3, 3)).T
            m[:] = data
        else:
            raise ValueError('Bad arguments for method!')

        # Return the new matrix.
        return m

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in
        the commponents dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to get.

        Returns
        -------
        self[(row, col)] : float
            Value of specified attribute (matrix element at name,
            which maps to (row, col).

        Raises
        ------
        AttributeError
            If an illegal attribute name is specified.
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of a computed attribute.

        Set the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in
        the components dictionary.

        Parameters
        ----------
        name : str
            Name of attribute to set.
        value : int or float
            Value for attribute to set

        Returns
        -------
        None

        Raises
        ------
        AttributeError
            If an illegal attribute name is specified.
        """
        self[components[name]] = value

    def createTranspose(self):
        """Create a new, transposed copy of the existing matrix.

        Transpose a copy of the matrix.

        Returns
        -------
        m : UnwritableMatrixIJK
            The transpose of the matrix.
        """
        m = UnwritableMatrixIJK(self.T)
        return m

    def createUnitizedColumns(self):
        """Create a copy of the matrix with unitized columns.

        Unitize each column of the copy independently.

        Returns
        -------
        m : UnwritableMatrixIJK
            The unitized column version of this matrix
        """
        vi = UnwritableVectorIJK(self[:, 0].tolist())
        vj = UnwritableVectorIJK(self[:, 1].tolist())
        vk = UnwritableVectorIJK(self[:, 2].tolist())
        viu = vi.createUnitized()
        vju = vj.createUnitized()
        vku = vk.createUnitized()
        m = UnwritableMatrixIJK(viu, vju, vku)
        return m

    def createInverse(self, *args):
        """Create an inverted copy of the matrix.

        Compute the matrix inverse.

        Parameters
        ----------
        tolerance : float (optional, ignored)
            Inversion tolerance.

        Returns
        -------
        m : UnwritableMatrixIJK
            Inverse of the matrix.
        """
        m = np.linalg.inv(self)
        return m

    def createInvorted(self):
        """Compute the inverse of an orthogonal matrix.

        If this method is invoked on matrices whose columns are not orthogonal,
        the resultant matrix is likely not the inverse sought. Use the more
        general createInverse() method instead.

        Returns
        -------
        m : UnwritableMatrixIJK
            The inverse of this matrix if it is orthogonal.

        Raises
        ------
        BugException
            If this matrix is not orthogonal.
        """
        # First create the transpose, then all that's left is to scale the rows
        # appropriately.
        matrix = self.createInverse()
        return matrix

    def getII(self):
        """Get the ith row, ith column component.

        Returns
        -------
        self[0, 0] : float
            The ith row, ith column value.
        """
        return self[0, 0]

    def getJI(self):
        """Get the jth row, ith column component.

        Returns
        -------
        self[1, 0] : float
            The jth row, ith column value.
        """
        return self[1, 0]

    def getKI(self):
        """Get the Kth row, ith column component.

        Returns
        -------
        self[2, 0] : float
            The kth row, ith column value.
        """
        return self[2, 0]

    def getIJ(self):
        """Get the ith row, jth column component.

        Returns
        -------
        self[0, 1] : float
            The ith row, jth column value.
        """
        return self[0, 1]

    def getJJ(self):
        """Get the jth row, jth column component.

        Returns
        -------
        self[1, 1] : float
            The jth row, jth column value.
        """
        return self[1, 1]

    def getKJ(self):
        """Get the kth row, jth column component.

        Returns
        -------
        self[2, 1] : float
            The kth row, jth column value.
        """
        return self[2, 1]

    def getIK(self):
        """Get the ith row, kth column component.

        Returns
        -------
        self[0, 2] : float
            The ith row, kth column value.
        """
        return self[0, 2]

    def getJK(self):
        """Get the jth row, kth column component.

        Returns
        -------
        self[1, 2] : float
            The jth row, kth column value.
        """
        return self[1, 2]

    def getKK(self):
        """Get the kth row, kth column component.

        Returns
        -------
        self[2, 2] : float
            The kth row, kth column value.
        """
        return self[2, 2]

    def get(self, row, column):
        """Get the component from the specified row and column.

        Parameters
        ----------
        row : int
            Row of element to return (0|1|2).
        column : int
            Column of element to return (0|1|2).

        Returns
        -------
        self[row, column] : float
            The value of the element at [row, column].
        """
        return self[row][column]

    def getIthColumn(self, *args):
        """Copy the ith column components into the supplied vector.

        Copy the contents of column i into a vector and return it. If no
        buffer is provided to hold the results, a new vector is created.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method
        buffer : VectorIJK (optional)
            Buffer to hold result.
        """
        if len(args) == 0:
            buffer = VectorIJK()
        elif len(args) == 1:
            (buffer,) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = self[:, 0]
        return buffer

    def getJthColumn(self, *args):
        """Copy the jth column components into the supplied vector.

        Copy the contents of column j into a vector and return it. If no
        buffer is provided to hold the results, a new vector is created.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method
        buffer : VectorIJK (optional)
            Buffer to hold result.
        """
        if len(args) == 0:
            buffer = VectorIJK()
        elif len(args) == 1:
            (buffer,) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = self[:, 1]
        return buffer

    def getKthColumn(self, *args):
        """Copy the kth column components into the supplied vector.

        Copy the contents of column k into a vector and return it. If no
        buffer is provided to hold the results, a new vector is created.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method
        buffer : VectorIJK (optional)
            Buffer to hold result.
        """
        if len(args) == 0:
            buffer = VectorIJK()
        elif len(args) == 1:
            (buffer,) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = self[:, 2]
        return buffer

    def getColumn(self, *args):
        """Copy the specified column components into the supplied vector.

        Copy the contents of the specified column into a vector and return
        it. If no buffer is provided to hold the results, a new vector is
        created.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method
        columnIndex : int
            Index of column to retrieve (0|1|2).
        buffer : VectorIJK (optional)
            Buffer to hold result.
        """
        if len(args) == 1:
            (columnIndex,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (columnIndex, buffer) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = self[:, columnIndex]
        return buffer

    def getDeterminant(self):
        """Compute the determinant of the matrix.

        Compute the determinant of the matrix.

        Returns
        -------
        det : float
            The determinant of the instance.
        """
        det = np.linalg.det(self)
        return det

    def getTrace(self):
        """Compute the trace of the matrix.

        Compute the trace of the matrix.

        Returns
        -------
        trace : float
            The trace of the instance.
        """
        trace = self.trace()
        return trace

    def isRotation(self, *args):
        """Check if this is a rotation matrix.

        Do the components of the instance represent a rotation? Default
        tolerance value for normality and zero determinant are used if
        not provided.

        Parameters
        ----------
        *args : tuple of object.
            Arguments for polymorphic method.
        normTolerance : float (optional)
            Tolerance for vector normal relative to unity.
        determinantTolerance : float (optional)
            Tolerance for matrix determinant relative to unity.

        Returns
        -------
        isRotation : bool
            True if matrix represents a rotation, otherwise False.
        """
        if len(args) == 0:
            normTolerance = UnwritableMatrixIJK.NORM_TOLERANCE
            determinantTolerance = UnwritableMatrixIJK.DETERMINANT_TOLERANCE
        elif len(args) == 2:
            (normTolerance, determinantTolerance) = args
        else:
            raise ValueError('Invalid parameters for method!')
        isRotation = False
        try:
            checkRotation(
                self[0, 0], self[1, 0], self[2, 0],
                self[0, 1], self[1, 1], self[2, 1],
                self[0, 2], self[1, 2], self[2, 2],
                normTolerance, determinantTolerance)
            isRotation = True
        except MalformedRotationException:
            pass
        return isRotation

    def mxv(self, *args):
        """Compute the product of this matrix with a vector.

        Multiply a vector by this matrix, and return the vector result.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method.
        v : UnwritableVectorIJK
            Vector to multiply by this matrix.
        buffer : VectorIJK (optional)
            Buffer to hold the result.
        """
        if len(args) == 1:
            (v,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (v, buffer) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = np.dot(self, v)
        return buffer

    def mtxv(self, *args):
        """Compute the product of this matrix transpose with a vector.

        Multiply a vector by the transpose of this matrix, and return the
        vector result.

        Parameters
        ----------
        *args : tuple of object
            Parameters for polymorphic method.
        v : UnwritableVectorIJK
            Vector to multiply by the transpose of this matrix.
        buffer : VectorIJK (optional)
            Buffer to hold the result.
        """
        if len(args) == 1:
            (v,) = args
            buffer = VectorIJK()
        elif len(args) == 2:
            (v, buffer) = args
        else:
            raise ValueError('Invalid parameters for method!')
        buffer[:] = np.dot(self.T, v)
        return buffer

    @staticmethod
    def copyOf(matrix):
        """Make an unwritable copy of the supplied matrix.

        This method makes an unwritable copy only if necessary. It tries to
        avoid making a copy wherever possible.

        Parameters
        ----------
        matrix : UnwritableMatrixIJK
            A matrix to copy.

        Returns
        -------
        buffer : UnwritableMatrixIJK
            Either a reference to matrix (if matrix is already an instance
            of UnwritableMatrixIJK, otherwise an unwritable copy of matrix's
            contents
        """
        if isinstance(matrix, UnwritableMatrixIJK):
            buffer = matrix
        else:
            buffer = UnwritableMatrixIJK(matrix)
        return buffer
