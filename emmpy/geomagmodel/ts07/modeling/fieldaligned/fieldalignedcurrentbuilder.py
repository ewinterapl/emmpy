"""emmpy.geomagmodel.ts07.modeling.fieldaligned.fieldalignedcurrentbuilder"""


# import static com.google.common.base.Preconditions.checkNotNull;
# import static crucible.core.math.CrucibleMath.pow;
# import static crucible.core.math.vectorfields.VectorFields.scale;
# import static crucible.core.math.vectorfields.VectorFields.scaleLocation;
# import crucible.core.designpatterns.Builder;
# import crucible.core.math.vectorfields.VectorField;
# import magmodel.core.math.TrigParity;
# import magmodel.core.math.deformation.SphericalFieldDeformation;
# import magmodel.core.math.vectorfields.SphericalVectorField;
# import magmodel.core.modeling.fac.ConicalCurrentMagneticField;
# import magmodel.core.modeling.fac.TwoConicalFields;

from emmpy.crucible.core.designpatterns.builder import Builder


# Below are the TS07 values, if you don't overrride these, this is what will
# be used
D_THETA = [0.06, 0.09]
D_PHI = [0.055, 0.030]
BM = [[0.1618068350, 0.7058026940], [0.1278764024, 0.4036015198]]
THETA0 = [[0.7113544659, 0.5567714182], [0.8867880020, 0.7247997430]]

# Static coefficients used in the coordinate deformations of r and theta.
# Given in Tsyganenko 2002-1, Table 2, eq. 18 and 19
A = [
    [[-0.1797957553, 2.999642482, -0.9322708978, -0.6811059760,
      0.2099057262, -8.358815746, -14.86033550, 0.3838362986, -16.30945494],
     [-0.2845938535, 5.715471266, -2.472820880, -0.7738802408,
      0.3478293930, -11.37653694, -38.64768867, 0.6932927651, -212.4017288]],
    [[-0.2320034273, 1.805623266, -32.37241440, -0.9931490648, 0.3175085630,
      -2.492465814, -16.21600096, 0.2695393416, -6.752691265],
     [-0.3302974212, 2.827730930, -45.44405830, -1.611103927, 0.4927112073,
      -0.003258457559, -49.59014949, 0.3796217108, -233.7884098]]
]

B = [
    [[4.537022847, 2.685836007, 27.97833029, 6.330871059, 1.876532361,
      18.95619213],
     [4.944204937, 3.071270411, 33.05882281, 7.387533799, 2.366769108,
      79.22572682]],
    [[3.971794901, 14.54477563, 41.10158386, 7.912889730, 1.258297372,
      9.583547721],
     [4.312666980, 18.05051709, 28.95320323, 11.09948019, 0.7471649558,
      67.10246193]]
]

C = [
    [[0.9651528100, 0.4217195118, -0.08957770020, -1.823555887, 0.7457045438,
      -0.5785916524, -1.010200918, 0.01112389357, 0.09572927448,
      -0.3599292276],
     [0.6154290178, 0.5592050551, -0.1796585105, -1.654932210, 0.7309108776,
      -0.4926292779, -1.130266095, -0.009613974555, 0.1484586169,
      -0.2215347198]],
    [[1.014141963, 0.5104134759, -0.1790430468, -1.756358428, 0.7561986717,
      -0.6775248254, -0.04014016420, 0.01446794851, 0.1200521731,
      -0.2203584559],
     [0.5667096597, 0.6468519751, -0.1560665317, -1.460805289, 0.7719653528,
      -0.6658988668, 0.2515179349E-05, 0.02426021891, 0.1195003324,
      -0.2625739255]]
]

D = [
    [[8.713700514, 0.9763932955, 3.834602998, 2.49211838],
     [7.883592948, 0.02768251655, 2.950280953, 1.212634762]],
    [[4.508963850, 0.8221623576, 1.779933730, 1.102649543],
     [4.377172556, 0.2421190547, 2.503482679, 1.071587299]]
]


