# package crucible.core.exceptions;

# /**
#  * A {@link RuntimeException} intended to perform the same function as {@link InterruptedException}
#  * in cases where the API can not declare the checked variant provided by the JDK.
#  * 
#  * @author turnefs1
#  *
#  */
from emmpy.crucible.core.exceptions.crucibleruntimeexception import CrucibleRuntimeException

class RuntimeInterruptedException(CrucibleRuntimeException):

    serialVersionUID = 1

    def __init__(self, *args):
        CrucibleRuntimeException.__init__(self, *args)

    #   /**
    #    * Default exception with no detail message
    #    */
    #   public RuntimeInterruptedException() {
    #     super();
    #   }

    #   /**
    #    * Exception with detail message
    #    * 
    #    * @param message tbe details
    #    */
    #   public RuntimeInterruptedException(String message) {
    #     super(message);
    #   }

    # }
