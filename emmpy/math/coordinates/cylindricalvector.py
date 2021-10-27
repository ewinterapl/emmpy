"""A 3-dimensional vector in cylindrical (rho, phi, z) coordinates.

The cylindrical coordinates standard is defined in ISO 31-11 (1992), a
summary of which can be found here:

https://en.wikipedia.org/wiki/ISO_31-11

This class provides a representation of a vector in cylindrical
coordinates, and methods to convert vectors between cylindrical and
Cartesian coordinates.

Position vectors (i.e. vectors relative to the origin) are converted from
cylindrical (rho, phi, z) to Cartesian (x, y, z) coordinates using the
transformation:

    x = rho*cos(phi)
(1) y = rho*sin(phi)
    z = z

To convert from Cartesian (x, y, z) to cylindrical (rho, phi, z)
coordinates:

    rho = sqrt(x**2 + y**2)
(2) phi = atan2(y, x)
    z   = z

A value vector is a vector relative to an arbitrary position. This type of
vector is converted between cylindrical and Cartesian coordinates using a
set of rotations, resulting in a basis vector transformation:

(3) A_cyl = A_rho*u_rho + A_phi*u_phi + A_z*u_z

to or from:

(4) A_car = A_x*u_x + A_y*u_y + A_z*u_z

where u_rho, u_phi, and u_z are the unit vectors in the cylindrical rho,
phi, and z directions at the base of the value vector, and u_x, u_y, and
u_z are the equivalent Cartesian basis vectors at the base of the value
vector. The cylindrical basis vectors can be written in terms of the
Cartesian basis vectors using:

    u_rho =  cos(phi)*u_x + sin(phi)*u_y
(5) u_phi = -sin(phi)*u_x + cos(phi)*u_y
    u_z   = u_z

or:

    | u_rho |     | u_x |
(6) | u_phi | = T | u_y |
    | u_z   |     | u_z |

where:

        |  cos(phi) sin(phi) 0 |
(7) T = | -sin(phi) cos(phi) 0 |
        |     0        0     1 |

The cylindrical-to-Cartesian basis vector transformation is the transpose
of T:

    | u_x |                | u_rho |
(8) | u_y | = TRANSPOSE(T) | u_phi |
    | u_z |                | u_z   |

To convert from a Cartesian to cylindrical basis, apply the transformation
T to the Cartesian basis vectors:

(9) A_cyl =   A_rho*( cos(phi)*u_x + sin(phi)*u_y)
            + A_phi*(-sin(phi)*u_x + cos(phi)*u_y)
            + A_z*u_z
          =   (A_rho*cos(phi) - A_phi*sin(phi))*u_x
            + (A_rho*sin(phi) + A_phi*cos(phi))*u_y
            + A_z*u_z
          = A_car
          = A_x*u_x + A_y*u_y + A_z*u_z

and so:

     A_x = A_rho*cos(phi) - A_phi*sin(phi)
(10) A_y = A_rho*sin(phi) + A_phi*cos(phi)
     A_z = A_z

or:

     | A_x |                | A_rho |
(11) | A_y | = TRANSPOSE(T) | A_phi |
     | A_z |                | A_z   |

The Cartesian-to-cylindrical basis transformation is the inverse
transformation, and thus the transpose of the transformation matrix:

     | A_rho |     | A_x |
(12) | A_phi | = T | A_y |
     | u_z   |     | A_z |

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.matrices.matrix3d import Matrix3D
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
        in ISO standard 31-11. The value is guaranteed to be in the range
        [-pi, pi].
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


def cylindricalToCartesian(cylindrical):
    """Convert a cylindrical vector to Cartesian coordinates.

    Convert a cylindrical vector to Cartesian coordinates.

    Parameters
    ----------
    cylindrical : CylindricalVector
        Cylindrical vector to convert to Cartesian coordinates.

    Returns
    -------
    cartesian : CartesianVector
        Input cylindrical vector converted to Cartesian coordinates.
    """
    (rho, phi, z) = (cylindrical.rho, cylindrical.phi, cylindrical.z)
    x = rho*cos(phi)
    y = rho*sin(phi)
    cartesian = CartesianVector(x, y, z)
    return cartesian


def cartesianToCylindrical(cartesian):
    """Convert a Cartesian vector to cylindrical coordinates.

    Convert a Cartesian vector to cylindrical.

    The angle phi is guaranteed to be in the range [0, 2*pi).

    Parameters
    ----------
    cartesian : CartesianVector
        Cartesian vector to convert to cylindrical coordinates.

    Returns
    -------
    cylindrical : CylindricalVector
        Input Cartesian vector converted to cylindrical coordinates.
    """
    (x, y, z) = (cartesian.x, cartesian.y, cartesian.z)
    if x == y == 0:
        rho = 0
        phi = 0
    else:
        rho = sqrt(x**2 + y**2)
        phi = atan2(y, x)
        if phi < 0:
            phi += 2*pi
    cylindrical = CylindricalVector(rho, phi, z)
    return cylindrical


def getCylindricalBasisToCartesianBasisTransformation(cylindricalPosition):
    """Compute the cylindrical-to-Cartesian transformation matrix.

    Compute the cylindrical-to-Cartesian transformation matrix at the
    specified cylindrical position

    Parameters
    ----------
    cylindricalPosition : CylindricalVector
        Cylindrical position vector to define the transformation matrix.

    Returns
    -------
    m : Matrix3D
        Transformation matrix for cylindrical-to-Cartesian basis
        transformation.
    """
    phi = cylindricalPosition.phi
    cos_phi = cos(phi)
    sin_phi = sin(phi)
    m = Matrix3D([[cos_phi, -sin_phi, 0],
                  [sin_phi, cos_phi, 0],
                  [0, 0, 1]])
    return m


def getCartesianBasisToCylindricalBasisTransformation(cartesianPosition):
    """Compute the Cartesian-to-cylindrical transformation matrix.

    Compute the Cartesian-to-cylindrical transformation matrix at the
    specified Cartesian position

    Parameters
    ----------
    cartesianPosition : CartesianVector
        Cartesian position vector to define the transformation matrix.

    Returns
    -------
    m : Matrix3D
        Transformation matrix for Cartesian-to-cylindrical basis
        transformation.
    """
    cylindricalPosition = cartesianToCylindrical(cartesianPosition)
    m = getCylindricalBasisToCartesianBasisTransformation(cylindricalPosition)
    m = Matrix3D(m.T)
    return m


def cylindricalBasisToCartesianBasis(cylindricalPosition, cylindricalValue):
    """Convert a cylindrical vector to a Cartesian basis.

    Convert a cylindrical value vector to a Cartesian basis. The basis
    transformation matrix is derived from the cylindrical position vector,
    not the cylindrical value vector.

    Parameters
    ----------
    cylindricalPosition : CylindricalVector
        Cylindrical position vector to define the transformation matrix.
    cylindricalValue : CylindricalVector
        Cylindrical value vector to convert to Cartesian basis at the
        cylindrical position.

    Returns
    -------
    cartesianValue : CartesianVector
        Input cylindrical value vector converted to Cartesian basis at
        the specified cylindrical position.
    """
    m = getCylindricalBasisToCartesianBasisTransformation(cylindricalPosition)
    cartesianValue = CartesianVector(m.dot(cylindricalValue))
    return cartesianValue


def cartesianBasisToCylindricalBasis(cartesianPosition, cartesianValue):
    """Convert a Cartesian vector to a cylindrical basis.

    Convert a Cartesian vector to a cylindrical basis. The basis
    transformation matrix is derived from the Cartesian position vector,
    not the Cartesian value vector.

    Parameters
    ----------
    cartesianPosition : CartesianVector
        Cartesian position vector to define the transformation matrix.
    cartesianlValue : CartesianVector
        Cartesian value vector to convert to cylindrical basis at the
        Cartesian position.

    Returns
    -------
    cylindricalValue : CylindricalVector
        Input Cartesian vector converted to cylindrical basis at the
        specified Cartesian position.
    """
    m = getCartesianBasisToCylindricalBasisTransformation(cartesianPosition)
    cylindricalValue = CylindricalVector(m.dot(cartesianValue))
    return cylindricalValue
