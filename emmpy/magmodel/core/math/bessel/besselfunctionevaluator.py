""" Python version of the BesselFunctionEvaluator interface

DESCRIBE

Classes
-------
BesselFunctionEvaluator
    DESCRIBE
"""


from emmpy.com.google.common.base.preconditions import Preconditions


class BesselFunctionEvaluator:

    __BIGNO = 1e10
    __BIGNI = 1e-10

    """BesselFunctionEvaluator

    DESCRIBE
    
    Based on the original Java interface:
    magmodel.core.math.bessel.BesselFunctionEvaluator
    """

    def __init__(self, size):
        """Initialize a new BesselFunctionEvaluator object.

        DESCRIBE

        Since this Python class represents a Java interface, all methods MUST
        be overridden in classes inheriting from this class.

        Parameters
        ----------
        self : BesselFunctionEvaluator
            New object to initialize.
        size : int
            DESCRIBE

        Returns
        -------
        self : BesselFunctionEvaluator
            New object after initialization.
        """
        super().__init__()
        self.__reference = AtomicReference(TimeBesselFunctionPair(NaN, null))
        Preconditions.checkArgument(size > 1)
        self.__n = size
        IACC = 40
        self.__m = ((self.__n + int(sqrt(IACC * n))) / 2)

    def besselj0(self, x):
        """DESCRIBE

        DESCRIBE

        Parameters
        ----------
        self : BesselFunctionEvaluator
            This object.
        x : float
            DESCRIBE

        Returns
        -------
        ? : float
            DESCRIBE
        """
        tfp = self.__reference.get()
        if tfp.getTime() == x:
            return tfp.getFunctionEvaluations()[0]
        functionEvaluations = besselj0jn(self.__n, x)
        self.__reference.set(TimeBesselFunctionPair(x, functionEvaluations))
        return functionEvaluations[0]

    def besselj1(self, x):
        """DESCRIBE

        DESCRIBE

        Parameters
        ----------
        self : BesselFunctionEvaluator
            This object.
        x : float
            DESCRIBE

        Returns
        -------
        ? : float
            DESCRIBE
        """
        tfp = self.__reference.get()
        if tfp.getTime() == x:
            return tfp.getFunctionEvaluations()[1]
        functionEvaluations = besselj0jn(self.__n, x)
        self.__reference.set(TimeBesselFunctionPair(x, functionEvaluations))
        return functionEvaluations[1]

    def besseljn(self, n, x):
        """DESCRIBE

        DESCRIBE

        Parameters
        ----------
        self : BesselFunctionEvaluator
            This object.
        n : int
        x : float
            DESCRIBE

        Returns
        -------
        ? : float
            DESCRIBE
        """
        tfp = self.__reference.get()
        if tfp.getTime() == x:
            return tfp.getFunctionEvaluations()[n]
        functionEvaluations = besselj0jn(self.__n, x)
        self.__reference.set(TimeBesselFunctionPair(x, functionEvaluations))
        return functionEvaluations[n]

    def besselj0jn(self, n, x):
        """DESCRIBE

        DESCRIBE

        Parameters
        ----------
        self : BesselFunctionEvaluator
            This object.
        n : int
        x : float
            DESCRIBE

        Returns
        -------
        ? : float
            DESCRIBE
        """
        bessJ = [None] * (n + 1)
        ax = abs(x)
        tox = 2.0 / ax
        # start at some large m, larger than the desired n, multiply by 2 to ensure
        # m starts at an even number

        evnsum = 0.0 # keeps track of the sum of the even Js (J0+J2+J4+...)
        iseven = False

        # we set the value of Jm to some arbitrary value, here Jm=1, after the loop
        # is done, the values will be normalized using the sum
        bjp = 0.0
        bj = 1.0

        # initialize to zero
        # TODO, this is a little different than the fortran code
        bessJ[0] = 1.0
        for i in range(1, n + 1):
            bessJ[i] = 0.0

        if ax < 1.0E-12:
            return bessJ

        for j in range(self.__m, 0, -1):
            # the next value int the recursion relation J_n-1 = (2*n/x)*Jn - J_n+1
            bjm = j * tox * bj - bjp
            bjp = bj  # decrement so shift J_n+1 ot Jn
            bj = bjm  # decrement so shift J_n ot J_n-1

            # if the value gets too large, shift the decimal of everything by 10 places
            if abs(bj) > self.__BIGNO:
                bj = bj * self.__BIGNI
                bjp = bjp * self.__BIGNI
                evnsum = evnsum * self.__BIGNI
            for i in range(j + 1, n + 1):
                bessJ[i] = bessJ[i] * self.__BIGNI;

        # only sum over the even Jns
        if iseven:
            evnsum = evnsum + bj
        iseven = not iseven

        if j <= n:
            bessJ[j] = bjp  # Jj(x)

        # sum is currently the sum of all the evens
        # use Miller's algorithm for Bessel functions which uses the identity:
        # 1.0 = 2.0*sum(J_evens) - J0, thus the quantity (2.0*sum(J_evens) - J0)
        # is used as a normalization factor
        bnorm = 2.0 * evnsum - bj

        # normalize the Bessel functions
        for i in range(1, n + 1):
            bessJ[i] = bessJ[i] / bnorm
        bessJ[0] = bj / bnorm  # J0(x)

        # Apply Jn(-x) = (-1)^n * Jn(x)
        if x < 0.0:
            for i in range(1, n + 1, 2):
                bessJ[i] = -bessJ[i]

        return bessJ
