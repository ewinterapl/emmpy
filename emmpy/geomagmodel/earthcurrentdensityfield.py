"""Compute the current density field around Earth.

Constructs the current density from the magnetic field via Ampere's Law.
This is computed numerically using the finite difference method.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""

# Import standard modules.

# Import 3rd-party modules.

# Import project modules.
from emmpy.math.vectorfields.vectorfield import VectorField


# Program constants


class EarthCurrentDensityField(VectorField):
    """Compute the current density field around Earth.

    Constructs the current density from the magnetic field via Ampere's
    Law. This is computed numerically using the finite difference method.

    Attributes
    ----------
    """

    def __init__(self):
        """Initialize a new EarthCurrentDensityField object.

        Initialize a new EarthCurrentDensityField object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """


# package geomagmodel;

# import static crucible.core.math.vectorfields.VectorFields.curl;
# import static crucible.core.math.vectorfields.VectorFields.quadraticApproximation;
# import static crucible.core.math.vectorfields.VectorFields.scale;

# import crucible.core.math.vectorfields.VectorField;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
# import crucible.core.units.FundamentalPhysicalConstants;

# /**
#  * Constructs the current density from the magnetic field via Ampere's Law. This is computed
#  * numerically using the finite difference method.
#  * 
#  * @author G.K.Stephens
#  *
#  */
# public class EarthCurrentDensityField implements VectorField {

#   // RE = 6371.2 KM is the standard radius of the Earth in geomagnetism
#   private final static double radiusOfEarthKM = 6371.2;

#   private final VectorField jField;

#   /**
#    * Constructor for the current density in units of nA/m^2.
#    * 
#    * @param magneticField a {@link VectorField} represents the magnetic field at Earth, where the
#    *        inputs are location in Earth radii and the output is in nT
#    * @param dr the step size
#    */
#   public EarthCurrentDensityField(VectorField magneticField, double dr) {

#     double mu0 = FundamentalPhysicalConstants.MAGNETIC_CONSTANT;

#     // convert units
#     this.jField = scale(curl(quadraticApproximation(magneticField, dr, dr, dr)),
#         1.0 / (radiusOfEarthKM * 1000.0 * mu0));
#   }

#   @Override
#   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
#     return jField.evaluate(location, buffer);
#   }

# }
