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
from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds
from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)
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

    def getWaveExpansion(self):
        """Return the wave expansion.
        
        Return the wave expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion1D
            Coefficients for wave expansion.
        """
        return self.waveExpansion


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

    def getTailExpansion(self):
        """Return the tail expansion.
        
        Return the tail expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion1D
            Coefficients for tail expansion.
        """
        return self.tailExpansion

    def getWaveExpansion(self):
        """Return the wave expansion.
        
        Return the wave expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion1D
            Coefficients for wave expansion.
        """
        return self.waveExpansion


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
                tailS.tailExpansion, tailS.getWaveExpansion(),
                tailO.getTailExpansion(), tailO.getWaveExpansion(),
                tailE.getTailExpansion(), tailE.getWaveExpansion())
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
        for i in range(1, numRadialExpansions + 1):
            fileName = "tailamebhr_%02d.par" % i
            inFile = os.path.join(staticCoeffDirectory, fileName)
            values = nones((numShieldAzimuthalExpansions,
                            numShieldRadialExpansions))
            waveNumberValues = nones((numShieldRadialExpansions,))
            with open(inFile) as f:
                for l in range(numShieldAzimuthalExpansions):
                    for k in range(1, numShieldRadialExpansions + 1):
                        # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                        line = f.readline()
                        val = float(line.split()[0])
                        values[l][k - 1] = val
                for k in range(1, numShieldRadialExpansions + 1):
                    # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                    line = f.readline()
                    val = float(line.split()[0])
                    waveNumberValues[k - 1] = val
            expansions[i - 1] = ArrayCoefficientExpansion2D(values, 0, 1)
            waveExpansions[i - 1] = ArrayCoefficientExpansion1D(
                waveNumberValues, 1
            )

        return SymmetricCylindricalExpansionPair(
            Expansion1Ds.createFromArray(expansions, 1),
            Expansion1Ds.createFromArray(waveExpansions, 1)
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
        for n in range(1, numRadialExpansions + 1):
            for m in range(1, numAzimuthalExpansions + 1):
                inFile = os.path.join(staticCoeffDirectory,
                                      fileName + "%02d_%02d.par" % (n, m))
                with open(inFile) as f:
                    values = nones((numShieldAzimuthalExpansions,
                                    numShieldRadialExpansions))
                    for l in range(numShieldAzimuthalExpansions):
                        for k in range(1, numShieldRadialExpansions + 1):
                            # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                            line = f.readline()
                            val = float(line.split()[0])
                            values[l][k - 1] = val
                    waveNumberValues = nones((numShieldRadialExpansions,))
                    for k in range(1, numShieldRadialExpansions + 1):
                        line = f.readline()
                        val = float(line.split()[0])
                        waveNumberValues[k - 1] = val
                expansions[m - 1][n - 1] = ArrayCoefficientExpansion2D(
                    values, 0, 1
                )
                waveExpansions[m - 1][n - 1] = ArrayCoefficientExpansion1D(
                    waveNumberValues, 1
                )
        return AsymmetricCylindricalExpansionPair(
            Expansion2Ds.createFromArray(expansions, 1, 1),
            Expansion2Ds.createFromArray(waveExpansions, 1, 1)
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
