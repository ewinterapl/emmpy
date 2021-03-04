"""emmpy.java.lang.double
"""


import struct
import sys

from emmpy.java.lang.object import Object


class Double(Object):
    MAX_VALUE = sys.float_info.max

    def doubleToLongBits(x: float) -> int:
        """Convert a float to the corresponding IEEE 754 bit pattern.

        NOTE: This Python version gives the same results as the Java '>>>'
        operator *only* for non-negative numbers.

        Reference:
        https://stackoverflow.com/questions/23624212/how-to-convert-a-float-into-hex
        """
        return struct.unpack('<I', struct.pack('<f', x))[0]
