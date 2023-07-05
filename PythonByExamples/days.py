#!/usr/bin/python3

# Get number of days
# Output hours, minutes, and seconds in that days
#
# Seconds
# Minutes
# Hours
#
#
# Minutes in a Day = 60minutes * 24hours
# Seconds in an Hour = 60seconds * 60minutes
# Seconds in a Day = SecondsInHour * MinutesInDay

numberOfDays = int(input("Enter Day(s): "))

SECONDS: int = 60
MINUTE: int = SECONDS # Seconds
HOUR: int = 60 # Minutes
DAY: int = 24 # Hours

#secondsInHour = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
#minutesInDay = MINUTES_PER_HOUR * HOURS_PER_DAY
#secondsInDay = secondsInHour * HOURS_PER_DAY

#hoursInNDays = HOURS_PER_DAY * numberOfDays
#minutesInNDays = minutesInDay * numberOfDays
#secondsInNDays = secondsInDay * numberOfDays

hours = numberOfDays * DAY
minutes = hours * MINUTE
seconds = minutes * SECONDS

print()
print("In", numberOfDays, "there are...")
print(seconds, "seconds")
print(minutes, "minutes")
print(hours, "hours")
