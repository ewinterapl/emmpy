"""A 2-dimensional vector in polar (radius, angle) coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.vectors.vector2d import Vector2D


class PolarVector(Vector2D):
    """A 2-dimensional vector in polar (radius, angle) coordinates.

    Attributes
    ----------
    None
    """

    def __new__(cls, radius=0, angle=0):
        """Create a new PolarVector object.

        Allocate a new PolarVector object by allocating a Vector2D
        object which will be expanded upon.

        Parameters
        ----------
        radius : float, optional, default None
            Value of radius coordinate (unspecified units).
        angle : float, optional, default None
            Value of angle about z-axis (radians).
            Value of the axial position (unspecified units).

        Returns
        -------
        v : PolarVector
            The newly-created object.
        """
        v = Vector2D.__new__(cls, radius, angle)
        return v

    def getRadius(self):
        """Return the radius.

        Return the radius.

        Parameters
        ----------
        None

        Returns
        -------
        radius : float
            The polar radius.
        """
        return self[0]

    def getAngle(self):
        """Return the angle.

        Return the angle.

        Parameters
        ----------
        None

        Returns
        -------
        angle : float
            The angle around the z-axis.
        """
        return self[1]

    def getVectorIJ(self):
        """Return the vector as a VectorIJ.

        Return the vector as a VectorIJ.

        Parameters
        ----------
        None

        Returns
        -------
        self : VectorIJ
            The vector.
        """
        return self

    def getI(self):
        """Return the 1st vector component.

        Return the 1st vector component.

        Parameters
        ----------
        None

        Returns
        -------
        self[0] : float
            The 1st vector component.
        """
        return self[0]

    def getJ(self):
        """Return the 2nd vector component.

        Return the 2nd vector component.

        Parameters
        ----------
        None

        Returns
        -------
        self[1] : float
            The 2nd vector component.
        """
        return self[1]


# The null vector in polar coordinates.
ZERO = PolarVector(0, 0)
