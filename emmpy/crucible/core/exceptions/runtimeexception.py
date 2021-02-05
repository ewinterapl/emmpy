# This class was created to take the place of the Java RuntimeException class.

class RuntimeException(Exception):

    def __init__(self, *args):
        Exception.__init__(self, *args)
