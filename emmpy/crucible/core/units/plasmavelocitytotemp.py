# /**
#  * Filename: PlasmaVelocityToTemp.java Author : vandejd1 Created : Feb 9, 2009
#  * 
#  * Copyright (C) 2008 The Johns Hopkins University Applied Physics Laboratory (JHU/APL) All rights
#  * reserved
#  */
# package crucible.core.units;


# /**
#  * converts a plasma velocity in km/sec to a temperature in kelvins
#  * 
#  * @author vandejd1
#  */

from emmpy.crucible.core.units.fundamentalphysicalconstants import FundamentalPhysicalConstants

class PlasmaVelocityToTemp:

    #   /**
    #    * a value for the mass, put into the right units for the conversion formula
    #    */
    #   private double mm;

    #   /**
    #    * the molar gas constant tucked away in a field so I don't have to get it out of the constants
    #    * class class later; its final to encourage compiler optimization
    #    */
    #   final private double R;

    def __init__(self, massInAmu):
        constants = FundamentalPhysicalConstants.getInstance()
        #     // part of the formual (getting the mass into the right units) can be done here:
        u = constants.getAMUInKg()
        self.mm = massInAmu * u * constants.getAvagadrosNumber()
        self.R = constants.getMolarGasConstantR()

    def getTempInKelvins(self, thermalSpeedInKmPerSec):
        #     // The formula (in Javascript) was obtained from:
        #     // http://hyperphysics.phy-astr.gsu.edu/Hbase/kinetic/kintem.html#c3
        #     //
        #     // function
        #     // vcal(){fh=document.forms[0];R=8.31451;u=1.66054*Math.pow(10,-27);mm=fh.m.value*u*6.0221367*Math.pow(10,23);
        #     // tt=fh.t.value;
        #     // vvp=Math.sqrt(2*R*tt/mm);fh.vp.value=vvp;fh.vpk.value=vvp*3600/1000;fh.vpc.value=vvp*3600/(5280*.3048);vvm=Math.sqrt(8*R*tt/(mm*Math.PI));fh.vm.value=vvm;fh.vmk.value=vvm*3600/1000;fh.vmc.value=vvm*3600/(5280*.3048);vvr=Math.sqrt(3*R*tt/mm);fh.vr.value=vvr;fh.vrk.value=vvr*3600/1000;fh.vrc.value=vvr*3600/(5280*.3048)}

        #     // Values for the constants were replaced with more precise values obtained from NIST:
        #     // http://physics.nist.gov/cuu/Constants/

        #     // part of the formula is done in the constructor

        speedInMetersPerSec = thermalSpeedInKmPerSec * 1000.0
        tempInKelvins = speedInMetersPerSec * speedInMetersPerSec * self.mm / (2.0 * self.R)
        return tempInKelvins

    #   /**
    #    * a test case using the original constants from the Javascript:
    #    * 
    #    * @param args
    #    */
    #   public static void main(String[] args) {
    #     double SPEED = 2.0; // units are km/sec

    #     double massInAmu = 1.0;
    #     double factorToGetThermalSpeedToKmPerSec = 1.0;

    #     double R = 8.31451;
    #     double u = 1.66054e-27;
    #     double mm = massInAmu * u * 6.0221367e23;
    #     double speedInMetersPerSec = SPEED * factorToGetThermalSpeedToKmPerSec * 1000.0;
    #     double tempInKelvins = speedInMetersPerSec * speedInMetersPerSec * mm / (2.0 * R);

    #     System.out.println("" + tempInKelvins);

    #   }

    # }
