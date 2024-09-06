import sys

locations = sys.path
print(locations)

for location in locations:
    print(location)


import calendar

leap_days = calendar.leapdays(2000, 2050)
print(leap_days)

is_it_leap = calendar.isleap(2036)
print(is_it_leap)

