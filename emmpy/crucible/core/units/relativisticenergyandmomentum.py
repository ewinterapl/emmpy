# package crucible.core.units;

# import static com.google.common.base.Preconditions.checkArgument;
# import static crucible.core.math.CrucibleMath.sqrt;

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.units.fundamentalphysicalconstants import FundamentalPhysicalConstants
from emmpy.crucible.core.math.cruciblemath import CrucibleMath

class RelativisticEnergyAndMomentum:

    #   private RelativisticEnergyAndMomentum() {}

    C = FundamentalPhysicalConstants.SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC

    #   /**
    #    * Converts kinetic energy to momentum.
    #    * 
    #    * <pre>
    #    * E<sub>tot</sub><sup>2</sup> = (E<sub>k</sub>+E<sub>0</sub>)<sup>2</sup> = (pc)<sup>2</sup>+(m<sub>0</sub>c<sup>2</sup>)<sup>2</sup>
    #    * p = (1/c) [(E<sub>k</sub>+m<sub>0</sub>c<sup>2</sup>)<sup>2</sup>-(m<sub>0</sub>c<sup>2</sup>)<sup>2</sup>]<sup>1/2</sup>
    #    * </pre>
    #    * 
    #    * @param kineticEnergyInJoules the kinetic energy of the particle in Joules
    #    * @param restMassInKilograms the rest mass of the particle in kilograms
    #    * @return the relativistic momentum of the particle in kg*m/s
    #    */
    @classmethod
    def convertKineticEnergyToMomentumSI(cls, kineticEnergyInJoules, restMassInKilograms):
        Preconditions.checkArgument(kineticEnergyInJoules >= 0, "The kinetic energy (%s) must be greater than or equal to zero" % kineticEnergyInJoules)
        Preconditions.checkArgument(restMassInKilograms >= 0, "The rest mass (%s) must be greater than or equal to zero" % restMassInKilograms)
        m0 = restMassInKilograms
        ek = kineticEnergyInJoules
        e0 = restMassInKilograms * cls.C * cls.C
        return (1.0 / cls.C) * CrucibleMath.sqrt((ek + e0) * (ek + m0 * cls.C * cls.C) - e0 * e0)
