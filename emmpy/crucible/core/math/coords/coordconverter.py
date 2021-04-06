"""emmpy.crucible.core.math.coords.coordconverter

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class CoordConverter:
    """An interface which allows for the conversion between different
    coordinate systems to Cartesian.

    The four methods allow you to convert positions and states from Cartesian
    to the coordinate system and back. It is templated on the Unwritable and
    Writable version of the coordinate class.

    @author G.K.Stephens

    @param <U> The Unwritable Coordinate class.
    @param <W> The Writable version of the Coordinate class.
    """

    def __init__(self):
        """INTERFACE - DO NOT INSTANTIATE."""
        raise Exception

    def toCoordinate(self, cartesian):
        """INTERFACE - DO NOT INVOKE.

        Converts a Cartesian position to another coordinate system position.

        @param cartesian A {@link UnwritableVectorIJK} holding the Cartesian
        position.
        @param coordinateBuffer A coordinate buffer holding the position in
        this coordinate system.
        @return a reference to buffer for convenience.
        """
        raise Exception

    def toCartesian(self, coordinate):
        """INTERFACE - DO NOT INVOKE.

        Converts a coordinate system position to a Cartesian position.

        @param coordinate A coordinate holding the position in this coordinate
        system.
        @param cartesianBuffer A {@link UnwritableVectorIJK} buffer holding the
        Cartesian position.
        @return a reference to buffer for convenience.
        """
        raise Exception
