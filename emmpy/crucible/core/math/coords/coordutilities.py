"""emmpy.crucible.core.math.coords.coordutilities

This class is for convenience methods related to angles and coordinate
converters. Its not meant to grow into an alternative coordinate conversion
API, so if you find that you want to add lots of methods here, see first if
your conversion needs are already met with other existing converters.

@author vandejd1
"""


from math import pi


def toLatitude(colatInRadians):
    """converts colatitude in radians to latitude in radians"""
    return pi/2 - colatInRadians

def toColatitude(latInRadians):
    """converts latitude in radians to colatitude in radians"""
    return pi/2 - latInRadians
