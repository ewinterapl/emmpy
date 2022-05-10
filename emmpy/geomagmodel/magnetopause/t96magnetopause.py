"""Compute the magnetopause according to the T96 model.

An implementation of the T96 magnetopause as described in Tsyganenko (1995)
[https://doi.org/10.1029/94JA03193]. The T96 magnetopause model was constructed
using an ellipsoid, described using the following equations (eq. (1) from
above):

    X = x0 - a(1 - s*t)
    Y = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * cos(phi)
    Z = a(s0^2 - 1)^.5 * (1 - t^2)^.5 * sin(phi)

connected to a cylinder. See Fig. 2 from the above paper.

This model was later adapted by fitting its ellipsoidal part to the Shue et al
(1998) model [https://doi.org/10.1029/98JA01103], as described in
Tsyganenko (2002) [https://doi.org/10.1029/2001JA000219]. This magnetopause
boundary would become the basis for other the T01, TS05, and TS07D models.

Specifically, this class is equivalent the T96_MGNP_08 subroutine contained in
the Geopack code.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# Import standard modules.
from math import atan2, cos, sin, sqrt

# Import 3rd-party modules.
import numpy as np

# Import project modules.
from emmpy.geomagmodel.magnetopause.magnetopauseoutput import (
    MagnetopauseOutput
)
from emmpy.geomagmodel.t01.deformation.positionbender import PositionBender
from emmpy.geomagmodel.t01.deformation.twistwarpffunction import (
    TwistWarpFfunction
)
from emmpy.math.coordinates.vectorijk import VectorIJK


# Program constants.

# Nominal pressure used to scale the magnetopause (nPa)
averagePressure = 2.0


class T96Magnetopause:
    """Compute the magnetopause according to the T96 model.

    Attributes
    ----------
    scaledA0 : float
        XXX
    sigma0 : float
        XXX
    scaledX0 : float
        XXX
    XM : float
        Center of the ellipsoid
    semiMinorAxis : float
        XXX
    """

    def __init__(self, dynamicPressure, a0, sigma0, x00, scalingPowerIndex):
        """Initialize a new T96Magnetopause object.

        Initialize a new T96Magnetopause object.

        Parameters
        ----------
        dynamicPressure : float
            Solar wind dynamic pressure (nPa)
        a0 : float
            XXX
        sigma0 : float
            XXX
        x00 : float
            XXX
        scalingPowerIndex : float
            Referred to as Kappa in the literature.

        Returns
        -------
        None
        """

        # Compute the ratio of the dynamic pressure to the average pressure.
        pdynRatio = dynamicPressure/averagePressure

        # Scale the magnetopause parameters.
        scalingFactor = pow(pdynRatio, scalingPowerIndex)
        self.scaledA0 = a0/scalingFactor
        self.sigma0 = sigma0
        self.scaledX0 = x00/scalingFactor
        self.XM = self.scaledX0 - self.scaledA0
        self.semiMinorAxis = self.scaledA0*sqrt((sigma0**2 - 1))

    def evaluate(self, positionGSM):
        """Evaluate the magnetopause model.

        For any point in space (xgsw, ygsw, zgsw), compute the position of a
        point (xmgnp, ymgnp, zmgnp) at the T96 model magnetopause with the
        same value of the ellipsoidal tau-coordinate, and the distance between
        them. This is not the shortest distance d_min to the boundary, but this
        distance asymptotically approaches d_min, as the observation point gets
        closer to the magnetopause.

        The pressure-dependent magnetopause is that used in the T96_01 model
        as described in Tsyganenko, JGR 100, p. 5599 (1995), and
        ESA SP-389, p. 181, Oct. 1996.

        Original code by N.A. Tsyganenko, 1 August 1995, revised 3 April 2003.

        Parameters
        ----------
        positionGSM : VectorIJK
            Position in GSM coordinates.

        Returns
        -------
        mo : MagnetopauseOutput
            Results of magnetopause calculations.
        """
        # Extract the position coordinates.
        xGsw = positionGSM.i
        yGsw = positionGSM.j
        zGsw = positionGSM.k

        # XM is the x-coordinate of the seam between the ellipsoid and the
        # cylinder. For details of the ellipsoidal coordinates, see
        # N.A. Tsyganenko, "Solution of Chapman-Ferraro Problem for an
        # Ellipsoidal Magnetopause", Planetary and Space Science v37,
        # p1037 (1989)
        phiGsw = 0.0
        if yGsw != 0 or zGsw != 0:
            phiGsw = atan2(yGsw, zGsw)
        rhoGsw = sqrt(yGsw**2 + zGsw**2)
        withinMagnetosphere = False
        magnetopauseLocation = None

        if xGsw < self.XM:
            # We are in the tailward of the ellipsoid center, so the
            # magnetopause is defined using the cylinder.
            xMgnp = xGsw
            yMgnp = self.semiMinorAxis*sin(phiGsw)
            zMgnp = self.semiMinorAxis*cos(phiGsw)
            # The magnetopause is outside of where we are, so we are in the
            # magnetosphere.
            if self.semiMinorAxis > rhoGsw:
                withinMagnetosphere = True
            magnetopauseLocation = VectorIJK(xMgnp, yMgnp, zMgnp)
        else:
            # Otherwise, we are in the ellipse region.
            XKSI = (xGsw - self.scaledX0)/self.scaledA0 + 1
            XDZT = rhoGsw/self.scaledA0
            sq1 = sqrt((1.0 + XKSI)*(1 + XKSI) + XDZT**2)
            sq2 = sqrt((1.0 - XKSI) * (1 - XKSI) + XDZT**2)
            sigma = 0.5*(sq1 + sq2)
            tau = 0.5*(sq1 - sq2)

            # Now calculate (X,Y,Z) for the closest point on the magnetopause.
            xMgnp = self.scaledX0 - self.scaledA0*(1 - self.sigma0*tau)
            arg = (self.sigma0**2 - 1)*(1 - tau**2)
            if arg < 0:
                arg = 0.0
            rhoMagnetopause = self.scaledA0*sqrt(arg)
            yMgnp = rhoMagnetopause*sin(phiGsw)
            zMgnp = rhoMagnetopause*cos(phiGsw)
            if sigma > self.sigma0:
                withinMagnetosphere = False
            if sigma <= self.sigma0:
                withinMagnetosphere = True
            magnetopauseLocation = VectorIJK(xMgnp, yMgnp, zMgnp)

        # Now compute the distance between the points (xGsw, yGsw, zGsw) and
        # (xMgnp, yMgnp, zMgnp).
        distance = np.linalg.norm(positionGSM - magnetopauseLocation)

        return MagnetopauseOutput(magnetopauseLocation, distance, withinMagnetosphere)

    def apply(self, positionGSM):
        """Check if a point is within the magnetosphere.

        Check if a point is within the magnetosphere.

        Parameters
        ----------
        positionGSM : VectorIJK
            Position in GSM coordinates.

        Returns
        -------
        mo.isWithinMagnetosphere : bool
            True if the position is inside the magnetopause, otherwise False.
        """
        mo = self.evaluate(positionGSM)
        return mo.withinMagnetosphere


    @staticmethod
    def createGeopack(dynamicPressure):
        """Construct the Geopack-equivalent T96 magnetopause model.

        Construct the T96 magnetopause model consistent with the T96_MGNP_08
        subroutine from Geopack.

        Note: This does not apply the dipole tilt angle deformation effects.

        Parameters
        ----------
        dynamicPressure : float
            Solar wind dynamic pressure (nPa)

        Returns
        -------
        t96mp : T96Magnetopause
            A new T96 magnetopause model.
        """
        # These values are very similar to those given in the T96 paper:
        # x0 = 5.48 RE, a = 70.48 RE, sigma0 = 1.078, see eq. (2).
        A0 = 70.0
        sigma0 = 1.08
        X00 = 5.48

        # The value used in the T96 model, see the second T96 paper, section 3.1.
        # This value was determined by a best fit to data.
        scalingPowerIndex = 0.14

        # Create the new model.
        t96mp =  T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex)
        return t96mp

    @staticmethod
    def createTS07(dynamicPressure):
        """Construct the TS07-equivalent T96 magnetopause model.

        Construct the T96 magnetopause model consistent with the TS07D model.

        Note: This does not apply the dipole tilt angle deformation effects.

        Parameters
        ----------
        dynamicPressure : float
            Solar wind dynamic pressure (nPa)

        Returns
        -------
        t96mp : T96Magnetopause
            A new T96 magnetopause model.
        """
        # These values originate in the T01 model source code. They are similar
        # (although not quite the same) as those given in the first T01 paper
        # [https://doi.org/2001JA000219, section 2.4]:

        # x0 = 3.486, sigma0 = 1.198, a = 35.13

        # According to the paper they were "... derived by fitting the surface
        # (equation (26)) to an average boundary of Shue et al. [1998]". These
        # values were also used in the TS05 model and the TS07 model.
        A0 = 34.586
        sigma0 = 1.1960
        X00 = 3.4397

        # The value used in the TS07D model, very similar to that used in the
        # TS05 model (0.152759)
        scalingPowerIndex = 0.155

        # Create the new model.
        t96mp =  T96Magnetopause(dynamicPressure, A0, sigma0, X00, scalingPowerIndex)
        return t96mp

    @staticmethod
    def createBentTS07(dynamicPressure, dipoleTiltAngle, hingeDist, warpParam,
                       twistFact):
        """Create a model with the dipole tilt angle deformation.
        
        Create a model with the dipole tilt angle deformation. This method
        creates a standard T96Magnetopause object, then modifies it by
        replacing the apply() method with a custom version.

        Parameters
        ----------
        dynamicPressure : float
            Solar wind dynamic pressure (nPa).
        dipoleTiltAngle : float
            Dipole tilt angle in (radians).
        hingeDist : float
            Hinging distance RH as defined in the TS07D model.
        warpParam : float
            Warping parameter G as defined in the TS07D model.
        twistFact : float
            Twisting parameter T as defined in the TS07D model.

        Returns
        -------
        t96mp : T96Magnetopause
            New T96Magnetopause obejct for the dipole-tilted model.
        """
        bender = PositionBender(dipoleTiltAngle, hingeDist)
        warper = TwistWarpFfunction(warpParam, twistFact, dipoleTiltAngle)

        # The value from TS05 according to the Fortran source.
        scalingPowerIndex = 0.155

        pdynScaling = pow(averagePressure, scalingPowerIndex)

        # Create the model object.
        unbent = T96Magnetopause.createTS07(averagePressure)

        # Create the custom apply method.
        def my_apply(location):
            pdynScaledLocation = pdynScaling*VectorIJK(location)
            buffer = VectorIJK()
            bentLocation = bender.evaluate(pdynScaledLocation, buffer)
            bentWarpedLocation = warper.evaluate(bentLocation, buffer)
            return unbent.apply(bentWarpedLocation)
        unbent.apply = my_apply

        return unbent
