"""A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector3d import Vector3D


# Map vector component names to indices.
components = {'rho': 0, 'phi': 1, 'z': 2}


class CylindricalVector(Vector3D):
    """A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

    This class implements a 3-dimensional vector in cylindrical
    (rho, phi, z) coordinates.

    This class may be used directly as a Numpy array.

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

    def __new__(cls, rho=None, phi=None, z=None):
        """Create a new CylindricalVector object.

        Allocate a new CylindricalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        rho : float (optional)
            Value of radius coordinate (unspecified units).
        phi : float (optional)
            Value of azimuthal angle (radians).
        z : float (optional)
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
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (rho, phi, or z).
        """
        return self[components[name]]

    def __setattr__(self, name, value):
        """Set the value of a computed attribute.

        Set the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.
    
        Returns
        -------
        None
        """
        self[components[name]] = value
