"""Non-linear parameters for the TS07 geomagnetic field model.

Non-linear parameters for the TS07 geomagnetic field model.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class Ts07NonLinearParameters:
    """Non-linear parameters for the TS07 geomagnetic field model.

    A container class for all the non-linear parameters of the TS07D model,
    current sheet thicknesses, hinge distance, warping parameter, region-1 FAC
    scaling, region-2 FAC scaling, and the twisting parameter.

    Attributes
    ----------
    facRegion1Kappa : float
        FAC region 1 kappa scaling factor.
    facRegion2Kappa : float
        FAC region 2 kappa scaling factor.
    currThicks : list of float
        Current sheet thicknesses.
    hingeDist : float
        Hinge distance,
    warpParam : float
        Warping parameter.
    twistFact : float
        Twist factor.
    """

    def __init__(
        self, facRegion1Kappa, facRegion2Kappa, currThicks, hingeDist,
        warpParam, twistFact
    ):
        """Initialize a new Ts07NonLinearParameters object.

        Initialize a new Ts07NonLinearParameters object.

        Parameters
        ----------
        facRegion1Kappa : float
            FAC region 1 kappa scaling factor.
        facRegion2Kappa : float
            FAC region 2 kappa scaling factor.
        currThicks : list of float
            Current sheet thicknesses.
        hingeDist : float
            Hinge distance,
        warpParam : float
            Warping parameter.
        twistFact : float
            Twist factor.
        """
        self.facRegion1Kappa = facRegion1Kappa
        self.facRegion2Kappa = facRegion2Kappa
        self.currThicks = currThicks
        self.hingeDist = hingeDist
        self.warpParam = warpParam
        self.twistFact = twistFact
