"""emmpy.magmodel.core.time.utcnumerator

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


from emmpy.crucible.core.time.utcepoch import UTCEpoch


class UTCNumerator:

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE

        Converts an UTCEpoch to a double that corresponds to the location of
        the epoch on a number line and also does the inverse.

        This is used to turn time series data into proper functions.

        @author G.K.Stephens
        """
        raise Exception

    def numerate(self, epoch):
        """Converts an UTCEpoch into a value on a number line.

        INTERFACE - DO NOT INVOKE

        @param epoch the input epoch
        @return a double that represents the value of the UTCEpoch on a number
        line
        """
        raise Exception

    def calendarize(self, epoch):
        """Converts a double representing a value on a number line back into an
        UTCEpoch.

        INTERFACE - DO NOT INVOKE

        @param epoch an input double that represents a value on a number line
        @return the {@link UTCEpoch} that the input double corresponds to
        """
        raise Exception
