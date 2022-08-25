"""Create a set of TS07D static coefficients.

Create a set of TS07D static coefficients.

Authors
-------
Nicholas Sharp
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import os

from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)
from emmpy.magmodel.math.expansions.arrayexpansion1d import ArrayExpansion1D
from emmpy.magmodel.math.expansions.arrayexpansion2d import ArrayExpansion2D
from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.utilities.nones import nones


class SymmetricCylindricalExpansionPair:
    """Wrap a pair of symmetric expansion coefficient sets.

    Wrap a pair of symmetric expansion coefficients.

    Attributes
    ----------
    tailExpansion : Expansion1D
        Coefficients for tail expansion.
    waveExpansion : Expansion1D
        Coefficients for wave expansion.
    """

    def __init__(self, tailExpansion, waveExpansion):
        """Initialize a new SymmetricCylindricalExpansionPair object.

        Initialize a new SymmetricCylindricalExpansionPair object.

        Parameters
        ----------
        tailExpansion : Expansion1D
            Coefficients for tail expansion.
        waveExpansion : Expansion1D
            Coefficients for wave expansion.
        """
        self.tailExpansion = tailExpansion
        self.waveExpansion = waveExpansion


class AsymmetricCylindricalExpansionPair:
    """Wrap a pair of asymmetric expansion coefficient sets.

    Wrap a pair of asymmetric expansion coefficients.

    Attributes
    ----------
    tailExpansion : Expansion1D
        Coefficients for tail expansion.
    waveExpansion : Expansion1D
        Coefficients for wave expansion.
    """

    def __init__(self, tailExpansion, waveExpansion):
        """Initialize a new AsymmetricCylindricalExpansionPair object.

        Initialize a new AsymmetricCylindricalExpansionPair object.

        Parameters
        ----------
        tailExpansion : Expansion1D
            Coefficients for tail expansion.
        waveExpansion : Expansion1D
            Coefficients for wave expansion.
        """
        self.tailExpansion = tailExpansion
        self.waveExpansion = waveExpansion


class TS07DStaticCoefficientsFactory:
    """Build shielding coefficients from a directory of files.

    Use this class to construct ThinCurrentSheetShieldingCoefficients from
    the directory where the coefficients are located.

    The coefficients must be in the format as located at the model
    webpage:

    http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.

    Attributes
    ----------
    None
    """

    @staticmethod
    def create(*args):
        """Create a new set of static coefficients.
        
        Create a new set of static coefficients.
        
        Parameters
        ----------
        staticCoeffDirectory : str
            Path to the directory where the static coefficients live.
        numAzimuthalExpansions : int, optional
            Number of azimuthal expansions.
        numRadialExpansions : int, optional
            Number of radial expansions.

        Returns
        -------
        result : ThinCurrentSheetShieldingCoefficients
            Coefficient set from files in the directory.
        """
        if len(args) == 1:
            (staticCoeffDirectory,) = args
            numAzimuthalExpansions = 4
            numRadialExpansions = 5
            return TS07DStaticCoefficientsFactory.create(
                staticCoeffDirectory, numAzimuthalExpansions,
                numRadialExpansions)
        elif len(args) == 3:
            (staticCoeffDirectory, numAzimuthalExpansions,
             numRadialExpansions) = args
            tailS = TS07DStaticCoefficientsFactory.readTailS(
                staticCoeffDirectory, numRadialExpansions)
            tailO = TS07DStaticCoefficientsFactory.readTail(
                staticCoeffDirectory, numAzimuthalExpansions,
                numRadialExpansions, "tailamhr_o_")
            tailE = TS07DStaticCoefficientsFactory.readTail(
                staticCoeffDirectory, numAzimuthalExpansions,
                numRadialExpansions, "tailamhr_e_")
            return ThinCurrentSheetShieldingCoefficients(
                numAzimuthalExpansions, numRadialExpansions,
                tailS.tailExpansion, tailS.waveExpansion,
                tailO.tailExpansion, tailO.waveExpansion,
                tailE.tailExpansion, tailE.waveExpansion)
        else:
            raise Exception

    @staticmethod
    def readTailS(staticCoeffDirectory, numRadialExpansions):
        """Read in tail shielding coefficients from a file.

        Read in tail shielding coefficients from a file.

        Parameters
        ----------
        staticCoeffDirectory : str
            Path to directory containing the coefficient files.
        numRadialExpansions : int
            The number of radial expansions.
        
        Returns
        -------
        result : SymmetricCylindricalExpansionPair
            The coefficients.
        """
        numShieldAzimuthalExpansions = 15
        numShieldRadialExpansions = 5
        expansions = nones((numRadialExpansions,))
        waveExpansions = nones((numRadialExpansions,))
        for i in range(numRadialExpansions):
            fileName = "tailamebhr_%02d.par" % (i + 1)
            inFile = os.path.join(staticCoeffDirectory, fileName)
            values = nones((numShieldAzimuthalExpansions,
                            numShieldRadialExpansions))
            waveNumberValues = nones((numShieldRadialExpansions,))
            with open(inFile) as f:
                for l in range(numShieldAzimuthalExpansions):
                    for k in range(numShieldRadialExpansions):
                        # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                        line = f.readline()
                        val = float(line.split()[0])
                        values[l][k] = val
                for k in range(numShieldRadialExpansions):
                    # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                    line = f.readline()
                    val = float(line.split()[0])
                    waveNumberValues[k] = val
            expansions[i] = ArrayCoefficientExpansion2D(values)
            waveExpansions[i] = ScalarExpansion1D(waveNumberValues)

        return SymmetricCylindricalExpansionPair(
            ArrayExpansion1D(expansions),
            ArrayExpansion1D(waveExpansions)
        )

    @staticmethod
    def readTail(staticCoeffDirectory, numAzimuthalExpansions,
                 numRadialExpansions, fileName):
        """Read in tail coefficients from a file.

        Read in tail coefficients from a file.

        Parameters
        ----------
        staticCoeffDirectory : str
            Path to directory containing the coefficient files.
        numAzimuthalExpansions : int
            Number of azimuthal expansions.
        numRadialExpansions : int
            The number of radial expansions.
        fileName : str
            Name of file containing coefficients.
        
        Returns
        -------
        result : AsymmetricCylindricalExpansionPair
            The coefficients.
        """
        numShieldAzimuthalExpansions = 15
        numShieldRadialExpansions = 5
        expansions = nones((numAzimuthalExpansions, numRadialExpansions))
        waveExpansions = nones((numAzimuthalExpansions, numRadialExpansions))
        for n in range(numRadialExpansions):
            for m in range(numAzimuthalExpansions):
                inFile = os.path.join(staticCoeffDirectory,
                                      fileName + "%02d_%02d.par" % (n + 1, m + 1))
                with open(inFile) as f:
                    values = nones((numShieldAzimuthalExpansions,
                                    numShieldRadialExpansions))
                    for l in range(numShieldAzimuthalExpansions):
                        for k in range(numShieldRadialExpansions):
                            line = f.readline()
                            val = float(line.split()[0])
                            values[l][k] = val
                    waveNumberValues = nones((numShieldRadialExpansions,))
                    for k in range(numShieldRadialExpansions):
                        line = f.readline()
                        val = float(line.split()[0])
                        waveNumberValues[k] = val
                expansions[m][n] = ArrayCoefficientExpansion2D(values)
                waveExpansions[m][n] = ScalarExpansion1D(waveNumberValues)
        return AsymmetricCylindricalExpansionPair(
            ArrayExpansion2D(expansions),
            ArrayExpansion2D(waveExpansions)
        )

    @staticmethod
    def retrieveOriginalBuiltInCoefficientsPath():
        """Fetch the static coefficients that are in the source code.

        This method handles the details of grabbing the static
        coefficients that are in the source code.

        THIS IS A QUICK HACK FOR TESTING

        Parameters
        ----------
        None

        Returns
        -------
        path : str
            Path to the coefficients file.
        """
        path = os.path.join(os.getenv('EMMPY_STATIC_COEFFICIENTS_PATH'),
                            'coeffs_n8_m6')
        return path
