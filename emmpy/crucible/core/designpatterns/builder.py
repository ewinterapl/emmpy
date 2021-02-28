class Builder:

    """Builder

    An interface implementing the "builder" design pattern.
    Based on the original Java class:
    crucible.core.designpatterns.Builder

    Since this is an interface, all methods must be overridden
    in classes implementing this interface.
    """

    def __init__(self):
        """Initialize a new Builder object.

        Parameters
        ----------
        self : Builder
            New object to initialize.

        Returns
        -------
        self : Builder
            New object after initialization.

        Raises
        ------
        Exception
            If called.
        """
        raise Exception

    def build(self):
        """Build something.

        Parameters
        ----------
        self : Builder
            This Builder object.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If called.
        """
        raise Exception
