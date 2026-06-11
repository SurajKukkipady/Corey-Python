# Lists, tuples and sets
# Lists are mutable, tuples are immutable, sets are unordered and unindexed


courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
courses.append('Art')
print(courses)
courses.insert(0, 'Education')
print(courses)

courses_2 = ['Education', 'Art']
print(courses_2)

courses_3 = courses + courses_2
print(courses_3)

courses_3.remove('Education')
print(courses_3)

popped = courses_3.pop()
print(courses_3)
print(popped)

courses_3.reverse()
print(courses_3)
courses_3.sort()
print(courses_3)
courses_3.sort(reverse=True)
print(courses_3)

print(courses_3.index('Education'))

for index, course in enumerate(courses_3, start=1):
    print(index, course)

