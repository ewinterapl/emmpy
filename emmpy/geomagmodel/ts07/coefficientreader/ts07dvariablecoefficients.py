"""Time-variable coefficients for the TS07D geomagnetic field model.

Time-variable coefficients for the TS07D geomagnetic field model.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.geomagmodel.ts07.coefficientreader.ts07nonlinearparameters import (
    Ts07NonLinearParameters
)


class TS07DVariableCoefficients:
    """Time-variable coefficients for the TS07D geomagnetic field model.

    A container class that groups together the time-dependent coefficients
    and parameters needed to construct the TS07D geomagnetic field model
    and derivative models.

    To construct this class, use the TS07DVariableCoefficientsUtils class.

    Attributes
    ----------
    cfAmplitude : float
        The amplitude for the dipole shielding field.
    equatorialCoeffs : Ts07EquatorialVariableCoefficients
        The parameters and coefficients for constructing the equatorial
        currents.
    facCoeffs : Ts07FacVariableCoefficients
        The parameters and coefficients for constructing the field-aligned
        currents.
    nonLinearParameters : Ts07NonLinearParameters
        nonLinearParameters
    """

    def __init__(self, cfAmplitude, equatorialCoeffs, facCoeffs):
        """Initialize a new TS07DVariableCoefficients object.

        Constructor is package private, should be constructed using the
        TS07DVariableCoefficientsUtils class.

        Parameters
        ----------
        cfAmplitude : float
            The amplitude for the dipole shielding field.
        equatorialCoeffs : Ts07EquatorialVariableCoefficients
            The parameters and coefficients for constructing the equatorial
            currents.
        facCoeffs : Ts07FacVariableCoefficients
            The parameters and coefficients for constructing the
            field-aligned currents.
        nonLinearParameters : Ts07NonLinearParameters
            nonLinearParameters
        """
        self.cfAmplitude = cfAmplitude
        self.equatorialCoeffs = equatorialCoeffs
        self.facCoeffs = facCoeffs
        currThicks = equatorialCoeffs.currThicks
        hingeDist = equatorialCoeffs.hingeDist
        warpParam = equatorialCoeffs.warpingParam
        twistFact = equatorialCoeffs.twistParam
        self.nonLinearParameters = Ts07NonLinearParameters(
            facCoeffs.region1KappaScaling,
            facCoeffs.getRegion2KappaScaling(),
            currThicks, hingeDist, warpParam, twistFact
        )

    def getEquatorialCoefficients(self):
        """Return the equatorial coefficients.

        Return the equatorial coefficients.

        Parameters
        ----------
        None

        Returns
        -------
        result : Ts07EquatorialVariableCoefficients
            The equatorial coefficients.
        """
        return self.equatorialCoeffs

    def getDipoleShieldingAmplitude(self):
        """Return the dipole shielding amplitude.

        Return the dipole shielding amplitude.

        Parameters
        ----------
        None

        Returns
        -------
        result : float
            The dipole shielding amplitude.
        """
        return self.cfAmplitude

    def getFacCoefficients(self):
        """Return the field-aligned current coefficients.

        Return the field-aligned current coefficients.

        Parameters
        ----------
        None

        Returns
        -------
        result : Ts07FacVariableCoefficients
            The field-aligned current coefficients.
        """
        return self.facCoeffs

    def getNonLinearParameters(self):
        """Return all the non-linear parameters in the TS07D model.

        Return all the non-linear parameters in the TS07D model.

        Parameters
        ----------
        None

        Returns
        -------
        result : Ts07NonLinearParameters
            The nonlinear parameters.
        """
        return self.nonLinearParameters
