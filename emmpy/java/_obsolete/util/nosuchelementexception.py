""" Python module implementing a port of the Java class
java.util.NoSuchElementException

DESCRIBE

Classes
-------
NoSuchElementException
    Python version of the Java class java.util.NoSuchElementException
"""


class NoSuchElementException(Exception):

    """NoSuchElementException

    Python version of the Java class java.util.NoSuchElementException.
    
    Based on the original Java class:
    java.util.NoSuchElementException
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new NoSuchElementException object.

        DESCRIBE

        Parameters
        ----------
        self : NoSuchElementException
            New object to initialize.
        
        Returns
        -------
        self : NoSuchElementException
            New object after initialization.
        """
        Exception.__init__(self, *args, **kwargs)
