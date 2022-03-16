"""A 3-dimensional vector in spherical (r, theta, phi) coordinates.

The spherical coordinates standard is defined in ISO 31-11 (1992), a
summary of which can be found here:

https://en.wikipedia.org/wiki/ISO_31-11

This class provides a representation of a vector in spherical coordinates,
and methods to convert vectors between spherical and Cartesian
coordinates.

Position vectors (i.e. vectors relative to the origin) are converted from
spherical (r, theta, phi) to Cartesian (x, y, z) coordinates using the
transformation:

    x = r*sin(theta)*cos(phi)
(1) y = r*sin(theta)*sin(phi)
    z = r*cos(theta)

To convert from Cartesian (x, y, z) to spherical (r, theta, phi)
coordinates:

    r = sqrt(x**2 + y**2 + z**2)
(2) theta = atan2(sqrt(x**2 + y**2), z)
    phi = atan2(y, x)

A value vector is a vector relative to an arbitrary position. This type of
vector is converted between spherical and Cartesian coordinates using a
set of rotations, resulting in a basis vector transformation:

(3) A_sph = A_r*u_r + A_theta*u_theta + A_phi*u_phi

to or from:

(4) A_car = A_x*u_x + A_y*u_y + A_z*u_z

where u_r, u_theta, and u_phi are the unit vectors in the spherical r,
theta, and phi directions at the base of the value vector, and u_x, u_y,
and u_z are the equivalent Cartesian basis vectors at the base of the
value vector. The spherical basis vectors can be written in terms of the
Cartesian basis vectors using:

    u_r     = sin(theta)*cos(phi)*u_x + sin(theta)*sin(phi)*u_y + cos(theta)*u_z
(3) u_theta = cos(theta)*cos(phi)*u_x + cos(theta)*sin(phi)*u_y - sin(theta)*u_z
    u_phi   = -sin(phi)*u_x + cos(phi)*u_y + 0*u_z

or:

    | u_r     |     | u_x |
(6) | u_theta | = T | u_y |
    | u_phi   |     | u_z |

where:

        | sin(theta)*cos(phi) sin(theta)*sin(phi)  cos(theta) |
(7) T = | cos(theta)*cos(phi) cos(theta)*sin(phi) -sin(theta) |
        |       -sin(phi)            cos(phi)          0      |

The spherical-to-Cartesian basis vector transformation is the transpose
of T:

    | u_x |                | u_r     |
(8) | u_y | = TRANSPOSE(T) | u_theta |
    | u_z |                | u_phi   |

To convert from a Cartesian to spherical basis, apply the transformation
T to the Cartesian basis vectors:

(9) A_sph =   A_r*(sin(theta)*cos(phi)*u_x + sin(theta)*sin(phi)*u_y * cos(theta)*u_z)
            + A_theta*(cos(theta)*cos(phi)*u_x + cos(theta)*sin(phi)*u_y -sin(theta)*u_z)
            + A_z*(-sin(phi)*u_x + cos(phi)*u_y)
          =   (A_r*sin(theta)*cos(phi) + A_theta*cos(theta)*cos(phi) - A_z*sin(phi))*u_x
            + (A_r*sin(theta)*sin(phi) + A_theta*cos(theta)*sin(phi) + A_z*cos(phi))*u_y
            + (A_r*cos(theta) - A_theta*sin(theta))*u_z
          = A_car
          = A_x*u_x + A_y*u_y + A_z*u_z

and so:

     A_x = A_r*sin(theta)*cos(phi) + A_theta*cos(theta)*cos(phi) - A_z*sin(phi)
(10) A_y = A_r*sin(theta)*sin(phi) + A_theta*cos(theta)*sin(phi) + A_z*cos(phi)
     A_z = A_r*cos(theta) - A_theta*sin(theta)

or:

     | A_x |                | A_r     |
(11) | A_y | = TRANSPOSE(T) | A_theta |
     | A_z |                | A_phi   |

The Cartesian-to-spherical basis transformation is the inverse
transformation, and thus the transpose of the transformation matrix:

     | A_r     |     | A_x |
(12) | A_theta | = T | A_y |
     | u_phi   |     | A_z |

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, sin, sqrt

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.matrices.matrix3d import Matrix3D
from emmpy.math.vectors.vector3d import Vector3D


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
        in ISO standard 31-11. The value is guaranteed to be in the range
        [0, pi].
    phi : float
        Value of azimuthal angle (radians). The name is specified
        in ISO standard 31-11. The value is guaranteed to be in the range
        [-pi, pi].

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


def sphericalToCartesian(spherical):
    """Convert a spherical coordinate vector to Cartesian coordinates.

    Convert a spherical coordinate vector to Cartesian coordinates.

    Parameters
    ----------
    spherical : SphericalVector
        Spherical coordinate vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector
        Input spherical coordinate vector converted to Cartesian coordinates.
    """
    (r, theta, phi) = (spherical.r, spherical.theta, spherical.phi)
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    cartesian = CartesianVector(x, y, z)
    return cartesian


def cartesianToSpherical(cartesian):
    """Convert a Cartesian vector to spherical coordinates.

    Convert a Cartesian vector to spherical coordinates.

    The angle phi is guaranteed to be in the range [-pi, pi).

    Parameters
    ----------
    cartesian : CartesianVector
        Cartesian vector to convert to spherical coordinates.

    Returns
    -------
    spherical : SphericalVector
        Input Cartesian vector converted to spherical coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
    r = sqrt(x**2 + y**2 + z**2)
    theta = atan2(sqrt(x**2 + y**2), z)
    phi = atan2(y, x)
    spherical = SphericalVector(r, theta, phi)
    return spherical


