"""emmpy.crucible.core.math.units.localtimetoradiansconversions

Filename: LocalTimeToRadiansConversions.java
Author : vandejd1 Created : Aug 28, 2008 3:11:12 PM

Copyright (C) 2008 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved
"""


from math import pi


class LocalTimeToRadiansConversions:
    """This class offers a conversion between so-called localtime and
    longitude.

    The longitude is positive east longitude and the localtime is expressed as
    fractional hours (0.0 to 24.0)

    author vandejd1
    """

    @staticmethod
    def localtimeHoursToRadians(localtimeHours):
        """Convert local time to radians

        param localtimeHours convert a clock angle expressed in fractional
        hours from 0 to 24.0 (inclusive on both ends) into a longitude from -Pi
        to Pi (also inclusive on both ends); the zero clock angle (midnight) is
        at the -X axis and the clock angle increases as you go towards -Y,
        which is 6 o'clock.
        return longitude from -Pi to Pi (positive east longitude, with +X
        having lon=0 and +Y having lon=PI/2)
        """
        # first convert to radians ( divide by 24, multiply by 2Pi), then
        # subtract Pi because of the offset between the zero point of the clock
        # face and the coordinate frame
        return localtimeHours*(pi*2/24) - pi

    @staticmethod
    def radiansToLocaltime(posEastLongInRads):
        """Convert radians to local time

        param posEastLongInRads given a longitude in radians (either 0 to 2Pi
        or -Pi to +Pi, or any valid longitude, actually), convert this to a
        clock angle where the 0 clock angle is defined at Pi radians (the -X
        axis) and increases as you go from -X to -Y, where -Y is 6 o'clock and
        +x is 12 noon (i.e., 12.0)
        return the localtime in fractional hours
        """
        # I want to know how far around past the -X axis this longitude is, and
        # the east longitude tells me how far around from +X it is, so I first
        # subtract off Pi
        posEastLongInRads -= pi

        # make sure the longitude is from 0 to 2*Pi:
        TWOPI = pi*2
        while posEastLongInRads < 0:
            posEastLongInRads += TWOPI
        while posEastLongInRads > TWOPI:
            posEastLongInRads -= TWOPI

        # now convert to hours:
        return posEastLongInRads/TWOPI*24
