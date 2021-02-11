class Builder:

    """Builder

    An interface implementing the "builder" design pattern.
    Based on the original Java class:
    crucible.core.designpatterns.Builder

    Since this is an interface, all methods must be overridden
    in classes implementing this interface
    """

    def __init__(self):
        raise Exception

    def build(self):
        raise Exception
