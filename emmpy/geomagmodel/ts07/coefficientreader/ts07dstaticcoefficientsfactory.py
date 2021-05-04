"""emmpy.geomagmodel.ts07.coefficientreader.ts07dstaticcoefficientsfactory"""


# import java.io.File;
# import java.io.IOException;
# import java.net.URL;
# import java.nio.file.Path;
# import java.util.Scanner;
# import magmodel.core.RetrievePathFromUrl;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.CoefficientExpansions;
# import magmodel.core.math.expansions.Expansion1D;
# import magmodel.core.math.expansions.Expansion1Ds;
# import magmodel.core.math.expansions.Expansion2D;
# import magmodel.core.math.expansions.Expansion2Ds;

import os

from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.geomagmodel.ts07.coefficientreader.thincurrentsheetshieldingcoefficients import (
    ThinCurrentSheetShieldingCoefficients
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion2d import (
    CoefficientExpansion2D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)


class SymmetricCylindricalExpansionPair:
    """@author stephgk1"""

    def __init__(self, tailExpansion, waveExpansion):
        self.tailExpansion = tailExpansion
        self.waveExpansion = waveExpansion

    def getTailExpansion(self):
        return self.tailExpansion

    def getWaveExpansion(self):
        return self.waveExpansion


class AsymmetricCylindricalExpansionPair:
    """@author stephgk1"""

    def __init__(self, tailExpansion, waveExpansion):
        self.tailExpansion = tailExpansion
        self.waveExpansion = waveExpansion

    def getTailExpansion(self):
        return self.tailExpansion

    def getWaveExpansion(self):
        return self.waveExpansion


class TS07DStaticCoefficientsFactory:
    """Use this class to construct ThinCurrentSheetShieldingCoefficients from
    the directory where the coefficients are located.

    The coefficients must be in the format as located at the model webpage:
    http://geomag_field.jhuapl.edu/model/TAIL_PAR.zip.

    @author Nicholas Sharp
    @author G.K.Stephens
    """

    def __init__(self):
        """Private constructor"""
        pass

    @staticmethod
    def create(*args):
        if len(rgs) == 1:
            (staticCoeffDirectory,) = args
            # Parses the static coefficients needed for the TS07D model from
            # the directory where the coefficients live.
            # @param staticCoeffDirectory the directory where the static
            # coefficients live, must be in the format that is on the webpage.
            # return a new set of ThinCurrentSheetShieldingCoefficients
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
                tailS.getTailExpansion(), tailS.getWaveExpansion(),
                tailO.getTailExpansion(), tailO.getWaveExpansion(),
                tailE.getTailExpansion(), tailE.getWaveExpansion())
        else:
            raise Exception

    @staticmethod
    def createFromBuiltInNewSet(numAzimuthalExpansions, numRadialExpansions):
        return TS07DStaticCoefficientsFactory.create(
            TS07DStaticCoefficientsFactory.retrieveNewBuiltInCoefficientsPath(),
            numAzimuthalExpansions, numRadialExpansions)


    @staticmethod
    def createFromBuiltInOriginalSet(numAzimuthalExpansions, numRadialExpansions):
        return TS07DStaticCoefficientsFactory.create(
            TS07DStaticCoefficientsFactory.retrieveOriginalBuiltInCoefficientsPath(),
            numAzimuthalExpansions, numRadialExpansions)

    @staticmethod
    def readTailS(staticCoeffDirectory, numRadialExpansions):
        """Reads in the Tail shielding coefficients from file

        @param staticCoeffDirectory
        @return the coefficients
        """
        numShieldAzimuthalExpansions = 15
        numShieldRadialExpansions = 5
        expansions = [None]*numRadialExpansions
        waveExpansions = [None]*numRadialExpansions
        for i in range(1, numRadialExpansions + 1):
            fileName = "tailamebhr_%02d.par" % i
            inFile = os.path.join(staticCoeffDirectory, fileName)
            values = (
                [[None]*numShieldRadialExpansions]*numShieldAzimuthalExpansions
            )
            waveNumberValues = [None]*numShieldRadialExpansions
            with open(fileName) as f:
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
            expansions[i - 1] = (
                CoefficientExpansions.createExpansionFromArray(values, 0, 1)
            )
            waveExpansions[i - 1] = (
                CoefficientExpansions.createExpansionFromArray(
                    waveNumberValues, 1)
            )

        return SymmetricCylindricalExpansionPair(
            Expansion1Ds.createFromArray(expansions, 1),
            Expansion1Ds.createFromArray(waveExpansions, 1)
        )

    @staticmethod
    def readTail(staticCoeffDirectory, numAzimuthalExpansions,
                 numRadialExpansions, fileName):
        """Reads in the Tail coefficients from file"""
        numShieldAzimuthalExpansions = 15
        numShieldRadialExpansions = 5
        expansions = [[None]*numRadialExpansions]*numAzimuthalExpansions
        waveExpansions = [[None]*numRadialExpansions]*numAzimuthalExpansions
        for n in range(1, numRadialExpansions + 1):
            for m in range(1, numAzimuthalExpansions + 1):
                inFile = os.path.join(staticCoeffDirectory,
                                      fileName + "%02d_%02d.par" % (n, m))
                with open(inFile) as f:
                    values = (
                        [[None]*numRadialExpansions]*
                         numShieldAzimuthalExpansions
                    )
                    for l in range(numShieldAzimuthalExpansions):
                        for k in range(1, numShieldRadialExpansions + 1):
                            # IS THIS RIGHT? ASSUMES 1 VALUE PER LINE.
                            line = f.readline()
                            val = float(line.split()[0])
                            values[l][k - 1] = val
                    waveNumberValues = [None]*numShieldRadialExpansions
                    for k in range(1, numShieldRadialExpansions + 1):
                        line = f.readline()
                        val = float(line.split()[0])
                        waveNumberValues[k - 1] = val
                expansions[m - 1][n - 1] = (
                    CoefficientExpansions.createExpansionFromArray(
                        values, 0, 1)
                )
                waveExpansions[m - 1][n - 1] = (
                    CoefficientExpansions.createExpansionFromArray(
                        waveNumberValues, 1)
                )
        return AsymmetricCylindricalExpansionPair(
            Expansion2Ds.createFromArray(expansions, 1, 1),
            Expansion2Ds.createFromArray(waveExpansions, 1, 1)
        )

    @staticmethod
    def retrieveNewBuiltInCoefficientsPath():
        """this method handles the details of grabbing the static coefficients
        that are in the source code"""
        raise Exception
        # public static Path retrieveNewBuiltInCoefficientsPath() {
        #     URL url = ThinCurrentSheetShieldingCoefficients.class.getResource("staticcoefficients/coeffs_n40_m8/");
        #     if (url == null) {
        #     String me = ThinCurrentSheetShieldingCoefficients.class.getPackage().getName().replace(".", "/")
        #         + "/staticcoefficients/coeffs_n40_m8/";
        #     String jar = ThinCurrentSheetShieldingCoefficients.class.getProtectionDomain().getCodeSource().getLocation()
        #         .getPath();
        #     String urlString = "jar:file:" + jar + "!/" + me;
        #     try {
        #         url = new URL(urlString);
        #     } catch (Exception e) {
        #         throw new RuntimeException(e);
        #     }
        #     }
        #     return RetrievePathFromUrl.retrieve(url);
        # }

    @staticmethod
    def retrieveOriginalBuiltInCoefficientsPath():
        """this method handles the details of grabbing the static coefficients
        that are in the source code
        """
        raise Exception
        #   public static Path retrieveOriginalBuiltInCoefficientsPath() {
        #     URL url = ThinCurrentSheetShieldingCoefficients.class.getResource("staticcoefficients/coeffs_n8_m6/");
        #     if (url == null) {
        #       String me = ThinCurrentSheetShieldingCoefficients.class.getPackage().getName().replace(".", "/")
        #           + "/staticcoefficients/coeffs_n8_m6/";
        #       String jar = ThinCurrentSheetShieldingCoefficients.class.getProtectionDomain().getCodeSource().getLocation()
        #           .getPath();
        #       String urlString = "jar:file:" + jar + "!/" + me;
        #       try {
        #         url = new URL(urlString);
        #       } catch (Exception e) {
        #         throw new RuntimeException(e);
        #       }
        #     }
        #     return RetrievePathFromUrl.retrieve(url);
        #   }
        # }