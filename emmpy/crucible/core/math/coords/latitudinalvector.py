"""A 3-D vector in latitudinal (radius, latitude, longitude) coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector3d import Vector3D


class LatitudinalVector(Vector3D):
    """A 3-D vector in latitudinal (radius, latitude, longitude) coordinates.

    A 3-D vector in latitudinal (radius, latitude, longitude) coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self, radius, latInRadians, longInRadians):
        """Initialize a new LatitudinalVector object.

        Initialize a new LatitudinalVector object.

        Parameters
        ----------
        radius : float
            Radius in arbitrary length units.
        latInRadians : float
            Latitude in radians.
        longInRadians : float
            Longitude in radians.
        """
        self[:] = [radius, latInRadians, longInRadians]

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

    def getLatitude(self):
        """Return the latitude.

        Return the latitude.

        Parameters
        ----------
        None

        Returns
        -------
        self[1] : float
            The latitude.
        """
        return self[1]

    def getLongitude(self):
        """Return the longitude.

        Return the longitude.

        Parameters
        ----------
        None

        Returns
        -------
        self[2] : float
            The longitude.
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
        """Return the vector as a VectorIJK.

        Return the 3rd component.

        Parameters
        ----------
        None

        Returns
        -------
        self[2] : float
            The 3rd component.

        Notes
        -----
        This method needs to be fixed to return an actual VectorIJK
        object.
        """
        return self


# The ZERO vector.
ZERO = LatitudinalVector(0, 0, 0)
