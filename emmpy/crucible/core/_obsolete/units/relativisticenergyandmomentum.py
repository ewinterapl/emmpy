# """emmpy.crucible.core.units.relativisticenergyandmomentum"""


# from math import sqrt

# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.crucible.core.units.fundamentalphysicalconstants import (
#     FundamentalPhysicalConstants
# )


# class RelativisticEnergyAndMomentum:

#     C = FundamentalPhysicalConstants.SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC

#     @classmethod
#     def convertKineticEnergyToMomentumSI(
#         cls, kineticEnergyInJoules, restMassInKilograms):
#         """Converts kinetic energy to momentum.

#         E_tot^2 = (E_k + E_0])^2 = (pc)^2 +(m_0 c^2)^2
#         p = (1/c) [(E_k +m_0 c^2)^2 - (m_0^2)^2]^1/2

#         param kineticEnergyInJoules the kinetic energy of the particle in
#         Joule s
#         param restMassInKilograms the rest mass of the particle in kilograms
#         return the relativistic momentum of the particle in kg*m/s
#         """
#         Preconditions.checkArgument(
#             kineticEnergyInJoules >= 0,
#             "The kinetic energy (%s) must be greater than or equal to zero" %
#             kineticEnergyInJoules)
#         Preconditions.checkArgument(
#             restMassInKilograms >= 0,
#             "The rest mass (%s) must be greater than or equal to zero" %
#             restMassInKilograms)
#         m0 = restMassInKilograms
#         ek = kineticEnergyInJoules
#         e0 = restMassInKilograms * cls.C * cls.C
#         return 1.0/cls.C*sqrt((ek + e0)*(ek + m0*cls.C*cls.C) - e0*e0)
