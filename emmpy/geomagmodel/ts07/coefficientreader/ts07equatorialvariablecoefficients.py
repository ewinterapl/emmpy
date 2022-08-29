"""Variable equatorial coefficients for the TS07 geomagnetic field model.

Variable equatorial coefficients for the TS07 geomagnetic field model.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


import numbers

import numpy as np

class Ts07EquatorialVariableCoefficients:
    """Variable equatorial coefficients for TS07 geomagnetic field model.

    Variable equatorial coefficients for TS07 geomagnetic field model.

    Attributes
    ----------
    currThicks : array-like of float
        currThicks
    hingeDist : float
        Hinge distance.
    warpingParam : float
        Warping parameter.
    twistParam : float
        Twist parameter.
    equatorialLinearCoeffs : list of Ts07EquatorialLinearCoefficients
        Equatorial linear coefficients.
    """

    def __init__(self, currThicks, hingeDist, warpingParam, twistParam,
                 equatorialLinearCoeffs):
        """Initialize a new Ts07EquatorialVariableCoefficients object.

        Initialize a new Ts07EquatorialVariableCoefficients object.

        Parameters
        ----------
        currThicks : float or list of float
            Current sheet thicknesses.
        hingeDist : float
            Hinge distance.
        warpingParam : float
            Warping parameter.
        twistParam : float
            Twist parameter.
        equatorialLinearCoeffs : list of Ts07EquatorialLinearCoefficients
            Equatorial linear coefficients.
        
        Raises
        ------
        TypeError
            If invalid parameters are provided.
        """
        if isinstance(currThicks, numbers.Real):
            self.currThicks = [currThicks]
        elif isinstance(currThicks, (list, np.ndarray)):
            # The current sheet thickness and the number of sets of linear
            # coeffs must be the same size.
            self.currThicks = currThicks
        else:
            raise TypeError
        self.hingeDist = hingeDist
        self.warpingParam = warpingParam
        self.twistParam = twistParam
        self.equatorialLinearCoeffs = equatorialLinearCoeffs

    def getTotalNumberOfParameters(self):
        """Return the total number of parameters.

        Return the total number of parameters.

        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Total number of parameters.
        """
        return (self.getTotalNumberOfLinearParameters() +
                self.getTotalNumberOfNonLinearParameters())

    def getTotalNumberOfLinearParameters(self):
        """Return the total number of linear parameters.
        
        Return the total number of linear parameters.

        Parameters
        ----------
        None

        Returns
        -------
        numLinear : int
            Total number of linear parameters.
        """
        numLinear = 0

        # Loop through all the linear parameters and add them up.
        for lin in self.equatorialLinearCoeffs:
            m = lin.numAzimuthalExpansions
            n = lin.numRadialExpansions
            numLinear += 2 * (n + 2 * (n * m))
        return numLinear

    def getTotalNumberOfNonLinearParameters(self):
        """Return the total number of nonlinear parameters.
        
        Return the total number of nonlinear parameters.
        
        Parameters
        ----------
        None

        Returns
        -------
        result : int
            Total number of nonlinear parameters.
        """
        # currThicks, hingeDist, warpingParam, TwistParam.
        return len(self.currThicks) + 3
