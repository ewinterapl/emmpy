""" Python port of the Preconditions Java class from Google Guava.

Classes
-------
Preconditions
    Provides data validation functions.
"""


class Preconditions:
    """Preconditions

    Based on the original Java Preconditions class documented at:
    https://guava.dev/releases/19.0/api/docs/com/google/common/base/Preconditions.html

    This class provides static methods which implement data validation.
    """

    @staticmethod
    def checkArgument(b, s=None, *args):
        """Verify that a condition is True.

        If the first argument is True, do nothing. If the first argument is
        False, raise an Exception, optionally detailed by the remaining
        arguments.

        Parameters
        ----------
        b : bool
            A boolean value.
        args : str [, obj1, obj2, ...], (optional)
            First element is a string. Remaining (optional) elements are
            substituted into the first argument, treating it as a format
            string.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If the first argument is False.
        """
        if not b:
            if s is not None:
                if len(args) > 0:
                    raise Exception(s % tuple(args))
                else:
                    raise Exception(s)
            else:
                raise Exception

    @staticmethod
    def checkElementIndex(i, n, s=None):
        """Verify that a sequence index is within range.

        If the index is within the specified range, return the index.
        Otherwise, raise an Exception.

        Parameters
        ----------
        i : int
            Integer index.
        n : int
            Maximum index value + 1.
        s : str, optional
            Message string to use in Exception.

        Returns
        -------
        i : int
            Index supplied as first argument.

        Raises
        ------
        Exception
            If the first argument is < 0 or >= n.
        """
        if i < 0 or i >= n:
            raise Exception(s)
        return i

    @staticmethod
    def checkNotNull(o, s=None, *args):
        """Verify that an object is not null (None).

        If the object is not None, return it. If the object is None, raise an
        Exception.

        Parameters
        ----------
        o : object
            Any object reference.
        s : str, optional
            Message string to use in Exception.
        args : obj1, obj2, ... (optional)
            Remaining (optional) elements are
            substituted into the first argument, treating it as a format
            string.

        Returns
        -------
        o : object
            Any object reference.

        Raises
        ------
        Exception
            If the object reference is None.
        """
        # Need source code for this method.
        if o is None:
            if s is not None:
                if len(args) > 0:
                    raise Exception(s % tuple(args))
                else:
                    raise Exception(s)
            else:
                raise Exception
        return o
