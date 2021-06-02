class OptionalDouble:

    """OptionalDouble

    Based on the original Java OptionalDouble class documented at:
    https://docs.oracle.com/javase/8/docs/api/java/util/OptionalDouble.html
    """

    def __init__(self):
        """Initialize a new OptionalDouble object.

        Parameters
        ----------
        self : OptionalDouble
            New object to initialize.
        
        Returns
        -------
        self : OptionalDouble
            New object after initialization.
        """
        pass

    @classmethod
    def empty(cls):
        """Create a new, empty OptionalDouble object.

        Parameters
        ----------
        cls : OptionalDouble class
            Class to create instance of.
        
        Returns
        -------
        object : OptionalDouble
            New OptionalDouble object.
        """
        return cls()
