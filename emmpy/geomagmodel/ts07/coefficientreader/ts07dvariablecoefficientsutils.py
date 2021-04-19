"""emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils"""


# import static com.google.common.base.Preconditions.checkArgument;
# import static java.lang.Integer.parseInt;
# import static java.lang.String.format;
# import static magmodel.core.math.expansions.CoefficientExpansions.createUnity;

# import java.io.BufferedWriter;
# import java.io.FileNotFoundException;
# import java.io.IOException;
# import java.nio.charset.Charset;
# import java.nio.file.DirectoryStream;
# import java.nio.file.FileVisitResult;
# import java.nio.file.FileVisitor;
# import java.nio.file.Files;
# import java.nio.file.Path;
# import java.nio.file.SimpleFileVisitor;
# import java.nio.file.StandardOpenOption;
# import java.nio.file.attribute.BasicFileAttributes;
# import java.util.Arrays;
# import java.util.Collections;
# import java.util.List;
# import java.util.Scanner;

# import com.google.common.annotations.VisibleForTesting;
# import com.google.common.base.Function;
# import com.google.common.cache.CacheBuilder;
# import com.google.common.cache.CacheLoader;
# import com.google.common.cache.LoadingCache;
# import com.google.common.collect.ImmutableList;
# import com.google.common.collect.Lists;
# import com.google.common.primitives.Doubles;

# import crucible.core.collections.ArrayUtilities;
# import crucible.core.data.list.indexable.GaugedIndexable;
# import crucible.core.data.list.indexable.GaugedIndexables;
# import crucible.core.time.UTCEpoch;
# import geomagmodel.ts07.modeling.fieldaligned.FacConfigurationOptions;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.expansions.CoefficientExpansion1D;
# import magmodel.core.math.expansions.CoefficientExpansion2D;
# import magmodel.core.math.expansions.CoefficientExpansions;
# import magmodel.core.time.UTCNumerator;


