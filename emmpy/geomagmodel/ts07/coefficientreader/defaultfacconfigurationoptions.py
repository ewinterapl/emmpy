"""emmpy.geomagmodel.ts07.coefficientreader.defaultfacconfigurationoptions"""


from emmpy.geomagmodel.ts07.coefficientreader.facconfiguration import (
    FacConfiguration
)
# from emmpy.geomagmodel.ts07.coefficientreader.facregion import (
#     FacRegion
# )
# from emmpy.geomagmodel.ts07.modeling.fieldaligned.facconfigurationoptions import (
#     FacConfigurationOptions
# )
# from emmpy.magmodel.core.math.trigparity import TrigParity


class DefaultFacConfigurationOptions(FacConfiguration):
    """author G.K.Stephens"""

    # TS07D = 4
    # FAC6 = 6
    # FAC12 = 12
    # FAC16 = 16

    # r1_m1_theta0 = 0.7113544659
    # r1_m2_theta0 = 0.5567714182
    # r2_m1_theta0 = 0.8867880020
    # r2_m2_theta0 = 0.7247997430
    # r1_deltaTheta = 0.06
    # r2_deltaTheta = 0.09
    # shielded = True

    # def __init__(self, numberOfFields):
    #     """Constructor"""
    #     self.numberOfFields = numberOfFields

    # def createFromCoeffs(self, coeffs):
    #     if self.numberOfFields == DefaultFacConfigurationOptions.TS07D:
    #         return DefaultFacConfigurationOptions.getTs07(coeffs)
    #     elif self.numberOfFields == DefaultFacConfigurationOptions.FAC6:
    #         return DefaultFacConfigurationOptions.get6Fac(coeffs)
    #     elif self.numberOfFields == DefaultFacConfigurationOptions.FAC12:
    #         return DefaultFacConfigurationOptions.get12Fac(coeffs)
    #     elif self.numberOfFields == DefaultFacConfigurationOptions.FAC16:
    #         return DefaultFacConfigurationOptions.get16Fac(coeffs)
    #     else:
    #         raise Exception

    # def getNumberOfFields(self):
    #     return self.numberOfFields

    # @staticmethod
    # def getTs07(coeffs):
    #     """The TS07 Field Aligned currents"""

    #     smoothed = False
    #     count = 0

    #     # region 1
    #     region1Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m1_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m2_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2
    #     region2Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     return (region1Mode1Asym, region1Mode2Asym, region2Mode1Asym,
    #             region2Mode1Sym)

    # @staticmethod
    # def get6Fac(coeffs):
    #     smoothed = True
    #     count = 0

    #     # region 1
    #     region1Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m1_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m2_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded)
    #     count += 1

    #     # region 2
    #     region2Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded)
    #     count += 1
    #     region2Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2 modified
    #     region2Mode1AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     return (region1Mode1Asym, region1Mode2Asym, region2Mode1Asym,
    #             region2Mode1Sym, region2Mode1AsymMod, region2Mode1SymMod)

    # @staticmethod
    # def get12Fac(coeffs):
    #     smoothed = True
    #     count = 0

    #     # region 1
    #     region1Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m1_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m2_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m1_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m2_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2
    #     region2Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m2_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m2_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2 modified
    #     region2Mode1AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m2_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m2_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     return (region1Mode1Asym, region1Mode2Asym, region1Mode1Sym,
    #             region1Mode2Sym, region2Mode1Asym, region2Mode2Asym,
    #             region2Mode1Sym, region2Mode2Sym, region2Mode1AsymMod,
    #             region2Mode2AsymMod, region2Mode1SymMod, region2Mode2SymMod)

    # @staticmethod
    # def get16Fac(coeffs):
    #     smoothed = True
    #     count = 0

    #     # region 1
    #     region1Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m1_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m2_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m1_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m2_theta0 +
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 1 modified
    #     region1Mode1AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m1_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r1_m2_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode1SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m1_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region1Mode2SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_1, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r1_m2_theta0,
    #         DefaultFacConfigurationOptions.r1_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2
    #     region2Mode1Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2Asym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m2_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2Sym = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m2_theta0 -
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     # region 2 modified
    #     region2Mode1AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2AsymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.ODD,
    #         DefaultFacConfigurationOptions.r2_m2_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode1SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 1, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m1_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1
    #     region2Mode2SymMod = FacConfigurationOptions(
    #         coeffs[count], FacRegion.REGION_2, 2, TrigParity.EVEN,
    #         DefaultFacConfigurationOptions.r2_m2_theta0,
    #         DefaultFacConfigurationOptions.r2_deltaTheta,
    #         smoothed, DefaultFacConfigurationOptions.shielded
    #     )
    #     count += 1

    #     return (region1Mode1Asym, region1Mode2Asym, region1Mode1Sym,
    #             region1Mode2Sym, region1Mode1AsymMod, region1Mode2AsymMod,
    #             region1Mode1SymMod, region1Mode2SymMod, region2Mode1Asym,
    #             region2Mode2Asym, region2Mode1Sym, region2Mode2Sym,
    #             region2Mode1AsymMod, region2Mode2AsymMod, region2Mode1SymMod,
    #             region2Mode2SymMod)
