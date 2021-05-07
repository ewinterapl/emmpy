"""emmpy.crucible.core.units.plasmavelocitytotemp

Filename: PlasmaVelocityToTemp.java
Author : vandejd1 Created : Feb 9, 2009

Copyright (C) 2008 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved
"""


from emmpy.crucible.core.units.fundamentalphysicalconstants import (
    FundamentalPhysicalConstants
)


class PlasmaVelocityToTemp:
    """converts a plasma velocity in km/sec to a temperature in kelvins

    author vandejd1
    """

    def __init__(self, massInAmu):
        constants = FundamentalPhysicalConstants.getInstance()
        # part of the formula (getting the mass into the right units) can be
        # done here:
        u = constants.getAMUInKg()
        # a value for the mass, put into the right units for the conversion
        # formula
        self.mm = massInAmu*u*constants.getAvagadrosNumber()
        # the molar gas constant tucked away in a field so I don't have to get
        # it out of the constants class later; its final to encourage compiler
        # optimization
        self.R = constants.getMolarGasConstantR()

    def getTempInKelvins(self, thermalSpeedInKmPerSec):
        """The formula (in Javascript) was obtained from:

        http://hyperphysics.phy-astr.gsu.edu/Hbase/kinetic/kintem.html#c3

        function vcal() {
            fh = document.forms[0];
            R = 8.31451;
            u = 1.66054*Math.pow(10, -27);
            mm = fh.m.value*u*6.0221367*Math.pow(10, 23);
            tt = fh.t.value;
            vvp = Math.sqrt(2*R*tt/mm);
            fh.vp.value = vvp;
            fh.vpk.value = vvp*3600/1000;
            fh.vpc.value = vvp*3600/(5280*.3048);
            vvm = Math.sqrt(8*R*tt/(mm*Math.PI));
            fh.vm.value = vvm;
            fh.vmk.value = vvm*3600/1000;
            fh.vmc.value = vvm*3600/(5280*.3048);
            vvr = Math.sqrt(3*R*tt/mm);
            fh.vr.value = vvr;
            fh.vrk.value = vvr*3600/1000;
            fh.vrc.value = vvr*3600/(5280*.3048)
        }

        Values for the constants were replaced with more precise values
        obtained from NIST: http://physics.nist.gov/cuu/Constants/

        part of the formula is done in the constructor
        """
        speedInMetersPerSec = thermalSpeedInKmPerSec*1000
        tempInKelvins = (
            speedInMetersPerSec*speedInMetersPerSec*self.mm/(2*self.R))
        return tempInKelvins
