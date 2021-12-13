import calendar
date = input("Please enter a date in this order - day month year with / between each one: ")
day = date[0:1]
month = int(date[3])
year = int(date[5:9])
#0 = 'Monday'
#1 = 'Tuesday'
day_name = calendar.weekday(int(day), int(month), int(year))
print(day_name)
#final_day = calendar.weekday(year, month, day)
