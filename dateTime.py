import datetime

now = datetime.datetime.now()
jan1 = datetime.datetime.strptime(str(now.year)+"-01-01", "%Y-%m-%d")
date = datetime.datetime.strptime(str(now.date()), "%Y-%m-%d")
diff = date - jan1
print(diff)
print(diff.days)
