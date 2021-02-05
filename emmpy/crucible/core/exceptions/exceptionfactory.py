# package crucible.core.exceptions;

# /**
#  * Interface describing an exception factory, designed to convert one type of exceptions to another
#  * for abdicating control of exception generation to the user or implementor of an interface.
#  * <p>
#  * TODO: Provide a simple example.
#  * </p>
#  * 
#  * @author F.S.Turner
#  * 
#  * @param <I> Input exception type
#  * @param <O> Output exception type
#  */

# public interface ExceptionFactory<O extends Throwable, I extends Throwable> {
class ExceptionFactory:

    #   public O create(I exception);
    def __init__(self, e):
        pass

    # }
