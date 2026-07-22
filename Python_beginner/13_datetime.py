import datetime

#d = datetime.datetime.now()
d = datetime.datetime.today()

print(d)
print(d.year)
print(d.month)
print(d.weekday())
print(d.isoweekday())

tdelta = datetime.timedelta(days=7)

print(d + tdelta)
