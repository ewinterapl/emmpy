"""Direct Python port of ModelRunApp.java"""


import sys

from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
# from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
# from emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils import (
#     TS07DVariableCoefficientsUtils
# )
from emmpy.geomagmodel.ts07.modeling.equatorial.currentsheethalfthicknesses import (
    CurrentSheetHalfThicknesses
)
# from emmpy.geomagmodel.ts07.ts07dmodelbuilder import TS07DModelBuilder
# from emmpy.magmodel.core.math.bessel.albertbesselfunctionevaluator import (
#     AlbertBesselFunctionEvaluator
# )
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)
from emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield import (
    ThinAsymmetricCurrentSheetBasisVectorField
)


def ModelRunApp():
    print("Starting ModelRunApp()")
    runThinSheet()
    # runTs07D()
    print("Ending ModelRunApp()")


def runThinSheet():
    """Builds and runs the thin sheet model"""
    print("Starting runThinSheet()")

    # use a resolution of (M,N)=(4,5)
    numAz = 4
    numRad = 5

    # the standard value of rho0
    tailLength = 20.0

    # a typical value of D
    currSheetThick = 2.3

    # Construct a constant current sheet half thickness
    currentSheetHalfThickness = (
        CurrentSheetHalfThicknesses.createConstant(currSheetThick)
    )

    # Set all the linear coeffs to 1.0
    coeffs = TailSheetCoefficients.createUnity(numAz, numRad)

    # # use Jay Albert's Bessel function evaluator
    # bessel = AlbertBesselFunctionEvaluator(14)
    bessel = None

    # now construct the thin sheet field model
    model = ThinAsymmetricCurrentSheetBasisVectorField(
        tailLength, currentSheetHalfThickness, coeffs, bessel
    )

    # evaluate the model at r=(4,5,-2)
    pos = UnwritableVectorIJK(4.0, 5.0, -2.0)

#     # evaluate the magnetic field
#     bVect = model.evaluate(pos)
#     print(bVect.toString())

    print("Ending runThinSheet()")


# def runTs07D():
#     """Builds and runs the TS07D model"""
#     print("Starting runTs07D()")

#     # use a coeffs file from the March 2015 St. Patty's Day storm
#     coeffsFile = "/Users/winteel1/mag/2015_076_16_20.par"

#     # read the coeffs/parameters from the file
#     coeffs = TS07DVariableCoefficientsUtils.create(coeffsFile)

#     # read the dipole tilt angle and dynamic pressure from the coeffs file
#     dipoleTilt = TS07DVariableCoefficientsUtils.readDipoleTiltAngle(coeffsFile)
#     pDyn = TS07DVariableCoefficientsUtils.readDynamicPressure(coeffsFile)

#     # construct the model builder
#     modelBuilder = TS07DModelBuilder.create(dipoleTilt, pDyn, coeffs)

#     # optional setting to use Jay Albert's Bessel function evaluator
#     modelBuilder.withAlbertBessel()

#     # now construct the TS07D model
#     model = modelBuilder.build()

#     # evaluate the model at r=(4,5,-2)
#     pos = UnwritableVectorIJK(4.0, 5.0, -2.0)

#     # evaluate the magnetic field
#     # TEMPORARY BUFFER - REMOVE LATER.
#     buffer = VectorIJK()
#     bVect = model.evaluate(pos, buffer)
#     print(bVect)

#     print("Ending runTs07D()")


if __name__ == "__main__":
    args = sys.argv
    print("Starting main()")
    ModelRunApp()
    print("Ending main()")
