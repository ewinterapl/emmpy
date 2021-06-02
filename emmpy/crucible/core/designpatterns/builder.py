"""emmpy.crucible.core.designpatterns.builder

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class Builder:
    """Simple interface defining the builder pattern.

    A builder is different from a factory, in that a factory generally provides
    methods that are used to immediately create an object of interest. The
    builder provides an API that is used to configure the construction of a
    complex object. Effectively it provides a means to grow the construction
    API independently of the object or interface to be constructed.

    While this is not enforced via the interface mechanism, methods designed to
    configure the builder on a specific implementation of a builder should
    always return references to the instance. This allows method call chaining,
    which is typical of the builder pattern. Further, it is useful to name the
    methods on the builder in a manner that lets them be read using natural
    language, i.e. withOption(Option option), etc.

    This interface would not technically have to exist to support the
    {@link Blueprint} interface, but we felt it was useful in that all builders
    should have the build method on them.

    @author F.S.Turner

    @param <T> the type of object the builder creates
    @param <E> the type of exception the builder throws

    @see Blueprint
    """

    def __init__(self):
        """INTERFACE - NO NOT INSTANTIATE."""
        raise Exception

    def build(self):
        """Builds the object or interface of interest.

        INTERFACE - DO NOT INVOKE.

        @return a newly created implementation of the desired interface or
        object
        @throws BuildFailedException implementors of this interface are
        encouraged to utilize this runtime exception or a descendant of it to
        indicate that a build has failed for any reason. It is, however; not
        explicitly required.
        """
        raise Exception
