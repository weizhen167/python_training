import datetime
from datetime import tzinfo
from datetime import timedelta


class Tz_Sub(tzinfo):

    def utcoffset(self, date_time):
        return timedelta(hours=-5)

    def dst(self, date_time):
        return timedelta(hours=0)

tz = Tz_Sub()
dt = datetime.datetime(1969, 7, 20, hour=15, minute=18, second=0)
weekday_list = {'0': "Monday", '1': "Tuesday", '2': "Wednesday", '3': "Thursday",
                '4': "Friday", '5': "Saturday", '6': "Sunday", '7': "ISO Error"}


# 1 - Getting different time formats
print dt.now(tz)
print dt.today()


print dt.utcnow()

print dt.now()-dt.utcnow()

# time tuple is useful!
print dt.timetuple()


# 2 - Ordinals
print '\n\n\n\n'
print dt.toordinal()
print dt.fromordinal(718998)
print dt.fromordinal(350)


# 3 - ISO
print '\n\n\n'
print weekday_list[str(dt.weekday())]
print str(dt.isoweekday())


# 4 - Custom formats ( Sunday, 23. August 1987 08:30AM )
print '\n\n\n'

print dt.ctime()
print dt.strftime('%A %d %B, %Y')
print dt.strftime('_%Y%m%d')






# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %d - day of the month (01 to 31)
# %D - same as %m/%d/%y
# %e - day of the month (1 to 31)
# %H - hour, using a 24-hour clock (00 to 23)
# %I - hour, using a 12-hour clock (01 to 12)
# %j - day of the year (001 to 366)
# %m - month (01 to 12)
# %M - minute
# %n - newline character
# %p - either am or pm according to the given time value
# %r - time in a.m. and p.m. notation
# %R - time in 24 hour notation
# %S - second
# %t - tab character
# %T - current time, equal to %H:%M:%S
# %x - preferred date representation without the time
# %X - preferred time representation without the date
# %y - year without a century (range 00 to 99)
# %Y - year including the century
# %% - a literal % character