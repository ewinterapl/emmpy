"""emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils"""


import os
import re

from emmpy.crucible.core.time.utcepoch import UTCEpoch

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
from emmpy.geomagmodel.ts07.coefficientreader.ts07nonlinearparameters import (
    Ts07NonLinearParameters
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07facvariablecoefficients import (
    Ts07FacVariableCoefficients
)
from emmpy.magmodel.core.math.expansions.coefficientexpansions import (
    CoefficientExpansions
)
from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.java.lang.runtimeexception import RuntimeException


class TS07DVariableCoefficientsUtils:
    """A utility class for constructing and manipulating
    TS07DVariableCoefficients, and allows for reading and writing the
    coefficients to a file.

    @author Nicholas Sharp
    @author G.K.Stephens
    """

    def __init__(self):
        """DO NOT INSTANTIATE"""
        raise Exception

    @staticmethod
    def createTS07D(variableCoefficientsFile):
        """Constructs the standard TS07D set of coefficients from the ASCII
        file.

        This set of coefficient can be used to construct the TS07D model.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return a newly constructed set of TS07DVariableCoefficients
        constructed by parsing the ASCII file
        """
        # below is the default TS07 configuration
        azimuthal = 4
        radial = 5
        numCurrentSheets = 1
        ts07Fac = DefaultFacConfigurationOptions.TS07D
        return TS07DVariableCoefficientsUtils.create(
            variableCoefficientsFile, numCurrentSheets, azimuthal, radial,
            ts07Fac
        )

    @staticmethod
    def create(*args):
        if len(args) == 1:
            (variableCoefficientsFile,) = args
            # Constructs the TS07D set of coefficients from the ASCII file
            # WITH a customized resolution. This set of coefficient can be
            # used to construct the TS07D model. The model configuration is
            # interpreted from the file.
            # @param variableCoefficientsFile an ASCII file containing a list
            # of the coefficients
            # @return a newly constructed set of TS07DVariableCoefficients
            # constructed by parsing the ASCII file
            numCurrentSheets = (
                TS07DVariableCoefficientsUtils.readCurrentSheetNumber(
                    variableCoefficientsFile
                )
            )
            numAzimuthalExpansions = (
                TS07DVariableCoefficientsUtils.readAzimuthalExpansionNumber(
                    variableCoefficientsFile
                )
            )
            numRadialExpansions = (
                TS07DVariableCoefficientsUtils.readRadialExpansionNumber(
                    variableCoefficientsFile
                )
            )
            facConfiguration = (
                TS07DVariableCoefficientsUtils.readFACConfiguration(
                    variableCoefficientsFile
                )
            )
            return TS07DVariableCoefficientsUtils.create(
                variableCoefficientsFile, numCurrentSheets,
                numAzimuthalExpansions, numRadialExpansions, facConfiguration
            )
        elif len(args) == 4:
            (variableCoefficientsFile, numAzimuthalExpansions,
             numRadialExpansions, facConfiguration) = args
            # Constructs the TS07D set of coefficients from the ASCII file WITH
            # a customized resolution. This set of coefficient can be used to
            # construct the TS07D model.
            # @param variableCoefficientsFile an ASCII file containing a list
            # of the coefficients
            # @param numAzimuthalExpansions referred to as m
            # @param numRadialExpansions referred to as n
            # @param facConfiguration describes how to build the field aligned
            # current system
            # @return a newly constructed set of TS07DVariableCoefficients
            # constructed by parsing the ASCII file
            numCurrentSheets = 1
            return TS07DVariableCoefficientsUtils.create(
                variableCoefficientsFile, numCurrentSheets,
                numAzimuthalExpansions, numRadialExpansions,
                facConfiguration
            )
        elif len(args) == 5:
            (variableCoefficientsFile, numCurrentSheets,
             numAzimuthalExpansions, numRadialExpansions,
             facConfiguration) = args
            # Constructs the TS07D set of coefficients from the ASCII file WITH
            # a customized resolution and with MANY current sheets. This set of
            # coefficient can be used to construct the TS07D model.
            # This is package private because (at least for now) we want to
            # limit the public API to only support 1 or 2 current sheets, not
            # many current sheets.
            # @param variableCoefficientsFile an ASCII file containing a list
            # of the coefficients
            # @param numCurrentSheets the number of current sheets
            # @param numAzimuthalExpansions referred to as m
            # @param numRadialExpansions referred to as n
            # @param facConfiguration describes how to build the field aligned
            # current system
            # @return a newly constructed set of TS07DVariableCoefficients
            # constructed by parsing the ASCII file

            # the number of asymmetric expansions is simply the n*m
            numAsymmetricExpansions = (
                numRadialExpansions*numAzimuthalExpansions)

            # half the number of equatorial expansion coefficients, r+2*(r*a),
            # this is half the expansions as the dynamic pressure terms double
            # this number
            numHalfExpansions = numRadialExpansions + 2*numAsymmetricExpansions

            numExpansions = numHalfExpansions*2*numCurrentSheets

            # tot = 1(dipShield)+numExpansions+numSheets+
            # 5(hinge,warp,Kappa1,Kappa2,twist)+fac
            totalNumberOfCoefficients = (
                1 + numExpansions + numCurrentSheets + 5 +
                facConfiguration.getNumberOfFields()
            )

            coeffs = [None]*totalNumberOfCoefficients
            lineNumber = 0
            for line in open(variableCoefficientsFile):
                try:
                    coeffs[lineNumber] = float(line.split()[0])
                    lineNumber += 1
                except ValueError:
                    break

            # NOTE, this is a deviation from the FORTRAN code, the FORTRAN
            # code handles this in the WARPED subroutine
            twist = coeffs[-1]/10
            coeffs[-1] = twist

            return TS07DVariableCoefficientsUtils.createFromArray(
                coeffs, numCurrentSheets, numAzimuthalExpansions,
                numRadialExpansions, facConfiguration
            )
        elif len(args) == 6:
            if isinstance(args[1], list):
                (utcNumerator, coeffsFiles, numCurrentSheets,
                 numAzimuthalExpansions, numRadialExpansions, facConfiguration,
                 maxCacheSize) = args

                # sort them in case they aren't ordered
                coeffsFiles.sort()

                # Reading the files takes some time, so let's use a cache

                # // cache loader
                # CacheLoader<Integer, TS07DVariableCoefficients> cacheLoader =
                #     new TS07DVariableCoefficientsCacheLoader(coeffsFiles, numCurrentSheets,
                #         numAzimuthalExpansions, numRadialExpansions, facConfiguration);

                # // make the cache
                # final LoadingCache<Integer, TS07DVariableCoefficients> loadingCache =
                #     CacheBuilder.newBuilder().maximumSize(maxCacheSize).build(cacheLoader);

                # // turn it into a GaugedIndexable
                # GaugedIndexable<TS07DVariableCoefficients> gi =
                #     new TS07DVariableCoefficientsGaugedIndexable(coeffsFiles, utcNumerator, loadingCache);

                # // add the searching
                # GaugedIndexable<TS07DVariableCoefficients> coefficients = GaugedIndexables.binarySearch(gi);

                # // finally, interpolate the function
                # return TS07DVariableCoefficientsUtils.interpolate(coefficients);
                # }
            elif isinstance(args[1], str):
                pass
                # * Constructs a {@link Function} of {@link TS07DVariableCoefficients} as a function of time from a
                # * directory (or directory tree) of {@link TS07DVariableCoefficients} files. The file names must
                # * match YEAR_DOY_HH_MM.par, and the time axis is determined by the file name and the input
                # * {@link UTCNumerator}. The coefficients are linearly interpolated.
                # * <p>
                # * TODO the current implementation will not step into sym links.
                # *
                # * @param utcNumerator
                # * @param variableCoeffsDir the directory that contains the variable coefficients files, the file
                # *        name must be in the format YEAR_DOY_HH_MM.par.
                # * @param numAzimuthalExpansions
                # * @param numRadialExpansions
                # * @param facConfiguration
                # *
                # * @return a newly constructed {@link Function} that takes a {@link Double} representing the time
                # *         (matching the time system from the input from the {@link UTCNumerator}) and returns a
                # *         {@link TS07DVariableCoefficients}, that is interpolated
                # */
                #   public static Function<Double, TS07DVariableCoefficients> create(final UTCNumerator utcNumerator,
                #       final Path variableCoeffsDir, final int numCurrentSheets, final int numAzimuthalExpansions,
                #       final int numRadialExpansions, final FacConfiguration facConfiguration) {

                #     // recursively loop through the directory tree
                #     final List<Path> coeffsFiles = Lists.newArrayList();
                #     try {

                #       FileVisitor<Path> visitor = new SimpleFileVisitor<Path>() {
                #         @Override
                #         public FileVisitResult visitFile(Path file,
                #             @SuppressWarnings("unused") BasicFileAttributes attrs) throws IOException {
                #           if (FILE_NAME_FILTER.accept(file)) {
                #             coeffsFiles.add(file);
                #           }
                #           return FileVisitResult.CONTINUE;
                #         }
                #       };

                #       Files.walkFileTree(variableCoeffsDir, visitor);

                #     } catch (IOException e) {
                #       throw new RuntimeException(e);
                #     }

                #     int maxCacheSize = 50;

                #     return create(utcNumerator, coeffsFiles, numCurrentSheets, numAzimuthalExpansions,
                #         numRadialExpansions, facConfiguration, maxCacheSize);
                #   }
            else:
                raise Exception

        #   /**
        #    * Full constructor, in general you should not call this.
        #    *
        #    * @param cfAmplitude
        #    * @param equatorialCoeffs
        #    * @param facCoeffs
        #    * @return
        #    */
        #   private static TS07DVariableCoefficients create(double cfAmplitude,
        #       Ts07EquatorialVariableCoefficients equatorialCoeffs, Ts07FacVariableCoefficients facCoeffs) {
        #     return new TS07DVariableCoefficients(cfAmplitude, equatorialCoeffs, facCoeffs);
        #   }

        # }
        else:
            raise Exception

    @staticmethod
    def createWithThinCurrentSheet(
        variableCoefficientsFile, numAzimuthalExpansions, numRadialExpansions,
        facConfiguration
    ):
        """Constructs the TS07D set of coefficients from the ASCII file WITH a
        customized resolution and with TWO current sheets.

        This set of coefficient can be used to construct the TS07D model.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @param numAzimuthalExpansions referred to as m
        @param numRadialExpansions referred to as n
        @param facConfiguration describes how to build the field aligned
        current system
        @return a newly constructed set of TS07DVariableCoefficients
        constructed by parsing the ASCII file
        """
        numCurrentSheets = 2
        return TS07DVariableCoefficientsUtils.create(
            variableCoefficientsFile, numCurrentSheets, numAzimuthalExpansions,
            numRadialExpansions, facConfiguration
        )

    @staticmethod
    def readQ(variableCoefficientsFile):
        """Parses the Q value (the value of the objective function) from the
        variable coefficients file.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return the Q value parsed from the file
        """
        Q = None
        for line in open(variableCoefficientsFile):
            if "Q=" in line:
                Q = float(line.split()[-1])
                break
        return Q

    @staticmethod
    def readBrms(variableCoefficientsFile):
        """Parses the B-rms value from the variable coefficients file.

        @param variableCoefficientsFile an ASCII file containing a list of the coefficients
        @return the B-rms value parsed from the file
        """
        B_rms = None
        for line in open(variableCoefficientsFile):
            if "B_rms=" in line:
                B_rms = float(line.split()[-1])
                break
        return B_rms

    @staticmethod
    def readDynamicPressure(variableCoefficientsFile):
        """Parses the dynamic pressure from the variable coefficients file.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return the dynamic pressure parsed from the file
        """
        Pdyn = None
        for line in open(variableCoefficientsFile):
            if "Pdyn=" in line:
                Pdyn = float(line.split()[-1])
                break
        return Pdyn

    @staticmethod
    def readDipoleTiltAngle(variableCoefficientsFile):
        """Parses the dipole tilt angle from the variable coefficients file.

        @param variableCoefficientsFile an ASCII file containing a list of the coefficients
        @return the dipole tilt angle parsed from the file
        """
        tilt = None
        for line in open(variableCoefficientsFile):
            if "tilt=" in line:
                tilt = float(line.split()[-1])
                break
        return tilt

    @staticmethod
    def readCurrentSheetNumber(variableCoefficientsFile):
        """Parses the number of current sheets from the variable coefficients
        file.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return the number of current sheets parsed from the file
        """
        numCurrSheets = 0
        for line in open(variableCoefficientsFile):
            if " # current sheet thickness" in line:
                numCurrSheets += 1
        return numCurrSheets

    @staticmethod
    def readAzimuthalExpansionNumber(variableCoefficientsFile):
        """Parses the azimuthal expansion number from the variable coefficients
        file.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return the azimuthal expansion number parsed from the file
        """
        m = 0
        for line in open(variableCoefficientsFile):
            if "M=" in line:
                m_str = line.split()[-1]
                m = int(m_str)
                break
        return m

    @staticmethod
    def readRadialExpansionNumber(variableCoefficientsFile):
        """Parses the radial expansion number from the variable coefficients
        file.

        @param variableCoefficientsFile an ASCII file containing a list of
        the coefficients
        @return the radial expansion number parsed from the file
        """
        n = 0
        for line in open(variableCoefficientsFile):
            if "N=" in line:
                n_str = line.split()[-1]
                n = int(n_str)
                break
        return n

    @staticmethod
    def readFACConfiguration(variableCoefficientsFile):
        """Parses the FAC configuration number from the variable coefficients
        file.

        @param variableCoefficientsFile an ASCII file containing a list of the
        coefficients
        @return the FAC configuration number parsed from the file
        """
        count = 0
        for line in open(variableCoefficientsFile):
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
            raise RuntimeException(
                "Invalid number of FACs to construct a "
                "DefaultFacConfiguration"
            )

    @staticmethod
    def createFromArray(
        coeffs, numCurrentSheets, numAzimuthalExpansions, numRadialExpansions,
        facConfiguration
    ):
        """Constructs a newly constructed Ts07FacVariableCoefficients from an
        array of doubles.

        A double array is the data structured used in the Fortran version of
        the code.

        @param coefficients an array containing the coefficients
        @param numAzimuthalExpansions referred to as m
        @param numRadialExpansions referred to as n
        @param facConfiguration describes how to build the field aligned
        current system
        @return a newly constructed {@link TS07DVariableCoefficients}
        """

        # the number of asymmetric expansions is simply the n*m
        numAsymmetricExpansions = numRadialExpansions*numAzimuthalExpansions

        # half the number of equatorial expansion coefficients, r+2*(r*a), this
        # is half the expansions as the dynamic pressure terms double this
        # number
        numHalfExpansions = numRadialExpansions + 2*numAsymmetricExpansions

        numExpansions = numHalfExpansions*2*numCurrentSheets

        # 2*halfExpansions + 11 other coefficients
        totalNumberOfCoefficients = (
            numExpansions + 1 + numCurrentSheets + 5 +
            facConfiguration.getNumberOfFields()
        )

        # Parse file data into proper variables. This too will need to be
        # changed if different coefficient formats are use.
        cfAmplitude = coeffs[0]

        eqLinearCoeffs = []

        # loop through the number of current sheets
        # for (int nCurr = 0; nCurr < numCurrentSheets; nCurr++) {
        for nCurr in range(numCurrentSheets):
            index = nCurr*numHalfExpansions*2
            aSym = [None]*numRadialExpansions
            aSymPdynDependent = [None]*numRadialExpansions
            aOdd = [[None]*numRadialExpansions]*numAzimuthalExpansions
            aOddPdynDependent = (
                [[None]*numRadialExpansions]*numAzimuthalExpansions
            )
            aEven = [[None]*numRadialExpansions]*numAzimuthalExpansions
            aEvenPdynDependent = (
                [[None]*numRadialExpansions]*numAzimuthalExpansions
            )
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

            aSymExpansion = (
                CoefficientExpansions.createExpansionFromArray(aSym, 1)
            )
            aSymPdynDependentExpansion = (
                CoefficientExpansions.createExpansionFromArray(
                    aSymPdynDependent, 1
                )
            )
            aOddExpansion = (
                CoefficientExpansions.createExpansionFromArray(aOdd, 1, 1)
            )
            aOddPdynDependentExpansion = (
                CoefficientExpansions.createExpansionFromArray(
                    aOddPdynDependent, 1, 1
                )
            )
            aEvenExpansion = (
                CoefficientExpansions.createExpansionFromArray(aEven, 1, 1)
            )
            aEvenPdynDependentExpansion = (
                CoefficientExpansions.createExpansionFromArray(
                    aEvenPdynDependent, 1, 1
                )
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

        numFacFields = facConfiguration.getNumberOfFields()

        # the field aligned current amplitudes
        facAmps = [None]*numFacFields
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
        # handles this in the WARPED subroutine
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

    @staticmethod
    def writeToFile(*args):
        if len(args) == 2:
            (outputFile, coeffs) = args
            # Given a set of TS07DVariableCoefficients, writes the files to an
            # ASCII file in the standard format.
            # @param outputFile the output file to write
            # @param coeffs the set of TS07DVariableCoefficients
            TS07DVariableCoefficientsUtils.writeToFile(
                outputFile, coeffs, -9999.99, -9999.99
            )
        elif len(args) == 4:
            (outputFile, coeffs, qValue, brms) = args
            # Given a set of TS07DVariableCoefficients, writes the files to an
            # ASCII file in the standard format.
            # @param outputFile
            # @param coeffs
            # @param qValue
            # @param brms
            formatString = "%15.6G"
            TS07DVariableCoefficientsUtils.writeToFile(
                outputFile, formatString, coeffs, qValue, brms
            )
        elif len(args) == 5:
            (outputFile, format, coeffs, qValue, brms) = args
            with open(outputFile, "w") as f:
                # f.write(format % coeffs.getDipoleShieldingAmplitude(),
                #         "  # dipole shielding field amp.", sep="")
                s = format % coeffs.getDipoleShieldingAmplitude() + "  # dipole shielding field amp.\n"
                f.write(s)
                for eqLinearCoeffs in coeffs.getEquatorialCoefficients().getLinearCoeffs():
                    aSym = eqLinearCoeffs.getCoeffs().getTailSheetSymmetricValues()
                    aSymPdynDep = eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetSymmetricValues()
                    aOdd = eqLinearCoeffs.getCoeffs().getTailSheetOddValues()
                    aOddPdynDep = eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetOddValues()
                    aEven = eqLinearCoeffs.getCoeffs().getTailSheetEvenValues()
                    aEvenPdynDep = eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetEvenValues()

                    # Start with the dynamic pressure independent expansion
                    for n in range(aSym.getLowerBoundIndex(), aSym.getUpperBoundIndex() + 1):
                        descriptor = "  # n-%s eq. amp.\n" % n
                        s = format % aSym.getCoefficient(n) + descriptor
                        f.write(s)

                    for n in range(aOdd.getJLowerBoundIndex(), aOdd.getJUpperBoundIndex() + 1):
                        for m in range(aOdd.getILowerBoundIndex(), aOdd.getIUpperBoundIndex() + 1):
                            descriptor = "  # m-%s n-%s odd eq. amp.\n" % (m, n)
                            s = format % aOdd.getCoefficient(m, n) + descriptor
                            f.write(s)

                    for n in range(aEven.getJLowerBoundIndex(), aEven.getJUpperBoundIndex() + 1):
                        for m in range(aEven.getILowerBoundIndex(), aEven.getIUpperBoundIndex() + 1):
                            descriptor = "  # m-%s n-%s even eq. amp.\n" % (m, n)
                            s = format % aEven.getCoefficient(m, n) + descriptor
                            f.write(s)

                    # now do the dynamic pressure dependent expansion
                    for n in range(aSymPdynDep.getLowerBoundIndex(), aSymPdynDep.getUpperBoundIndex() + 1):
                        descriptor = "  # n-%s * sqrt(pdyn) eq. amp.\n" % n
                        s = format % aSymPdynDep.getCoefficient(n) + descriptor
                        f.write(s)

                    for n in range(aOddPdynDep.getJLowerBoundIndex(), aOddPdynDep.getJUpperBoundIndex() + 1):
                        for m in range(aOddPdynDep.getILowerBoundIndex(), aOddPdynDep.getIUpperBoundIndex() + 1):
                            descriptor = "  # m-%s n-%s odd * sqrt(pdyn) eq. amp.\n" % (m, n)
                            s = format % aOddPdynDep.getCoefficient(m, n) + descriptor
                            f.write(s)

                    for n in range(aEvenPdynDep.getJLowerBoundIndex(), aEvenPdynDep.getJUpperBoundIndex() + 1):
                        for m in range(aEvenPdynDep.getILowerBoundIndex(), aEvenPdynDep.getIUpperBoundIndex() + 1):
                            descriptor = "  # m-%s n-%s even * sqrt(pdyn) eq. amp.\n" % (m, n)
                            s = format % aEvenPdynDep.getCoefficient(m, n) + descriptor
                            f.write(s)

                for facConfiguration in coeffs.getFacCoefficients().getFacConfigurations():
                    tp = facConfiguration.getTrigParity()
                    if tp.equals(TrigParity.EVEN):
                        ss = "sym"
                    else:
                        ss = "asym"
                    s = format % facConfiguration.getAmplitudeScaling() + "  # reg-" + str(facConfiguration.getRegion().getAsInt()) + " M-" + str(facConfiguration.getMode()) + " " + ss + ". amp.\n"
                    f.write(s)

                for currentSheetThickness in coeffs.getEquatorialCoefficients().getCurrThicks():
                    s = format % currentSheetThickness + "  # current sheet thickness\n"
                    f.write(s)

                f.write(format % coeffs.getEquatorialCoefficients().getHingeDistance() + "  # hinge distance\n")
                f.write(format % coeffs.getEquatorialCoefficients().getWarpingParam() + "  # warping parameter\n")
                f.write(format % coeffs.getFacCoefficients().getRegion1KappaScaling() + "  # reg-1 scaling\n")
                f.write(format % coeffs.getFacCoefficients().getRegion2KappaScaling() + "  # reg-2 scaling\n")
                f.write(format % coeffs.getEquatorialCoefficients().getTwistParam()*10.0 + "  # twist factor * 10\n")

                f.write("     Q=" + format % qValue + "\n")
                f.write(" B_rms=" + format % brms + "\n")
                f.write("     M=", "%15d\n" % coeffs.getEquatorialCoefficients().getLinearCoeffs().get(0).getNumAzimuthalExpansions())
                f.write("     N=", "%15d\n" % coeffs.getEquatorialCoefficients().getLinearCoeffs().get(0).getNumRadialExpansions())
        else:
            raise Exception

    @staticmethod
    def append(inputFile, dyanmicPressure, dipoleTilt):
        format = "%15.6G\n"
        with open(inputFile, "a") as f:
            f.write("  Pdyn=" + format % dyanmicPressure)
            f.write("  tilt=" + format % dipoleTilt)

    @staticmethod
    def writeToAnnotatedFile(*args):
        if len(args) == 2:
            (outputFile, coeffs) = args
            # @param outputFile the output file to write
            # @param coeffs the set of {@link TS07DVariableCoefficients}
            TS07DVariableCoefficientsUtils.writeToAnnotatedFile(
                outputFile, coeffs, -9999.99, -9999.99)
        elif len(args) == 4:
            (outputFile, coeffs, qValue, brms) = args
            # Given a set of TS07DVariableCoefficients, writes the files to an
            # ASCII file in the annotated format.
            format = "%15.6G"
            TS07DVariableCoefficientsUtils.writeToFile(
                outputFile, format, coeffs, qValue, brms)

    @staticmethod
    def createUnityLinear(
        nonLinearParams, numAzimuthalExpansions, numRadialExpansions,
        facConfiguration
    ):
        """Constructs a set of coefficients where all the linear coefficients
        are set to 1 and the non-linear are supplied.

        # Since the linear coefficients are used in a linear expansion, it is
        # useful to set these all to one for linear regression needs.
        """

        # the linear parameters are fit with each evaluation of the model, so
        # it doesn't matter what they are set to initially,
        s = CoefficientExpansions.createUnity(1, numRadialExpansions)
        a = CoefficientExpansions.createUnity(
            1, numAzimuthalExpansions, 1, numRadialExpansions)
        numCurrentSheets = len(nonLinearParams.getCurrentSheetThicknesses())
        eqLinearCoeffs = []
        for i in range(numCurrentSheets):
            eqLinearCoeff = Ts07EquatorialLinearCoefficients.create(
                s, s, a, a, a, a, numAzimuthalExpansions, numRadialExpansions)
            eqLinearCoeffs.append(eqLinearCoeff)
        facCoeffsArray = [1.0]*facConfiguration.getNumberOfFields()
        equatorialCoeffs = Ts07EquatorialVariableCoefficients(
            nonLinearParams.getCurrentSheetThicknesses(),
            nonLinearParams.getHingeDist(), nonLinearParams.getWarpParam(),
            nonLinearParams.getTwistFact(), eqLinearCoeffs)
        facCoeffs = Ts07FacVariableCoefficients(
            nonLinearParams.getFacRegion1Kappa(),
            nonLinearParams.getFacRegion2Kappa(),
            facConfiguration.createFromCoeffs(facCoeffsArray))
        # all the linear parameters are set to 1
        unityCoeffs = TS07DVariableCoefficientsUtils.create(
            1.0, equatorialCoeffs, facCoeffs)
        return unityCoeffs

    @staticmethod
    def interpolate(*args):
        if len(args) == 1:
            pass
            # Given a GaugedIndexable of TS07DVariableCoefficients, i.e. a
            # discrete number of TS07DVariableCoefficients on a time line,
            # creates a Function where the coefficients have been linearly
            # interpolated.
            # @param coefficients a GaugedIndexable of
            # TS07DVariableCoefficients.
            # @return a Function of Doubles to TS07DVariableCoefficients,
            # where the coefficients have been linearly interpolated
            # public static Function<Double, TS07DVariableCoefficients> interpolate(
            #     final GaugedIndexable<TS07DVariableCoefficients> coefficients) {
            #     checkArgument(coefficients.size() > 1,
            #         "The size of the coefficients must be greater than 1 to interpolate, it was %s",
            #         coefficients.size());
            #     return new Function<Double, TS07DVariableCoefficients>() {
            #     @Override
            #     public TS07DVariableCoefficients apply(Double time) {
            #     int index = coefficients.indexLastLessThanOrEqualTo(time);
            #     // if we are on the last index, it is still valid to interpolate, but we must now grab the
            #     // second to last guy
            #     if (index == coefficients.size() - 1) {
            #         index--;
            #     }
            #     TS07DVariableCoefficients tv1 = coefficients.get(index);
            #     TS07DVariableCoefficients tv2 = coefficients.get(index + 1);
            #     return interpolate(tv1, tv2, coefficients.getGauge(index), coefficients.getGauge(index + 1),
            #         time);
            #     }
            # };
            # }
        elif len(args) == 5:
            if isinstance(args[0], TS07DVariableCoefficients):
                pass
                # /**
                # * Creates a new set of {@link TS07DVariableCoefficients} by interpolating between the two sets of
                # * input coefficients. Each individual coefficient is linearly interpolated.
                # *
                # * @param coefficients1 the first set of coefficients
                # * @param coefficients2 the second set of coefficients
                # * @param time1 the time associated with the first set of coefficients
                # * @param time2 the time associated with the second set of coefficients
                # * @param evaluateTime the time to evaluate the interpolation
                # * @return a newly constructed {@link TS07DVariableCoefficients} that is the linear interpolation
                # *         of each individual coefficient.
                # */
                # public static TS07DVariableCoefficients interpolate(final TS07DVariableCoefficients coefficients1,
                #     final TS07DVariableCoefficients coefficients2, double time1, double time2,
                #     double evaluateTime) {
                # checkArgument(evaluateTime >= time1,
                #     "the evaluation time (%s) must be greater than or equal to the first time (%s)",
                #     evaluateTime, time1);
                # checkArgument(evaluateTime <= time2,
                #     "the evaluation time (%s) must be less than or equal to the first time (%s)", evaluateTime,
                #     time2);
                # double cfAmplitude = interpolate(coefficients1.getDipoleShieldingAmplitude(),
                #     coefficients2.getDipoleShieldingAmplitude(), time1, time2, evaluateTime);
                # Ts07EquatorialVariableCoefficients eq = interpolate(coefficients1.getEquatorialCoefficients(),
                #     coefficients2.getEquatorialCoefficients(), time1, time2, evaluateTime);
                # Ts07FacVariableCoefficients fac = interpolate(coefficients1.getFacCoefficients(),
                #     coefficients2.getFacCoefficients(), time1, time2, evaluateTime);
                # return new TS07DVariableCoefficients(cfAmplitude, eq, fac);
                # }
            elif isinstance(args[0], Ts07NonLinearParameters):
                pass
                # public static Ts07NonLinearParameters interpolate(final Ts07NonLinearParameters coefficients1,
                #     final Ts07NonLinearParameters coefficients2, double time1, double time2,
                #     double evaluateTime) {
                #     checkArgument(coefficients1.getCurrentSheetThicknesses().size() == coefficients2
                #         .getCurrentSheetThicknesses().size(), "must be same size");
                #     double facRegion1Kappa = interpolate(coefficients1.getFacRegion1Kappa(),
                #         coefficients2.getFacRegion1Kappa(), time1, time2, evaluateTime);
                #     double facRegion2Kappa = interpolate(coefficients1.getFacRegion2Kappa(),
                #         coefficients2.getFacRegion2Kappa(), time1, time2, evaluateTime);
                #     List<Double> currThicks = Lists.newArrayList();
                #     for (int i = 0; i < coefficients1.getCurrentSheetThicknesses().size(); i++) {
                #     double currThick = interpolate(coefficients1.getCurrentSheetThicknesses().get(i),
                #         coefficients2.getCurrentSheetThicknesses().get(i), time1, time2, evaluateTime);
                #     currThicks.add(currThick);
                #     }
                #     double hingeDist = interpolate(coefficients1.getHingeDist(), coefficients2.getHingeDist(),
                #         time1, time2, evaluateTime);
                #     double warpParam = interpolate(coefficients1.getWarpParam(), coefficients2.getWarpParam(),
                #         time1, time2, evaluateTime);
                #     double twistFact = interpolate(coefficients1.getTwistFact(), coefficients2.getTwistFact(),
                #         time1, time2, evaluateTime);
                #     return new Ts07NonLinearParameters(facRegion1Kappa, facRegion2Kappa, currThicks, hingeDist,
                #         warpParam, twistFact);
                # }
            else:
                raise Exception
            #   @VisibleForTesting
            #   static double interpolate(double leftRange, double rightRange, double leftDomain,
            #       double rightDomain, double evaluateDomain) {

            #     double slope = (rightRange - leftRange) / (rightDomain - leftDomain);

            #     return (evaluateDomain - leftDomain) * slope + leftRange;
            #   }

            #   @VisibleForTesting
            #   static CoefficientExpansion1D interpolate(CoefficientExpansion1D leftRange,
            #       CoefficientExpansion1D rightRange, double leftDomain, double rightDomain,
            #       double evaluateDomain) {

            #     checkArgument(leftRange.getLowerBoundIndex() == rightRange.getLowerBoundIndex());
            #     checkArgument(leftRange.getUpperBoundIndex() == rightRange.getUpperBoundIndex());

            #     int firstRadialExpansionNumber = leftRange.getLowerBoundIndex();

            #     int length = leftRange.getUpperBoundIndex() - firstRadialExpansionNumber + 1;

            #     double[] r = new double[length];

            #     for (int i = 0; i < length; i++) {

            #       double leftValue = leftRange.getCoefficient(i + firstRadialExpansionNumber);
            #       double rightValue = rightRange.getCoefficient(i + firstRadialExpansionNumber);

            #       r[i] = interpolate(leftValue, rightValue, leftDomain, rightDomain, evaluateDomain);
            #     }

            #     return CoefficientExpansions.createExpansionFromArray(r, firstRadialExpansionNumber);
            #   }

            #   @VisibleForTesting
            #   static CoefficientExpansion2D interpolate(CoefficientExpansion2D leftRange,
            #       CoefficientExpansion2D rightRange, double leftDomain, double rightDomain,
            #       double evaluateDomain) {

            #     checkArgument(leftRange.getJLowerBoundIndex() == rightRange.getJLowerBoundIndex());
            #     checkArgument(leftRange.getJUpperBoundIndex() == rightRange.getJUpperBoundIndex());

            #     checkArgument(leftRange.getILowerBoundIndex() == rightRange.getILowerBoundIndex());
            #     checkArgument(leftRange.getIUpperBoundIndex() == rightRange.getIUpperBoundIndex());

            #     int firstRadialExpansionNumber = leftRange.getJLowerBoundIndex();
            #     int radialLength = leftRange.getJUpperBoundIndex() - firstRadialExpansionNumber + 1;

            #     int firstAzimuthalExpansionNumber = leftRange.getILowerBoundIndex();
            #     int azimuthalLength = leftRange.getIUpperBoundIndex() - firstAzimuthalExpansionNumber + 1;

            #     double[][] r = new double[azimuthalLength][radialLength];

            #     for (int m = 0; m < azimuthalLength; m++) {
            #       for (int n = 0; n < radialLength; n++) {

            #         double leftValue = leftRange.getCoefficient(m + firstAzimuthalExpansionNumber,
            #             n + firstRadialExpansionNumber);
            #         double rightValue = rightRange.getCoefficient(m + firstAzimuthalExpansionNumber,
            #             n + firstRadialExpansionNumber);

            #         r[m][n] = interpolate(leftValue, rightValue, leftDomain, rightDomain, evaluateDomain);
            #       }
            #     }

            #     return CoefficientExpansions.createExpansionFromArray(r, firstAzimuthalExpansionNumber,
            #         firstRadialExpansionNumber);
            #   }

            #   /**
            #    * Linearly interpolates between two equal sized arrays
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static double[] interpolate(double leftRange[], double[] rightRange, double leftDomain,
            #       double rightDomain, double evaluateDomain) {

            #     checkArgument(leftRange.length == rightRange.length);

            #     double[] r = new double[leftRange.length];

            #     for (int i = 0; i < leftRange.length; i++) {
            #       r[i] = interpolate(leftRange[i], rightRange[i], leftDomain, rightDomain, evaluateDomain);
            #     }

            #     return r;
            #   }

            #   /**
            #    * Linearly interpolates between two equal sized 2-D arrays
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static double[][] interpolate(double leftRange[][], double[][] rightRange, double leftDomain,
            #       double rightDomain, double evaluateDomain) {

            #     checkArgument(leftRange.length == rightRange.length && !ArrayUtilities.isRagged(leftRange)
            #         && !ArrayUtilities.isRagged(rightRange));

            #     double[][] r = new double[leftRange.length][leftRange[0].length];

            #     for (int i = 0; i < leftRange.length; i++) {
            #       r[i] = interpolate(leftRange[i], rightRange[i], leftDomain, rightDomain, evaluateDomain);
            #     }

            #     return r;
            #   }

            #   /**
            #    * Linearly interpolates between two equal sized 3-D arrays
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static double[][][] interpolate(double leftRange[][][], double[][][] rightRange,
            #       double leftDomain, double rightDomain, double evaluateDomain) {

            #     checkArgument(leftRange.length == rightRange.length && !ArrayUtilities.isRagged(leftRange)
            #         && !ArrayUtilities.isRagged(rightRange));

            #     double[][][] r = new double[leftRange.length][leftRange[0].length][leftRange[0][0].length];

            #     for (int i = 0; i < leftRange.length; i++) {
            #       r[i] = interpolate(leftRange[i], rightRange[i], leftDomain, rightDomain, evaluateDomain);
            #     }

            #     return r;

            #   }

            #   /**
            #    * Interpolates the {@link Ts07FacVariableCoefficients}
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static Ts07EquatorialVariableCoefficients interpolate(
            #       Ts07EquatorialVariableCoefficients leftRange, Ts07EquatorialVariableCoefficients rightRange,
            #       double leftDomain, double rightDomain, double evaluateDomain) {

            #     List<Double> currThicks = Lists.newArrayList();
            #     for (int i = 0; i < leftRange.getCurrThicks().size(); i++) {
            #       double currThick = interpolate(leftRange.getCurrThicks().get(i),
            #           rightRange.getCurrThicks().get(i), leftDomain, rightDomain, evaluateDomain);
            #       currThicks.add(currThick);
            #     }
            #     double hingeDist = interpolate(leftRange.getHingeDistance(), rightRange.getHingeDistance(),
            #         leftDomain, rightDomain, evaluateDomain);
            #     double warpingParam = interpolate(leftRange.getWarpingParam(), rightRange.getWarpingParam(),
            #         leftDomain, rightDomain, evaluateDomain);
            #     double twistParam = interpolate(leftRange.getTwistParam(), rightRange.getTwistParam(),
            #         leftDomain, rightDomain, evaluateDomain);

            #     List<Ts07EquatorialLinearCoefficients> linearCoeffs = Lists.newArrayList();
            #     for (int i = 0; i < leftRange.getLinearCoeffs().size(); i++) {
            #       Ts07EquatorialLinearCoefficients linearCoeff = interpolate(leftRange.getLinearCoeffs().get(i),
            #           rightRange.getLinearCoeffs().get(i), leftDomain, rightDomain, evaluateDomain);
            #       linearCoeffs.add(linearCoeff);
            #     }

            #     return new Ts07EquatorialVariableCoefficients(currThicks, hingeDist, warpingParam, twistParam,
            #         linearCoeffs);
            #   }

            #   /**
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static Ts07EquatorialLinearCoefficients interpolate(Ts07EquatorialLinearCoefficients leftRange,
            #       Ts07EquatorialLinearCoefficients rightRange, double leftDomain, double rightDomain,
            #       double evaluateDomain) {

            #     checkArgument(leftRange.getNumRadialExpansions() == rightRange.getNumRadialExpansions(),
            #         "Both set of variable coefficients must have the same number of radial expansions, they were (%s, %s).",
            #         leftRange.getNumRadialExpansions(), rightRange.getNumRadialExpansions());

            #     checkArgument(leftRange.getNumAzimuthalExpansions() == rightRange.getNumAzimuthalExpansions(),
            #         "Both set of variable coefficients must have the same number of azimuthal expansions, they were (%s, %s).",
            #         leftRange.getNumAzimuthalExpansions(), rightRange.getNumAzimuthalExpansions());

            #     CoefficientExpansion1D aSym = interpolate(leftRange.getCoeffs().getTailSheetSymmetricValues(),
            #         rightRange.getCoeffs().getTailSheetSymmetricValues(), leftDomain, rightDomain,
            #         evaluateDomain);
            #     CoefficientExpansion1D aSymPdynDependent =
            #         interpolate(leftRange.getPdynDependentCoeffs().getTailSheetSymmetricValues(),
            #             rightRange.getPdynDependentCoeffs().getTailSheetSymmetricValues(), leftDomain,
            #             rightDomain, evaluateDomain);

            #     CoefficientExpansion2D aOdd = interpolate(leftRange.getCoeffs().getTailSheetOddValues(),
            #         rightRange.getCoeffs().getTailSheetOddValues(), leftDomain, rightDomain, evaluateDomain);
            #     CoefficientExpansion2D aOddPdynDependent =
            #         interpolate(leftRange.getPdynDependentCoeffs().getTailSheetOddValues(),
            #             rightRange.getPdynDependentCoeffs().getTailSheetOddValues(), leftDomain, rightDomain,
            #             evaluateDomain);

            #     CoefficientExpansion2D aEven = interpolate(leftRange.getCoeffs().getTailSheetEvenValues(),
            #         rightRange.getCoeffs().getTailSheetEvenValues(), leftDomain, rightDomain, evaluateDomain);
            #     CoefficientExpansion2D aEvenPdynDependent =
            #         interpolate(leftRange.getPdynDependentCoeffs().getTailSheetEvenValues(),
            #             rightRange.getPdynDependentCoeffs().getTailSheetEvenValues(), leftDomain, rightDomain,
            #             evaluateDomain);

            #     return Ts07EquatorialLinearCoefficients.create(aSym, aSymPdynDependent, aOdd, aOddPdynDependent,
            #         aEven, aEvenPdynDependent, leftRange.getNumAzimuthalExpansions(),
            #         leftRange.getNumRadialExpansions());
            #   }

            #   /**
            #    * Interpolates the {@link Ts07FacVariableCoefficients}
            #    * 
            #    * @param leftRange
            #    * @param rightRange
            #    * @param leftDomain
            #    * @param rightDomain
            #    * @param evaluateDomain
            #    * @return
            #    */
            #   @VisibleForTesting
            #   static Ts07FacVariableCoefficients interpolate(Ts07FacVariableCoefficients leftRange,
            #       Ts07FacVariableCoefficients rightRange, double leftDomain, double rightDomain,
            #       double evaluateDomain) {

            #     double region1KappaScaling = interpolate(leftRange.getRegion1KappaScaling(),
            #         rightRange.getRegion1KappaScaling(), leftDomain, rightDomain, evaluateDomain);
            #     double region2KappaScaling = interpolate(leftRange.getRegion2KappaScaling(),
            #         rightRange.getRegion2KappaScaling(), leftDomain, rightDomain, evaluateDomain);

            #     ImmutableList.Builder<FacConfigurationOptions> facConfigurations = ImmutableList.builder();

            #     // TODO check size is same
            #     for (int i = 0; i < leftRange.getLienarCoefficients().length; i++) {

            #       // TODO check options are the same
            #       FacConfigurationOptions leftConfig = leftRange.getFacConfigurations().get(i);

            #       double amplitudeScaling = interpolate(leftRange.getLienarCoefficients()[i],
            #           rightRange.getLienarCoefficients()[i], leftDomain, rightDomain, evaluateDomain);

            #       facConfigurations.add(new FacConfigurationOptions(amplitudeScaling, leftConfig.getRegion(),
            #           leftConfig.getMode(), leftConfig.getTrigParity(), leftConfig.getTheta0(),
            #           leftConfig.getDeltaTheta(), leftConfig.isSmoothed(), leftConfig.isShielded()));
            #     }

            #     return new Ts07FacVariableCoefficients(region1KappaScaling, region2KappaScaling,
            #         facConfigurations.build());

            #     // double region1Mode1Asym = interpolate(leftRange.getRegion1Mode1Asym(),
            #     // rightRange.getRegion1Mode1Asym(), leftDomain, rightDomain, evaluateDomain);
            #     // double region1Mode2Asym = interpolate(leftRange.getRegion1Mode2Asym(),
            #     // rightRange.getRegion1Mode2Asym(), leftDomain, rightDomain, evaluateDomain);
            #     // double region2Mode1Asym = interpolate(leftRange.getRegion2Mode1Asym(),
            #     // rightRange.getRegion2Mode1Asym(), leftDomain, rightDomain, evaluateDomain);
            #     // double region2Mode1Sym = interpolate(leftRange.getRegion2Mode1Sym(),
            #     // rightRange.getRegion2Mode1Sym(), leftDomain, rightDomain, evaluateDomain);
            #     //
            #     // return new Ts07FacVariableCoefficients(region1KappaScaling, region2KappaScaling,
            #     // region1Mode1Asym, region1Mode2Asym, region2Mode1Asym, region2Mode1Sym);

            #   }
        else:
            raise Exception


    @staticmethod
    def getFileName(epoch):
        """Constructs a String representing the parameter file name in the
        format YEAR_DOY_HH_MM.par.

        This is the standard file name used for the TS07 parameter files.

        @param epoch the supplied epoch to construct the file name string
        @return a {@link String} of the file name in the format
        YEAR_DOY_HH_MM.par
        """
        return (
            "%04d_%03d_%02d_%02d.par" %
            (epoch.getYear(), epoch.getDoy(), epoch.getHour(), epoch.getMin(),
             epoch.getSec())
        )

    @staticmethod
    def getEpoch(fileName):
        """Parses the UTCEpoch from the standard TS07 parameter file name.

        @param fileName the standard TS07 parameter file name
        @return the {@link UTCEpoch} corresponding to the supplied file name
        """
        year = int(fileName[0:4])
        doy = int(fileName[5:8])
        hour = int(fileName[9:11])
        min = int(fileName[12:14])
        epoch = UTCEpoch(year, doy, hour, min, 0.0)
        return epoch

    @staticmethod
    def firstEpoch(variableCoeffsDir):
        """Finds the first UTCEpoch associated with the variable coefficients
        files in the supplied directory.

        @param variableCoeffsDir the directory that contains the variable
        coefficients files, the file name must be in the format
        YEAR_DOY_HH_MM.par.
        @return the first UTCEpoch of the file in the supplied directory
        """

        # recursively loop through the directory tree
        coeffsFiles = []
        p = ".*[0-9]{4}_[0-9]{3}_[0-9]{2}_[0-9]{2}\.par"
        for (r, d, files) in os.walk(variableCoeffsDir):
            for f in files:
                if re.match(p, f):
                    coeffsFiles.append(f)
        coeffsFiles.sort()
        firstEpoch = TS07DVariableCoefficientsUtils.getEpoch(
            coeffsFiles[0]
        )
        return firstEpoch

    @staticmethod
    def lastEpoch(variableCoeffsDir):
        """Finds the last UTCEpoch associated with the variable coefficients
        files in the supplied directory.

        @param variableCoeffsDir the directory that contains the variable
        coefficients files, the file name must be in the format
        YEAR_DOY_HH_MM.par.
        @return the last {@link UTCEpoch} of the file in the supplied directory
        """

        # recursively loop through the directory tree
        coeffsFiles = []
        p = ".*[0-9]{4}_[0-9]{3}_[0-9]{2}_[0-9]{2}\.par"
        for (r, d, files) in os.walk(variableCoeffsDir):
            for f in files:
                if re.match(p, f):
                    coeffsFiles.append(f)
        coeffsFiles.sort()
        lastEpoch = TS07DVariableCoefficientsUtils.getEpoch(
            coeffsFiles[-1]
        )
        return lastEpoch
