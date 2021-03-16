"""emmpy.geomagmodel.ts07.coefficientreader.ts07equatorialvariablecoefficients
"""

# package geomagmodel.ts07.coefficientreader;

# import static com.google.common.base.Preconditions.checkArgument;
# import static com.google.common.base.Preconditions.checkNotNull;

# import java.util.List;

# import com.google.common.collect.Lists;

class Ts07EquatorialVariableCoefficients:
    pass

    # /**
    #  * 
    #  * @author G.K.Stephens
    #  *
    #  */
    # public class Ts07EquatorialVariableCoefficients {

    #   private final List<Double> currThicks;
    #   private final double hingeDist;
    #   private final double warpingParam;
    #   private final double twistParam;
    #   private final List<Ts07EquatorialLinearCoefficients> equatorialLinearCoeffs;

    #   /**
    #    * 
    #    * @param currThick
    #    * @param hingeDist
    #    * @param warpingParam
    #    * @param twistParam
    #    * @param equatorialLinearCoeffs
    #    */
    #   public Ts07EquatorialVariableCoefficients(double currThick, double hingeDist, double warpingParam,
    #       double twistParam, Ts07EquatorialLinearCoefficients equatorialLinearCoeffs) {
    #     super();
    #     this.currThicks = Lists.newArrayList(checkNotNull(currThick));
    #     this.hingeDist = hingeDist;
    #     this.warpingParam = warpingParam;
    #     this.twistParam = twistParam;
    #     this.equatorialLinearCoeffs = Lists.newArrayList(checkNotNull(equatorialLinearCoeffs));
    #   }

    #   /**
    #    * 
    #    * @param currThicks
    #    * @param hingeDist
    #    * @param warpingParam
    #    * @param twistParam
    #    * @param equatorialLinearCoeffs
    #    */
    #   public Ts07EquatorialVariableCoefficients(List<Double> currThicks, double hingeDist,
    #       double warpingParam, double twistParam,
    #       List<Ts07EquatorialLinearCoefficients> equatorialLinearCoeffs) {
    #     super();

    #     // the current sheet thickness and the number of sets of linear coeffs must be the same size
    #     checkArgument(currThicks.size() == equatorialLinearCoeffs.size(),
    #         "The number of current sheet thickness must be the same number of current sheet linear expansions");

    #     this.currThicks = checkNotNull(currThicks);
    #     this.hingeDist = hingeDist;
    #     this.warpingParam = warpingParam;
    #     this.twistParam = twistParam;
    #     this.equatorialLinearCoeffs = checkNotNull(equatorialLinearCoeffs);
    #   }

    #   public List<Double> getCurrThicks() {
    #     return currThicks;
    #   }

    #   public double getHingeDistance() {
    #     return hingeDist;
    #   }

    #   public double getWarpingParam() {
    #     return warpingParam;
    #   }

    #   public double getTwistParam() {
    #     return twistParam;
    #   }

    #   public List<Ts07EquatorialLinearCoefficients> getLinearCoeffs() {
    #     return equatorialLinearCoeffs;
    #   }

    #   public int getTotalNumberOfParameters() {
    #     return getTotalNumberOfLinearParameters() + getTotalNumberOfNonLinearParameters();
    #   }

    #   public int getTotalNumberOfLinearParameters() {

    #     int numLinear = 0;

    #     // loop through all the linear parameters and add them up
    #     for (Ts07EquatorialLinearCoefficients lin : equatorialLinearCoeffs) {
    #       int m = lin.getNumAzimuthalExpansions();
    #       int n = lin.getNumRadialExpansions();
    #       numLinear += 2 * (n + 2 * (n * m));
    #     }

    #     return numLinear;
    #   }

    #   public int getTotalNumberOfNonLinearParameters() {
    #     // currThicks, hingeDist, warpingParam,TwistParam
    #     return currThicks.size() + 3;
    #   }



    #   @Override
    #   public String toString() {
    #     return "Ts07EquatorialVariableCoefficients [currThicks=" + currThicks + ", hingeDist="
    #         + hingeDist + ", warpingParam=" + warpingParam + ", twistParam=" + twistParam
    #         + ", equatorialLinearCoeffs=" + equatorialLinearCoeffs + "]";
    #   }

    #   @Override
    #   public int hashCode() {
    #     final int prime = 31;
    #     int result = 1;
    #     result = prime * result + ((currThicks == null) ? 0 : currThicks.hashCode());
    #     result =
    #         prime * result + ((equatorialLinearCoeffs == null) ? 0 : equatorialLinearCoeffs.hashCode());
    #     long temp;
    #     temp = Double.doubleToLongBits(hingeDist);
    #     result = prime * result + (int) (temp ^ (temp >>> 32));
    #     temp = Double.doubleToLongBits(twistParam);
    #     result = prime * result + (int) (temp ^ (temp >>> 32));
    #     temp = Double.doubleToLongBits(warpingParam);
    #     result = prime * result + (int) (temp ^ (temp >>> 32));
    #     return result;
    #   }

    #   @Override
    #   public boolean equals(Object obj) {
    #     if (this == obj) {
    #       return true;
    #     }
    #     if (obj == null) {
    #       return false;
    #     }
    #     if (getClass() != obj.getClass()) {
    #       return false;
    #     }
    #     Ts07EquatorialVariableCoefficients other = (Ts07EquatorialVariableCoefficients) obj;
    #     if (currThicks == null) {
    #       if (other.currThicks != null) {
    #         return false;
    #       }
    #     } else if (!currThicks.equals(other.currThicks)) {
    #       return false;
    #     }
    #     if (equatorialLinearCoeffs == null) {
    #       if (other.equatorialLinearCoeffs != null) {
    #         return false;
    #       }
    #     } else if (!equatorialLinearCoeffs.equals(other.equatorialLinearCoeffs)) {
    #       return false;
    #     }
    #     if (Double.doubleToLongBits(hingeDist) != Double.doubleToLongBits(other.hingeDist)) {
    #       return false;
    #     }
    #     if (Double.doubleToLongBits(twistParam) != Double.doubleToLongBits(other.twistParam)) {
    #       return false;
    #     }
    #     if (Double.doubleToLongBits(warpingParam) != Double.doubleToLongBits(other.warpingParam)) {
    #       return false;
    #     }
    #     return true;
    #   }


    # }
