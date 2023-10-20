##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

import calendar

# Create a plain text calendar for January 2025 starting on Thursday
plain_calendar = calendar.TextCalendar(calendar.THURSDAY)
plain_text = plain_calendar.formatmonth(2025, 1, 0, 0)
print("Plain Text Calendar:")
print(plain_text)

# Create an HTML formatted calendar for January 2025 starting on Thursday
html_calendar = calendar.HTMLCalendar(calendar.THURSDAY)
html_text = html_calendar.formatmonth(2025, 1)
print("HTML Formatted Calendar:")
print(html_text)

# Loop over the days of April 2025 and print each day
print("Days of April 2025:")
for day in plain_calendar.itermonthdays(2025, 4):
    print(day)

# Get names of days and months
print("Month Names:")
for month_name in calendar.month_name:
    print(month_name)

print("Day Names:")
for day_name in calendar.day_name:
    print(day_name)

# Calculate audit days based on a rule: Second Monday of every month in 2025
print("Audit Days in 2025:")
for month in range(1, 13):
    mycal = calendar.monthcalendar(2025, month)
    week1 = mycal[1]
    week2 = mycal[2]

    if week1[calendar.MONDAY] != 0:
        audit_day = week1[calendar.MONDAY]
    else:
        audit_day = week2[calendar.MONDAY]

    print("%s: %d" % (calendar.month_name[month], audit_day))
