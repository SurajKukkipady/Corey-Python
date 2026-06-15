student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "CompSci"]}

print(student)
print(student["name"])
print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "Not Found"))

student.update({"name": "Johnny", "age": 29, 'phone': '555-5555'})
print(student)

print(len(student))
print(student.keys())
print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)