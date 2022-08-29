"""Utilities for time-dependent coefficients.

Utilities for time-dependent (variable) coefficients.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import re

import numpy as np

from emmpy.exceptions.emmpyexception import EmmpyException

from emmpy.geomagmodel.ts07.coefficientreader.defaultfacconfigurationoptions import (
    DefaultFacConfigurationOptions
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficients import (
    TS07DVariableCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatoriallinearcoefficients import (
    Ts07EquatorialLinearCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients import (
    Ts07EquatorialVariableCoefficients
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07facvariablecoefficients import (
    Ts07FacVariableCoefficients
)
from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


def readNumberOfAzimuthalExpansions(path):
    """Read the number of azimuthal expansions.

    Read the number of azimuthal expansions from the coefficients file.

    Parameters
    ----------
    path : str
        Path to file containing coefficients.
    
    Returns
    -------
    m : int
        The number of azimuthal expansions.
    """
    numAzimuthalExpansions = 0
    for line in open(path):
        if "M=" in line:
            numAzimuthalExpansions = int(line.split()[-1])
            break
    return numAzimuthalExpansions


def readNumberOfCurrentSheets(path):
    """Read the number of current sheets.

    Read the number of current sheets from the coefficients file.

    Parameters
    ----------
    path : str
        Path to file containing coefficients.
    
    Returns
    -------
    numCurrentSheets : int
        The number of current sheets.
    """
    numCurrentSheets = 0
    for line in open(path):
        if " # current sheet thickness" in line:
            numCurrentSheets += 1
    return numCurrentSheets


def readNumberOfRadialExpansions(path):
    """Read the number of radial expansions.

    Read the number of radial expansions from the coefficients file.

    Parameters
    ----------
    path : str
        Path to file containing coefficients.
    
    Returns
    -------
    numRadialExpansions : int
        The number of radial expansions.
    """
    numRadialExpansions = 0
    for line in open(path):
        if "N=" in line:
            numRadialExpansions = int(line.split()[-1])
            break
    return numRadialExpansions


def readFACConfiguration(path):
    """Read the FAC configuration.

    Parse the FAC configuration from the coefficients file.

    Parameters
    ----------
    path : str
        Path to file containing coefficients.
    
    Returns
    -------
    fac_confiuration : DefaultFacConfigurationOptions
        The FAC configuration based on the number of FAC lines from the file.
    
    Raises
    ------
    EmmpyException
        If the coefficients file contains an invalid FAC configuration
        code.
    """
    count = 0
    for line in open(path):
        if re.search("# reg-[1|2] M-[1|2]", line):
            count += 1
    if count == 4:
        return DefaultFacConfigurationOptions(
            DefaultFacConfigurationOptions.TS07D)
    elif count == 6:
        return DefaultFacConfigurationOptions(
            DefaultFacConfigurationOptions.FAC6)
    elif count == 12:
        return DefaultFacConfigurationOptions(
            DefaultFacConfigurationOptions.FAC12)
    elif count == 16:
        return DefaultFacConfigurationOptions(
            DefaultFacConfigurationOptions.FAC16)
    else:
        raise EmmpyException(
            "Invalid number of FACs to construct a FAC configuration."
        )

class TS07DVariableCoefficientsUtils:
    """Utilities for time-dependent coefficients.

    A utility class for constructing and manipulating
    TS07DVariableCoefficients, and allows for reading and writing the
    coefficients to a file.

    Attributes
    ----------
    None
    """

    @staticmethod
    def create(*args):
        """Create a new set of variable coefficients.

        Create a new set of variable coefficients.

        Parameters
        ----------
        path : str
            Path to coefficients file.

        Returns
        -------
        result : TS07DVariableCoefficients
            The variable coefficients.
        
        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        (path,) = args

        # Read the description of the coefficients.
        numCurrentSheets = readNumberOfCurrentSheets(path)
        numAzimuthalExpansions = readNumberOfAzimuthalExpansions(path)
        numRadialExpansions = readNumberOfRadialExpansions(path)
        facConfiguration = readFACConfiguration(path)

        # The number of asymmetric expansions is simply n*m.
        numAsymmetricExpansions = (
            numRadialExpansions*numAzimuthalExpansions
        )

        # Half the number of equatorial expansion coefficients, r+2*(r*a).
        # This is half the expansions as the dynamic pressure terms double
        # this number.
        numHalfExpansions = numRadialExpansions + 2*numAsymmetricExpansions
        numExpansions = numHalfExpansions*2*numCurrentSheets

        totalNumberOfCoefficients = (
            1 + numExpansions + numCurrentSheets + 5 +
            facConfiguration.numberOfFields
        )

        coeffs = np.empty((totalNumberOfCoefficients,))
        lineNumber = 0
        for line in open(path):
            try:
                coeffs[lineNumber] = float(line.split()[0])
                lineNumber += 1
            except ValueError:
                break

        # NOTE, this is a deviation from the FORTRAN code, the FORTRAN
        # code handles this in the WARPED subroutine.
        twist = coeffs[-1]/10
        coeffs[-1] = twist

        return TS07DVariableCoefficientsUtils.createFromArray(
            coeffs, numCurrentSheets, numAzimuthalExpansions,
            numRadialExpansions, facConfiguration
        )

    @staticmethod
    def readDynamicPressure(variableCoefficientsFile):
        """Parse the dynamic pressure from the variable coefficients file.

        Parse the dynamic pressure from the variable coefficients file.

        Parameters
        ----------
        variableCoefficientsFile : str
            An ASCII file containing a list of the coefficients.
        
        Returns
        -------
        Pdyn : float
            The dynamic pressure parsed from the file.
        """
        Pdyn = None
        for line in open(variableCoefficientsFile):
            if "Pdyn=" in line:
                Pdyn = float(line.split()[-1])
                break
        return Pdyn

    @staticmethod
    def readDipoleTiltAngle(variableCoefficientsFile):
        """Parse the dipole tilt angle from the variable coefficients file.

        Parse the dipole tilt angle from the variable coefficients file.

        Parameters
        ----------
        variableCoefficientsFile : str
            An ASCII file containing a list of the coefficients.
        
        Returns
        -------
        tilt : float
            The dipole tilt angle parsed from the file.
        """
        tilt = None
        for line in open(variableCoefficientsFile):
            if "tilt=" in line:
                tilt = float(line.split()[-1])
                break
        return tilt

    @staticmethod
    def readTwistFactor(variableCoefficientsFile):
        """Parse the twist factor from the variable coefficients file.

        Parse the twist factor from the variable coefficients file.

        Parameters
        ----------
        variableCoefficientsFile : str
            An ASCII file containing a list of the coefficients.
        
        Returns
        -------
        twist_factor : float
            The twist factor parsed from the file.
        """
        twist_factor = None
        for line in open(variableCoefficientsFile):
            if "twist factor" in line:
                twist_factor = float(line.split()[0])
                break
        return twist_factor

    @staticmethod
    def createFromArray(
        coeffs, numCurrentSheets, numAzimuthalExpansions, numRadialExpansions,
        facConfiguration
    ):
        """Create a new Ts07FacVariableCoefficients from an array.

        A double array is the data structured used in the Fortran version of
        the code.

        Parameters
        ----------
        coefficients : np.array of float
            An array containing the coefficients.
        numAzimuthalExpansions : int
            Referred to as m.
        numRadialExpansions : int
            Referred to as n.
        facConfiguration : FacConfiguration
            Describes how to build the field aligned current system.
        
        Returns
        -------
        result : TS07DVariableCoefficients
            The new variable coefficients object.
        """
        # The number of asymmetric expansions is simply n*m.
        numAsymmetricExpansions = numRadialExpansions*numAzimuthalExpansions

        # Half the number of equatorial expansion coefficients, r+2*(r*a), this
        # is half the expansions as the dynamic pressure terms double this
        # number.
        numHalfExpansions = numRadialExpansions + 2*numAsymmetricExpansions
        numExpansions = numHalfExpansions*2*numCurrentSheets

        # Parse file data into proper variables. This too will need to be
        # changed if different coefficient formats are use.
        cfAmplitude = coeffs[0]
        eqLinearCoeffs = []

        # Loop through the number of current sheets.
        for nCurr in range(numCurrentSheets):
            index = nCurr*numHalfExpansions*2
            aSym = np.empty((numRadialExpansions,))
            aSymPdynDependent = np.empty((numRadialExpansions,))
            aOdd = np.empty((numAzimuthalExpansions, numRadialExpansions))
            aOddPdynDependent = np.empty((numAzimuthalExpansions, numRadialExpansions))
            aEven = np.empty((numAzimuthalExpansions, numRadialExpansions))
            aEvenPdynDependent = np.empty((numAzimuthalExpansions, numRadialExpansions))
            for n in range(numRadialExpansions):
                index += 1
                aSym[n] = coeffs[index]
                aSymPdynDependent[n] = coeffs[index + numHalfExpansions]
            for n in range(numRadialExpansions):
                for m in range(numAzimuthalExpansions):
                    index += 1
                    aOdd[m][n] = coeffs[index]
                    aOddPdynDependent[m][n] = coeffs[index + numHalfExpansions]
                    aEven[m][n] = coeffs[index + numAsymmetricExpansions]
                    aEvenPdynDependent[m][n] = (
                        coeffs[index + numHalfExpansions +
                               numAsymmetricExpansions]
                    )
            aSymExpansion = ScalarExpansion1D(aSym)
            aSymPdynDependentExpansion = ScalarExpansion1D(aSymPdynDependent)
            aOddExpansion = ArrayCoefficientExpansion2D(aOdd)
            aOddPdynDependentExpansion = ArrayCoefficientExpansion2D(
                aOddPdynDependent
            )
            aEvenExpansion = ArrayCoefficientExpansion2D(aEven)
            aEvenPdynDependentExpansion = ArrayCoefficientExpansion2D(
               aEvenPdynDependent
            )
            equatorialLinearCoeffs = (
                Ts07EquatorialLinearCoefficients.create(
                    aSymExpansion, aSymPdynDependentExpansion,
                    aOddExpansion, aOddPdynDependentExpansion,
                    aEvenExpansion, aEvenPdynDependentExpansion,
                    numAzimuthalExpansions, numRadialExpansions
                )
            )
            eqLinearCoeffs.append(equatorialLinearCoeffs)

        numFacFields = facConfiguration.numberOfFields

        # The field aligned current amplitudes.
        facAmps = np.empty((numFacFields,))
        for i in range(numFacFields):
            facAmps[i] = coeffs[numExpansions + 1 + i]

        currThicks = coeffs[
            numExpansions + numFacFields + 1:
            numExpansions + numFacFields + 1 + numCurrentSheets
        ]
        hingeDist = coeffs[numExpansions + numFacFields + numCurrentSheets + 1]
        warpParam = coeffs[numExpansions + numFacFields + numCurrentSheets + 2]
        facKappa1 = coeffs[numExpansions + numFacFields + numCurrentSheets + 3]
        facKappa2 = coeffs[numExpansions + numFacFields + numCurrentSheets + 4]
        # NOTE, this is a deviation from the FORTRAN code, the FORTRAN code
        # handles this in the WARPED subroutine.
        twistFact = coeffs[numExpansions + numFacFields + numCurrentSheets + 5]

        equatorialVariableCoeffs = Ts07EquatorialVariableCoefficients(
            currThicks, hingeDist, warpParam, twistFact, eqLinearCoeffs
        )

        fac = Ts07FacVariableCoefficients(
            facKappa1, facKappa2, facConfiguration.createFromCoeffs(facAmps)
        )

        return TS07DVariableCoefficients(
            cfAmplitude, equatorialVariableCoeffs, fac
        )
