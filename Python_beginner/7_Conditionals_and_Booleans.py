# Comparisons:
# Equal: ==
# Not equal: !=
# Greater than: >
# Less than: <
# Greater than or equal to: >=
# Less than or equal to: <=
# Object identity: is

language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

print('*************')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

print('*************')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a==b)
print(a is b)

# False Values:
# False
# None
# Zero
# Empty sequence '', [], ()

