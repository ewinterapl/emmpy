"""Numerical values for mathematical and physical constants.

Author : vandejd1
Created :Feb 9, 2009

Copyright (C) 2008 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved

This class offers access to constants in two ways: a raw form, where you can
get the value of the constant through the public final static fields of the
class. The units of these values will be whatever they were in the source
material from whcih the value was obtained.

But in striving to present a uniform way of thinking about units within
crucible, it is beneficial to present things with an agreed upon "strong
preference" for units. See the table in the package-info.java for this package
for the preferred units within crucible.

To support this approach, this class can also be instantiated and the constants
obtained through methods which ensure that the values obtained for the
constants conform to the standard, strong preference for units use within
crucible. This instance is available as a singleton, since you really only ever
need one of these, and it further emphasizes that you should not sub-class of
this class.

So - within crucible, you should use the singleton (so that your use of units
is "typical"). Outside of crucible, you can use the constants however you want.

@author vandejd1
"""


from math import pi


class FundamentalPhysicalConstants:
    """Numerical values for mathematical and physical constants."""

    # units: J/ ( mol * K )
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    MOLAR_GAS_CONST_R = 8.314472

    # units: 1/mol
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    AVAGADROs_NUMBER_NA = 6.02214179e23

    # units: J K-1
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    BOLTZMANS_CONSTANT_k = 1.3806504e-23

    # units: C (Coulombs)
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    ELECTRON_CHARGE = 1.602176487e-19

    # units: kg
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    ATOMIC_MASS_UNIT_KG = 1.660538782e-27

    ELECTRON_MASS_KG = 9.10938291e-31

    # units: u (same as AMU)
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    ELECTRON_MASS_AMU = 5.4857990943e-4

    ELECTRON_MASS_ENERGY_EQUIVALENT_MEV = 0.510998928

    PROTON_MASS_AMU = 1.007276466812

    PROTON_MASS_KG = 1.67262177710e-27

    PROTON_MASS_ENERGY_EQUIVALENT_MEV = 938.272046

    # units: m/s
    # This is a defined value.
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC = 299792458.0

    # units: N*A<sup>2</sup>
    # Also known as the permeability of free space. This is an exact value.
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    MAGNETIC_CONSTANT = 4*pi*1E-7

    # units: F*M<sup>-1</sup>
    # Also known as the permittivity of free space.
    # Since c is defined, this is an exact value.
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    ELECTRIC_CONSTANT = 1/(
        MAGNETIC_CONSTANT*SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC *
        SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC
    )

    # units: m<sup>3</sup>*kg<sup>-1</sup>*s<sup>-2</sup>
    # The Newtonian constant of Gravitation (G)
    # copied from NIST: http://physics.nist.gov/cuu/Constants/
    NEWTONIAN_CONSTANT_OF_GRAVITATION = 6.67384

    # units: m
    # The official definition of the AU provided by the IAU.
    # see http://www.iau.org/static/resolutions/IAU2012_English.pdf
    AU_IN_METERS = 149597870700.0

    # Return the Julian Date of 2000 JAN 01 12:00:00 (2000 JAN 1.5).
    # units: days
    JULIAN_DATE_OF_J2000 = 2451545.0

    SECONDS_PER_DAY = 86400.0

    TWOPI = 2*pi

    HALFPI = pi/2

    def __init__(self):
        """Build a new obejct."""
        raise RuntimeError('Call instance() instead')

    def getAUinKm(self):
        """Return the length of an astronomical unit in kilometers."""
        return self.AU_IN_METERS / 1000.0

    def getSpeedOfLightInKmPerSec(self):
        """Return the speed of light in kilometers per second."""
        return self.SPEED_OF_LIGHT_IN_VACUUM_M_per_SEC / 1000.0

    def getElectronMassInU(self):
        """Get the electron mass in atomic mass units."""
        return self.ELECTRON_MASS_AMU

    def getAMUInKg(self):
        """Get the mass of an atomic mass unit in kilograms."""
        return self.ATOMIC_MASS_UNIT_KG

    def getMolarGasConstantR(self):
        """Get the value of the molar gas constant."""
        return self.MOLAR_GAS_CONST_R

    def getAvagadrosNumber(self):
        """Get the value of Avogadro's number."""
        return self.AVAGADROs_NUMBER_NA
