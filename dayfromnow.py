import datetime
today = datetime.date.today()
someday = datetime.date(2025, 1, 25)
diff = someday - today
test = diff.days
print(test)