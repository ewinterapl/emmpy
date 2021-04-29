import unittest

from emmpy.crucible.core.time.utcepoch import UTCEpoch


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertIsNotNone(utce)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour)
        self.assertEqual(utce.min, minute)
        self.assertAlmostEqual(utce.sec, second)
        # This date/time same as the one above.
        (year, month, day, hour, minute, second) = (2021, 2, 1, 1, 2, 3.4)
        utce = UTCEpoch(year, month, day, hour, minute, second)
        self.assertIsNotNone(utce)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour)
        self.assertEqual(utce.min, minute)
        self.assertAlmostEqual(utce.sec, second)

    def test_toString(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.toString(), "2021-032T01:02:03.456")

    def test_noSubsecondsString(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.noSubsecondsString(), "2021-032T01:02:03")

    def test_fromString(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456)
        s = "2021-032T01:02:03.456"
        utce = UTCEpoch.fromString(s)
        self.assertIsNotNone(utce)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour)
        self.assertEqual(utce.min, minute)
        self.assertAlmostEqual(utce.sec, second)

    def test_roundToMilliseconds(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456)
        utce = UTCEpoch(year, doy, hour, minute, second)
        dt = utce.roundToMilliseconds()
        self.assertEqual(dt[0], year)
        self.assertEqual(dt[1], doy)
        self.assertEqual(dt[2], hour)
        self.assertEqual(dt[3], minute)
        self.assertEqual(dt[4], int(second))
        self.assertEqual(dt[5], round((second - int(second))*1000))

    def test_createValueRoundedToMillisecs(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = utce1.createValueRoundedToMillisecs()
        self.assertEqual(utce2.year, year)
        self.assertEqual(utce2.doy, doy)
        self.assertEqual(utce2.hour, hour)
        self.assertEqual(utce2.min, minute)
        roundedSecond = int(second) + round((second - int(second))*1000)/1000
        self.assertAlmostEqual(utce2.sec, roundedSecond)

    def test_getNumberOfMillisAsInt(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.getNumberOfMillisAsInt(second),
                         round((second - int(second))*1000))

    def test_roundToMicroseconds(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.4567891)
        utce = UTCEpoch(year, doy, hour, minute, second)
        dt = utce.roundToMicroseconds()
        self.assertEqual(dt[0], year)
        self.assertEqual(dt[1], doy)
        self.assertEqual(dt[2], hour)
        self.assertEqual(dt[3], minute)
        self.assertEqual(dt[4], int(second))
        self.assertEqual(dt[5], 456)
        self.assertEqual(dt[6], 789)

    def test_createValueRoundedToMicrosecs(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = utce1.createValueRoundedToMicrosecs()
        self.assertEqual(utce2.year, year)
        self.assertEqual(utce2.doy, doy)
        self.assertEqual(utce2.hour, hour)
        self.assertEqual(utce2.min, minute)
        self.assertAlmostEqual(utce2.sec, second)

    def test_getCurrentUTC(self):
        # Need test here.
        pass

    def test_getNextMin(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getNextMin(year, doy, hour, minute)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour)
        self.assertEqual(utce.min, minute + 1)

    def test_getPreviousMin(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getPreviousMin(year, doy, hour, minute)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour)
        self.assertEqual(utce.min, minute - 1)

    def test_getNextHour(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getNextHour(year, doy, hour)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour + 1)

    def test_getPreviousHour(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getPreviousHour(year, doy, hour)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy)
        self.assertEqual(utce.hour, hour - 1)

    def test_getNextDay(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getNextDay(year, doy)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy + 1)

    def test_getPreviousDay(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce = UTCEpoch.getPreviousDay(year, doy)
        self.assertEqual(utce.year, year)
        self.assertEqual(utce.doy, doy - 1)

    def test_getNextMonth(self):
        (year, month, day, hour, minute, second) = (2021, 2, 1, 1, 2, 3.4)
        utce = UTCEpoch.getNextMonth(year, month)
        self.assertEqual(utce.year, year)
        # NEED TO CONVERT DOY TO MONTHDAY
        # self.assertEqual(utce.month, month + 1)

    def test_getPreviousMonth(self):
        (year, month, day, hour, minute, second) = (2021, 2, 1, 1, 2, 3.4)
        utce = UTCEpoch.getPreviousMonth(year, month)
        self.assertEqual(utce.year, year)
        # NEED TO CONVERT DOY TO MONTHDAY
        # self.assertEqual(utce.month, month - 1)

    def test_getYear(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.getYear(), year)

    def test_getMonth(self):
        (year, month, day, hour, minute, second) = (2021, 2, 1, 1, 2, 3.4)
        utce = UTCEpoch(year, month, day, hour, minute, second)
        self.assertEqual(utce.getMonth(), month)

    def test_getDom(self):
        (year, month, day, hour, minute, second) = (2021, 2, 1, 1, 2, 3.4)
        utce = UTCEpoch(year, month, day, hour, minute, second)
        self.assertEqual(utce.getDom(), day)

    def test_getDoy(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.getDoy(), doy)

    def test_getHour(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.getHour(), hour)

    def test_getMin(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.getMin(), minute)

    def test_getSec(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertAlmostEqual(utce.getSec(), second)

    def test_compareTo(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = UTCEpoch(year - 1, doy, hour, minute, second)
        utce3 = UTCEpoch(year, doy + 1, hour, minute, second)
        self.assertEqual(utce1.compareTo(utce1), 0)
        self.assertEqual(utce1.compareTo(utce2), 1)
        self.assertEqual(utce1.compareTo(utce3), -1)

    def test_hashCode(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertEqual(utce.hashCode(), 33551179974)

    def test_equals(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = UTCEpoch(year - 1, doy, hour, minute, second)
        self.assertTrue(utce1.equals(utce1))
        self.assertFalse(utce1.equals(utce2))

    def test_createValueRoundedToSeconds(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = utce1.createValueRoundedToSeconds()
        self.assertEqual(utce2.year, year)
        self.assertEqual(utce2.doy, doy)
        self.assertEqual(utce2.hour, hour)
        self.assertEqual(utce2.min, minute)
        self.assertAlmostEqual(utce2.sec, int(second))

    def test_roundToSeconds(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.4567891)
        utce = UTCEpoch(year, doy, hour, minute, second)
        dt = utce.roundToSeconds()
        self.assertEqual(dt[0], year)
        self.assertEqual(dt[1], doy)
        self.assertEqual(dt[2], hour)
        self.assertEqual(dt[3], minute)
        self.assertEqual(dt[4], int(second))

    def test_createValueRoundedToMinutes(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.456789)
        utce1 = UTCEpoch(year, doy, hour, minute, second)
        utce2 = utce1.createValueRoundedToMinutes()
        self.assertEqual(utce2.year, year)
        self.assertEqual(utce2.doy, doy)
        self.assertEqual(utce2.hour, hour)
        self.assertEqual(utce2.min, round(minute + second/60))

    def test_roundToMinutes(self):
        (year, doy, hour, minute, second) = (2021, 32, 1, 2, 3.4567891)
        utce = UTCEpoch(year, doy, hour, minute, second)
        dt = utce.roundToMinutes()
        self.assertEqual(dt[0], year)
        self.assertEqual(dt[1], doy)
        self.assertEqual(dt[2], hour)
        self.assertEqual(dt[3], round(minute + second/60))

    def test_getAsFractionalDoy(self):
        (year, doy, hour, minute, second) = (2021, 59, 1, 2, 3.4)
        utce = UTCEpoch(year, doy, hour, minute, second)
        self.assertAlmostEqual(utce.getAsFractionalDoy(),
                               doy + hour/24 + minute/1440 + second/86400)


if __name__ == '__main__':
    unittest.main()
