"""emmpy.crucible.core.units.angleconversions"""


from math import radians

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.units.fundamentalphysicalconstants import (
    FundamentalPhysicalConstants
)


class AngleConversions:

    @staticmethod
    def convertHourAngle(hours, minutes, seconds):
        """Converts an hour angle to radians

        param hours number of hours
        param minutes number of minutes
        param seconds number of seconds
        return the equivalent angle expressed in radians
        """
        Preconditions.checkArgument(
            hours < 24 and hours >= 0, "hours must be 0-23")
        Preconditions.checkArgument(
            minutes < 60 and minutes >= 0, "minutes must be 0-59")
        Preconditions.checkArgument(
            seconds < 60.0 and seconds >= 0, "seconds must be 0-<60")
        return (
            hours/24 + minutes/(24*60) +
            seconds/(24*3600)*FundamentalPhysicalConstants.TWOPI
        )

    @staticmethod
    def convertSexagesimal(degrees, minutes, seconds):
        """Converts a Sexagesimal angle to radians

        param degrees number of degrees
        param minutes number of minutes
        param seconds number of seconds
        return the equivalent angle expressed in radians
        """
        Preconditions.checkArgument(
            degrees < 360 and degrees >= 0, "hours must be 0-23")
        Preconditions.checkArgument(
            minutes < 60 and minutes >= 0, "minutes must be 0-59")
        Preconditions.checkArgument(
            seconds < 60.0 and seconds >= 0, "seconds must be 0-<60")
        return radians(degrees + minutes / 60.0 + seconds / 3600.0)
