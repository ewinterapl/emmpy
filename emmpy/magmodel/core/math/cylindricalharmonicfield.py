"""emmpy.magmodel.core.math.cylindricalharmonicfield"""


from math import cosh, sinh

from scipy.special import jv

from emmpy.magmodel.core.chebysheviteration import ChebyshevIteration
from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.magmodel.core.math.vectorfields.basisvectorfield import (
    BasisVectorField
)
from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds


class CylindricalHarmonicField(BasisVectorField):
    """A vector field that is associated with the scalar potential solution of
    Laplace's equation in Cylindrical coordinates.

    Uses a Fourier-Bessel expansion representation, e.q. from TS07 eq. 20:

    Evaluates <b>F</b> = -&#x2207;U = &#931; &#931; <b>F</b><sub>mn</sub>=-&#931; &#931; &#x2207; U<sub>mn</sub>
                        m n      m n

    where:

       U<sub>mn</sub> = c<sub>mn</sub>J<sub>m</sub>(k<sub>n</sub>&#961;){sin(m&#966;)}sinh(k<sub>n</sub>z)
                     {cos(m&#966;)}

       the cos(m&#966;) is even parity and sin(m&#966;) is odd parity
       J<sub>m</sub> are Bessel functions

    </pre>

    author G.K.Stephens
    """

    # float invMaxVal
    invMaxVal = pow(10.0, 8.0)

    def __init__(self, coefficientsExpansion, waveNumberExpansion, bessel,
                 trigParity):
        """Constructs a shielding Fourier-Bessel expansion of the form:

        <p>
        <img src="doc-files/cylindricalHarmonicSol2.png" />
        <p>

        param CoefficientExpansion2D coefficientsExpansion an expansion
        containing the linear scaling coefficients (c<sub>mn</sub>)
        param CoefficientExpansion1D waveNumberExpansion an expansion
        containing the non-linear wave numbers (k<sub>n</sub>)
        param BesselFunctionEvaluator bessel evaluates the Bessel function
        <J<sub>m</sub>
        param TrigParity trigParity is this of the sine or cosine variety
        """
        # CoefficientExpansion2D coefficientsExpansion
        self.coefficientsExpansion = coefficientsExpansion
        # CoefficientExpansion1D waveNumberExpansion
        self.waveNumberExpansion = waveNumberExpansion
        # BesselFunctionEvaluator bessel
        self.bessel = bessel
        # firstM, lastM, firstN, lastN
        self.firstM = coefficientsExpansion.getILowerBoundIndex()
        self.lastM = coefficientsExpansion.getIUpperBoundIndex()
        self.firstN = coefficientsExpansion.getJLowerBoundIndex()
        self.lastN = coefficientsExpansion.getJUpperBoundIndex()
        # TrigParity trigParity
        self.trigParity = trigParity

    def evaluateExpansion2D(self, location):
        """Returns the full expansion results.

        param UnwritableVectorIJK location
        return Expansion2D<UnwritableVectorIJK>
        """
        # UnwritableVectorIJK[][] expansions
        expansions = []
        for i in range(self.coefficientsExpansion.iSize()):
            expansions.append([])
            for j in range(self.coefficientsExpansion.jSize()):
                expansions[i].append(None)
        # float x, y
        x = location.getI()
        y = location.getJ()
        # CylindricalVector cylindricalLocation
        cylindricalLocation = CoordConverters.convertToCylindrical(location)
        # float rho, phi, z
        rho = cylindricalLocation.getCylindricalRadius()
        phi = cylindricalLocation.getLongitude()
        z = cylindricalLocation.getHeight()

        # Precompute the sin(m*phi) and cos(m*phi), this greatly speeds up the
        # code.
        # float[] sinMphis, cosMphis
        sinMphis = [None]*(self.lastM + 1)
        cosMphis = [None]*(self.lastM + 1)
        ChebyshevIteration.evaluateTrigExpansions(phi, sinMphis, cosMphis,
                                                  self.trigParity)
        for n in range(self.firstN, self.lastN + 1):

            # the wave number
            # float kn, rhoK, coshKZ, sinhKZ
            kn = abs(self.waveNumberExpansion.getCoefficient(n))
            rhoK = rho*kn
            coshKZ = cosh(z*kn)
            sinhKZ = sinh(z*kn)

            # Cap rho^-1 and (coA*rho)^-1 at 10^8
            # float rhoKInv, rhoInv
            rhoKInv = min(1/rhoK, CylindricalHarmonicField.invMaxVal)
            rhoInv = min(1/rho, CylindricalHarmonicField.invMaxVal)

            # Calculate Bessel terms and their derivatives
            # [float] jns, jnsDer
            jns = []
            for i in range(self.lastM + 1):
                jns.append(jv(i, rhoK))
            jnsDer = [None]*len(jns)
            for m in range(1, self.lastM + 1):
                jnsDer[m] = jns[m - 1] - m*jns[m]*rhoKInv
            jnsDer[0] = -jns[1]

            for m in range(self.firstM, self.lastM + 1):
                # sine if odd, -cosine if even
                # float sinLPhi
                sinLPhi = sinMphis[m - self.firstM]
                # cosine if odd, sine if even
                # float cosLPhi
                cosLPhi = cosMphis[m - self.firstM]
                # float jM, jMDer, bRho, bPhi, bz, bx, by
                jM = jns[m]
                jMDer = jnsDer[m]
                bRho = kn*jMDer*cosLPhi*sinhKZ
                bPhi = rhoInv*m*jM*sinLPhi*sinhKZ
                bz = kn*cosLPhi*coshKZ*jM
                bx = x*rhoInv*bRho + y*rhoInv*bPhi
                by = y*rhoInv*bRho - x*rhoInv*bPhi
                # get the linear scaling coefficient
                # float coeff
                coeff = self.coefficientsExpansion.getCoefficient(m, n)
                # scale the vector, the minus sign comes from the B=-dell U
                # VectorIJK vect
                vect = VectorIJK(bx, by, bz).scale(-coeff)
                expansions[m - self.firstM][n - self.firstN] = vect
        return Expansion2Ds.createFromArray(
            expansions, self.firstM, self.firstN
        )

    def getFirstAzimuthalExpansionNumber(self):
        """return int"""
        return self.firstM

    def getLastAzimuthalExpansionNumber(self):
        """return int"""
        return self.lastM

    def getFirstRadialExpansionNumber(self):
        """return int"""
        return self.firstN

    def getLastRadialExpansionNumber(self):
        """return int"""
        return self.lastN

    def getTrigParity(self):
        """return TrigParity"""
        return self.trigParity

    def getBessel(self):
        """return BesselFunctionEvaluator"""
        return self.bessel

    def getCoefficients(self):
        """return CoefficientExpansion2D"""
        return self.coefficientsExpansion

    def getWaveNumberExpansion(self):
        """return CoefficientExpansion1D"""
        return self.waveNumberExpansion

    def evaluateExpansion(self, location):
        """evaluateExpansion

        param UnwritableVectorIJK location
        return ImmutableList<UnwritableVectorIJK>
        """
        functions = []
        expansions = self.evaluateExpansion2D(location)
        for m in range(self.firstM, self.lastM + 1):
            for n in range(self.firstN, self.lastN + 1):
                functions.append(expansions.getExpansion(m, n))
        return functions

    def getNumberOfBasisFunctions(self):
        """return int"""
        return (
            self.coefficientsExpansion.iSize() *
            self.coefficientsExpansion.jSize()
        )