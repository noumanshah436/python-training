# Using `zoneinfo`, a module introduced in Python 3.9, allows you to work with time zones in a more efficient and standardized way compared to third-party
# libraries like `pytz`. Here's how you can use `zoneinfo` for managing time zones in your code.

# ### Using `zoneinfo` for Time Zone Management

# 1. **Import the `zoneinfo` Module**:
#    You need to import the `ZoneInfo` class from the `zoneinfo` module.

# 2. **Setting Up Time Zones**:
#    Use `ZoneInfo` to create a timezone object for your specific timezone.

# 3. **Getting Local Time**:
#    When you want to get the current time in a specific timezone, you can use the timezone-aware datetime objects.


### Key Changes and Benefits:

# - **Standard Library**: `zoneinfo` is part of the standard library in Python 3.9+, which means you don't have to install any external dependencies like `pytz`.
# - **Simplicity**: The syntax for creating and using timezones is straightforward and follows the standard practices for working with time in Python.
# - **Timezone Database**: `zoneinfo` uses the IANA Time Zone Database, which is the same source that libraries like `pytz` use, ensuring you have accurate timezone information.


# Get all available timezones


from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import zoneinfo


available_timezones = zoneinfo.available_timezones()
# print(available_timezones)  # Prints a list of available timezones


# **********************************

dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("Asia/Karachi"))
print(dt)

print(dt.tzname())
# **********************************


user_tz = ZoneInfo("Asia/Karachi")

print(user_tz.key)
print(str(user_tz))

# **********************************

### Handling Timezone Names

# Make sure to use valid IANA timezone names (e.g., `'America/New_York'`, `'Europe/Rome'`, etc.) when creating a `ZoneInfo` object. 
# You can check for valid timezone names using:

try:
    user_tz = ZoneInfo("Asia/Karachi")
    user_tz = ZoneInfo("invalid tz")
except ZoneInfoNotFoundError:
    print(f"invalid timezone")