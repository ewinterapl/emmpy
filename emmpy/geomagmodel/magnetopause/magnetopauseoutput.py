"""XXX.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class MagnetopauseOutput:
    """XXX.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new MagnetopauseOutput object.

        Initialize a new MagnetopauseOutput object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """


###############################################################################
# package magnetopause;

# import crucible.core.math.vectorspace.UnwritableVectorIJK;

# /**
#  * A container class for the output of the magnetopause methods mirroring the output of the
#  * magnetopause subroutines in the Geopack FORTRAN code (T96_MGNP_08 and SHUETAL_MGNP_08). This
#  * contains a boolean indicating if the query point is inside or outside the magnetopause along with
#  * a point located on the magnetopause boundary that is approximately the closest point located on
#  * the magnetopause to the query point.
#  * 
#  * @author G.K.Stephens
#  *
#  */
# public class MagnetopauseOutput {

#   private final UnwritableVectorIJK magnetopauseLocation;
#   private final double distanceToMagnetopause;
#   private final boolean withinMagnetosphere;

#   /**
#    * Constructor
#    * 
#    * @param magnetopauseLocation
#    * @param distanceToMagnetopause
#    * @param withinMagnetosphere
#    */
#   MagnetopauseOutput(UnwritableVectorIJK magnetopauseLocation, double distanceToMagnetopause,
#       boolean withinMagnetosphere) {
#     super();
#     this.magnetopauseLocation = magnetopauseLocation;
#     this.distanceToMagnetopause = distanceToMagnetopause;
#     this.withinMagnetosphere = withinMagnetosphere;
#   }

#   /**
#    * The distance between the query point and the point located on the magnetopause boundary that is
#    * approximately the closest point to it.
#    * 
#    * @return the distance
#    */
#   public double getDistanceToMagnetopause() {
#     return distanceToMagnetopause;
#   }

#   /**
#    * @return true if the query point is within the magnetopause (inside the magnetosphere), false if
#    *         it is outside the magnetopaause (outside the magnetosphere)
#    */
#   public boolean isWithinMagnetosphere() {
#     return withinMagnetosphere;
#   }

#   /**
#    * A point located on the magnetopause boundary that is approximately the closest point on the
#    * magnetopause to the query point.
#    * 
#    * @return a point on the magnetopause boundary
#    */
#   public UnwritableVectorIJK getMagnetopauseLocation() {
#     return magnetopauseLocation;
#   }

#   @Override
#   public String toString() {
#     return "MagnetopauseOutput [magnetopauseLocation=" + magnetopauseLocation
#         + ", distanceToMagnetopause=" + distanceToMagnetopause + ", withinMagnetosphere="
#         + withinMagnetosphere + "]";
#   }

#   @Override
#   public int hashCode() {
#     final int prime = 31;
#     int result = 1;
#     long temp;
#     temp = Double.doubleToLongBits(distanceToMagnetopause);
#     result = prime * result + (int) (temp ^ (temp >>> 32));
#     result =
#         prime * result + ((magnetopauseLocation == null) ? 0 : magnetopauseLocation.hashCode());
#     result = prime * result + (withinMagnetosphere ? 1231 : 1237);
#     return result;
#   }

#   @Override
#   public boolean equals(Object obj) {
#     if (this == obj) {
#       return true;
#     }
#     if (obj == null) {
#       return false;
#     }
#     if (getClass() != obj.getClass()) {
#       return false;
#     }
#     MagnetopauseOutput other = (MagnetopauseOutput) obj;
#     if (Double.doubleToLongBits(distanceToMagnetopause) != Double
#         .doubleToLongBits(other.distanceToMagnetopause)) {
#       return false;
#     }
#     if (magnetopauseLocation == null) {
#       if (other.magnetopauseLocation != null) {
#         return false;
#       }
#     } else if (!magnetopauseLocation.equals(other.magnetopauseLocation)) {
#       return false;
#     }
#     if (withinMagnetosphere != other.withinMagnetosphere) {
#       return false;
#     }
#     return true;
#   }

# }