def getSphericalBasisToCartesianBasisTransformation(sphericalPosition):
    """Compute the spherical-to-Cartesian transformation matrix.

    Compute the spherical-to-Cartesian transformation matrix at the
    specified spherical position

    Parameters
    ----------
    sphericalPosition : SphericalVector
        Spherical position vector to define the transformation matrix.

    Returns
    -------
    m : Matrix3D
        Transformation matrix for spherical-to-Cartesian basis
        transformation.
    """
    theta = sphericalPosition.theta
    phi = sphericalPosition.phi
    sin_theta = sin(theta)
    cos_theta = cos(theta)
    sin_phi = sin(phi)
    cos_phi = cos(phi)
    m = Matrix3D([[sin_theta*cos_phi, cos_theta*cos_phi, -sin_phi],
                  [sin_theta*sin_phi, cos_theta*sin_phi,  cos_phi],
                  [cos_theta,         -sin_theta,         0]])
    return m


def getCartesianBasisToSphericalBasisTransformation(cartesianPosition):
    """Compute the Cartesian-to-spherical transformation matrix.

    Compute the Cartesian-to-spherical transformation matrix at the
    specified Cartesian position

    Parameters
    ----------
    cartesianPosition : CartesianVector
        Cartesian position vector to define the transformation matrix.

    Returns
    -------
    m : Matrix3D
        Transformation matrix for Cartesian-to-spherical basis
        transformation.
    """
    sphericalPosition = cartesianToSpherical(cartesianPosition)
    m = getSphericalBasisToCartesianBasisTransformation(sphericalPosition)
    m = Matrix3D(m.T)
    return m


def sphericalBasisToCartesianBasis(sphericalPosition, sphericalValue):
    """Convert a spherical vector to a Cartesian basis.

    Convert a spherical value vector to a Cartesian basis. The basis
    transformation matrix is derived from the spherical position vector,
    not the spherical value vector.

    Parameters
    ----------
    sphericalPosition : SphericalVector
        Spherical position vector to define the transformation matrix.
    sphericalValue : SphericalVector
        Spherical value vector to convert to Cartesian basis at the
        spherical position.

    Returns
    -------
    cartesianValue : CartesianVector
        Input spherical value vector converted to Cartesian basis at
        the specified spherical position.
    """
    m = getSphericalBasisToCartesianBasisTransformation(sphericalPosition)
    cartesianValue = CartesianVector(m.dot(sphericalValue))
    return cartesianValue


def cartesianBasisToSphericalBasis(cartesianPosition, cartesianValue):
    """Convert a Cartesian vector to a spherical basis.

    Convert a Cartesian vector to a spherical basis. The basis
    transformation matrix is derived from the Cartesian position vector,
    not the Cartesian value vector.

    Parameters
    ----------
    cartesianPosition : CartesianVector
        Cartesian position vector to define the transformation matrix.
    cartesianlValue : CartesianVector
        Cartesian value vector to convert to spherical basis at the
        Cartesian position.

    Returns
    -------
    sphericalValue : SphericalVector
        Input Cartesian vector converted to spherical basis at the
        specified Cartesian position.
    """
    m = getCartesianBasisToSphericalBasisTransformation(cartesianPosition)
    sphericalValue = SphericalVector(m.dot(cartesianValue))
    return sphericalValue
