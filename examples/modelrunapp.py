"""Direct Python port of ModelRunApp.java."""


import sys

import numpy as np

from emmpy.crucible.crust.vectorfieldsij.differentiablescalarfieldij import (
    DifferentiableScalarFieldIJ
)
from emmpy.geomagmodel.ts07.coefficientreader.ts07dvariablecoefficientsutils import (
    TS07DVariableCoefficientsUtils
)
from emmpy.geomagmodel.ts07.ts07dmodelbuilder import TS07DModelBuilder
from emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetcoefficients import (
    TailSheetCoefficients
)
from emmpy.magmodel.core.modeling.equatorial.expansion.thinasymmetriccurrentsheetbasisvectorfield import (
    ThinAsymmetricCurrentSheetBasisVectorField
)
from emmpy.math.coordinates.cartesianvector import CartesianVector


def ModelRunApp(coeffsFile):
    """Run the models."""
    runThinSheet()
    runTs07D(coeffsFile)


def runThinSheet():
    """Build and run the thin sheet model."""

    # use a resolution of (M,N)=(4,5)
    numAz = 4
    numRad = 5

    # the standard value of rho0
    tailLength = 20.0

    # a typical value of D
    currSheetThick = 2.3

    # Construct a constant current sheet half thickness
    currentSheetHalfThickness = DifferentiableScalarFieldIJ.createConstant(
        currSheetThick
    )

    # Set all the linear coeffs to 1.0
    coeffs = TailSheetCoefficients.createUnity(numAz, numRad)

    # now construct the thin sheet field model
    model = ThinAsymmetricCurrentSheetBasisVectorField(
        tailLength, currentSheetHalfThickness, coeffs
    )

    # evaluate the model at r=(4,5,-2)
    pos = CartesianVector(4.0, 5.0, -2.0)

    # evaluate the magnetic field
    bVect = model.evaluate(pos)
    print(bVect)

    # Check the computed values against the expected values.
    bVect_ref = CartesianVector(-0.47654433563669696, 2.0705600362600864,
                                1.5889255378262552)
    for i in range(len(bVect)):
        if not np.isclose(bVect[i], bVect_ref[i]):
            print("bVect[%d] is wrong: %s != %s!" %
                  (i, bVect[i], bVect_ref[i])
            )


def runTs07D(coeffsFile):
    """Build and run the TS07D model."""

    # read the coeffs/parameters from the file
    coeffs = TS07DVariableCoefficientsUtils.create(coeffsFile)

    # read the dipole tilt angle and dynamic pressure from the coeffs file
    dipoleTilt = TS07DVariableCoefficientsUtils.readDipoleTiltAngle(coeffsFile)
    pDyn = TS07DVariableCoefficientsUtils.readDynamicPressure(coeffsFile)

    # construct the model builder
    modelBuilder = TS07DModelBuilder.create(dipoleTilt, pDyn, coeffs)

    # now construct the TS07D model
    model = modelBuilder.build()

    # evaluate the model at r=(4,5,-2)
    pos = CartesianVector(4.0, 5.0, -2.0)

    # evaluate the magnetic field
    bVect = model.evaluate(pos)
    print(bVect)

    # Check the computed values atoxgainst the expected values.
    # These reference values were generated by the Java code.
    bVect_ref = CartesianVector(18.11269495223987, 19.89715571940947,
                                17.20252488064584)
    for i in range(len(bVect_ref)):
        if not np.isclose(bVect[i], bVect_ref[i]):
            print("bVect[%d] is wrong: %s != %s!" %
                  (i, bVect[i], bVect_ref[i])
            )


if __name__ == "__main__":
    coeffsFile = sys.argv[1]
    ModelRunApp(coeffsFile)
