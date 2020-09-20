import requests
import json
import final_message
import pytz
from tzlocal import get_localzone
import datetime

# use your local timezone name here
# NOTE: pytz.reference.LocalTimezone() would produce wrong result here

## You could use `tzlocal` module to get local timezone on Unix and Win32
# from tzlocal import get_localzone # $ pip install tzlocal

# # get local timezone
# local_tz = get_localzone()

#timezone= get_localzone()
#print(timezone)

def convert_time(year, month, day, hour, mins, second):
    utc_datetime = datetime.datetime(year, month, day, hour, mins, second, 0, tzinfo=pytz.utc)
    local_timezone = pytz.timezone("Australia/Melbourne")
    local_datetime = utc_datetime.replace(tzinfo=pytz.utc)
    local_datetime = local_datetime.astimezone(local_timezone)
    return local_datetime

def time_convert(date):
    year=int(date[0:4])
    month=int(date[6:7])
    day=int(date[8:10])
    hour=int(date[11:13])
    mins=int(date[14:16])
    second=int(date[17:19])
    return convert_time(year, month, day, hour, mins, second).hour, convert_time(year, month, day, hour, mins, second).minute

def time_test(webhook):
    occurredAt=webhook["occurredAt"]
    hour = time_convert(occurredAt)[0]
    mins = time_convert(occurredAt)[1]
    time_now=datetime.time(hour,mins)
    then=datetime.time(1,59)
    later=datetime.time(8,30)
    if (time_now>then) & (time_now<=later):
        pass
    else:
        final_message.final_post(webhook)
    return
