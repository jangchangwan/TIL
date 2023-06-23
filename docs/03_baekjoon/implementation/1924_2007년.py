import calendar

month, day = map(int,input().split())
weekList = [ "MON","TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(weekList[calendar.weekday(2007, month, day)]) 

