"""emmpy.magmodel.core.math.coords.cylindricalcoordsxaligned"""


from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.vectorspace.bas import CylindricalVector
from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.units.fundamentalphysicalconstants import (
    FundamentalPhysicalConstants
)


# class CylindricalBasisVectorField:
#     """CylindricalBasisVectorField

#     This is a wrapper class used by CylindricalCoordsXAligned.
#     """

#     def __init__(self, cartesian):
#         """Constructor"""
#         self.cartesian = cartesian

#     def evaluate(self, location):

#         # convert the coordinate to Cartesian
#         locCart = CylindricalCoordsXAligned.convert(location)

#         # evaluate the Cartesian field
#         fieldCart = self.cartesian.evaluate(locCart)

#         # convert the field to cylindrical
#         return self.ccxa.convertFieldValue(locCart, fieldCart)

class CylindricalCoordsXAligned:
    """CylindricalCoordsXAligned"""

    @staticmethod
    def convert(*args):
        if isinstance(args[0], UnwritableVectorIJK):
            (cartesian,) = args
            # Converts a Cartesian coordinate to cylindrical coordinate
            # @param cartesian a UnwritableVectorIJK holding the Cartesian
            # coordinate
            # @return a CylindricalVector holding the cylindrical coordinate
            x = cartesian.getI()
            y = cartesian.getJ()
            z = cartesian.getK()

            # Use temporary variables for computing R.
            big = max(abs(y), abs(z))

            # Convert to cylindrical coordinates
            height = x
            cylindricalRadius = 0
            longitude = 0
            if big == 0:
                cylindricalRadius = 0
                longitude = 0
            else:
                y = y/big
                z = z/big
                cylindricalRadius = big*sqrt(y*y + z*z)
                longitude = atan2(z, y)
            if longitude < 0:
                longitude += FundamentalPhysicalConstants.TWOPI
            return CylindricalVector(cylindricalRadius, longitude, height)
        elif isinstance(args[0], CylindricalVector):
            (cyl,) = args
            # Converts a cylindrical coordinate to Cartesian coordinate
            # @param cyl a CylindricalVector holding the cylindrical coordinate
            # @return a UnwritableVectorIJK holding the Cartesian coordinate
            x = cyl.getHeight()
            phi = cyl.getLongitude()
            rho = cyl.getCylindricalRadius()
            y = rho*cos(phi)
            z = rho*sin(phi)
            return UnwritableVectorIJK(x, y, z)
        else:
            raise Exception

    @staticmethod
    def convertFieldValue(*args):
        if (isinstance(args[0], UnwritableVectorIJK) and
            isinstance(args[1], UnwritableVectorIJK)):
            # Converts a Cartesian vector field value to a cylindrical vector
            # field value
            # @param cartesian the Cartesian coordinate
            # @param field the Cartesian field value at that coordinate
            # @return the cylindrical vector field value
            (cartesian, field) = args
            y = cartesian.getJ()
            z = cartesian.getK()
            bx = field.getI()
            by = field.getJ()
            bz = field.getK()
            rho = sqrt(y*y + z*z)
            cosPhi = y/rho
            sinPhi = z/rho
            if rho == 0:
                cosPhi = 1.0
                sinPhi = 0.0
            brho = cosPhi*by + sinPhi*bz
            bphi = -sinPhi*by + cosPhi*bz
            return CylindricalVector(brho, bphi, bx)
        elif (isinstance(args[0], CylindricalVector) and
              isinstance(args[1], CylindricalVector)):
            # Converts a cylindrical vector field value to a Cartesian vector
            # field value
            # @param pos the cylindrical coordinate
            # @param field the cylindrical field value at that coordinate
            # @return the Cartesian vector field value
            (pos, field) = args
            phi = pos.getLongitude()
            brho = field.getCylindricalRadius()
            bphi = field.getLongitude()
            bx = field.getHeight()
            cosPhi = cos(phi)
            sinPhi = sin(phi)
            by = cosPhi*brho - sinPhi*bphi
            bz = sinPhi*brho + cosPhi*bphi
            return UnwritableVectorIJK(bx, by, bz)
        else:
            raise Exception

    @staticmethod
    def convertBasisField(*args):
        if isinstance(args[0], UnwritableVectorIJK):
            (cartesian,) = args
            # Converts a Cartesian BasisVectorField to a CylindricalBasisVectorField
            # @param cartesian a Cartesian BasisVectorField
            # return a newly constructed CylindricalBasisVectorField
            #   public static CylindricalBasisVectorField
            # convertBasisField(BasisVectorField cartesian) {
            cylbvf = CylindricalBasisVectorField(cartesian)
            #     return new CylindricalBasisVectorField() {

            #       @Override
            #       public CylindricalVector evaluate(CylindricalVector location) {

            #         // convert the coordinate to Cartesian
            #         UnwritableVectorIJK locCart = convert(location);

            #         // evaluate the Cartesian field
            #         UnwritableVectorIJK fieldCart = cartesian.evaluate(locCart);

            #         // convert the field to cylindrical
            #         return convertFieldValue(locCart, fieldCart);
            #       }
        elif isinstance(args[0], CylindricalBasisVectorField):
            (cylField,) = args
            #   /**
            #    * Converts a Cartesian {@link BasisVectorField} to a {@link CylindricalBasisVectorField}
            #    * 
            #    * @param cartesian a Cartesian {@link BasisVectorField}
            #    * @return a newly constructed {@link CylindricalBasisVectorField}
            #    */
            #   public static BasisVectorField convertBasisField(CylindricalBasisVectorField cylField) {

            #     return new BasisVectorField() {
        else:
            raise Exception

    @staticmethod
    def convertField(cartesian):
        pass
        #   /**
        #    * Converts a Cartesian {@link VectorField} to a {@link CylindricalVectorField}
        #    * 
        #    * @param cartesian a Cartesian {@link VectorField}
        #    * @return a newly constructed {@link CylindricalVectorField}
        #    */
        #   public static CylindricalVectorField convertField(VectorField cartesian) {

        #     return new CylindricalVectorField() {

        #       // CylindricalVectorField has a default method that evaluates the Cartesian field, we must
        #       // override that method here because otherwise the conversion will go through the standard +Z
        #       // aligned conversion
        #       @Override
        #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
        #         return cartesian.evaluate(location, buffer);
        #       }

        #   /**
        #    * Converts a {@link CylindricalVectorField} to a Cartesian {@link VectorField}
        #    * 
        #    * @param cylField a {@link CylindricalVectorField}
        #    * @return a newly constructed Cartesian {@link VectorField}
        #    */
        #   public static VectorField convertField(CylindricalVectorField cylField) {

        #     return new VectorField() {

        #       @Override
        #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {

        #         CylindricalVector locSphere = convert(location);
                
        #         CylindricalVector fieldSphere = cylField.evaluate(locSphere);
                
        #         UnwritableVectorIJK fieldValue = convertFieldValue(locSphere, fieldSphere);

        #         buffer.setTo(fieldValue);

        #         return buffer;
        #       }

        #     };

        #   }

        # }

    def evaluateExpansion(self, location):
        pass
        #       @Override
        #       public ImmutableList<CylindricalVector> evaluateExpansion(CylindricalVector location) {

        #         // convert the coordinate to Cartesian
        #         UnwritableVectorIJK locCart = convert(location);

        #         // evaluate the Cartesian field
        #         ImmutableList<UnwritableVectorIJK> fieldCartExpansion =
        #             cartesian.evaluateExpansion(locCart);

        #         ImmutableList.Builder<CylindricalVector> fieldCylExpansion = ImmutableList.builder();

        #         for (UnwritableVectorIJK fieldCart : fieldCartExpansion) {
        #           fieldCylExpansion.add(convertFieldValue(locCart, fieldCart));
        #         }

        #         return fieldCylExpansion.build();
        #       }

        #       @Override
        #       public ImmutableList<UnwritableVectorIJK> evaluateExpansion(UnwritableVectorIJK location) {

        #         CylindricalVector locCyl = convert(location);

        #         ImmutableList<CylindricalVector> fieldCylExpansion = cylField.evaluateExpansion(locCyl);

        #         ImmutableList.Builder<UnwritableVectorIJK> fieldExpansion = ImmutableList.builder();

        #         for (CylindricalVector fieldCyl : fieldCylExpansion) {
        #           fieldExpansion.add(convertFieldValue(locCyl, fieldCyl));
        #         }

        #         return fieldExpansion.build();
        #       }

    def getNumberOfBasisFunctions(self):
        pass
        #       @Override
        #       public int getNumberOfBasisFunctions() {
        #         return cartesian.getNumberOfBasisFunctions();
        #       }

        #     };

        #   }

        #       @Override
        #       public int getNumberOfBasisFunctions() {
        #         return cylField.getNumberOfBasisFunctions();
        #       }

        #     };

        #   }


    def evaluate(self, location):
        pass
        #       @Override
        #       public CylindricalVector evaluate(CylindricalVector location) {

        #         // convert the coordinate to Cartesian
        #         UnwritableVectorIJK locCart = convert(location);

        #         // evaluate the Cartesian field
        #         UnwritableVectorIJK fieldCart = cartesian.evaluate(locCart);

        #         // convert the field to cylindrical
        #         return convertFieldValue(locCart, fieldCart);
        #       }
        #     };

        #   }
