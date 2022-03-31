"""Compute the current density field around Earth.

Constructs the current density from the magnetic field via Ampere's Law.
This is computed numerically using the finite difference method.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# import static crucible.core.math.vectorfields.VectorFields.curl;
# import static crucible.core.math.vectorfields.VectorFields.quadraticApproximation;
# import static crucible.core.math.vectorfields.VectorFields.scale;

# Import standard modules.

# Import 3rd-party modules.
from scipy.constants import mu_0  # SI units

# Import project modules.
from emmpy.math.vectorfields.vectorfield import VectorField


# Program constants

# Earth radius in kilometers.
radius_of_earth_meters = 6371200.0


class EarthCurrentDensityField(VectorField):
    """Compute the current density field around Earth.

    Constructs the current density from the magnetic field via Ampere's
    Law. This is computed numerically using the finite difference method.

    Attributes
    ----------
    jField : 
        Current density field (nA/m^2)
    """

    def __init__(self, magneticField, dr):
        """Initialize a new EarthCurrentDensityField object.

        Initialize a new EarthCurrentDensityField object.

        Parameters
        ----------
        magneticField : VectorField
            Represents the magnetic field around Earth, where the
            inputs are location in Earth radii and the output is in nT.
        dr : float
            Step size.

        Returns
        -------
        None
        """
        self.jField = None

#     // convert units
#     this.jField = scale(curl(quadraticApproximation(magneticField, dr, dr, dr)),
#         1.0 / (radiusOfEarthKM * 1000.0 * mu0));
#   }

#   @Override
#   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
#     return jField.evaluate(location, buffer);
#   }

# }
