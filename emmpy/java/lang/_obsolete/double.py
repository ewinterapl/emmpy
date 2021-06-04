"""emmpy.java.lang.double"""


import math
import struct
import sys


class Double:
    MAX_VALUE = sys.float_info.max
    POSITIVE_INFINITY = math.inf

    @staticmethod
    def doubleToLongBits(x):
        """Convert a float to the corresponding IEEE 754 bit pattern.

        NOTE: This Python version gives the same results as the Java '>>>'
        operator *only* for non-negative numbers.

        Reference:
        https://stackoverflow.com/questions/23624212/how-to-convert-a-float-into-hex
        """
        return struct.unpack('<I', struct.pack('<f', x))[0]