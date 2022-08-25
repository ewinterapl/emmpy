"""Cylindrical coordinates aligned along the X-axis."""


from math import atan2, cos, pi, sin, sqrt
from emmpy.math.coordinates.cartesianvector import CartesianVector

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.vectorijk import VectorIJK


class CylindricalCoordsXAligned:
    """Cylindrical coordinates aligned along the X-axis."""

    @staticmethod
    def convert(vector):
        """Convert between Cartesian and X-aligned cylindrical coordinates.

        If the input vector is Cartesian, convert it to x-aligned
        cylindrical. If cylindrical, assume it is x-aligned cyliindrical
        and convert it to Cartesian.

        Parameters
        ----------
        vector : VectorIJK or CylindricalVector
            Vector to convert.

        Returns
        -------
        convertedVector : CylindricalVector or VectorIJK
            The converted vector.

        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if isinstance(vector, CartesianVector):
            # Convert from Cartesian coordinates ...
            x = vector.x
            y = vector.y
            z = vector.z
            # ... to x-aligned cylindrical coordinates.
            rho = sqrt(y**2 + z**2)
            phi = atan2(z, y)
            if phi < 0:
                phi += 2*pi
            cyl_z = x
            convertedVector = CylindricalVector(rho, phi, cyl_z)
        elif isinstance(vector, CylindricalVector):
            # Convert from x-aligned cylindrical coordinates ...
            rho = vector.rho
            phi = vector.phi
            cyl_z = vector.z
            # ... to Cartesian coordinates.
            x = cyl_z
            y = rho*cos(phi)
            z = rho*sin(phi)
            convertedVector = CartesianVector(x, y, z)
        else:
            raise TypeError
        return convertedVector

    @staticmethod
    def convertFieldValue(position, value):
        """Convert field values between Cartesian and X-aligned cylindrical.

        If the input position is in Cartesian coordinates, convert the
        value vector from Cartesian to x-aligned cylindrical. If the input
        position is in x-aligned cylindrical, convert the value from
        x-aligned cylindrical to Cartesian.

        Parameters
        ----------
        position, value : VectorIJK or CylindricalVector
            Vector position and value to convert.

        Returns
        -------
        convertedValue: CylindricalVector or VectorIJK
            Converted vector value.

        Raises
        ------
        TypeError
            If incorrect parameters are provided.
        """
        if isinstance(position, CartesianVector):
            # Convert from Cartesian coordinates ...
            y = position.y
            z = position.z
            vx = value.x
            vy = value.y
            vz = value.z
            # ... to x-aligned cylindrical coordinates.
            rho = sqrt(y**2 + z**2)
            if rho == 0:
                cosPhi = 1.0
                sinPhi = 0.0
            else:
                cosPhi = y/rho
                sinPhi = z/rho
            vrho = cosPhi*vy + sinPhi*vz
            vphi = -sinPhi*vy + cosPhi*vz
            convertedValue = CylindricalVector(vrho, vphi, vx)
        elif isinstance(position, CylindricalVector):
            # Convert from x-aligned cylindrical coordinates ...
            rho = position.rho
            phi = position.phi
            v_rho = value.rho
            v_phi = value.phi
            v_x = value.z
            cosPhi = cos(phi)
            sinPhi = sin(phi)
            # ... to Cartesian coordinates.
            vx = v_x
            vy = cosPhi*v_rho - sinPhi*v_phi
            vz = sinPhi*v_rho + cosPhi*v_phi
            convertedValue = VectorIJK(vx, vy, vz)
        else:
            raise TypeError
        return convertedValue

    @staticmethod
    def convertBasisField(basisVectorField):
        """Convert a BVF between Cartesian and x-aligned cylindrical.

        Convert a basis vector field between Cartesian coordinates and
        x-aligned cylindrical coordinates.

        Parameters
        ----------
        basisVectorField : CylindricalBasisVectorField or BasisVectorField
            The basis vector field to convert.

        Returns
        -------
        converted_bvf : BasisVectorField or CylindricalBasisVectorField
            The converted basis vector field.

        Raises
        ------
        TypeError
            If incorrect parameters are provided.
        """
        if isinstance(basisVectorField, CylindricalBasisVectorField):
            # Convert from x-aligned cylindrical coordinates to Cartesian
            # coordinates using a custom object.
            cyl_bvf = basisVectorField
            cart_bvf = BasisVectorField()

            def my_evaluateExpansion(location):
                locCyl = CylindricalCoordsXAligned.convert(CartesianVector(location))
                fieldCylExpansion = cyl_bvf.evaluateExpansion(locCyl)
                fieldExpansion = []
                for fieldCyl in fieldCylExpansion:
                    fieldExpansion.append(
                        CylindricalCoordsXAligned.convertFieldValue(
                            locCyl, fieldCyl
                        )
                    )
                return fieldExpansion
            cart_bvf.evaluateExpansion = my_evaluateExpansion
            cart_bvf.getNumberOfBasisFunctions = (
                lambda: cyl_bvf.getNumberOfBasisFunctions()
            )
            converted_bvf = cart_bvf
        elif isinstance(basisVectorField, BasisVectorField):
            # Convert from Cartesian coordinates to x-aligned cylindrical
            # coordinates using a custom object.
            cart_bvf = basisVectorField
            cyl_bvf = CylindricalBasisVectorField()

            def my_evaluate(cylindricalLocation):
                cartesianLocation = CylindricalCoordsXAligned.convert(
                    cylindricalLocation)
                cartesianValue = cart_bvf.evaluate(cartesianLocation)
                cylindricalValue = CylindricalCoordsXAligned.convertFieldValue(
                    cartesianLocation, cartesianValue)
                return cylindricalValue
            cyl_bvf.evaluate = my_evaluate

            def my_evaluateExpansion(location):
                cylindricalLocation = location
                cartesianLocation = CylindricalCoordsXAligned.convert(
                    cylindricalLocation)
                cartesianExpansion = cart_bvf.evaluateExpansion(
                    cartesianLocation
                )
                cylindricalExpansion = []
                for fieldCart in cartesianExpansion:
                    cylindricalExpansion.append(
                        CylindricalCoordsXAligned.convertFieldValue(
                            CartesianVector(cartesianLocation), CartesianVector(fieldCart)))
                return cylindricalExpansion
            cyl_bvf.evaluateExpansion = my_evaluateExpansion
            cyl_bvf.getNumberOfBasisFunctions = (
                lambda: cart_bvf.getNumberOfBasisFunctions()
            )
            converted_bvf = cyl_bvf
        else:
            raise TypeError
        return converted_bvf
