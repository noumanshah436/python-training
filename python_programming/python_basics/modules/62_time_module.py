# *************************************************************************
import time

#  summary:

# 1) time_object or time_tuple =(year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
#     i.e.       time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#           time.struct_time  (tm_year=2020, tm_mon=4, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0,
#                                tm_wday=0, tm_yday=111, tm_isdst=-1)

# 2) time.ctime(seconds)    =>  convert  seconds to a readable string (like Thu Jan  1 05:00:00 1970)
# 3) time.time()           =>  return current seconds since epoch (when your computer thinks time began)
#    time.ctime(time.time())    =>  return string which represent current time
#    time.localtime()       =>  return local time object ( time.struct_time object )
#    time.gmtime()          =>  return UTC time object   ( time.struct_time object)

# 4) time.strftime(format, time_object)   =>  formats a time_object to a string
# 5) time.strptime(time_string, format)   => (convert time_string to time_object)
# 6) time.asctime(time_tuple)  => ( convert  time_object or time_tuple   to  time_string   )
# 7) time.mktime(time_tuple)   =>  convert time_object to seconds since epoch

# print(time.asctime(time.localtime(0)))

#
#  get instance of time (year, month, day, hours, minutes, secs, dayOfWeek, dayOfYear, daylight_savings_time)
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)
print(time.localtime().tm_hour)
print(time.localtime().tm_min)
print(time.localtime().tm_sec)
print(time.localtime().tm_wday)
print(time.localtime().tm_yday)
print(time.localtime().tm_isdst)
# *************************************************************************
# print(time.ctime(0))   # convert a time expressed in seconds (since epoch if sec = 0 ) to a readable string
# #                      epoch = when your computer thinks time began (reference point)

# print(time.time())      # return current seconds since epoch
# print(time.ctime(time.time()))      # will get current time


# *************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string

# time_object = time.localtime()   # return local time( time.struct_time object )
# time_object = time.gmtime()      # UTC time (time.struct_time object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)

# print(type(local_time))
# print(local_time)
#
# print(type(time_object))
# print(time_object)

# *************************************************************************
"""  time.strptime(string_string, format) => ( convert time_string to time_object )
-> parses(takes) a string representing time/date and its format string  
-> returns a struct_time object of the given time_string  """

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")    # format should match time_string
# print(time_object)

# *************************************************************************
"""time.asctime(time_tuple)  => ( convert  time_object   to  time_string   )
-> accepts a time_object or a tuple up to 9 elements and returns a readable string representation of time
-> parameter list = (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)

-> parse -1 or 0 for dst(daylight savings time)    """

#
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
"""  time.mktime accepts a time_object or a tuple up to 9 elements and
    returns second from epoc time since given tuple time  """

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# seconds = time.mktime(time_tuple)
# print(seconds)


#
# *************************
# import datetime
# print("\nhello")
# print(datetime.datetime.today)
#
# time = datetime.datetime.now().time()
# print(time)
