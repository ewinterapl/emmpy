"""emmpy.geomagmodel.ts07.modeling.fieldaligned.ts07dfieldalignedmagneticfield"""


from emmpy.crucible.core.math.vectorfields.vectorfields import VectorFields
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.geomagmodel.ts07.modeling.fieldaligned.fieldalignedcurrentbuilder import (
    FieldAlignedCurrentBuilder
)
from emmpy.geomagmodel.ts07.modeling.fieldaligned.fieldalignedcurrentshiedingbuilder import (
    FieldAlignedCurrentShiedingBuilder
)

from emmpy.magmodel.core.math.trigparity import TrigParity
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
            basisCoefficientsBuilder.append(amp)
            region = option.getRegion()
            kappa = region1KappaScaling
            if region == 2:
                kappa = region2KappaScaling
            shieldingParity = TrigParity.EVEN
            scaleFactor = amp*scaling
            if option.getTrigParity() is TrigParity.EVEN:
                scaleFactor = -scaleFactor
                shieldingParity = TrigParity.ODD

            builder = FieldAlignedCurrentBuilder(
                option.getRegion(), option.getMode(), option.getTrigParity(),
                dipoleTiltAngle, dynamicPressure, kappa, scaleFactor)
            builder.withTheta0(option.getTheta0())
            builder.withDeltaTheta(option.getDeltaTheta())
            builder.setSmoothing(option.isSmoothed())

            field = builder.build()
            internalFieldsBuilder.append(field)

            if option.isShielded():
                shieldingField = FieldAlignedCurrentShiedingBuilder(
                    option.getRegion(), option.getMode(),
                    shieldingParity, dipoleTiltAngle, dynamicPressure, kappa,
                    amp).build()
                shieldingFieldsBuilder.append(shieldingField)
                basisFunctionsBuilder.append(
                    VectorFields.scale(VectorFields.add(field, shieldingField), 1.0/amp))
            else:
                basisFunctionsBuilder.append(VectorFields.scale(field, 1.0/amp))

        self.internalFields = internalFieldsBuilder
        self.shieldingFields = shieldingFieldsBuilder
        self.internalField = VectorFields.addAll(self.internalFields)

        # Scale position vector for solar wind (see Tsy 2002-1 2.4)
        self.shieldingField = VectorFields.addAll(self.shieldingFields)

        self.basisFunctions = basisFunctionsBuilder
        self.basisCoefficients = basisCoefficientsBuilder

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

    def evaluate(self, location, buffer):
        """Evaluate the field.

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """

        # evaluate the FAC internal fields
        # UnwritableVectorIJK internal, shield
        internal = self.internalField.evaluate(location)
        shield = VectorIJK(0, 0, 0)

        # if shielding fields are turned on, evaluate those
        if self.includeShielding:
            shield = self.shieldingField.evaluate(location)

        # add the internal+shielding
        v = VectorIJK.addAll([internal, shield], buffer)
        return v

    def getBasisFunctions(self):
        """Return the list of basis functions.

        return [VectorField]
        """
        return self.basisFunctions

    def getBasisCoefficients(self):
        """Return the list of basis coefficients

        return [float]
        """
        return self.basisCoefficients

    def evaluateExpansion(self, location):
        """evaluateExpansion

        param UnwritableVectorIJK location
        return ImmutableList<UnwritableVectorIJK>
        """
        # [UnwritableVectorIJK] values
        values = []
        # int count
        count = 0
        # VectorField basisFunction
        for basisFunction in self.basisFunctions:
            # float coeff
            coeff = self.basisCoefficients[count]
            count += 1
            bfe = basisFunction.evaluate(location)
            v = VectorIJK(coeff, bfe)
            values.append(v)
        return values

    def getNumberOfBasisFunctions(self):
        """Get the number of basis functions.

        return int
        """
        return self.basisFunctions.size()

    def getInternalFields(self):
        """Return the list of internal fields.

        return [VectorField]
        """
        return self.internalFields

    def getShieldingFields(self):
        """Return the list of shielding fields.

        return [VectorField]
        """
        return self.shieldingFields
