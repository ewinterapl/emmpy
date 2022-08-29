"""Manage calculations for field-aligned currents.

Manage calculations for field-aligned currents.

Authors
-------
Nicholas Sharp
Eric Winter (eric.winter@jhuapl.edu)
"""


import emmpy.math.vectorfields.vectorfields as vectorfields
from emmpy.geomagmodel.ts07.modeling.fieldaligned.fieldalignedcurrentbuilder import (
    FieldAlignedCurrentBuilder
)
from emmpy.geomagmodel.ts07.modeling.fieldaligned.fieldalignedcurrentshiedingbuilder import (
    FieldAlignedCurrentShiedingBuilder
)
from emmpy.magmodel.math.trigparity import EVEN, ODD
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import add, addAll


class Ts07DFieldAlignedMagneticField(BasisVectorField):
    """Manage calculations for field-aligned currents.

    Manage calculations for field-aligned currents.

    Citations:
    Tsyganenko and Sitnov 2007 - "Magnetospheric Configurations from a
    high-resolution data-based magnetic field model" , Journal of
    Geophysical Research
    Tsyganenko 2002 - "A New Magnetosphere Magnetic Field Model -
    Mathematical Structure", section 2.3, Journal of Geophysical Research

    Attributes
    ----------
    includeShielding : bool
        True to compute shielding field.
    internalFields : list of VectorField
        internalFields
    internalField : VectorField
        internalField
    shieldingFields : list of VectorField
        shieldingFields
    shieldingField : VectorField
        shieldingField
    basisFunctions : list of VectorField
        basisFunctions
    basisCoefficients : list of float
        basisCoefficients
    """

    def __init__(self, dipoleTiltAngle, dynamicPressure, region1KappaScaling,
                 region2KappaScaling, options, includeShielding):
        """Initialize a new Ts07DFieldAlignedMagneticField object.

        Initialize a new Ts07DFieldAlignedMagneticField object.

        Parameters
        ----------
        dipoleTiltAngle : float
            dipoleTiltAngle
        dynamicPressure : float
            dynamicPressure
        region1KappaScaling : float
            region1KappaScaling
        region2KappaScaling : float
            region2KappaScaling
        options : list of FacConfigurationOptions
            options
        includeShielding : bool
            True to compute shielding field.
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

        # Construct all the fields, unlike in the original TS07D, instead of 4
        # FAC systems, this now supports any number.
        for option in options:
            amp = option.amplitudeScaling
            basisCoefficientsBuilder.append(amp)
            region = option.region
            kappa = region1KappaScaling
            if region == 2:
                kappa = region2KappaScaling
            shieldingParity = EVEN
            scaleFactor = amp*scaling
            if option.trigParity is EVEN:
                scaleFactor = -scaleFactor
                shieldingParity = ODD

            builder = FieldAlignedCurrentBuilder(
                option.region, option.mode, option.trigParity,
                dipoleTiltAngle, dynamicPressure, kappa, scaleFactor)
            builder.withTheta0(option.theta0)
            builder.withDeltaTheta(option.deltaTheta)
            builder.smoothing = option.smoothed

            field = builder.build()
            internalFieldsBuilder.append(field)

            if option.shielded:
                shieldingField = FieldAlignedCurrentShiedingBuilder(
                    option.region, option.mode,
                    shieldingParity, dipoleTiltAngle, dynamicPressure, kappa,
                    amp).build()
                shieldingFieldsBuilder.append(shieldingField)
                basisFunctionsBuilder.append(
                    vectorfields.scale(add(field, shieldingField), 1.0/amp))
            else:
                basisFunctionsBuilder.append(vectorfields.scale(field, 1.0/amp))

        self.internalFields = internalFieldsBuilder
        self.shieldingFields = shieldingFieldsBuilder
        self.internalField = addAll(self.internalFields)

        # Scale position vector for solar wind (see Tsy 2002-1 2.4).
        self.shieldingField = addAll(self.shieldingFields)

        self.basisFunctions = basisFunctionsBuilder
        self.basisCoefficients = basisCoefficientsBuilder

    @staticmethod
    def create(dipoleTiltAngle, dynamicPressure, region1KappaScaling,
               region2KappaScaling, options, includeShielding):
        """Create a new Ts07DFieldAlignedMagneticField module.

        Creates a new Ts07DFieldAlignedMagneticField module from the
        provided list of FacConfigurationOptions.

        Parameters
        ----------
        dipoleTiltAngle : float
            The dipole tilt angle.
        dynamicPressure : float
            The dynamic pressure.
        region1KappaScaling : float
            The global spatial scaling of the region-1 FAC modules.
        region2KappaScaling : float
            The global spatial scaling of the region-2 FAC modules.
        options : list of FacConfigurationOptions
            options
        includeShielding :bool;
            includeShielding
        
        Returns
        -------
        result : Ts07DFieldAlignedMagneticField
            The newly-constructed field.
        """
        return Ts07DFieldAlignedMagneticField(
            dipoleTiltAngle, dynamicPressure, region1KappaScaling,
            region2KappaScaling, options, includeShielding)

    def evaluate(self, location, buffer):
        """Evaluate the field.

        Evaluate the field.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        buffer : VectorIJK
            Buffer to hold result.
        
        Returns
        -------
        v : VectorIJK
            Evaluation of field at location.
        """
        # Evaluate the FAC internal fields.
        internal = self.internalField.evaluate(location)
        shield = VectorIJK(0, 0, 0)

        # If shielding fields are turned on, evaluate those.
        if self.includeShielding:
            shield = self.shieldingField.evaluate(location)

        # Add the internal+shielding.
        v = VectorIJK.addAll([internal, shield], buffer)
        return v

    def evaluateExpansion(self, location):
        """Evaluate the expansion at a location.

        Evaluate the expansion at a location.

        Parameters
        ----------
        location : VectorIJK
            Location for evaluation.
        
        Returns
        -------
        values : list of VectorIJK
            Evaluation of expansion components at location.
        """
        values = []
        count = 0
        for basisFunction in self.basisFunctions:
            coeff = self.basisCoefficients[count]
            count += 1
            bfe = basisFunction.evaluate(location)
            v = coeff*VectorIJK(bfe)
            values.append(v)
        return values

    def getNumberOfBasisFunctions(self):
        """Get the number of basis functions.

        Get the number of basis functions.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Number of basis functions.
        """
        return self.basisFunctions.size()
