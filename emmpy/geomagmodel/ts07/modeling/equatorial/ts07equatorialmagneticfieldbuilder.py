"""emmpy.geomagmodel.ts07.modeling.equatorial.ts07equtorialmagneticfieldbuilder"""


# from emmpy.com.google.common.base.preconditions import Preconditions
# from emmpy.magmodel.core.math.bessel.coltbesselfunctionevaluator import (
#     ColtBesselFunctionEvaluator
# )


class Ts07EquatorialMagneticFieldBuilder:
    """A Builder for constructing the TS07D empirical magnetic field
    model and derivatives of the model.

    author Nicholas Sharp
    author G.K.Stephens
    """
    pass

    # def __init__(self, dipoleTiltAngle, dynamicPressure, coeffs, tailLength,
    #              shieldingCoeffs):
    #     """Constructor

    #     @param dipoleTiltAngle
    #     @param dynamicPressure
    #     @param coeffs
    #     @param tailLength
    #     @param shieldingCoeffs
    #     """
    #     self.dipoleTiltAngle = dipoleTiltAngle
    #     self.dynamicPressure = dynamicPressure
    #     self.coeffs = Preconditions.checkNotNull(coeffs)
    #     self.tailLength = tailLength
    #     self.shieldingCoeffs = Preconditions.checkNotNull(shieldingCoeffs)
    #     self.bessel = ColtBesselFunctionEvaluator()
    #     self.includeShield = True
    #     self.withTA15deformation = 0

    # def withAlbertBessel(self):
    #     """Use Jay Albert's faster Bessel function evaluator.

    #     By default, the Bessel function evaluator will be Tsyganenko's, if this
    #     is set, Jay Albert's Bessel function evaluator will be used instead.
    #     Jay Albert's implementation is about 4 times faster, although it gives
    #     slightly different, but negligible, differences.

    #     @return this builder object
    #     """
    #     # self.bessel = AlbertBesselFunctionEvaluator(14)
    #     return self

    # def set_withTA15deformation(self, bzIMF):
    #     """Use the TA15 bending and warping deformation instead of the T01
    #     bending and warping deformation.

    #     By default, the model uses the T01 bending and warping deformation.

    #     @param bzIMF the z-component of the IMF (interplanetary magnetic field)
    #     averaged over the previous 30 minutes
    #     @return this builder object
    #     """
    #     self.withTA15deformation = bzIMF
    #     return self

    # def withEquatorialShielding(self):
    #     """Turn on equatorial shielding.

    #     By default, the equatorial shielding fields are evaluated, so if you
    #     haven't previously turned them off, you won't need to call this.

    #     @return this builder object
    #     """
    #     self.includeShield = True
    #     return self

    # def withoutEquatorialShielding(self):
    #     """Turn off equatorial shielding.

    #     By default, the equatorial shielding fields are evaluated. Evaluating
    #     the shielding of the equatorial fields, is about 90% of the computation
    #     time required of the model. Since they are not needed in all
    #     applications, like computing the current density inside the
    #     magnetopause, the option to turn them off can significantly speed up
    #     the code.

    #     @return this builder object
    #     """
    #     self.includeShield = False
    #     return self

    # def build(self):
    #     """Builder"""
    #     numCurrSheets = len(self.coeffs.getCurrThicks())
    #     hingeDistance = self.coeffs.getHingeDistance()
    #     warpingParam = self.coeffs.getWarpingParam()
    #     twistParam = self.coeffs.getTwistParam()

    #     #     BasisVectorField[] equatorialFields = new BasisVectorField[numCurrSheets];

    #     #     // loop through each of the current sheets
    #     #     for (int currSheetIndex = 0; currSheetIndex < numCurrSheets; currSheetIndex++) {

    #     #       double currSheetThick = coeffs.getCurrThicks().get(currSheetIndex);

    #     #       Ts07EquatorialLinearCoefficients linearCoeffs = coeffs.getLinearCoeffs().get(currSheetIndex);

    #     #       /*
    #     #        * Check the inputs
    #     #        */
    #     #       checkArgument(dynamicPressure > 0, "dynamic pressure must be greater than zero");
    #     #       // check that the number of expansions is consistent
    #     #       checkArgument(
    #     #           linearCoeffs.getNumAzimuthalExpansions() == shieldingCoeffs.getNumAzimuthalExpansions(),
    #     #           "The number of radial expansions for the variable coefficients "
    #     #               + "is %s, while for the shielding coefficients it is %s",
    #     #           linearCoeffs.getNumAzimuthalExpansions(), shieldingCoeffs.getNumAzimuthalExpansions());
    #     #       checkArgument(
    #     #           linearCoeffs.getNumRadialExpansions() == shieldingCoeffs.getNumRadialExpansions(),
    #     #           "The number of radial expansions for the variable coefficients "
    #     #               + "is %s, while for the shielding coefficients it is %s",
    #     #           linearCoeffs.getNumRadialExpansions(), shieldingCoeffs.getNumRadialExpansions());

    #     #       // Construct a constant current sheet half thickness
    #     #       DifferentiableScalarFieldIJ currentSheetHalfThickness =
    #     #           CurrentSheetHalfThicknesses.createConstant(currSheetThick);

    #     #       // Construct the shielded thin current sheet
    #     #       ShieldedThinCurrentSheetField thinCurrentSheet = ShieldedThinCurrentSheetField.createUnity(
    #     #           currentSheetHalfThickness, tailLength, bessel, shieldingCoeffs, includeShield);

    #     #       /*
    #     #        * if the with TA15 deformation was called, apply the TA15 deformation instead of the T01
    #     #        * deformation
    #     #        */
    #     #       BasisVectorField bentWarpedField = thinCurrentSheet;
    #     #       if (withTA15deformation.isPresent()) {

    #     #         // warp the shielded thin current sheet
    #     #         BasisVectorField warpedField = DeformationII.deformBasisField(dipoleTiltAngle,
    #     #             hingeDistance, warpingParam, twistParam, thinCurrentSheet);

    #     #         double bzIMF = withTA15deformation.getAsDouble();

    #     #         // now apply the bending deformation to the warped field
    #     #         bentWarpedField =
    #     #             DeformationI.deformBasisField(dipoleTiltAngle, hingeDistance, bzIMF, warpedField);
    #     #       }
    #     #       // the T01 deformation (standard for TS07D)
    #     #       else {

    #     #         // warp the shielded thin current sheet
    #     #         BasisVectorField warpedField = TwistWarpFfunction.deformBasisField(dipoleTiltAngle,
    #     #             warpingParam, twistParam, thinCurrentSheet);

    #     #         // now apply the bending deformation to the warped field
    #     #         bentWarpedField =
    #     #             PositionBender.deformBasisField(dipoleTiltAngle, hingeDistance, warpedField);
    #     #       }

    #     #       // Scale position vector for solar wind (see Tsy 2002-1 2.4)
    #     #       /*
    #     #        * Note: this is a point of inconsistency with the Fortran code, in the Fortran this
    #     #        * calculation is done in single precision. When the field values are very large, this can
    #     #        * result in tenths of differences between the Java and the Fortran version of the model
    #     #        */
    #     #       double pdynScaling = pow(dynamicPressure / 2.0, 0.155);
    #     #       BasisVectorField scaledBentWarpedField =
    #     #           BasisVectorFields.scaleLocation(bentWarpedField, pdynScaling);

    #     #       CoefficientExpansion1D coeffs = linearCoeffs.getCoeffs().getAsSingleExpansion();
    #     #       CoefficientExpansion1D pdynCoeffs =
    #     #           linearCoeffs.getPdynScaledCoeffs(dynamicPressure).getAsSingleExpansion();

    #     #       // Finally, expand the coefficients by including a term that includes the dynamical pressure
    #     #       BasisVectorField equatorialField =
    #     #           BasisVectorFields.expandCoefficients2(scaledBentWarpedField, coeffs, pdynCoeffs);

    #     #       equatorialFields[currSheetIndex] = equatorialField;
    #     #     }

    #     #     return BasisVectorFields.concatAll(equatorialFields);
    #     #   }

    # # }
