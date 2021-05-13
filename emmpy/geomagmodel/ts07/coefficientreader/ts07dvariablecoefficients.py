"""emmpy.geomagmodel.ts07.coefficientreaderts07dvariablecoefficients"""


# from emmpy.java.lang.double import Double
from emmpy.geomagmodel.ts07.coefficientreader.ts07nonlinearparameters import (
    Ts07NonLinearParameters
)


class TS07DVariableCoefficients:
    """A container class that groups together the time-dependent coefficients
    and parameters needed to construct the TS07D geomagnetic field model and
    derivative models.

    To construct this class, use the TS07DVariableCoefficientsUtils class.

    author Nicholas Sharp
    author G.K.Stephens
    """

    def __init__(self, cfAmplitude, equatorialCoeffs, facCoeffs):
        """Constructor

        Constructor is package private, should be constructed using the
        TS07DVariableCoefficientsUtils class.

        param cfAmplitude the amplitude for the dipole shielding field
        param equatorialCoeffs the parameters and coefficients for
        constructing the equatorial currents
        param facCoeffs the parameters and coefficients for constructing the
        field aligned currents
        """
        self.cfAmplitude = cfAmplitude
        self.equatorialCoeffs = equatorialCoeffs
        self.facCoeffs = facCoeffs
        currThicks = equatorialCoeffs.getCurrThicks()
        hingeDist = equatorialCoeffs.getHingeDistance()
        warpParam = equatorialCoeffs.getWarpingParam()
        twistFact = equatorialCoeffs.getTwistParam()
        self.nonLinearParameters = Ts07NonLinearParameters(
            facCoeffs.getRegion1KappaScaling(),
            facCoeffs.getRegion2KappaScaling(),
            currThicks, hingeDist, warpParam, twistFact
        )

    # def getEquatorialCoefficients(self):
    #     """@return the linear and non-linear equatorial parameters"""
    #     return self.equatorialCoeffs

    def getDipoleShieldingAmplitude(self):
        """return the amplitude of the dipole shielding field"""
        return self.cfAmplitude

    # def getFacCoefficients(self):
    #     """@return the field-aligned current linear and non-linear
    #     parameters"""
    #     return self.facCoeffs

    # def getNonLinearParameters(self):
    #     """@return all the non-linear parameters in the TS07D model"""
    #     return self.nonLinearParameters

    # def getTotalNumberOfParameters(self):
    #     """@return the total number of non-linear and linear parameters in the
    #     TS07D model"""
    #     return (
    #         self.getTotalNumberOfLinearParameters() +
    #         self.getTotalNumberOfNonLinearParameters()
    #     )

    # def getTotalNumberOfLinearParameters(self):
    #     """@return the total number of linear parameters (coefficients) in the
    #     TS07D model"""
    #     return (
    #         1 + self.equatorialCoeffs.getTotalNumberOfLinearParameters() +
    #         len(self.facCoeffs.getLienarCoefficients())
    #     )

    # def getTotalNumberOfNonLinearParameters(self):
    #     """@return the total number of non-linear parameters in the TS07D
    #     model"""
    #     # the number of equatorial parameters + 2 for the FAC parameters
    #     return (
    #         self.equatorialCoeffs.getTotalNumberOfNonLinearParameters() + 2
    #     )

    # def toString(self):
    #     return (
    #         "TS07DVariableCoefficients [cfAmplitude=%s, equatorialCoeffs=%s,"
    #         " facCoeffs=%s, nonLinearParameters=%s]"
    #         % (self.cfAmplitude, self.equatorialCoeffs, self.facCoeffs,
    #            self.nonLinearParameters)
    #     )

    # def hashCode(self):
    #     prime = 31
    #     result = 1
    #     temp = Double.doubleToLongBits(self.cfAmplitude)
    #     result = prime*result + temp ^ (temp >> 32)
    #     result = prime*result
    #     if self.equatorialCoeffs:
    #         result += self.equatorialCoeffs.hashCode()
    #     result = prime*result
    #     if self.facCoeffs:
    #         result += self.facCoeffs.hashCode()
    #     result = prime*result
    #     if self.nonLinearParameters:
    #         result == self.nonLinearParameters.hashCode()
    #     return result

    # def equals(self, obj):
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if self.__class__ != obj.__class__:
    #         return False
    #     other = obj
    #     if (Double.doubleToLongBits(self.cfAmplitude) !=
    #         Double.doubleToLongBits(other.cfAmplitude)):
    #         return False
    #     if self.equatorialCoeffs is None:
    #         if other.equatorialCoeffs is not None:
    #             return False
    #     elif not self.equatorialCoeffs.equals(other.equatorialCoeffs):
    #         return False
    #     if self.facCoeffs is None:
    #         if other.facCoeffs is not None:
    #             return False
    #     elif not self.facCoeffs.equals(other.facCoeffs):
    #         return False
    #     if self.nonLinearParameters is None:
    #         if other.nonLinearParameters is not None:
    #             return False
    #     elif not self.nonLinearParameters.equals(other.nonLinearParameters):
    #         return False
    #     return True
