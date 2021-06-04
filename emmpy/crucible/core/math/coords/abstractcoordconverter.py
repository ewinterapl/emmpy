"""Base class for coordinate converters."""


from emmpy.crucible.core.math.coords.coordconverter import CoordConverter


class AbstractCoordConverter(CoordConverter):
    """Encapsulate the two state methods on the CoordConverter interface.

    Since these methods are really just leveraging a {@link Transformation},
    they need not be reimplimented every time.

    Particularly, this class is meant to ensure the Thread safety of
    implementations of {@link CoordConverter} in a consistent way. It is
    important that the incoming {@link Transformation} is thread safe
    (preferably stateless).

    TODO The other two methods should also be accomplished leveraging some
    other class, this will then ensure the thread safety of those two methods
    as well. Also, this returns the templated classes {@link WritableState} and
    {@link State}, not the concrete classes, so these methods will need to be
    casted if you want the real state.

    @author G.K.Stephens

    @param <C> a {@link AbstractVector} type
    """

    def __init__(self, jacobian):
        """Build a new AbstractCoordConverter object.

        @param jacobian the incoming Jacobian must be thread safe for this
        class to be thread safe. Implementations contained in this package are
        assumed to be thread safe.
        """
        self.jacobian = jacobian
