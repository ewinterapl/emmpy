"""emmpy.geomagmodel.ts07.modeling.fieldaligned.ts07dfieldalignedmagneticfield"""


# from emmpy.magmodel.core.math.trigparity import TrigParity
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class Ts07DFieldAlignedMagneticField(BasisVectorField):
    """Manages calculations for the Field Aligned Current Modules.

    Citations:
    Tsyganenko and Sitnov 2007 - "Magnetospheric Configurations from a
    high-resolution data-based magnetic field model" , Journal of Geophysical
    Research
    Tsyganenko 2002 - "A New Magnetosphere Magnetic Field Model -
    Mathematical Structure", section 2.3, Journal of Geophysical Research

    author Nicholas Sharp
    """
    pass

    def __init__(self, dipoleTiltAngle, dynamicPressure, region1KappaScaling,
                 region2KappaScaling, options, includeShielding):
        """Constructor

        double dipoleTiltAngle
        double dynamicPressure
        double region1KappaScaling
        double region2KappaScaling
        Iterable<FacConfigurationOptions> options
        boolean includeShielding
        return Ts07DFieldAlignedMagneticField
        """

        self.includeShielding = includeShielding

        # Magnitudes are multiplied by 800 to approximately normalize them with
        # the magnitudes of other basis functions. The actual value of this
        # normalization factor is quite arbitrary because it will be adjusted
        # for in the linear fitting process.
        # TODO I'm not sure why this has to be negated, in Tsy.'s code, he
        # rotates the sine implementation instead of replacing it with a
        # cosine. My guess is that he rotates it the wrong way making it a -cos
        # instead
        scaling = 800.0

        internalFieldsBuilder = []
        shieldingFieldsBuilder = []
        basisFunctionsBuilder = []
        basisCoefficientsBuilder = []

        # construct all the fields, unlike in the original TS07D, instead of 4
        # FAC systems, this now supports any number
        for option in options:
            amp = option.getAmplitudeScaling()
    #         basisCoefficientsBuilder.append(amp)
    #         region = option.getRegion()
    #         kappa = region1KappaScaling
    #         if region == 2:
    #             kappa = region2KappaScaling

    #         shieldingParity = TrigParity.EVEN
    #         scaleFactor = amp*scaling
    #         # if option.getTrigParity().equals(TrigParity.EVEN):
    #         if option.getTrigParity() is TrigParity.EVEN:
    #             scaleFactor = -scaleFactor
    #             shieldingParity = TrigParity.ODD

    # #       FieldAlignedCurrentBuilder builder =
    # #           new FieldAlignedCurrentBuilder(option.getRegion().getAsInt(), option.getMode(),
    # #               option.getTrigParity(), dipoleTiltAngle, dynamicPressure, kappa, scaleFactor);
    # #       builder.withTheta0(option.getTheta0());
    # #       builder.withDeltaTheta(option.getDeltaTheta());
    # #       builder.setSmoothing(option.isSmoothed());

    # #       VectorField field = builder.build();
    # #       internalFieldsBuilder.add(field);

    # #       if (option.isShielded()) {

    # #         VectorField shieldingField =
    # #             new FieldAlignedCurrentShiedingBuilder(option.getRegion().getAsInt(), option.getMode(),
    # #                 shieldingParity, dipoleTiltAngle, dynamicPressure, kappa, amp).build();

    # #         shieldingFieldsBuilder.add(shieldingField);

    # #         basisFunctionsBuilder.add(scale(add(field, shieldingField), 1.0 / amp));

    # #       } else {
    # #         basisFunctionsBuilder.add(scale(field, 1.0 / amp));
    # #       }

    # #     }

    # #     this.internalFields = internalFieldsBuilder.build();
    # #     this.shieldingFields = shieldingFieldsBuilder.build();

    # #     this.internalField = addAll(internalFields.toArray(new VectorField[internalFields.size()]));

    # #     // Scale position vector for solar wind (see Tsy 2002-1 2.4)
    # #     this.shieldingField = addAll(shieldingFields.toArray(new VectorField[shieldingFields.size()]));

    # #     this.basisFunctions = basisFunctionsBuilder.build();
    # #     this.basisCoefficients = basisCoefficientsBuilder.build();
    # #   }

    @staticmethod
    def create(dipoleTiltAngle, dynamicPressure, region1KappaScaling,
               region2KappaScaling, options, includeShielding):
        """Creates a new Ts07DFieldAlignedMagneticField module from the
        provided list of FacConfigurationOptions.

        param dipoleTiltAngle the dipole tilt angle
        param dynamicPressure the dynamic pressure
        param facKappaScale_R1 the global spatial scaling of the region-1
        field aligned current modules
        param facKappaScale_R2 the global spatial scaling of the region-2
        field aligned current modules
        param options (list)
        param includeShielding (bool)
        return a newly constructed
        CopyOfModifiedTs07DFieldAlignedMagneticField
        """
        return Ts07DFieldAlignedMagneticField(
            dipoleTiltAngle, dynamicPressure, region1KappaScaling,
            region2KappaScaling, options, includeShielding)

    # #   @Override
    # #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

    # #     // evaluate the FAC internal fields
    # #     UnwritableVectorIJK internal = internalField.evaluate(location);
    # #     UnwritableVectorIJK shield = new UnwritableVectorIJK(0, 0, 0);

    # #     // if shielding fields are turned on, evaluate those
    # #     if (includeShielding) {
    # #       shield = shieldingField.evaluate(location);
    # #     }

    # #     // add the internal+shielding
    # #     return VectorIJK.addAll(Lists.newArrayList(internal, shield), buffer);
    # #   }

    # #   public ImmutableList<VectorField> getBasisFunctions() {
    # #     return basisFunctions;
    # #   }

    # #   public ImmutableList<Double> getBasisCoefficients() {
    # #     return basisCoefficients;
    # #   }

    # #   @Override
    # #   public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {

    # #     ImmutableList.Builder<UnwritableVectorIJK> values = ImmutableList.builder();

    # #     int count = 0;
    # #     for (VectorField basisFunction : basisFunctions) {
    # #       double coeff = basisCoefficients.get(count++);
    # #       values.add(new UnwritableVectorIJK(coeff, basisFunction.evaluate(location)));
    # #     }

    # #     return values.build();
    # #   }

    # #   @Override
    # #   public int getNumberOfBasisFunctions() {
    # #     return basisFunctions.size();
    # #   }

    # #   public ImmutableList<VectorField> getInternalFields() {
    # #     return internalFields;
    # #   }

    # #   public ImmutableList<VectorField> getShieldingFields() {
    # #     return shieldingFields;
    # #   }

    # # }
