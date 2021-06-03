"""emmpy.crucible.core.time.utcepoch"""


import calendar
import dateutil.parser
import datetime

from emmpy.java.lang.double import Double


class UTCEpoch:
    """This class represents a single epoch (i.e. moment) in time in the
    Coordinated Universal Time (abbreviated to UTC) time standard.

    @author vandejd1
    """

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 5:
            (year, doy, hour, min, sec) = args
            # @param year a standard year starting from 1
            # @param doy the day of the year, starting from 1, which
            # corresponds to January 1st
            # @param hour the hour of the day, ranging from 0 - 23
            # @param min the minute of the hour, ranging from 0 - 59
            # @param sec the second of the minute, ranging from
            # 0.0 - <60.0 for minutes not containing a leap second,
            # from 0.0 - <61.0 for minutes that contain a positive
            # leapsecond, and 0.0 - <59.0 for minutes that contain
            # a negative leapsecond
            self.year = year
            self.doy = doy
            self.hour = hour
            self.min = min
            self.sec = sec
        elif len(args) == 6:
            (year, month, monthDay, hour, min, sec) = args
            # @param year a standard year, which starts from 1
            # @param month a standard month, starting from 1, which corresponds
            # to January
            # @param monthDay a standard day of month, starting from 1, which
            # accounts for leap years
            # @param hour the hour of the day, ranging from 0 - 23
            # @param min the minute of the hour, ranging from 0 - 59
            # @param sec the second of the minute, ranging from 0.0 - <60.0
            # for minutes not containing a leap second, from 0.0 - <61.0
            # for minutes that contain a positive leapsecond, and 0.0 - <59.0
            # for minutes that contain a negative leapsecond
            self.year = year
            self.doy = (
                datetime.datetime(year, month, monthDay).timetuple().tm_yday
            )
            self.hour = hour
            self.min = min
            self.sec = sec
        else:
            raise Exception

    def toString(self):
        """A string in the form year-doyThh:mm:ss.sss"""
        # First round to the nearest millisecond:
        vals = self.roundToMilliseconds()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_intSec = vals[4]
        other_millis = vals[5]
        return (
            "%4d-%03dT%02d:%02d:%02d.%03d" %
            (other_yr, other_doy, other_hr, other_min, other_intSec,
             other_millis)
        )

    def noSubsecondsString(self):
        """similar to toString() but the seconds field has been rounded to the
        nearest second

        @return a String representing the UTCEpoch in which the seconds field
        has been rounded to the nearest second
        """

        # First round to the nearest millisecond:
        vals = self.roundToMilliseconds()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_intSec = vals[4]
        return (
            "%4d-%03dT%02d:%02d:%02d" %
            (other_yr, other_doy, other_hr, other_min, other_intSec)
        )

    @staticmethod
    def fromString(timeString):
        """Utility for reversing UTCEpoch.toString(). Use for any other purpose
        is not recommended

        @param timeString the output of a call to UTCEpoch toString()
        """
        d = dateutil.parser.isoparse(timeString)
        utc = UTCEpoch(d.year, d.month, d.day, d.hour, d.minute,
                       d.second + d.microsecond/1e6)
        return utc

    def roundToMilliseconds(self):
        """this should be private, but I made it package private for testing
        purposes only!!!"""
        other_yr = self.getYear()
        other_doy = self.getDoy()
        other_hr = self.getHour()
        other_min = self.getMin()
        other_intSec = int(self.getSec())
        other_millis = self.getNumberOfMillisAsInt(self.getSec())
        if other_millis == 1000:
            other_millis = 0
            other_intSec += 1
            if other_intSec == 60:
                other_intSec = 0
                other_min += 1
                if other_min == 60:
                    other_min = 0
                    other_hr += 1
                    if other_hr == 24:
                        other_hr = 0
                        other_doy += 1
                        if ((calendar.isleap(other_yr) and other_doy > 366) or
                            (not calendar.isleap(other_yr) and
                             other_doy > 365)):
                            other_doy = 1
                            other_yr += 1
        return [other_yr, other_doy, other_hr, other_min, other_intSec,
                other_millis]

    def createValueRoundedToMillisecs(self):
        """@return a newly created UTCEpoch where the seconds field has been
        rounded to the nearest millisecond
        """
        vals = self.roundToMilliseconds()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_intSec = vals[4]
        other_millis = vals[5]
        return UTCEpoch(
            other_yr, other_doy, other_hr, other_min,
            other_intSec + other_millis/1000)

    def getNumberOfMillisAsInt(self, sec):
        """THIS SHOULD BE A STATIC METHOD."""
        intSec = int(sec)
        rawMillis = sec - intSec
        intMillis = int((rawMillis*1000.0) + 0.5)
        return intMillis

    def roundToMicroseconds(self):
        """this should be private, but I made it package private for testing
        purposes only!!!
        """

        other_yr = self.getYear()
        other_doy = self.getDoy()
        other_hr = self.getHour()
        other_min = self.getMin()
        sec = self.getSec()
        other_intSec = int(sec)
        otherJustMillis = 1000*(sec - other_intSec)
        other_intMillis = int(otherJustMillis)
        otherJustMicros = 1000*(otherJustMillis - other_intMillis)
        other_intMicros = round(otherJustMicros)
        if other_intMicros == 1000:
            other_intMicros = 0
            other_intMillis += 1
            if other_intMillis == 1000:
                other_intMillis = 0
                other_intSec += 1
                if other_intSec == 60:
                    other_intSec = 0
                    other_min += 1
                    if other_min == 60:
                        other_min = 0
                        other_hr += 1
                        if other_hr == 24:
                            other_hr = 0
                            other_doy += 1
                            if ((calendar.isleap(other_yr) and other_doy > 366)
                                or
                                (not calendar.isleap(other_yr) and other_doy >
                                 365)):
                                other_doy = 1
                                other_yr += 1
        return [other_yr, other_doy, other_hr, other_min, other_intSec,
                other_intMillis, other_intMicros]

    def createValueRoundedToMicrosecs(self):
        """@return a newly created UTCEpoch where the seconds field has been
        rounded to the nearest microssecond
        """
        vals = self.roundToMicroseconds()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_intSec = vals[4]
        other_millis = vals[5]
        other_micros = vals[6]
        return UTCEpoch(
            other_yr, other_doy, other_hr, other_min,
            other_intSec + other_millis/1000 + other_micros/1.e6
        )

    @staticmethod
    def getCurrentUTC():
        """@return the current UTCEpoch"""
        now = datetime.datetime.now().timetuple()
        return UTCEpoch(
            now.tm_year, now.tm_yday, now.tm_hour, now.tm_min, now.tm_sec
        )

    @staticmethod
    def getNextMin(year, doy, hour, min):
        """Get next minute

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds to
        January 1st
        @param hour the hour of the day, ranging from 0 - 23
        @param min the minute of the hour, ranging from 0 - 59
        @return UTCEpoch with the minute field incremented by 1; leap days are
        accounted for, but not leap seconds
        """
        nextMin = min + 1
        nextHour = hour
        nextDoy = doy
        nextYear = year
        if nextMin > 59:
            next = UTCEpoch.getNextHour(nextYear, nextDoy, nextHour)
            nextMin = 0
            nextHour = next.getHour()
            nextDoy = next.getDoy()
            nextYear = next.getYear()
        return UTCEpoch(nextYear, nextDoy, nextHour, nextMin, 0)

    @staticmethod
    def getPreviousMin(year, doy, hour, min):
        """Get the previous minute

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds to
        January 1st
        @param hour the hour of the day, ranging from 0 - 23
        @param min the minute of the hour, ranging from 0 - 59
        @return UTCEpoch with the minute field decremented by 1; leap days are
        accounted for, but not leap seconds
        """
        prevMin = min - 1
        prevHour = hour
        prevDoy = doy
        prevYear = year
        if prevMin < 0:
            prev = UTCEpoch.getPreviousHour(prevYear, prevDoy, prevHour)
            prevMin = 59
            prevHour = prev.getHour()
            prevDoy = prev.getDoy()
            prevYear = prev.getYear()
        return UTCEpoch(prevYear, prevDoy, prevHour, prevMin, 0)

    @staticmethod
    def getNextHour(year, doy, hour):
        """Get the next hour

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds to
        January 1st
        @return UTCEpoch with the hour field incremented by 1; leap days are
        accounted for, but not leap seconds
        """
        nextHour = hour + 1
        nextDoy = doy
        nextYear = year
        if nextHour > 23:
            next = UTCEpoch.getNextDay(nextYear, nextDoy)
            nextHour = 0
            nextDoy = next.getDoy()
            nextYear = next.getYear()
        return UTCEpoch(nextYear, nextDoy, nextHour, 0, 0)

    @staticmethod
    def getPreviousHour(year, doy, hour):
        """Get the previous hour

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds to
        January 1st
        @param hour the hour of the day, ranging from 0 - 23
        @return UTCEpoch with the hour field decremented by 1; leap days are
        accounted for, but not leap seconds
        """
        prevHour = hour - 1
        prevDoy = doy
        prevYear = year
        if prevHour < 0:
            prev = UTCEpoch.getPreviousDay(prevYear, prevDoy)
            prevHour = 23
            prevDoy = prev.getDoy()
            prevYear = prev.getYear()
        return UTCEpoch(prevYear, prevDoy, prevHour, 0, 0)

    @staticmethod
    def getNextDay(year, doy):
        """Get the next day

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds
        to January 1st
        @return UTCEpoch with the day field incremented by 1; leap days are
        accounted for, but not leap seconds
        """
        nextDoy = doy + 1
        nextYear = year
        if ((calendar.isleap(nextYear) and nextDoy > 366) or
            (not calendar.isleap(nextYear) and nextDoy > 365)):
            nextYear = year + 1
            nextDoy = 1
        return UTCEpoch(nextYear, nextDoy, 0, 0, 0)

    @staticmethod
    def getPreviousDay(year, doy):
        """Get the previous day

        @param year a standard year, which starts from 1
        @param doy the day of the year, starting from 1, which corresponds to
        January 1st
        @return UTCEpoch with the day field decremented by 1; leap days are
        accounted for, but not leap seconds
        """
        prevDoy = doy - 1
        prevYear = year
        if prevDoy < 1:
            prevYear -= 1
            if calendar.isleap(prevYear):
                prevDoy = 366
            else:
                prevDoy = 365
        return UTCEpoch(prevYear, prevDoy, 0, 0, 0)

    @staticmethod
    def getNextMonth(year, month):
        """Get the next month

        @param year a standard year, which starts from 1
        @param month a standard month, starting from 1, which corresponds to
        January
        @return UTCEpoch with the month field incremented by 1; leap days are
        accounted for, but not leap seconds
        """
        nextMonth = month + 1
        nextYear = year
        if nextMonth > 12:
            nextYear = year + 1
            nextMonth = 1
        return UTCEpoch(nextYear, nextMonth, 1, 0, 0, 0)

    @staticmethod
    def getPreviousMonth(year, month):
        """Get the previous month

        @param year a standard year, which starts from 1
        @param month a standard month, starting from 1, which corresponds to
        January
        @return UTCEpoch with the month field decremented by 1; leap days are
        accounted for, but not leap seconds
        """
        previousMonth = month - 1
        previousYear = year
        if previousMonth < 1:
            previousYear = year - 1
            previousMonth = 12
        return UTCEpoch(previousYear, previousMonth, 1, 0, 0, 0)

    def getYear(self):
        """@return the standard year starting from 1"""
        return self.year

    def getMonth(self):
        """@return the integer month of the year starting from 1 that
        corresponds to January (1 to 12)"""
        s = "%s %s" % (self.year, self.doy)
        d = datetime.datetime.strptime(s, "%Y %j")
        return d.month

    def getDom(self):
        """@return the integer day of month, starting from 1, i.e. January 8th
        will have a day of month of 8"""
        s = "%s %s" % (self.year, self.doy)
        d = datetime.datetime.strptime(s, "%Y %j")
        return d.day

    def getDoy(self):
        """@return the integer day of year, starting from 1 that corresponds to
        January 1st (1 to 365/366 for leap years)"""
        return self.doy

    def getHour(self):
        """@return the integer hour of the day, starting from 0 (0 to 59)"""
        return self.hour

    def getMin(self):
        """@return the integer minute of the hour, starting from 0 (0 to 59)"""
        return self.min

    def getSec(self):
        """@return the double second of the minute,

        starting from 0.0 (0.0 to 59.999... except in the case of a positive
        leap second where the range is 0.0 to 60.999... or 0.0 to 58.999... in
        case of a negative leap second, note a negative leap second has never
        been issued)
        """
        return self.sec

    def compareTo(self, o):
        if self.year < o.year:
            return -1
        if self.year > o.year:
            return 1
        if self.doy < o.doy:
            return -1
        if self.doy > o.doy:
            return 1
        if self.hour < o.hour:
            return -1
        if self.hour > o.hour:
            return 1
        if self.min < o.min:
            return -1
        if self.min > o.min:
            return 1
        if self.sec < o.sec:
            return -1
        if self.sec > o.sec:
            return 1
        return 0

    def hashCode(self):
        prime = 31
        result = 1
        result = prime*result + self.doy
        result = prime*result + self.hour
        result = prime * result + self.min
        temp = Double.doubleToLongBits(self.sec)
        result = prime*result + temp ^ (temp >> 32)
        result = prime*result + self.year
        return result

    def equals(self, obj):
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.doy != other.doy:
            return False
        if self.hour != other.hour:
            return False
        if self.min != other.min:
            return False
        if (
            Double.doubleToLongBits(self.sec) !=
            Double.doubleToLongBits(other.sec)):
            return False
        if self.year != other.year:
            return False
        return True

    def createValueRoundedToSeconds(self):
        """@return a newly created UTCEpoch where the seconds field has been
        rounded to the nearest whole second"""
        vals = self.roundToSeconds()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_sec = vals[4]
        return UTCEpoch(other_yr, other_doy, other_hr, other_min, other_sec)

    def roundToSeconds(self):
        other_yr = self.getYear()
        other_doy = self.getDoy()
        other_hr = self.getHour()
        other_min = self.getMin()
        other_sec = round(self.getSec())
        if other_sec == 60:
            other_sec = 0
            other_min += 1
            if other_min == 60:
                other_min = 0
                other_hr += 1
                if other_hr == 24:
                    other_hr = 0
                    other_doy += 1
                    if ((calendar.isleap(other_yr) and other_doy > 366) or
                        (not calendar.isleap(other_yr) and other_doy > 365)):
                        other_doy = 1
                        other_yr += 1
        return [other_yr, other_doy, other_hr, other_min, other_sec]

    def createValueRoundedToMinutes(self):
        """@return a newly created UTCEpoch where the minute field has been
        rounded to the nearest whole minute (the seconds field is set to 0.0)
        """
        vals = self.roundToMinutes()
        other_yr = vals[0]
        other_doy = vals[1]
        other_hr = vals[2]
        other_min = vals[3]
        other_sec = 0
        return UTCEpoch(other_yr, other_doy, other_hr, other_min, other_sec)

    def roundToMinutes(self):
        other_yr = self.getYear()
        other_doy = self.getDoy()
        other_hr = self.getHour()
        other_min = int(0.5 + self.getMin() + self.getSec()/60)
        if other_min == 60:
            other_min = 0
            other_hr += 1
            if other_hr == 24:
                other_hr = 0
                other_doy += 1
                if ((calendar.isleap(other_yr) and other_doy > 366) or
                    (not calendar.isleap(other_yr) and other_doy > 365)):
                    other_doy = 1
                    other_yr += 1
        return [other_yr, other_doy, other_hr, other_min]

    def getAsFractionalDoy(self):
        """@return the fractional day of year, where 1.0 is midnight
        January 1st."""
        return (self.getDoy() + self.getHour()/24 + self.getMin()/(24*60) +
                self.getSec()/(24*3600))