class TS07DVariableCoefficientsUtils:
    pass

    # /**
    #  * A utility class for constructing and manipulating {@link TS07DVariableCoefficients}, and allows
    #  * for reading and writing the coefficients to a file.
    #  * 
    #  * @author Nicholas Sharp
    #  * @author G.K.Stephens
    #  * 
    #  */
    # public class TS07DVariableCoefficientsUtils {

    #   /**
    #    * private constructor
    #    */
    #   private TS07DVariableCoefficientsUtils() {};

    #   /**
    #    * Constructs the standard TS07D set of coefficients from the ASCII file. This set of coefficient
    #    * can be used to construct the TS07D model.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return a newly constructed set of {@link TS07DVariableCoefficients} constructed by parsing the
    #    *         ASCII file
    #    */
    #   public static TS07DVariableCoefficients createTS07D(Path variableCoefficientsFile) {
    #     // below is the default TS07 configuration
    #     int azimuthal = 4;
    #     int radial = 5;
    #     int numCurrentSheets = 1;
    #     FacConfiguration ts07Fac = DefaultFacConfigurationOptions.TS07D;
    #     return create(variableCoefficientsFile, numCurrentSheets, azimuthal, radial, ts07Fac);
    #   }

    #   /**
    #    * Constructs the TS07D set of coefficients from the ASCII file WITH a customized resolution. This
    #    * set of coefficient can be used to construct the TS07D model. The model configuration is
    #    * interpreted from the file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return a newly constructed set of {@link TS07DVariableCoefficients} constructed by parsing the
    #    *         ASCII file
    #    */
    #   public static TS07DVariableCoefficients create(Path variableCoefficientsFile) {

    #     int numCurrentSheets = readCurrentSheetNumber(variableCoefficientsFile);
    #     int numAzimuthalExpansions = readAzimuthalExpansionNumber(variableCoefficientsFile);
    #     int numRadialExpansions = readRadialExpansionNumber(variableCoefficientsFile);
    #     FacConfiguration facConfiguration = readFACConfiguration(variableCoefficientsFile);

    #     return create(variableCoefficientsFile, numCurrentSheets, numAzimuthalExpansions,
    #         numRadialExpansions, facConfiguration);
    #   }

    #   /**
    #    * Constructs the TS07D set of coefficients from the ASCII file WITH a customized resolution. This
    #    * set of coefficient can be used to construct the TS07D model.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @param numAzimuthalExpansions referred to as m
    #    * @param numRadialExpansions referred to as n
    #    * @param facConfiguration describes how to build the field aligned current system
    #    * @return a newly constructed set of {@link TS07DVariableCoefficients} constructed by parsing the
    #    *         ASCII file
    #    */
    #   public static TS07DVariableCoefficients create(Path variableCoefficientsFile,
    #       int numAzimuthalExpansions, int numRadialExpansions, FacConfiguration facConfiguration) {
    #     int numCurrentSheets = 1;
    #     return create(variableCoefficientsFile, numCurrentSheets, numAzimuthalExpansions,
    #         numRadialExpansions, facConfiguration);
    #   }

    #   /**
    #    * Constructs the TS07D set of coefficients from the ASCII file WITH a customized resolution and
    #    * with TWO current sheets. This set of coefficient can be used to construct the TS07D model.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @param numAzimuthalExpansions referred to as m
    #    * @param numRadialExpansions referred to as n
    #    * @param facConfiguration describes how to build the field aligned current system
    #    * @return a newly constructed set of {@link TS07DVariableCoefficients} constructed by parsing the
    #    *         ASCII file
    #    */
    #   public static TS07DVariableCoefficients createWithThinCurrentSheet(Path variableCoefficientsFile,
    #       int numAzimuthalExpansions, int numRadialExpansions, FacConfiguration facConfiguration) {
    #     int numCurrentSheets = 2;
    #     return create(variableCoefficientsFile, numCurrentSheets, numAzimuthalExpansions,
    #         numRadialExpansions, facConfiguration);
    #   }


    #   /**
    #    * Constructs the TS07D set of coefficients from the ASCII file WITH a customized resolution and
    #    * with MANY current sheets. This set of coefficient can be used to construct the TS07D model.
    #    * <p>
    #    * This is package private because (at least for now) we want to limit the public API to only
    #    * support 1 or 2 current sheets, not many current sheets.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @param numCurrentSheets the number of current sheets
    #    * @param numAzimuthalExpansions referred to as m
    #    * @param numRadialExpansions referred to as n
    #    * @param facConfiguration describes how to build the field aligned current system
    #    * @return a newly constructed set of {@link TS07DVariableCoefficients} constructed by parsing the
    #    *         ASCII file
    #    */
    #   public static TS07DVariableCoefficients create(Path variableCoefficientsFile,
    #       int numCurrentSheets, int numAzimuthalExpansions, int numRadialExpansions,
    #       FacConfiguration facConfiguration) {

    #     // the number of asymmetric expansions is simply the n*m
    #     int numAsymmetricExpansions = numRadialExpansions * numAzimuthalExpansions;

    #     // half the number of equatorial expansion coefficients, r+2*(r*a), this
    #     // is half the expansions as the dynamic pressure terms double this
    #     // number
    #     int numHalfExpansions = numRadialExpansions + 2 * (numAsymmetricExpansions);

    #     int numExpansions = numHalfExpansions * 2 * numCurrentSheets;

    #     // tot = 1(dipShield)+numExpansions+numSheets+5(hinge,warp,Kappa1,Kappa2,twist)+fac
    #     int totalNumberOfCoefficients =
    #         1 + numExpansions + numCurrentSheets + 5 + facConfiguration.getNumberOfFields();

    #     double[] coeffs = new double[totalNumberOfCoefficients];

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     int line = 0;

    #     while (scanner.hasNextDouble()) {
    #       coeffs[line] = scanner.nextDouble();
    #       scanner.nextLine();
    #       line++;
    #     }

    #     // we want to perform a check to make sure the input file is of the
    #     // correct size
    #     // checkArgument(line == totalNumberOfCoefficients,
    #     //     "Your variable coffs file %s, had %s values, %s was expected", variableCoefficientsFile,
    #     //     line, totalNumberOfCoefficients);

    #     scanner.close();

    #     // NOTE, this is a deviation from the FORTRAN code, the FORTRAN code handles this in the WARPED
    #     // subroutine
    #     double twist = coeffs[coeffs.length - 1] / 10.0;
    #     coeffs[coeffs.length - 1] = twist;

    #     return createFromArray(coeffs, numCurrentSheets, numAzimuthalExpansions, numRadialExpansions,
    #         facConfiguration);
    #   }

    #   /**
    #    * Parses the Q value (the value of the objective function) from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the Q value parsed from the file
    #    */
    #   public static double readQ(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("Q=", 0);

    #     double pdyn = Double.parseDouble(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return pdyn;
    #   }

    #   /**
    #    * Parses the B-rms value from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the B-rms value parsed from the file
    #    */
    #   public static double readBrms(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("B_rms=", 0);

    #     double pdyn = Double.parseDouble(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return pdyn;
    #   }

    #   /**
    #    * Parses the dynamic pressure from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the dynamic pressure parsed from the file
    #    */
    #   public static double readDynamicPressure(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("Pdyn=", 0);

    #     double pdyn = Double.parseDouble(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return pdyn;
    #   }

    #   /**
    #    * Parses the dipole tilt angle from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the dipole tilt angle parsed from the file
    #    */
    #   public static double readDipoleTiltAngle(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("tilt=", 0);

    #     double pdyn = Double.parseDouble(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return pdyn;
    #   }

    #   /**
    #    * Parses the number of current sheets from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the number of current sheets parsed from the file
    #    */
    #   public static int readCurrentSheetNumber(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }

    #     String found = scanner.findWithinHorizon(" # current sheet thickness", 0);

    #     int numCurrSheets = 0;

    #     while (found != null) {
    #       found = scanner.findWithinHorizon(" # current sheet thickness", 0);
    #       numCurrSheets++;
    #     }

    #     scanner.close();

    #     return numCurrSheets;
    #   }


    #   /**
    #    * Parses the azimuthal expansion number from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the azimuthal expansion number parsed from the file
    #    */
    #   public static int readAzimuthalExpansionNumber(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("M=", 0);

    #     int m = parseInt(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return m;
    #   }

    #   /**
    #    * Parses the radial expansion number from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the radial expansion number parsed from the file
    #    */
    #   public static int readRadialExpansionNumber(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #     scanner.findWithinHorizon("N=", 0);

    #     int n = parseInt(scanner.next().replace(',', ' '));

    #     scanner.close();

    #     return n;
    #   }

    #   /**
    #    * Parses the radial expansion number from the variable coefficients file.
    #    * 
    #    * @param variableCoefficientsFile an ASCII file containing a list of the coefficients
    #    * @return the radial expansion number parsed from the file
    #    */
    #   public static DefaultFacConfigurationOptions readFACConfiguration(Path variableCoefficientsFile) {

    #     Scanner scanner;

    #     try {
    #       scanner = new Scanner(variableCoefficientsFile);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }

    #     int count = 0;

    #     while (scanner.findWithinHorizon("# reg-[1|2] M-[1|2]", 0) != null) {
    #       count++;
    #     }

    #     scanner.close();


    #     switch (count) {
    #       case 4:
    #         return DefaultFacConfigurationOptions.TS07D;
    #       case 6:
    #         return DefaultFacConfigurationOptions.FAC6;
    #       case 12:
    #         return DefaultFacConfigurationOptions.FAC12;
    #       case 16:
    #         return DefaultFacConfigurationOptions.FAC16;
    #       default:
    #         throw new RuntimeException("Invalid number of FACs to construct a DefaultFacConfiguration");
    #     }
    #   }


    #   /**
    #    * Constructs a newly constructed {@link Ts07FacVariableCoefficients} from an array of doubles. A
    #    * double array is the data structured used in the Fortran version of the code.
    #    * 
    #    * @param coefficients an array containing the coefficients
    #    * @param numAzimuthalExpansions referred to as m
    #    * @param numRadialExpansions referred to as n
    #    * @param facConfiguration describes how to build the field aligned current system
    #    * @return a newly constructed {@link TS07DVariableCoefficients}
    #    */
    #   public static TS07DVariableCoefficients createFromArray(double[] coeffs, int numCurrentSheets,
    #       int numAzimuthalExpansions, int numRadialExpansions, FacConfiguration facConfiguration) {

    #     // the number of asymmetric expansions is simply the n*m
    #     int numAsymmetricExpansions = numRadialExpansions * numAzimuthalExpansions;

    #     // half the number of equatorial expansion coefficients, r+2*(r*a), this
    #     // is half the expansions as the dynamic pressure terms double this
    #     // number
    #     int numHalfExpansions = numRadialExpansions + 2 * (numAsymmetricExpansions);

    #     int numExpansions = numHalfExpansions * 2 * numCurrentSheets;

    #     // 2*halfExpansions + 11 other coefficients
    #     int totalNumberOfCoefficients =
    #         numExpansions + 1 + numCurrentSheets + 5 + facConfiguration.getNumberOfFields();

    #     // we want to perform a check to make sure the input file is of the
    #     // correct size
    #     // checkArgument(coeffs.length == totalNumberOfCoefficients,
    #     //     "Your variable coffs array had %s values, %s was expected", coeffs.length,
    #     //     totalNumberOfCoefficients);

    #     // Parse file data into proper variables. This too will need to be
    #     // changed if different coefficient formats are use.
    #     double cfAmplitude = coeffs[0];

    #     List<Ts07EquatorialLinearCoefficients> eqLinearCoeffs = Lists.newArrayList();

    #     // loop through the number of current sheets
    #     for (int nCurr = 0; nCurr < numCurrentSheets; nCurr++) {

    #       int index = nCurr * numHalfExpansions * 2;

    #       double[] aSym = new double[numRadialExpansions];
    #       double[] aSymPdynDependent = new double[numRadialExpansions];
    #       double[][] aOdd = new double[numAzimuthalExpansions][numRadialExpansions];
    #       double[][] aOddPdynDependent = new double[numAzimuthalExpansions][numRadialExpansions];

    #       double[][] aEven = new double[numAzimuthalExpansions][numRadialExpansions];
    #       double[][] aEvenPdynDependent = new double[numAzimuthalExpansions][numRadialExpansions];

    #       for (int n = 0; n < numRadialExpansions; n++) {
    #         index++;
    #         aSym[n] = coeffs[index];
    #         aSymPdynDependent[n] = coeffs[index + numHalfExpansions];
    #       }

    #       for (int n = 0; n < numRadialExpansions; n++) {
    #         for (int m = 0; m < numAzimuthalExpansions; m++) {
    #           index++;
    #           aOdd[m][n] = coeffs[index];
    #           aOddPdynDependent[m][n] = coeffs[index + numHalfExpansions];
    #           aEven[m][n] = coeffs[index + numAsymmetricExpansions];
    #           aEvenPdynDependent[m][n] = coeffs[index + numHalfExpansions + numAsymmetricExpansions];
    #         }
    #       }

    #       CoefficientExpansion1D aSymExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aSym, 1);
    #       CoefficientExpansion1D aSymPdynDependentExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aSymPdynDependent, 1);

    #       CoefficientExpansion2D aOddExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aOdd, 1, 1);
    #       CoefficientExpansion2D aOddPdynDependentExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aOddPdynDependent, 1, 1);

    #       CoefficientExpansion2D aEvenExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aEven, 1, 1);
    #       CoefficientExpansion2D aEvenPdynDependentExpansion =
    #           CoefficientExpansions.createExpansionFromArray(aEvenPdynDependent, 1, 1);

    #       Ts07EquatorialLinearCoefficients equatorialLinearCoeffs =
    #           Ts07EquatorialLinearCoefficients.create(aSymExpansion, aSymPdynDependentExpansion,
    #               aOddExpansion, aOddPdynDependentExpansion, aEvenExpansion,
    #               aEvenPdynDependentExpansion, numAzimuthalExpansions, numRadialExpansions);

    #       eqLinearCoeffs.add(equatorialLinearCoeffs);
    #     }

    #     int numFacFields = facConfiguration.getNumberOfFields();

    #     // the field aligned current amplitudes
    #     double[] facAmps = new double[numFacFields];

    #     for (int i = 0; i < numFacFields; i++) {
    #       facAmps[i] = coeffs[numExpansions + 1 + i];
    #     }

    #     List<Double> currThicks = Doubles.asList(Arrays.copyOfRange(coeffs,
    #         numExpansions + numFacFields + 1, numExpansions + numFacFields + 1 + numCurrentSheets));
    #     double hingeDist = coeffs[numExpansions + numFacFields + numCurrentSheets + 1];
    #     double warpParam = coeffs[numExpansions + numFacFields + numCurrentSheets + +2];
    #     double facKappa1 = coeffs[numExpansions + numFacFields + numCurrentSheets + +3];
    #     double facKappa2 = coeffs[numExpansions + numFacFields + numCurrentSheets + 4];
    #     // NOTE, this is a deviation from the FORTRAN code, the FORTRAN code handles this in the WARPED
    #     // subroutine
    #     double twistFact = coeffs[numExpansions + numFacFields + numCurrentSheets + 5];

    #     Ts07EquatorialVariableCoefficients equatorialVariableCoeffs =
    #         new Ts07EquatorialVariableCoefficients(currThicks, hingeDist, warpParam, twistFact,
    #             eqLinearCoeffs);

    #     Ts07FacVariableCoefficients fac = new Ts07FacVariableCoefficients(facKappa1, facKappa2,
    #         facConfiguration.createFromCoeffs(facAmps));

    #     return new TS07DVariableCoefficients(cfAmplitude, equatorialVariableCoeffs, fac);
    #   }

    #   /**
    #    * Given a set of {@link TS07DVariableCoefficients}, writes the files to an ASCII file in the
    #    * standard format.
    #    * 
    #    * @param outputFile
    #    * @param coeffs
    #    * @param qValue
    #    * @param brms
    #    */
    #   public static void writeToFile(Path outputFile, TS07DVariableCoefficients coeffs, double qValue,
    #       double brms) {
    #     String format = "%15.6G\n";
    #     writeToFile(outputFile, format, coeffs, qValue, brms);
    #   }

    #   /**
    #    * 
    #    * @param inputFile
    #    * @param dyanmicPressure
    #    * @param dipoleTilt
    #    */
    #   public static void append(Path inputFile, double dyanmicPressure, double dipoleTilt) {
    #     String format = "%15.6G\n";

    #     BufferedWriter writer;
    #     try {

    #       writer = Files.newBufferedWriter(inputFile, Charset.defaultCharset(),
    #           StandardOpenOption.WRITE, StandardOpenOption.APPEND);

    #       writer.write("  Pdyn=" + format(format, dyanmicPressure));
    #       writer.write("  tilt=" + format(format, dipoleTilt));

    #       writer.flush();
    #       writer.close();
    #     } catch (FileNotFoundException e) {
    #       throw new RuntimeException(e);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #   }

    #   /**
    #    * Given a set of {@link TS07DVariableCoefficients}, writes the files to an ASCII file in the
    #    * annotated format.
    #    * 
    #    * @param outputFile
    #    * @param coeffs
    #    * @param qValue
    #    * @param brms
    #    */
    #   public static void writeToAnnotatedFile(Path outputFile, TS07DVariableCoefficients coeffs,
    #       double qValue, double brms) {
    #     String format = "%15.6G%s\n";
    #     writeToFile(outputFile, format, coeffs, qValue, brms);
    #   }

    #   /**
    #    * Given a set of {@link TS07DVariableCoefficients}, writes the files to an ASCII file in the
    #    * standard format.
    #    * 
    #    * @param outputFile the output file to write
    #    * @param coeffs the set of {@link TS07DVariableCoefficients}
    #    */
    #   public static void writeToFile(Path outputFile, TS07DVariableCoefficients coeffs) {
    #     writeToFile(outputFile, coeffs, -9999.99, -9999.99);
    #   }

    #   /**
    #    * Given a set of {@link TS07DVariableCoefficients}, writes the files to an ASCII file in the
    #    * annotated format.
    #    * 
    #    * @param outputFile the output file to write
    #    * @param coeffs the set of {@link TS07DVariableCoefficients}
    #    */
    #   public static void writeToAnnotatedFile(Path outputFile, TS07DVariableCoefficients coeffs) {
    #     writeToAnnotatedFile(outputFile, coeffs, -9999.99, -9999.99);
    #   }

    #   /**
    #    * Constructs a set of coefficients where all the linear coefficients are set to 1 and the
    #    * non-linear are supplied.
    #    * <p>
    #    * Since the linear coefficients are used in a linear expansion, it is useful to set these all to
    #    * one for linear regression needs.
    #    * 
    #    * @param nonLinearParams
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @param facConfiguration
    #    * @return
    #    */
    #   public static TS07DVariableCoefficients createUnityLinear(Ts07NonLinearParameters nonLinearParams,
    #       int numAzimuthalExpansions, int numRadialExpansions, FacConfiguration facConfiguration) {

    #     // the linear parameters are fit with each evaluation of the model, so it doesn't matter what
    #     // they are set to initially,
    #     CoefficientExpansion1D s = createUnity(1, numRadialExpansions);

    #     CoefficientExpansion2D a = createUnity(1, numAzimuthalExpansions, 1, numRadialExpansions);

    #     int numCurrentSheets = nonLinearParams.getCurrentSheetThicknesses().size();
    #     List<Ts07EquatorialLinearCoefficients> eqLinearCoeffs = Lists.newArrayList();
    #     for (int i = 0; i < numCurrentSheets; i++) {
    #       Ts07EquatorialLinearCoefficients eqLinearCoeff = Ts07EquatorialLinearCoefficients.create(s, s,
    #           a, a, a, a, numAzimuthalExpansions, numRadialExpansions);
    #       eqLinearCoeffs.add(eqLinearCoeff);
    #     }

    #     double[] facCoeffsArray = new double[facConfiguration.getNumberOfFields()];
    #     Arrays.fill(facCoeffsArray, 1.0);

    #     Ts07EquatorialVariableCoefficients equatorialCoeffs = new Ts07EquatorialVariableCoefficients(
    #         nonLinearParams.getCurrentSheetThicknesses(), nonLinearParams.getHingeDist(),
    #         nonLinearParams.getWarpParam(), nonLinearParams.getTwistFact(), eqLinearCoeffs);

    #     Ts07FacVariableCoefficients facCoeffs = new Ts07FacVariableCoefficients(
    #         nonLinearParams.getFacRegion1Kappa(), nonLinearParams.getFacRegion2Kappa(),
    #         facConfiguration.createFromCoeffs(facCoeffsArray));

    #     // all the linear parameters are set to 1
    #     TS07DVariableCoefficients unityCoeffs =
    #         TS07DVariableCoefficientsUtils.create(1.0, equatorialCoeffs, facCoeffs);

    #     return unityCoeffs;
    #   }


    #   /**
    #    * Given a {@link GaugedIndexable} of {@link TS07DVariableCoefficients}, i.e. a discrete number of
    #    * {@link TS07DVariableCoefficients} on a time line, creates a {@link Function} where the
    #    * coefficients have been linearly interpolated.
    #    * 
    #    * @param coefficients a {@link GaugedIndexable} of {@link TS07DVariableCoefficients}.
    #    * @return a {@link Function} of {@link Double}s to {@link TS07DVariableCoefficients}, where the
    #    *         coefficients have been linearly interpolated
    #    */
    #   public static Function<Double, TS07DVariableCoefficients> interpolate(
    #       final GaugedIndexable<TS07DVariableCoefficients> coefficients) {

    #     checkArgument(coefficients.size() > 1,
    #         "The size of the coefficients must be greater than 1 to interpolate, it was %s",
    #         coefficients.size());

    #     return new Function<Double, TS07DVariableCoefficients>() {

    #       @Override
    #       public TS07DVariableCoefficients apply(Double time) {

    #         int index = coefficients.indexLastLessThanOrEqualTo(time);

    #         // if we are on the last index, it is still valid to interpolate, but we must now grab the
    #         // second to last guy
    #         if (index == coefficients.size() - 1) {
    #           index--;
    #         }

    #         TS07DVariableCoefficients tv1 = coefficients.get(index);
    #         TS07DVariableCoefficients tv2 = coefficients.get(index + 1);

    #         return interpolate(tv1, tv2, coefficients.getGauge(index), coefficients.getGauge(index + 1),
    #             time);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a new set of {@link TS07DVariableCoefficients} by interpolating between the two sets of
    #    * input coefficients. Each individual coefficient is linearly interpolated.
    #    * 
    #    * @param coefficients1 the first set of coefficients
    #    * @param coefficients2 the second set of coefficients
    #    * @param time1 the time associated with the first set of coefficients
    #    * @param time2 the time associated with the second set of coefficients
    #    * @param evaluateTime the time to evaluate the interpolation
    #    * @return a newly constructed {@link TS07DVariableCoefficients} that is the linear interpolation
    #    *         of each individual coefficient.
    #    */
    #   public static TS07DVariableCoefficients interpolate(final TS07DVariableCoefficients coefficients1,
    #       final TS07DVariableCoefficients coefficients2, double time1, double time2,
    #       double evaluateTime) {

    #     checkArgument(evaluateTime >= time1,
    #         "the evaluation time (%s) must be greater than or equal to the first time (%s)",
    #         evaluateTime, time1);
    #     checkArgument(evaluateTime <= time2,
    #         "the evaluation time (%s) must be less than or equal to the first time (%s)", evaluateTime,
    #         time2);

    #     double cfAmplitude = interpolate(coefficients1.getDipoleShieldingAmplitude(),
    #         coefficients2.getDipoleShieldingAmplitude(), time1, time2, evaluateTime);

    #     Ts07EquatorialVariableCoefficients eq = interpolate(coefficients1.getEquatorialCoefficients(),
    #         coefficients2.getEquatorialCoefficients(), time1, time2, evaluateTime);

    #     Ts07FacVariableCoefficients fac = interpolate(coefficients1.getFacCoefficients(),
    #         coefficients2.getFacCoefficients(), time1, time2, evaluateTime);

    #     return new TS07DVariableCoefficients(cfAmplitude, eq, fac);
    #   }

    #   /**
    #    * 
    #    * @param coefficients1
    #    * @param coefficients2
    #    * @param time1
    #    * @param time2
    #    * @param evaluateTime
    #    * @return
    #    */
    #   public static Ts07NonLinearParameters interpolate(final Ts07NonLinearParameters coefficients1,
    #       final Ts07NonLinearParameters coefficients2, double time1, double time2,
    #       double evaluateTime) {

    #     checkArgument(coefficients1.getCurrentSheetThicknesses().size() == coefficients2
    #         .getCurrentSheetThicknesses().size(), "must be same size");

    #     double facRegion1Kappa = interpolate(coefficients1.getFacRegion1Kappa(),
    #         coefficients2.getFacRegion1Kappa(), time1, time2, evaluateTime);
    #     double facRegion2Kappa = interpolate(coefficients1.getFacRegion2Kappa(),
    #         coefficients2.getFacRegion2Kappa(), time1, time2, evaluateTime);

    #     List<Double> currThicks = Lists.newArrayList();

    #     for (int i = 0; i < coefficients1.getCurrentSheetThicknesses().size(); i++) {
    #       double currThick = interpolate(coefficients1.getCurrentSheetThicknesses().get(i),
    #           coefficients2.getCurrentSheetThicknesses().get(i), time1, time2, evaluateTime);
    #       currThicks.add(currThick);
    #     }

    #     double hingeDist = interpolate(coefficients1.getHingeDist(), coefficients2.getHingeDist(),
    #         time1, time2, evaluateTime);
    #     double warpParam = interpolate(coefficients1.getWarpParam(), coefficients2.getWarpParam(),
    #         time1, time2, evaluateTime);
    #     double twistFact = interpolate(coefficients1.getTwistFact(), coefficients2.getTwistFact(),
    #         time1, time2, evaluateTime);

    #     return new Ts07NonLinearParameters(facRegion1Kappa, facRegion2Kappa, currThicks, hingeDist,
    #         warpParam, twistFact);
    #   }

    #   /**
    #    * Constructs a {@link String} representing the parameter file name in the format
    #    * YEAR_DOY_HH_MM.par. This is the standard file name used for the TS07 parameter files.
    #    * 
    #    * @param epoch the supplied epoch to construct the file name string
    #    * @return a {@link String} of the file name in the format YEAR_DOY_HH_MM.par
    #    */
    #   public static String getFileName(UTCEpoch epoch) {
    #     return format("%04d_%03d_%02d_%02d.par", epoch.getYear(), epoch.getDoy(), epoch.getHour(),
    #         epoch.getMin(), epoch.getSec());
    #   }

    #   /**
    #    * Parses the {@link UTCEpoch} from the standard TS07 parameter file name.
    #    * 
    #    * @param fileName the standard TS07 parameter file name
    #    * @return the {@link UTCEpoch} corresponding to the supplied file name
    #    */
    #   public static UTCEpoch getEpoch(String fileName) {
    #     int year = parseInt(fileName.substring(0, 4));

    #     int doy = parseInt(fileName.substring(5, 8));

    #     int hour = parseInt(fileName.substring(9, 11));
    #     int min = parseInt(fileName.substring(12, 14));

    #     UTCEpoch epoch = new UTCEpoch(year, doy, hour, min, 0.0);

    #     return epoch;
    #   }

    #   /**
    #    * 
    #    * @param outputFile
    #    * @param format
    #    * @param coeffs
    #    * @param qValue
    #    * @param brms
    #    */
    #   private static void writeToFile(Path outputFile, String format, TS07DVariableCoefficients coeffs,
    #       double qValue, double brms) {

    #     BufferedWriter writer;
    #     try {
    #       writer =
    #           Files.newBufferedWriter(outputFile, Charset.defaultCharset(), StandardOpenOption.WRITE,
    #               StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
    #       // writer = Files.newWriter(outputFile.toFile(), Charsets.UTF_8);

    #       writer.write(
    #           format(format, coeffs.getDipoleShieldingAmplitude(), "  # dipole shielding field amp."));

    #       for (Ts07EquatorialLinearCoefficients eqLinearCoeffs : coeffs.getEquatorialCoefficients()
    #           .getLinearCoeffs()) {

    #         CoefficientExpansion1D aSym = eqLinearCoeffs.getCoeffs().getTailSheetSymmetricValues();
    #         CoefficientExpansion1D aSymPdynDep =
    #             eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetSymmetricValues();

    #         CoefficientExpansion2D aOdd = eqLinearCoeffs.getCoeffs().getTailSheetOddValues();
    #         CoefficientExpansion2D aOddPdynDep =
    #             eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetOddValues();

    #         CoefficientExpansion2D aEven = eqLinearCoeffs.getCoeffs().getTailSheetEvenValues();
    #         CoefficientExpansion2D aEvenPdynDep =
    #             eqLinearCoeffs.getPdynDependentCoeffs().getTailSheetEvenValues();


    #         // Start with the dynamic pressure independent expansion
    #         for (int n = aSym.getLowerBoundIndex(); n <= aSym.getUpperBoundIndex(); n++) {
    #           String descriptor = format("  # n-%s eq. amp.", n);
    #           writer.write(format(format, aSym.getCoefficient(n), descriptor));
    #         }

    #         for (int n = aOdd.getJLowerBoundIndex(); n <= aOdd.getJUpperBoundIndex(); n++) {
    #           for (int m = aOdd.getILowerBoundIndex(); m <= aOdd.getIUpperBoundIndex(); m++) {
    #             String descriptor = format("  # m-%s n-%s odd eq. amp.", m, n);
    #             writer.write(format(format, aOdd.getCoefficient(m, n), descriptor));
    #           }
    #         }

    #         for (int n = aEven.getJLowerBoundIndex(); n <= aEven.getJUpperBoundIndex(); n++) {
    #           for (int m = aEven.getILowerBoundIndex(); m <= aEven.getIUpperBoundIndex(); m++) {
    #             String descriptor = format("  # m-%s n-%s even eq. amp.", m, n);
    #             writer.write(format(format, aEven.getCoefficient(m, n), descriptor));
    #           }
    #         }

    #         // now do the dynamic pressure dependent expansion
    #         for (int n = aSymPdynDep.getLowerBoundIndex(); n <= aSymPdynDep.getUpperBoundIndex(); n++) {
    #           String descriptor = format("  # n-%s * sqrt(pdyn) eq. amp.", n);
    #           writer.write(format(format, aSymPdynDep.getCoefficient(n), descriptor));
    #         }

    #         for (int n = aOddPdynDep.getJLowerBoundIndex(); n <= aOddPdynDep
    #             .getJUpperBoundIndex(); n++) {
    #           for (int m = aOddPdynDep.getILowerBoundIndex(); m <= aOddPdynDep
    #               .getIUpperBoundIndex(); m++) {
    #             String descriptor = format("  # m-%s n-%s odd * sqrt(pdyn) eq. amp.", m, n);
    #             writer.write(format(format, aOddPdynDep.getCoefficient(m, n), descriptor));
    #           }
    #         }

    #         for (int n = aEvenPdynDep.getJLowerBoundIndex(); n <= aEvenPdynDep
    #             .getJUpperBoundIndex(); n++) {
    #           for (int m = aEvenPdynDep.getILowerBoundIndex(); m <= aEvenPdynDep
    #               .getIUpperBoundIndex(); m++) {
    #             String descriptor = format("  # m-%s n-%s even * sqrt(pdyn) eq. amp.", m, n);
    #             writer.write(format(format, aEvenPdynDep.getCoefficient(m, n), descriptor));
    #           }
    #         }
    #       }

    #       for (FacConfigurationOptions facConfiguration : coeffs.getFacCoefficients()
    #           .getFacConfigurations()) {
    #         String s = facConfiguration.getTrigParity().equals(TrigParity.EVEN) ? "sym" : "asym";
    #         writer.write(format(format, facConfiguration.getAmplitudeScaling(),
    #             "  # reg-" + facConfiguration.getRegion().getAsInt() + " M-"
    #                 + facConfiguration.getMode() + " " + s + ". amp."));
    #       }
    #       // writer.write(format(format, coeffs.getFacCoefficients().getRegion1Mode1Asym(),
    #       // " # reg-1 M-1 asym. amp."));
    #       // writer.write(format(format, coeffs.getFacCoefficients().getRegion1Mode2Asym(),
    #       // " # reg-1 M-2 asym. amp."));
    #       // writer.write(format(format, coeffs.getFacCoefficients().getRegion2Mode1Asym(),
    #       // " # reg-2 M-1 asym. amp."));
    #       // writer.write(format(format, coeffs.getFacCoefficients().getRegion2Mode1Sym(),
    #       // " # reg-2 M-1 sym. amp."));
    #       for (double currentSheetThickness : coeffs.getEquatorialCoefficients().getCurrThicks()) {
    #         writer.write(format(format, currentSheetThickness, "  # current sheet thickness"));
    #       }
    #       writer.write(format(format, coeffs.getEquatorialCoefficients().getHingeDistance(),
    #           "  # hinge distance"));
    #       writer.write(format(format, coeffs.getEquatorialCoefficients().getWarpingParam(),
    #           "  # warping parameter"));
    #       writer.write(format(format, coeffs.getFacCoefficients().getRegion1KappaScaling(),
    #           "  # reg-1 scaling"));
    #       writer.write(format(format, coeffs.getFacCoefficients().getRegion2KappaScaling(),
    #           "  # reg-2 scaling"));
    #       writer.write(format(format, coeffs.getEquatorialCoefficients().getTwistParam() * 10.0,
    #           "  # twist factor * 10"));

    #       writer.write("     Q=" + format(format, qValue, ""));
    #       writer.write(" B_rms=" + format(format, brms, ""));
    #       writer.write("     M=" + format("%15d\n",
    #           coeffs.getEquatorialCoefficients().getLinearCoeffs().get(0).getNumAzimuthalExpansions()));
    #       writer.write("     N=" + format("%15d\n",
    #           coeffs.getEquatorialCoefficients().getLinearCoeffs().get(0).getNumRadialExpansions()));
    #       writer.flush();
    #       writer.close();
    #     } catch (FileNotFoundException e) {
    #       throw new RuntimeException(e);
    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }
    #   }

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

    #   /**
    #    * Constructs a {@link Function} of {@link TS07DVariableCoefficients} as a function of time from a
    #    * directory (or directory tree) of {@link TS07DVariableCoefficients} files. The file names must
    #    * match YEAR_DOY_HH_MM.par, and the time axis is determined by the file name and the input
    #    * {@link UTCNumerator}. The coefficients are linearly interpolated.
    #    * <p>
    #    * TODO the current implementation will not step into sym links.
    #    * 
    #    * @param utcNumerator
    #    * @param variableCoeffsDir the directory that contains the variable coefficients files, the file
    #    *        name must be in the format YEAR_DOY_HH_MM.par.
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @param facConfiguration
    #    * 
    #    * @return a newly constructed {@link Function} that takes a {@link Double} representing the time
    #    *         (matching the time system from the input from the {@link UTCNumerator}) and returns a
    #    *         {@link TS07DVariableCoefficients}, that is interpolated
    #    */
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

    #   /**
    #    * 
    #    * @param utcNumerator
    #    * @param coeffsFiles
    #    * @param numAzimuthalExpansions
    #    * @param numRadialExpansions
    #    * @param facConfiguration
    #    * @param maxCacheSize
    #    * @return
    #    */
    #   public static Function<Double, TS07DVariableCoefficients> create(final UTCNumerator utcNumerator,
    #       final List<Path> coeffsFiles, final int numCurrentSheets, final int numAzimuthalExpansions,
    #       final int numRadialExpansions, final FacConfiguration facConfiguration, long maxCacheSize) {

    #     // sort them in case they aren't ordered
    #     Collections.sort(coeffsFiles);

    #     /*
    #      * Reading the files takes some time, so let's use a cache
    #      */

    #     // cache loader
    #     CacheLoader<Integer, TS07DVariableCoefficients> cacheLoader =
    #         new TS07DVariableCoefficientsCacheLoader(coeffsFiles, numCurrentSheets,
    #             numAzimuthalExpansions, numRadialExpansions, facConfiguration);

    #     // make the cache
    #     final LoadingCache<Integer, TS07DVariableCoefficients> loadingCache =
    #         CacheBuilder.newBuilder().maximumSize(maxCacheSize).build(cacheLoader);

    #     // turn it into a GaugedIndexable
    #     GaugedIndexable<TS07DVariableCoefficients> gi =
    #         new TS07DVariableCoefficientsGaugedIndexable(coeffsFiles, utcNumerator, loadingCache);

    #     // add the searching
    #     GaugedIndexable<TS07DVariableCoefficients> coefficients = GaugedIndexables.binarySearch(gi);

    #     // finally, interpolate the function
    #     return TS07DVariableCoefficientsUtils.interpolate(coefficients);
    #   }

    #   /**
    #    * Finds the first {@link UTCEpoch} associated with the variable coefficients files in the
    #    * supplied directory.
    #    * 
    #    * @param variableCoeffsDir the directory that contains the variable coefficients files, the file
    #    *        name must be in the format YEAR_DOY_HH_MM.par.
    #    * @return the first {@link UTCEpoch} of the file in the supplied directory
    #    */
    #   public static UTCEpoch firstEpoch(final Path variableCoeffsDir) {

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

    #       // sort them in case they aren't ordered
    #       Collections.sort(coeffsFiles);

    #       UTCEpoch firstEpoch = getEpoch(coeffsFiles.get(0).getFileName().toString());

    #       return firstEpoch;

    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }

    #   }

    #   /**
    #    * Finds the last {@link UTCEpoch} associated with the variable coefficients files in the supplied
    #    * directory.
    #    * 
    #    * @param variableCoeffsDir the directory that contains the variable coefficients files, the file
    #    *        name must be in the format YEAR_DOY_HH_MM.par.
    #    * @return the last {@link UTCEpoch} of the file in the supplied directory
    #    */
    #   public static UTCEpoch lastEpoch(final Path variableCoeffsDir) {

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

    #       // sort them in case they aren't ordered
    #       Collections.sort(coeffsFiles);

    #       UTCEpoch lastEpoch =
    #           getEpoch(coeffsFiles.get(coeffsFiles.size() - 1).getFileName().toString());

    #       return lastEpoch;

    #     } catch (IOException e) {
    #       throw new RuntimeException(e);
    #     }

    #   }

    #   /**
    #    * A filter that matches the naming convention of the parameter file, which looks like
    #    * 2012_123_08_54.par
    #    */
    #   private final static DirectoryStream.Filter<Path> FILE_NAME_FILTER =
    #       new DirectoryStream.Filter<Path>() {

    #         @Override
    #         public boolean accept(Path entry) throws IOException {
    #           return entry.getFileName().toString()
    #               .matches(".*[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9].par");
    #         }
    #       };

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
