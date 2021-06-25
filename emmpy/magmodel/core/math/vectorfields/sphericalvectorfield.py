"""A vector field in spherical coordinates."""


from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)
from emmpy.crucible.core.math.coords.vectorfieldvalueconversions import (
    VectorFieldValueConversions
)
from emmpy.crucible.core.math.vectorfields.scalarfield import ScalarField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.magmodel.core.math.vectorfields.sphericalscalarfield import (
    SphericalScalarField
)


class SphericalVectorField(VectorField):
    """A vector field in spherical coordinates.

    Represents a VectorField in spherical coordinates and provides the
    conversion from a SphericalVector field to a Cartesian vector field.

    where r is the radius, &#952; is the co-latitude angle, and &#966; is the
    longitude (or aziumuth) angle

    author G.K.Stephens
    """

    # Constructor is inherited from VectorField, and does nothing.

    @staticmethod
    def negate(vectorField):
        """Negate a vector field.

        param SphericalVectorField vectorField
        return SphericalVectorField
        """
        svf = SphericalVectorField()

        def my_evaluate(location):
            # SphericalVector location
            # SphericalVector vect
            vect = vectorField.evaluate(location)
            # SphericalVector negatedVect
            negatedVect = SphericalVector(
                -vect.getRadius(), -vect.getColatitude(), -vect.getLongitude()
            )
            return negatedVect
        svf.evaluate = my_evaluate
        return svf

    @staticmethod
    def extractRadial(vectorField):
        """Return the radial component of the field.

        param SphericalVectorField vectorField
        return SphericalScalarField
        """
        ssf = SphericalScalarField()
        # SphericalVector posSph
        ssf.evaluateScalar = (
            lambda posSph:
            vectorField.evaluate(posSph).getRadius()
        )
        return ssf

    @staticmethod
    def createRadialField():
        """Create a unit vector in the radial direction.

        return SphericalVectorField
        """
        svf = SphericalVectorField()
        # SphericalVector location
        svf.evaluate = lambda location: SphericalVector(1.0, 0.0, 0.0)
        return svf

    @staticmethod
    def createColatitudinalField():
        """Create a unit vector in the latitudinal direction.

        return SphericalVectorField
        """
        svf = SphericalVectorField()
        # SphericalVector location
        svf.evaluate = lambda location: SphericalVector(0.0, 1.0, 0.0)
        return svf

    @staticmethod
    def createAzimuthalField():
        """Create a unit vector in the azimuthal direction.

        return SphericalVectorField
        """
        svf = SphericalVectorField()
        # SphericalVector location
        svf.evaluate = lambda location: SphericalVector(0.0, 0.0, 1.0)
        return svf

    @staticmethod
    def scale(field, scaleFactor):
        """Scale a spherical vector field.

        The location is not scaled.

        param SphericalVectorField field a spherical vector field
        param double scaleFactor a value to scale the output
        return SphericalVectorField a newly created spherical vector field that
        computes the scale ( a*scaleFactor  )
        """
        svf = SphericalVectorField()

        def my_evaluate(location):
            # SphericalVector location
            # SphericalVector fieldVect
            fieldVect = field.evaluate(location)
            # SphericalVector scaledFieldVect
            scaledFieldVect = SphericalVector(
                fieldVect.getRadius()*scaleFactor,
                fieldVect.getColatitude()*scaleFactor,
                fieldVect.getLongitude()*scaleFactor
            )
            return scaledFieldVect
        svf.evaluate = my_evaluate
        return svf

    @staticmethod
    def add(a, b):
        """Add 2 spherical vector fields.

        param SphericalVectorField a a spherical vector field
        param SphericalVectorField b another spherical vector field
        return SphericalVectorField a newly created spherical vector field that
        computes the component-wise sum ( a + b )
        """
        addField = SphericalVectorField()

        def my_evaluate(location):
            # SphericalVector location
            # return SphericalVector
            # SphericalVector aVect
            aVect = a.evaluate(location)
            # SphericalVector bVect
            bVect = b.evaluate(location)
            return SphericalVector(
                aVect.getRadius() + bVect.getRadius(),
                aVect.getColatitude() + bVect.getColatitude(),
                aVect.getLongitude() + bVect.getLongitude()
            )
        addField.evaluate = my_evaluate
        return addField

    @staticmethod
    def addAll(fields):
        """Add a lost of spherical vector fields.

        param list of SphericalVectorField fields a varargs of spherical vector
        fields
        return SphericalVectorField a newly created spherical vector field that
        computes the component-wise sum ( a + b + ...) of all the vector fields
        """
        svf = SphericalVectorField()

        def my_evaluate(location):
            # SphericalVector location
            fr = 0.0
            ft = 0.0
            fp = 0.0
            # SphericalVectorField field
            for field in fields:
                # SphericalVector sphVect
                sphVect = field.evaluate(location)
                fr += sphVect.getRadius()
                ft += sphVect.getColatitude()
                fp += sphVect.getLongitude()
            return SphericalVector(fr, ft, fp)
        svf.evaluate = my_evaluate
        return svf

    @staticmethod
    def asSpherical(field):
        """Convert a Cartesian field to spherical coordinates.

        param VectorField field
        return SphericalVectorField
        """
        if isinstance(field, SphericalVectorField):
            return field
        else:
            assert(isinstance(field, VectorField))
            svf = SphericalVectorField()

            def my_evaluate(*args):
                # override this default method to improve the performance of
                # the code, we already have the field as a Cartesian field, so
                # there is no need to jump through the conversions
                if len(args) == 1:
                    # SphericalVector location
                    (location,) = args
                    assert(isinstance(location, SphericalVector))
                    # convert the Cartesian position to spherical
                    # UnwritableVectorIJK locCart
                    locCart = CoordConverters.convert(location)
                    # evaluate the field value
                    # UnwritableVectorIJK fieldValue
                    fieldValue = field.evaluate(locCart)
                    # construct the spherical vector field value for the given
                    # position
                    # CartesianVectorFieldValue cart
                    cart = CartesianVectorFieldValue(locCart, fieldValue)
                    # convert the vector field value back to Cartesian
                    # SphericalVector valueSphere
                    valueSphere = (
                        VectorFieldValueConversions.convertToSpherical(cart).getValue()
                    )
                    # return the value
                    return valueSphere
                elif len(args) == 2:
                    # UnwritableVectorIJK location
                    # VectorIJK buffer
                    (location, buffer) = args
                    assert(
                        isinstance(location, UnwritableVectorIJK) and
                        isinstance(buffer, VectorIJK))
                    return field.evaluate(location, buffer)
                else:
                    raise Exception
            svf.evaluate = my_evaluate
            return svf

    @staticmethod
    def extractFr(field):
        """Create a ScalarField from the radial components.

        param SphericalVectorField field
        return ScalarField a newly created capturing the radial component of
        the spherical vector field
        """
        sf = ScalarField()
        # UnwritableVectorIJK location
        sf.evaluate = (
            lambda location:
            field.evaluate(CoordConverters.convertToSpherical(location)).getRadius()
        )
        return sf

    @staticmethod
    def extractFtheta(field):
        """Create a ScalarField from the colatitudinal component.

        param SphericalVectorField field
        @return ScalarField a newly created capturing the colatitudinal
        component of the spherical vector field
        """
        sf = ScalarField()
        # UnwritableVectorIJK location
        sf.evaluate = (
            lambda location:
            field.evaluate(CoordConverters.convertToSpherical(location)).getColatitude()
        )
        return sf

    @staticmethod
    def extractFphi(field):
        """Create a ScalarField from the longitudinal component.

        param SphericalVectorField field
        return ScalarField a newly created capturing the longitudinal component
        of the spherical vector field
        """
        sf = ScalarField()
        # UnwritableVectorIJK location
        sf.evaluate = (
            lambda location:
            field.evaluate(CoordConverters.convertToSpherical(location)).getLongitude()
        )
        return sf

    def evaluate(self, *args):
        """Evaluate the field."""
        if len(args) == 1:
            (location,) = args
            assert(isinstance(location, SphericalVector))
            # Evaluate the field at the given position in spherical coordinates
            # units and such are up to the implementors
            # param location SphericalVector often location
            # return the resultant SphericalVector
            # throws FunctionEvaluationException if the function cannot perform
            # the evaluation
            raise Exception
        elif len(args) == 2:
            (location, buffer) = args
            assert(isinstance(location, VectorIJK))
            assert(isinstance(buffer, VectorIJK))

            # convert the Cartesian position to spherical
            # SphericalVector locSphere
            locSphere = CoordConverters.convertToSpherical(location)

            # evaluate the field value
            # SphericalVector fieldValue
            fieldValue = self.evaluate(locSphere)

            # construct the spherical vector field value for the given position
            # SphericalVectorFieldValue sphere
            sphere = SphericalVectorFieldValue(locSphere, fieldValue)

            # convert the vector field value back to Cartesian
            # UnwritableVectorIJK valueSphere
            valueSphere = (
                VectorFieldValueConversions.convert(sphere).getValue()
            )

            # return the value
            return buffer.setTo(valueSphere)

        else:
            raise Exception
