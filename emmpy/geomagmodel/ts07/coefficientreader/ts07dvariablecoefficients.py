"""Time-variable coefficients for the TS07D geomagnetic field model."""


from emmpy.geomagmodel.ts07.coefficientreader.ts07nonlinearparameters import (
    Ts07NonLinearParameters
)


class TS07DVariableCoefficients:
    """Time-variable coefficients for the TS07D geomagnetic field model.

    A container class that groups together the time-dependent coefficients
    and parameters needed to construct the TS07D geomagnetic field model and
    derivative models.

    To construct this class, use the TS07DVariableCoefficientsUtils class.

    author Nicholas Sharp
    author G.K.Stephens
    """

    def __init__(self, cfAmplitude, equatorialCoeffs, facCoeffs):
        """Build a new object.

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

    def getEquatorialCoefficients(self):
        """Return the equatorial coefficients."""
        return self.equatorialCoeffs

    def getDipoleShieldingAmplitude(self):
        """Return the amplitude of the dipole shielding field."""
        return self.cfAmplitude

    def getFacCoefficients(self):
        """Return the field-aligned current parameters."""
        return self.facCoeffs

    def getNonLinearParameters(self):
        """Return all the non-linear parameters in the TS07D model."""
        return self.nonLinearParameters

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
