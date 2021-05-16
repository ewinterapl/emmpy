"""emmpy.magmodel.core.math.coords.cylindricalcoordsxaligned"""


from math import atan2, cos, sin, sqrt

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.units.fundamentalphysicalconstants import (
    FundamentalPhysicalConstants
)
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)
from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
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
        if isinstance(args[0], BasisVectorField):
            (cartesian,) = args
            # Converts a Cartesian BasisVectorField to a CylindricalBasisVectorField
            # param cartesian a Cartesian BasisVectorField
            # return a newly constructed CylindricalBasisVectorField
            cylbvf = CylindricalBasisVectorField()

            def my_evaluate(location):
                # CylindricalVector location

                # convert the coordinate to Cartesian
                # UnwritableVectorIJK
                locCart = CylindricalCoordsXAligned.convert(location)

                #  evaluate the Cartesian field
                # UnwritableVectorIJK
                fieldCart = cartesian.evaluate(locCart)

                # convert the field to cylindrical
                return CylindricalCoordsXAligned.convertFieldValue(
                    locCart, fieldCart)
            cylbvf.evaluate = my_evaluate

            def my_evaluateExpansion(location):
                # CylindricalVector location

                # convert the coordinate to Cartesian
                # UnwritableVectorIJK
                locCart = CylindricalCoordsXAligned.convert(location)

                # evaluate the Cartesian field
                # list
                fieldCartExpansion = (
                    CylindricalCoordsXAligned.cartesian.evaluateExpansion(
                        locCart)
                )
                fieldCylExpansion = []
                # UnwritableVectorIJK fieldCart
                for fieldCart in fieldCartExpansion:
                    fieldCylExpansion.append(
                        CylindricalCoordsXAligned.convertFieldValue(
                            locCart, fieldCart))
                return fieldCylExpansion
            cylbvf = my_evaluateExpansion

            cylbvf.getNumberOfBasisFunctions = (
                lambda: cartesian.getNumberOfBasisFunctions()
            )
            return cylbvf

        elif isinstance(args[0], CylindricalBasisVectorField):
            (cylField,) = args
            # Converts a CylindricalBasisVectorField to a Cartesian
            # BasisVectorField
            # param cylField a CylindricalBasisVectorField
            # return a newly constructed Cartesian BasisVectorField
            bvf = BasisVectorField()
            def my_evaluateExpansion(location):
                # param UnwritableVectorIJK location
                # return ImmutableList<UnwritableVectorIJK>
                locCyl = CylindricalCoordsXAligned.convert(location)
                fieldCylExpansion = cylField.evaluateExpansion(locCyl)
                fieldExpansion = []
                for fieldCyl in fieldCylExpansion:
                    fieldExpansion.append(
                        CylindricalCoordsXAligned.convertFieldValue(
                            locCyl, fieldCyl
                        )
                )
                return fieldExpansion
            bvf.evaluateExpansion = my_evaluateExpansion
            bvf.getNumberOfBasisFunctions = (
                lambda: cylField.getNumberOfBasisFunctions()
            )
            return bvf
        else:
            raise Exception

    @staticmethod
    def convertField(cartesian):
        """Converts a Cartesian VectorField to a CylindricalVectorField

        param cartesian a Cartesian VectorField
        return a newly constructed CylindricalVectorField
        """
        cvf = CylindricalVectorField()
        # CylindricalVectorField has a default method that evaluates the
        # Cartesian field, we must override that method here because otherwise
        # the conversion will go through the standard +Z  aligned conversion
        def my_evaluate(*args):
            if len(args) == 1:
                (location,) = args
                # convert the coordinate to Cartesian
                locCart = CylindricalCoordsXAligned.convert(location)
                # evaluate the Cartesian field
                fieldCart = cartesian.evaluate(locCart)
                # convert the field to cylindrical
                return CylindricalCoordsXAligned.convertFieldValue(
                    locCart, fieldCart)
            elif len(args) == 2:
                (location, buffer) = args
                return cartesian.evaluate(location, buffer)
            else:
                raise Exception
        cvf.evaluate = my_evaluate
        return cvf

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
