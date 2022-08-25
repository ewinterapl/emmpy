"""Build a field-aligned current shielding field.

Build a field-aligned current shielding field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import emmpy.math.vectorfields.vectorfields as vectorfields
from emmpy.magmodel.math.perpendicularandparallelcartesianharmonicfield import (
    PerpendicularAndParallelCartesianHarmonicField
)
from emmpy.magmodel.math.trigparity import ODD
from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D
from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)
from emmpy.math.vectorfields.vectorfield import scaleLocation
from emmpy.utilities.nones import nones


class FieldAlignedCurrentShiedingBuilder:
    """Build a field-aligned current shielding field.

    Build a field-aligned current shielding field.

    Attributes
    ----------
    region : int
        FAC region code.
    mode : int
        Trigonometric mode.
    trigParityI : TrigParity
        Even for cosine, odd for sine.
    dipoleTilt : float
        Dipole tilt angle.
    dynamicPressure : float
        Dynamic pressure.
    kappa : float
        Kappa scaling factor.
    scalingCoefficient : float
        Scaling coefficient.
    """

    # Below are the TS07 values.
    kappaScaleAdj = [1.1, 1.0]
    T1ASym = [[0.2256245602, 0.1379899178], [0.1930034238, 0.1486276863]]
    T2ASym = [[-0.05841594319, 0.06607020029], [-0.02261109942, 0.06859991529]]
    pASym = [
        [[59.41537992, 41.18892281, 80.86101200],
         [145.0262164, 70.73187036, 85.51110098]],
        [[58.54144539, 67.45226850, 97.92374406],
         [159.3532209, 76.34445954, 84.74398828]]
    ]
    qASym = [
        [[10.36861082, 8.222335945, 19.97575641],
         [4.655207476, 5.747889264, 7.802304187]],
        [[12.05124381, 9.962933904, 15.91258637],
         [5.145153451, 6.310949163, 6.996159733]]
    ]
    rASym = [
        [[3.066809418, 7.893523804, 30.56212082],
         [21.47490989, 24.34554406, 31.34405345]],
        [[4.752449760, 10.46824379, 32.91856110],
         [12.76722651, 27.63870691, 32.69873634]]
    ]
    sASym = [
        [[2.050148531, 4.992657093, 2.300564232],
         [1.844169801, 4.867254550, 2.941393119]],
        [[1.804233877, 6.578149088, 2.515223491],
         [1.971629939, 4.436299219, 2.904964304]]
    ]

    # NOTE: all the below static shielding coeffs are floats to be consistent
    # with the original Fortran code. These values are cast to doubles, so if
    # you print them out there will be extra bits. This gives several more
    # digits of consistency with the Fortran code. The correct thing to do is
    # refit these guys using all double code.
    shieldingAmpASym = [
        [[46488.84663, -15541.95244, -23210.09824, -32625.03856, -109894.4551, -71415.32808,
          58168.94612, 55564.87578, -22890.60626, -6056.763968, 5091.368100, 239.7001538,
          -13899.49253, 4648.016991, 6971.310672, 9699.351891, 32633.34599, 21028.48811,
          -17395.96190, -16461.11037, 7447.621471, 2528.844345, -1934.094784, -588.3108359,
          -32588.88216, 10894.11453, 16238.25044, 22925.60557, 77251.11274, 50375.97787,
          -40763.78048, -39088.60660, 15546.53559, 3559.617561, -3187.730438, 309.1487975,
          88.22153914, -243.0721938, -63.63543051, 191.1109142, 69.94451996, -187.9539415,
          -49.89923833, 104.0902848, -120.2459738, 253.5572433, 89.25456949, -205.6516252,
          -44.93654156, 124.7026309, 32.53005523, -98.85321751, -36.51904756, 98.88241690,
          24.88493459, -55.04058524, 61.14493565, -128.4224895, -45.35023460, 105.0548704,
          -43.66748755, 119.3284161, 31.38442798, -92.87946767, -33.52716686, 89.98992001,
          25.87341323, -48.86305045, 59.69362881, -126.5353789, -44.39474251, 101.5196856],
         [210260.4816, -1443587.401, -1468919.281, 281939.2993, -1131124.839, 729331.7943,
          2573541.307, 304616.7457, 468887.5847, 181554.7517, -1300722.650, -257012.8601,
          645888.8041, -2048126.412, -2529093.041, 571093.7972, -2115508.353, 1122035.951,
          4489168.802, 75234.22743, 823905.6909, 147926.6121, -2276322.876, -155528.5992,
          -858076.2979, 3474422.388, 3986279.931, -834613.9747, 3250625.781, -1818680.377,
          -7040468.986, -414359.6073, -1295117.666, -346320.6487, 3565527.409, 430091.9496,
          -0.1565573462, 7.377619826, .4115646037, -6.146078880, 3.808028815, -.5232034932,
          1.454841807, -12.32274869, -4.466974237, -2.941184626, -.6172620658, 12.64613490,
          1.494922012, -21.35489898, -1.652256960, 16.81799898, -1.404079922, -24.09369677,
          -10.99900839, 45.94237820, 2.248579894, 31.91234041, 7.575026816, -45.80833339,
          -1.507664976, 14.60016998, 1.348516288, -11.05980247, -5.402866968, 31.69094514,
          12.28261196, -37.55354174, 4.155626879, -33.70159657, -8.437907434, 36.22672602]],
        [[162294.6224, 503885.1125, -27057.67122, -531450.1339, 84747.05678, -237142.1712,
          84133.61490, 259530.0402, 69196.05160, -189093.5264, -19278.55134, 195724.5034,
          -263082.6367, -818899.6923, 43061.10073, 863506.6932, -139707.9428, 389984.8850,
          -135167.5555, -426286.9206, -109504.0387, 295258.3531, 30415.07087, -305502.9405,
          100785.3400, 315010.9567, -15999.50673, -332052.2548, 54964.34639, -152808.3750,
          51024.67566, 166720.0603, 40389.67945, -106257.7272, -11126.14442, 109876.2047,
          2.978695024, 558.6019011, 2.685592939, -338.0004730, -81.99724090, -444.1102659,
          89.44617716, 212.0849592, -32.58562625, -982.7336105, -35.10860935, 567.8931751,
          -1.917212423, -260.2023543, -1.023821735, 157.5533477, 23.00200055, 232.0603673,
          -36.79100036, -111.9110936, 18.05429984, 447.0481000, 15.10187415, -258.7297813,
          -1.032340149, -298.6402478, -1.676201415, 180.5856487, 64.52313024, 209.0160857,
          -53.85574010, -98.52164290, 14.35891214, 536.7666279, 20.09318806, -309.7349530],
         [-131287.8986, -631927.6885, -318797.4173, 616785.8782, -50027.36189, 863099.9833,
          47680.20240, -1053367.944, -501120.3811, -174400.9476, 222328.6873, 333551.7374,
          -389338.7841, -1995527.467, -982971.3024, 1960434.268, 297239.7137, 2676525.168,
          -147113.4775, -3358059.979, -2106979.191, -462827.1322, 1017607.960,
          1039018.475, 520266.9296, 2627427.473, 1301981.763, -2577171.706, -238071.9956,
          -3539781.111, 94628.16420, 4411304.724, 2598205.733, 637504.9351, -1234794.298,
          -1372562.403, -2.646186796, -31.10055575, 2.295799273, 19.20203279, 30.01931202,
          -302.1028550, -14.78310655, 162.1561899, .4943938056, 176.8089129, -.2444921680,
          -100.6148929, 9.172262228, 137.4303440, -8.451613443, -84.20684224,
          -167.3354083, 1321.830393, 76.89928813, -705.7586223, 18.28186732, -770.1665162,
          -9.084224422, 436.3368157, -6.374255638, -107.2730177, 6.080451222, 65.53843753,
          143.2872994, -1028.009017, -64.22739330, 547.8536586, -20.58928632, 597.3893669,
          10.17964133, -337.7800252]]
    ]
    T1Sym = [[0.8213262337E-01, 0.8742978101E-01],
             [0.8407754233E-01, 0.8708605901E-01]]
    T2Sym = [[-0.7962186676E-05, -0.1028562327E-04],
             [-0.9613356793E-05, -0.1256706895E-04]]
    pSym = [
        [[148.5493329, 99.79912328, 70.78093196],
         [204.8672197, 110.7748799, 87.36036207]],
        [[247.9296982, 159.2471769, 102.3151816],
         [227.2102611, 115.9154291, 94.34364830]]
    ]
    qSym = [
        [[139.8135237, 91.96485261, 6.983488815],
         [281.5331360, 140.3461448, 17.07537768]],
        [[219.6475201, 107.9582783, 10.00264684],
         [241.4844439, 107.7583478, 22.36222385]]
    ]
    rSym = [
        [[35.23177574, 47.45346891, 58.44877918],
         [5.522491330, 31.06364270, 73.57632579]],
        [[15.81062488, 34.99767599, 133.0832773],
         [3.625357304, 64.03192907, 109.0743468]]
    ]
    sSym = [
        [[9.055554871, 19.80484284, 2.860045019],
         [6.729732641, 4.100970449, 2.780422877]],
        [[7.718306072, 25.22866153, 5.013583103],
         [6.282634037, 27.79399216, 2.270602235]]
    ]
    shieldingAmpSym = [
        [[4956703.683, -26922641.21, -11383659.85, 29604361.65, -38919785.97, 70230899.72,
          34993479.24, -90409215.02, 30448713.69, -48360257.19, -35556751.23, 57136283.60,
          -8013815.613, 30784907.86, 13501620.50, -35121638.52, 50297295.45, -84200377.18,
          -46946852.58, 107526898.8, -39003263.47, 59465850.17, 47264335.10, -68892388.73,
          3375901.533, -9181255.754, -4494667.217, 10812618.51, -17351920.97, 27016083.00,
          18150032.11, -33186882.96, 13340198.63, -19779685.30, -17891788.15, 21625767.23,
          16135.32442, 133094.0241, -13845.61859, -79159.98442, 432.1215298, -85438.10368,
          1735.386707, 41891.71284, 18158.14923, -105465.8135, -11685.73823, 62297.34252,
          -10811.08476, -87631.38186, 9217.499261, 52079.94529, -68.29127454, 56023.02269,
          -1246.029857, -27436.42793, -11972.61726, 69607.08725, 7702.743803, -41114.36810,
          12.08269108, -21.30967022, -9.100782462, 18.26855933, -7.000685929, 26.22390883,
          6.392164144, -21.99351743, 2.294204157, -16.10023369, -1.344314750, 9.342121230],
         [-1210748.720, -52324903.95, -14158413.33, 19426123.60, 6808641.947, -5138390.983,
          -1118600.499, -4675055.459, 2059671.506, -1373488.052, -114704.4353, -1435920.472,
          1438451.655, 61199067.17, 16549301.39, -22802423.47, -7814550.995, 5986478.728,
          1299443.190, 5352371.724, -2994351.520, 1898553.337, 203158.3658, 2270182.134,
          -618083.3112, -25950806.16, -7013783.326, 9698792.575, 3253693.134, -2528478.464,
          -546323.4095, -2217735.237, 1495336.589, -914647.4222, -114374.1054, -1200441.634,
          -507068.4700, 1163189.975, 998411.8381, -861919.3631, 5252210.872, -11668550.16,
          -4113899.385, 6972900.950, -2546104.076, 7704014.310, 2273077.192, -5134603.198,
          256205.7901, -589970.8086, -503821.0170, 437612.8956, -2648640.128, 5887640.735,
          2074286.234, -3519291.144, 1283847.104, -3885817.147, -1145936.942, 2589753.651,
          -408.7788403, 1234.054185, 739.8541716, -965.8068853, 3691.383679, -8628.635819,
          -2855.844091, 5268.500178, -1774.372703, 5515.010707, 1556.089289, -3665.434660]],
        [[-67763516.61, -49565522.84, 10123356.08, 51805446.10, -51607711.68, 164360662.1,
          -4662006.024, -191297217.6, -7204547.103, 30372354.93, -750371.9365, -36564457.17,
          61114395.65, 45702536.50, -9228894.939, -47893708.68, 47290934.33, -149155112.0,
          4226520.638, 173588334.5, 7998505.443, -33150962.72, 832493.2094, 39892545.84,
          -11303915.16, -8901327.398, 1751557.110, 9382865.820, -9054707.868, 27918664.50,
          -788741.7146, -32481294.42, -2264443.753, 9022346.503, -233526.0185, -10856269.53,
          -244450.8850, 1908295.272, 185445.1967, -1074202.863, 41827.75224, -241553.7626,
          -20199.12580, 123235.6084, 199501.4614, -1936498.464, -178857.4074, 1044724.507,
          121044.9917, -946479.9247, -91808.28803, 532742.7569, -20742.28628, 120633.2193,
          10018.49534, -61599.11035, -98709.58977, 959095.1770, 88500.43489, -517471.5287,
          -81.56122911, 816.2472344, 55.30711710, -454.5368824, 25.74693810, -202.5007350,
          -7.369350794, 104.9429812, 58.14049362, -685.5919355, -51.71345683, 374.0125033],
         [-43404887.31, 8896854.538, -8077731.036, -10247813.65, 6346729.086, -9416801.212,
          -1921670.268, 7805483.928, 2299301.127, 4856980.170, -1253936.462, -4695042.690,
          54305735.91, -11158768.10, 10051771.85, 12837129.47, -6380785.836, 12387093.50,
          1687850.192, -10492039.47, -5777044.862, -6916507.424, 2855974.911, 7027302.490,
          -26176628.93, 5387959.610, -4827069.106, -6193036.589, 2511954.143,
          -6205105.083, -553187.2984, 5341386.847, 3823736.361, 3669209.068, -1841641.700,
          -3842906.796, 281561.7220, -5013124.630, 379824.5943, 2436137.901, -76337.55394,
          548518.2676, 42134.28632, -281711.3841, -365514.8666, -2583093.138,
          -232355.8377, 1104026.712, -131536.3445, 2320169.882, -174967.6603,
          -1127251.881, 35539.82827, -256132.9284, -19620.06116, 131598.7965, 169033.6708,
          1194443.500, 107320.3699, -510672.0036, 1211.177843, -17278.19863, 1140.037733,
          8347.612951, -303.8408243, 2405.771304, 174.0634046, -1248.722950, -1231.229565,
          -8666.932647, -754.0488385, 3736.878824]]
    ]

    def __init__(self, region, mode, trigParityI, dipoleTilt, dynamicPressure,
                 kappa, scalingCoefficient):
        """Initialize a new FieldAlignedCurrentShiedingBuilder object.

        Initialize a new FieldAlignedCurrentShiedingBuilder object.

        Parameters
        ----------
        region : int
            FAC region code.
        mode : int
            Trigonometric mode.
        trigParityI : TrigParity
            Even for cosine, odd for sine.
        dipoleTilt : float
            Dipole tilt angle.
        dynamicPressure : float
            Dynamic pressure.
        kappa : float
            Kappa scaling factor.
        scalingCoefficient : float
            Scaling coefficient.
        """
        self.region = region
        self.mode = mode
        self.trigParityI = trigParityI
        self.dipoleTilt = dipoleTilt
        self.dynamicPressure = dynamicPressure
        self.kappa = kappa
        self.scalingCoefficient = scalingCoefficient

    def build(self):
        """Build the field-aligned current shielding field.

        Build the field-aligned current shielding field.

        Parameters
        ----------
        None

        Returns
        -------
        result : VectorField
            The field-aligned current shielding field.
        """
        dynamicPressureScalingFactor = pow(self.dynamicPressure/2, 0.155)
        aPerpenValues = nones((3, 3))
        aParallValues = nones((3, 3))
        xScale = (
            self.kappa -
            FieldAlignedCurrentShiedingBuilder.kappaScaleAdj[self.region - 1]
        )
        FieldAlignedCurrentShiedingBuilder.fillShieldingCoeffs(
            self.region, self.mode, self.dipoleTilt, xScale, self.trigParityI,
            aPerpenValues, aParallValues
        )
        if self.trigParityI is ODD:
            T1 = FieldAlignedCurrentShiedingBuilder.T1Sym
            T2 = FieldAlignedCurrentShiedingBuilder.T2Sym
            p = FieldAlignedCurrentShiedingBuilder.pSym
            q = FieldAlignedCurrentShiedingBuilder.qSym
            r = FieldAlignedCurrentShiedingBuilder.rSym
            s = FieldAlignedCurrentShiedingBuilder.sSym
            aPerpendicular = ArrayCoefficientExpansion2D(
                aPerpenValues).negate()
            aParallel = ArrayCoefficientExpansion2D(
                    aParallValues).negate()
        else:
            T1 = FieldAlignedCurrentShiedingBuilder.T1ASym
            T2 = FieldAlignedCurrentShiedingBuilder.T2ASym
            p = FieldAlignedCurrentShiedingBuilder.pASym
            q = FieldAlignedCurrentShiedingBuilder.qASym
            r = FieldAlignedCurrentShiedingBuilder.rASym
            s = FieldAlignedCurrentShiedingBuilder.sASym
            aPerpendicular = ArrayCoefficientExpansion2D(aPerpenValues)
            aParallel = ArrayCoefficientExpansion2D(aParallValues)
        psiT1 = self.dipoleTilt*T1[self.region - 1][self.mode - 1]
        psiT2 = self.dipoleTilt*T2[self.region - 1][self.mode - 1]
        pExpansion = ScalarExpansion1D(p[self.region - 1][self.mode - 1]).invert()
        qExpansion = ScalarExpansion1D(q[self.region - 1][self.mode - 1]).invert()
        rExpansion = ScalarExpansion1D(r[self.region - 1][self.mode - 1]).invert()
        sExpansion = ScalarExpansion1D(s[self.region - 1][self.mode - 1]).invert()
        f = vectorfields.scale(
            PerpendicularAndParallelCartesianHarmonicField.createWithRotation(
                self.trigParityI, psiT1, pExpansion, rExpansion,
                aPerpendicular, psiT2, qExpansion, sExpansion, aParallel),
                self.scalingCoefficient)
        return scaleLocation(f, dynamicPressureScalingFactor)

    @staticmethod
    def fillShieldingCoeffs(region, mode, dipoleTilt, xScale, trigParityI,
                            aPerpenValuesBuffer, aParallValuesBuffer):
        """Fill in the shielding coefficients.

        Fill in the shielding coefficients.

        Parameters
        ----------
        region : int
            FAC region code.
        mode : int
            Trigonometric mode.
        dipoleTilt : float
            Dipole tilt angle.
        xScale : float
            Scale factor for x-coordinate.
        trigParityI : TrigParity
            Even for cosine, odd for sine.
        aPerpenValuesBuffer : 2-D array-like of float
            Buffer to hold perpendicular values.
        aParallValuesBuffer : 2-D array-like of float
            Buffer to hold parallel values.

        Returns
        -------
        None
        """
        sinPsi = sin(dipoleTilt)
        cosPsi = cos(dipoleTilt)
        sin3Psi = 2*cosPsi  # Name kept from legacy... why is it so named?
        loop = 0
        for m in range(2):
            for i in range(3):
                for k in range(3):
                    coeff = 0.0
                    coeff2 = 0.0
                    coeff3 = 0.0
                    coeff4 = 0.0
                    if trigParityI is ODD:
                        coeff = FieldAlignedCurrentShiedingBuilder.shieldingAmpSym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff2 = FieldAlignedCurrentShiedingBuilder.shieldingAmpSym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff3 = FieldAlignedCurrentShiedingBuilder.shieldingAmpSym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff4 = FieldAlignedCurrentShiedingBuilder.shieldingAmpSym[region - 1][mode - 1][loop]
                        loop += 1
                    else:
                        coeff = FieldAlignedCurrentShiedingBuilder.shieldingAmpASym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff2 = FieldAlignedCurrentShiedingBuilder.shieldingAmpASym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff3 = FieldAlignedCurrentShiedingBuilder.shieldingAmpASym[region - 1][mode - 1][loop]
                        loop += 1
                        coeff4 = FieldAlignedCurrentShiedingBuilder.shieldingAmpASym[region - 1][mode - 1][loop]
                        loop += 1
                    if m == 0:
                        aPerpenValuesBuffer[i][k] = (
                            coeff + xScale*coeff2 +
                            cosPsi*(coeff3 + xScale*coeff4)
                        )
                    else:
                        aParallValuesBuffer[i][k] = (
                            sinPsi*(coeff + xScale*coeff2 +
                                    sin3Psi*(coeff3 + xScale*coeff4))
                        )
