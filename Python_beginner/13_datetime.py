import datetime

#d = datetime.datetime.now()
d = datetime.date.today()

print(d)
print(d.year)
print(d.month)
print(d.weekday())
print(d.isoweekday())

tdelta = datetime.timedelta(days=7)

print(d + tdelta)

bday = datetime.date(2027, 3, 6)

till_bday = bday - d
print(till_bday)
print(till_bday.total_seconds())

print('######### Time #########')

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

print('######### Date Time ########')

dt = datetime.datetime(2020, 1, 1, 12, 30, 45)
print(dt)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
