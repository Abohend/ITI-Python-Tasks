# 3) Datetime Reminder Script
#    - Ask user for a date (YYYY-MM-DD).
#    - Calculate how many days remain until that date.
#    - If it is in the past, print "This date has already passed."
#    - Otherwise, save the reminder into "reminders.txt" in format:
#         "{date} -> {days_left} days left"
#    - Append multiple reminders without overwriting.

import datetime
import re


def remind():
   dateS = input("Enter date (yyyy-mm-dd): ")
   
   while re.match(r'^\d{4}-\d{2}-\d{2}$', dateS) == None:
      print("Invalid date format.")
      dateS = input("Enter date (yyyy-mm-dd): ")
   
   targetDate = datetime.datetime.strptime(dateS, "%Y-%m-%d").date()

   daysLeft = (targetDate - targetDate.today()).days

   if daysLeft < 0:
      print("This date has already passed.")
   else:
      with open("reminders.txt", "a") as file:
         file.write(f"{dateS} -> {daysLeft} days left\n")
