"""A 3-dimensional vector in spherical (r, theta, phi) coordinates.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.tensors.vector3d import Vector3D


# Map vector component names to indices.
components = {'r': 0, 'theta': 1, 'phi': 2}


class SphericalVector(Vector3D):
    """A 3-dimensional vector in spherical (r, theta, phi) coordinates.

    This class implements a 3-dimensional vector in spherical
    (r, theta, phi) coordinates.

    This class may be used directly as a Numpy array.

    Attributes
    ----------
    r : float
        Value of radius coordinate (unspecified units).
    theta : float
        Value of the polar angle (radians). The name is specified
        in ISO standard 31-11.
    phi : float
        Value of azimuthal angle (radians). The name is specified
        in ISO standard 31-11.

    References
    ----------
    https://en.wikipedia.org/wiki/ISO_31-11
    """

    def __new__(cls, r=None, theta=None, phi=None):
        """Create a new SphericalVector object.

        Allocate a new SphericalVector object by allocating a Vector3D
        object which will be expanded upon.

        Parameters
        ----------
        r : float (optional)
            Value of radius coordinate (unspecified units).
        theta : float (optional)
            Value of the polar angle (radians).
        phi : float (optional)
            Value of azimuthal angle (radians).

        Returns
        -------
        v : SphericalVector
            The newly-created object.
        """
        v = Vector3D.__new__(cls, r, theta, phi)
        return v

    def __getattr__(self, name):
        """Return the value of a computed attribute.

        Return the value of an attribute not found by the standard
        attribute search process. The valid attributes are listed in the
        components dictionary.

        Returns
        -------
        self[0|1|2] : float
            Value of specified attribute (r, theta, or phi).
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