class FieldAlignedCurrentBuilder(Builder):
    """A builder that builds Field Aligned current modules.

    Note: this only includes the internal field and NOT the shielding field.

    @author G.K.Stephens
    """

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 4:
            (options, dipoleTilt, dynamicPressure, kappa) = args
            region = options.getRegion().getAsInt()
            # needed to construct the conical field, eq. 14 & 15 of T91
            self.mode = options.getMode()
            self.smoothed = options.isSmoothed()
            self.theta0 = options.getTheta0()
            self.deltaTheta = options.getDeltaTheta()
            self.trigParity = options.getTrigParity()
            # needed to deform the conical field, eq. 18 & 19 T02
            self.a = A[region - 1][mode - 1]
            self.b = B[region - 1][mode - 1]
            self.c = C[region - 1][mode - 1]
            self.d = D[region - 1][mode - 1]
            self.bmScaleFactor = BM[region - 1][mode - 1]
            # needed for stretching, eq. 21, 22, 23, 24, &25 T02
            self.dipoleTilt = dipoleTilt
            self.dynamicPressure = dynamicPressure
            self.kappa = kappa
            self.dPhi = D_PHI[region - 1]
            self.scalingCoefficient = options.getAmplitudeScaling()
        elif len(args) == 6:
            (region, mode, trigParity, dipoleTilt, dynamicPressure, kappa,
             scalingCoefficient) = args
            # @param region region 1 or 2
            # @param mode which mode (only 1 and 2 are currently available)
            # @param trigParity sine function is odd cosine is even
            # @param dipoleTilt the dipole tilt angle
            # @param dynamicPressure the dynamic pressure
            # @param kappa the global scaling coefficient
            # @param scalingCoefficient the
            self.mode = mode
            self.smoothed = False
            self.theta0 = THETA0[region - 1][mode - 1]
            self.deltaTheta = D_THETA[region - 1]
            self.trigParity = trigParity
            self.a = A[region - 1][mode - 1]
            self.b = B[region - 1][mode - 1]
            self.c = C[region - 1][mode - 1]
            self.d = D[region - 1][mode - 1]
            self.bmScaleFactor = BM[region - 1][mode - 1]
            self.dipoleTilt = dipoleTilt
            self.dynamicPressure = dynamicPressure
            self.kappa = kappa
            self.dPhi = D_PHI[region - 1]
            self.scalingCoefficient = scalingCoefficient
        else:
            raise Exception

    def withSmoothing(self):
        """Smooth the field aligned current."""
        self.smoothed = True
        return self

    def setSmoothing(self, smoothing):
        self.smoothed = smoothing
        return self

    def withTheta0(self, theta0):
        self.theta0 = theta0
        return self

    def withDeltaTheta(self, deltaTheta):
        self.deltaTheta = deltaTheta
        return self

    def build(self):
        # Note: this is a point of inconsistency with the Fortran code, in the
        # Fortran this calculation is done in single precision. When the field
        # values are very large, this can result in tenths of differences
        # between the Java and the Fortran version of the model
        dynamicPressureScalingFactor = pow(self.dynamicPressure/2, 0.155)

        # construct the conical field, eq. 14 & 15 of T91
        undeformedConicalField = None
        if self.smoothed:
            undeformedConicalField = (
                SmoothedConicalCurrentMagneticField(
                    self.theta0, self.deltaTheta, self.mode, self.trigParity
                )
            )
        else:
            undeformedConicalField = (
                ConicalCurrentMagneticField.create(
                    self.theta0, self.deltaTheta, self.mode, self.trigParity
                )
            )

        # deform the conical field,
        deformation = BirkelandDeformationFunction(a, b, c, d)
        deformedField = self.scale(
            SphericalFieldDeformation(undeformedConicalField,
                                      deformation),
            bmScaleFactor
        )

        # make it two cones
        twoCones = TwoConicalFields(deformedField)

        # scale the FIELD output by the coefficient
        scaledTwoCones = self.scale(twoCones, self.scalingCoefficient)

        stretchedField = ScaledField(
            StretchedField(
                scaledTwoCones, self.dipoleTilt, self.dPhi
            ), self.kappa
        )

        # Scale position vector for solar wind (see Tsy 2002-1 2.4)
        pDynScaledField = self.scaleLocation(
            stretchedField, dynamicPressureScalingFactor
        )

        return pDynScaledField
