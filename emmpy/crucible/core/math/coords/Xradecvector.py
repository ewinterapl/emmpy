"""A 3-D vector in celestial (radius, RA, DEC) coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector3d import Vector3D


class RaDecVector(Vector3D):
    """A 3-D vector in celestial (radius, RA, DEC) coordinates.

    A 3-D vector in celestial (radius, RA, DEC) coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self, radius, raRadians, decRadians):
        """Initialize a new RaDecVector object.

        Initialize a new RaDecVector object.

        Parameters
        ----------
        radius : float
            Radius in arbitrary length units.
        raRadians : float
            Right ascension in radians.
        decRadians : float
            Declination in radians.
        """
        self[:] = [radius, raRadians, decRadians]

    def getRadius(self):
        """Return the radius.

        Return the radius.

        Parameters
        ----------
        None

        Returns
        -------
        self[0] : float
            The radius.
        """
        return self[0]

    def getRightAscension(self):
        """Return the right ascension in radians.

        Return the right ascension in radians.

        Parameters
        ----------
        None

        Returns
        -------
        self[1] : float
            The right ascension in radians.
        """
        return self[1]

    def getDeclination(self):
        """Return the declination in radians.

        Return the declination in radians.

        Parameters
        ----------
        None

        Returns
        -------
        self[2] : float
            The declination in radians.
        """
        return self[2]

    def getI(self):
        """Return the 1st component.

        Return the 1st component.

        Parameters
        ----------
        None

        Returns
        -------
        self[0] : float
            The 1st component.
        """
        return self[0]

    def getJ(self):
        """Return the 2nd component.

        Return the 2nd component.

        Parameters
        ----------
        None

        Returns
        -------
        self[1] : float
            The 2nd component.
        """
        return self[1]

    def getK(self):
        """Return the 3rd component.

        Return the 3rd component.

        Parameters
        ----------
        None

        Returns
        -------
        self[2] : float
            The 3rd component.
        """
        return self[2]

    def getVectorIJK(self):
        """Return the vector.

        Return the vector. Note this does NOT cast it as a VectorIJK.

        Parameters
        ----------
        None

        Returns
        -------
        self : radecvector
            The vector.
        """
        return self


# # The ZERO vector.
# ZERO = RaDecVector(0, 0, 0)
