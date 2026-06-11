# tuple
# tuples are immutable

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
print('***************')
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # This will raise an error because tuples are immutable

# Set
# Sets are unordered and unindexed, they do not allow duplicate values
print('***************')
set_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(set_1)
print('Math' in set_1)



