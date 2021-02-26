"""Template for a Python module implementing a port of a Java interface file.

From PEP 257:
https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings

The docstring for a module should generally list the classes, exceptions and
functions (and any other objects) that are exported by the module, with a
one-line summary of each. (These summaries generally give less detail than
the summary line in the object's docstring.) The docstring for a package
(i.e., the docstring of the package's __init__.py module) should also list
the modules and subpackages exported by the package.

Classes
-------
InterfaceTemplate
    Template for the Python version of a Java interface
"""


class InterfaceTemplate:

    """InterfaceTemplate

    A Python interface template ...

    Based on the original Java interface:
    XXX.XXX.XXX
    """

    def __init__(self):
        """Initialize a new InterfaceTemplate object.

        The docstring for a function or method should summarize its behavior
        and document its arguments, return value(s), side effects, exceptions
        raised, and restrictions on when it can be called (all if applicable).
        Optional arguments should be indicated. It should be documented whether
        keyword arguments are part of the interface.

        Since this Python class represents a Java interface, all methods MUST
        be overridden in classes inheriting from this class.

        Parameters
        ----------
        self : InterfaceTemplate
            New object to initialize.

        Returns
        -------
        self : InterfaceTemplate
            New object after initialization.

        Raises
        ------
        Exception
            If called.
        """
        raise Exception
