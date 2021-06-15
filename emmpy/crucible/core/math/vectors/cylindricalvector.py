"""A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectors.vector3d import Vector3D


class CylindricalVector(Vector3D):
    """A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

    This class implements a 3-dimensional vector in cylindrical
    (rho, phi, z) coordinates.

    Attributes
    ----------
    rho : float
        Value of radius coordinate (unspecified units).
    phi : float
        Value of azimuthal angle (radians). The name is specified
        in ISO standard 31-11.
    z : float
        Value of the axial position (unspecified units). The name is
        specified in ISO standard 31-11.

    References
    ----------
    https://en.wikipedia.org/wiki/ISO_31-11
    """

    def __new__(cls, rho, phi, z):
        """Create a new CylindricalVector object.

        Allocate a new CylindricalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        rho : float
            Value of radius coordinate (unspecified units).
        phi : float
            Value of azimuthal angle (radians).
        z : float
            Value of the axial position (unspecified units).

        Returns
        -------
        v : CylindricalVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, rho, phi, z)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are

        rho : float
            Value of radius coordinate (unspecified units).
        phi : float
            Value of azimuthal angle (radians).
        z : float
            Value of the axial position (unspecified units).

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (rho, phi, or z).

        Raises
        ------
        AttributeError
            If an illegal attribute name is specified.
        """
        if name == 'rho':
            return self[0]
        elif name == 'phi':
            return self[1]
        elif name == 'z':
            return self[2]
        else:
            raise AttributeError
