def hello_func():
    print("hello func")

print(hello_func)
hello_func()

print('\n######### Using Return #########\n')
def hello_func_2():
    return 'Hello Function'

print(hello_func_2())
print(hello_func_2().upper())

print('\n########### Using argument #########\n')

def hello_func_3(greeting, name='You'):
    return f'{greeting} {name} '

print(hello_func_3('Hi there!'))
print(hello_func_3('Hi there!', name='Jose'))

print('\n########### Args and kwargs #########\n')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

def student_info_2(*args, **kwargs):
    print(args)
    print(kwargs)

cources = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info_2(*cources, **info)
student_info_2(cources, info)

print('\n########### Number of days in a month #########\n')

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(is_leap(2021))
print(days_in_month(2020, 2))
print(days_in_month(2021, 2))